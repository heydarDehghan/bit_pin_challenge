from rest_framework import serializers
from .models import Product, Rating


class ProductSerializer(serializers.ModelSerializer):
    # Include the num_users, avg_rating and user_rates fields in the serializer
    num_users = serializers.IntegerField(required=False)
    avg_rating = serializers.FloatField(required=False)
    user_rates = serializers.JSONField(required=False)

    class Meta:
        model = Product
        fields = ['title', 'text', 'num_users', 'avg_rating', 'user_rates']



class RatingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    product = serializers.StringRelatedField()

    class Meta:
        model = Rating
        fields = ['user', 'product', 'rate']