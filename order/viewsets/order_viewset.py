
from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers.order_serializers import OrderSerializer

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
