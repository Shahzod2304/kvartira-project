# Generated by Django 4.1 on 2022-09-03 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('productname', models.CharField(max_length=50, verbose_name='Mahsulot nomi')),
                ('photo', models.CharField(max_length=200, null=True, verbose_name='Rasm file_id')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Narx')),
                ('description', models.TextField(max_length=3000, null=True, verbose_name='Mahsulot haqida')),
                ('category_code', models.CharField(max_length=20, verbose_name='Kategoriya kodi')),
                ('category_name', models.CharField(max_length=30, verbose_name='Kategoriya nomi')),
                ('subcategory_code', models.CharField(max_length=20, verbose_name='Ost-kategoriya kodi')),
                ('subcategory_name', models.CharField(max_length=30, verbose_name='Ost-kategoriya nomi')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100, verbose_name='Ism')),
                ('username', models.CharField(max_length=100, null=True, verbose_name='Telegram username')),
                ('telegram_id', models.BigIntegerField(default=1, unique=True, verbose_name='Telegram ID')),
                ('email', models.CharField(max_length=50, null=True, verbose_name='Email')),
            ],
        ),
    ]
