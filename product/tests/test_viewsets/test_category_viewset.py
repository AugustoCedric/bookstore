import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from product.factories import CategoryFactory
from product.models import Category


class CategoryViewSetTests(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title="books")

    def test_get_all_category(self):
        response = self.client.get(reverse("category-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category_data = response.json()

        self.assertEqual(category_data[0]["title"], self.category.title)

    def test_create_category(self):
        data = {"title": "technology"}
        # Converter o dicionário para JSON
        response = self.client.post(
            reverse("category-list", kwargs={"version": "v1"}),
            data=json.dumps(data),  # Aqui você converte os dados para JSON
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verifica se a categoria foi realmente criada
        created_category = Category.objects.get(title="technology")
        self.assertEqual(created_category.title, "technology")

    def test_create_category_invalid_data(self):
        # Teste para verificar se o servidor responde corretamente com dados inválidos
        data = {"title": ""}  # Título vazio

        # Converter o dicionário para JSON
        response = self.client.post(
            reverse("category-list", kwargs={"version": "v1"}),
            data=json.dumps(data),  # Converter para JSON
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Verifica se o campo title está presente nos erros
        self.assertIn("title", response.data)
