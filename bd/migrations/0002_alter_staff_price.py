# Generated by Django 5.0.6 on 2024-06-05 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='price',
            field=models.IntegerField(verbose_name='Зарплата'),
        ),
    ]
