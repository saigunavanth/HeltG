# Generated by Django 3.1.2 on 2020-11-16 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_customer_order_orderitem_product_shippingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
