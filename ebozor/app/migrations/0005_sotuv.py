# Generated by Django 4.1.1 on 2022-10-04 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_ijara_manzil_delete_product_delete_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sotuv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=30)),
                ('photo', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('telegram', models.CharField(max_length=20)),
                ('tel_nomer', models.CharField(max_length=20)),
                ('tg_user', models.CharField(max_length=30)),
                ('price', models.PositiveIntegerField()),
                ('address', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.manzil')),
            ],
        ),
    ]
