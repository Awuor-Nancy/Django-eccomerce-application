# Generated by Django 4.0.6 on 2022-07-30 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(blank=True, max_length=255)),
                ('productDescription', models.TextField(blank=True, max_length=255)),
                ('productType', models.CharField(blank=True, max_length=255)),
                ('productPrice', models.IntegerField()),
                ('productImage', models.ImageField(upload_to='image')),
                ('productKeyword', models.CharField(blank=True, max_length=255)),
                ('productId', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]