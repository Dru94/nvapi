# Generated by Django 3.2.15 on 2022-08-31 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20220831_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='order_item', to='order.book'),
        ),
    ]
