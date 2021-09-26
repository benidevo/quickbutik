from orders.models import Order
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse

from .models import Order
from utils.top_products import get_top_products

class Home(View):
    '''
    View for Homepage Controller
    '''
    def get(self, request):
        orders = Order.objects.all()

        context = {
            'orders': orders,
        }

        return render(request, 'orders/home.html', context)
        

class TopProductsChart(View):
    '''
    Retrieve top 3 products and render to chart
    '''
    def get(self, request):
        top_products = get_top_products()
        labels = list(top_products.keys())
        data = list(top_products.values())
        
        return JsonResponse(data={
            'labels': labels,
            'data': data,
        })
