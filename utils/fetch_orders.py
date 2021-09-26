import requests

from orders.models import Product, Order

BASE_URL = 'https://api.quickbutik.com/v1/orders'
API_KEY = 'Basic V0MwKSlrODNOUm00ZE10KmYzI3guNHJSb1ZVaDJpI2g6V0MwKSlrODNOUm00ZE10KmYzI3guNHJSb1ZVaDJpI2g='

def fetch_orders():
    '''
    Retrieve all orders and their details from the API and persist them to database
    '''
    headers = {
        'Authorization': API_KEY
    }
    orders = requests.get(BASE_URL, headers=headers)
    orders_data = orders.json()

    for order in orders_data:
        order_id = int(order['order_id'])
        order_details = requests.get(f'{BASE_URL}?order_id={order_id}', headers=headers)
        order_details_data = order_details.json()
    
        # persist data to database
        for data in order_details_data:
            # save products
            product_id=data['products'][0]['product_id']
            title=data['products'][0]['title']
            qty=data['products'][0]['qty']
            sku=data['products'][0]['sku']
            
            product = Product(product_id=product_id, title=title, qty=qty, sku=sku)
            product.save()
            
            # save orders
            order_id = order_id
            order_date = data['date_created']
            order_status = data['status']
            total_pay_amount = data['total_pay_amount']
            customer_name = data['customer']['full_name']
            status = ''
            if order_status == '0':
                status = 'Unpaid'
            if order_status == '1':
                status = 'Paid'
            if order_status == '2':
                status = 'Done'
            if order_status == '0':
                status = 'Cancelled'

            order = Order(order_id=order_id, status=status, order_date=order_date, total_pay_amount=total_pay_amount, customer_name=customer_name, products=product)
            order.save()

            print('done')


fetch_orders()
