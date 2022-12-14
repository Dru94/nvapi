# Generated by Django 3.2.15 on 2022-08-31 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('class_number', models.CharField(max_length=10)),
                ('level', models.CharField(choices=[('PRIMARY', 'PRIMARY'), ('SENIOR', 'SENIOR')], max_length=100)),
                ('cost', models.PositiveBigIntegerField()),
                ('teachers_guide', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.PositiveBigIntegerField()),
                ('address', models.CharField(max_length=500)),
                ('phone_number', models.PositiveBigIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.customer')),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='order.book')),
            ],
        ),
    ]
