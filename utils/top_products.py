import itertools
from collections import Counter
from orders.models import Product

def multiply_order_qty(orders, qty):
    return [orders] * qty

def get_top_products():
    '''
    return a dictionary consisting the top three most sold products
    '''
    result = []
    products = Product.objects.all()

    for product in products:
        product_list = multiply_order_qty(product.title, product.qty)
        result.extend(product_list)
    
    result = dict(Counter(result))
    return dict(itertools.islice(result.items(), 3))
