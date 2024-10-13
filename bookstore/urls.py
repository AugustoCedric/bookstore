"""
Configuração de URLs para o projeto bookstore.

A lista `urlpatterns` direciona URLs para views. Para mais informações, consulte:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""


import debug_toolbar
from bookstore import views
from django.urls import include, path, re_path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),
    path('', views.home, name='home'),  # Rota para a página inicial
    re_path(r"^bookstore/(?P<version>(v1|v2))/", include("order.urls")),  # Rota para pedidos
    re_path(r"^bookstore/(?P<version>(v1|v2))/", include("product.urls")),  # Rota para produtos
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),

]

