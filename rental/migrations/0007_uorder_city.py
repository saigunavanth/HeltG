# Generated by Django 3.1.2 on 2020-11-24 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0006_auto_20201124_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='uorder',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
