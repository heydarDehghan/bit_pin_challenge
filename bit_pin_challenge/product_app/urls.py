from django.contrib import admin
from django.urls import path
from product_app.views import ProductViewSet, RatingViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'rating', RatingViewSet, basename='rating')
urlpatterns = router.urls

urlpatterns += [

]