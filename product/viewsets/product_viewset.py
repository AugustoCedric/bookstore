from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    # Não precisa de autenticação para o ProductViewSet
    authentication_classes = []  # Remove todas as classes de autenticação
    permission_classes = []  # Remove todas as classes de permissão

    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
