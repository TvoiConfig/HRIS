# Generated by Django 5.0.6 on 2024-06-06 13:48

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0004_alter_staff_character'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='', max_length=20, verbose_name='Наименование отдела')),
            ],
            options={
                'verbose_name': 'отдел',
                'verbose_name_plural': 'отделы',
                'db_table': 'offices',
            },
        ),
        migrations.AlterField(
            model_name='staff',
            name='character',
            field=models.TextField(max_length=100, verbose_name='Должность'),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата и Время')),
                ('description', models.TextField(verbose_name='Подробности')),
                ('auth_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bd.authuser', verbose_name='Работник')),
                ('worker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('number_cab', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bd.office', verbose_name='Выберите отдел')),
            ],
            options={
                'verbose_name': 'Выдача',
                'verbose_name_plural': 'Выдачи',
                'db_table': 'applications',
            },
        ),
    ]
