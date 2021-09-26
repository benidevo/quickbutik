from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_id', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('qty', models.IntegerField()),
                ('sku', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(null=True)),
                ('order_date', models.DateTimeField()),
                ('total_pay_amount', models.CharField(max_length=30)),
                ('customer_name', models.CharField(max_length=255)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.product')),
            ],
        ),
    ]
