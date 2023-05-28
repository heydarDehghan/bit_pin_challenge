from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response


from account_app.serializer import RegisterSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


# Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.",
        })


class ProfileApi(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.get_serializer(request.user)
        return Response({"user": user.data,
                         "message": "User Created Successfully."})


