from itertools import product

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Avg
from .models import Product, Rating
from .serializers import ProductSerializer, RatingSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_list_or_404, get_object_or_404


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        # Get all products with extra fields num_users, avg_rating and user_rates
        products = Product.objects.annotate(num_users=Count('rating'), avg_rating=Avg('rating__rate'))

        # Add a user_rates field that contains a list of user ids and rates for each product
        # for p in products:
        #     if p.rating_set.count() > 0:
        #         p.user_rates = list(p.rating_ste.all().values('user', 'rate'))

        # Serialize the products with the ProductSerializer
        serializer = ProductSerializer(products, many=True)
        # Return the serialized data as a response
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # Get the product with the given primary key
        product = Product.objects.get(pk=pk, rating__user_id=request.user.id)
        # Get the ratings for the product
        ratings = Rating.objects.filter(product=product)
        # Serialize the ratings with the RatingSerializer
        serializer = RatingSerializer(ratings, many=True)
        # Return the serialized data as a response
        return Response(serializer.data)

    def create(self, request):
        # Override the create method to create a new product
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()
        # Return the created product with extra fields
        product.num_users = 0
        product.avg_rating = 0.0
        product.user_rates = []
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RatingViewSet(viewsets.ModelViewSet):
    # Set the queryset and serializer class for the rating model
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        # Get the user, product and rate from the request data
        user = request.user
        product = get_object_or_404(Product, pk=request.data.get('product'))
        rate = request.data.get('rate')
        if rate in [0, 1, 2, 3, 4, 5]:
            # Check if the user has already rated the product
            rating = Rating.objects.filter(user_id=user.id, product_id=product.id).first()
            if rating:
                # If yes, update the existing rating with the new rate
                rating.rate = rate
                rating.save()
                serializer = self.get_serializer(rating)
                return Response(serializer.data, status=status.HTTP_200_OK)

            # If not, create a new rating with the user, product and rate
            rating = Rating.objects.create(user_id=user.id, product_id=product.id, rate=rate)
            serializer = self.get_serializer(rating)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'error_message': "you can't select this rate"}, status=status.HTTP_201_CREATED)
