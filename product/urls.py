# product/urls.py
from django.urls import include, path
from rest_framework import routers

from product.viewsets.category_viewset import CategoryViewSet
from product.viewsets.product_viewset import ProductViewSet

router = routers.SimpleRouter()
router.register(r"product", ProductViewSet, basename="product")
router.register(r"category", CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
]
