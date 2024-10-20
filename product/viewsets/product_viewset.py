# product/viewsets/product_viewset.py
from django.urls import include, path
from rest_framework import routers
from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.serializers.product_serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by("id")


router = routers.SimpleRouter()
router.register(r"product", ProductViewSet, basename="product")

urlpatterns = [
    path("", include(router.urls)),
]
