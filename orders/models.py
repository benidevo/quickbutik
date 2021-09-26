import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    product_id = models.IntegerField()
    title = models.CharField(max_length=255)
    qty = models.IntegerField()
    sku = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.title}'

class Order(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    order_id = models.IntegerField(null=True)
    order_date = models.DateTimeField()
    total_pay_amount = models.CharField(max_length=30)
    customer_name = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self. customer_name
