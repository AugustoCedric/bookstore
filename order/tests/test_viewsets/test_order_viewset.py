import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from order.factories import OrderFactory, UserFactory
from order.models import Order
from product.factories import CategoryFactory, ProductFactory
from product.models import Product


class TestOrderViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        # Criação de uma categoria e um produto para os testes
        self.category = CategoryFactory(title="technology")
        self.product = ProductFactory(
            title="mouse", price=100, category=[self.category]
        )
        # Criação de uma ordem usando o produto criado
        self.order = OrderFactory(product=[self.product])

        # Criação de um usuário e autenticação
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)  # Forçando a autenticação do usuário

    def test_order(self):
        # Testa a obtenção de todas as ordens
        response = self.client.get(
            reverse("order-list", kwargs={"version": "v1"})
        )

        # Verifica se a resposta é 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        order_data = json.loads(response.content)

        # Verifica se os dados da ordem retornada estão corretos
        self.assertEqual(
            order_data["results"][0]["product"][0]["title"], self.product.title
        )
        self.assertEqual(
            order_data["results"][0]["product"][0]["price"], self.product.price
        )
        self.assertEqual(
            order_data["results"][0]["product"][0]["active"], self.product.active
        )
        self.assertEqual(
            order_data["results"][0]["product"][0]["category"][0]["title"],
            self.category.title,
        )

    def test_create_order(self):
        # Preparação dos dados da ordem
        data = json.dumps({"products_id": [self.product.id], "user": self.user.id})

        # Realiza a requisição POST para criar uma nova ordem
        response = self.client.post(
            reverse("order-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        # Verifica se a resposta é 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verifica se a ordem foi criada corretamente
        created_order = Order.objects.get(user=self.user)
        self.assertEqual(created_order.user, self.user)
        self.assertIn(self.product, created_order.product.all())  # Verifica se o produto foi adicionado
