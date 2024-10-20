
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers.order_serializers import OrderSerializer

class OrderViewSet(ModelViewSet):

    serializer_class = OrderSerializer

    queryset = Order.objects.all().order_by("id")


    # Definindo autenticação e permissões para o OrderViewSet
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


