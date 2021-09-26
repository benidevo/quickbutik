from django.urls import path

from .views import Home, TopProductsChart

urlpatterns = [
    path('', Home.as_view(), name='Home_page'),
    path('top-products-chart/', TopProductsChart.as_view(), name='top-products-chart'),
]