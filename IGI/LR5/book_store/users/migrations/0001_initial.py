# Generated by Django 5.0.6 on 2024-09-24 16:06

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(message='Номер телефона должен быть в формате: +375(29|33|44)XXXXXXX', regex='^\\+375(?:29|33|44)\\d{7}$')])),
                ('date_of_birth', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=25, unique=True, validators=[django.core.validators.RegexValidator(message='Номер телефона должен быть в формате: +375(29|33|44)XXXXXXX', regex='^\\+375(?:29|33|44)\\d{7}$')])),
                ('date_of_birth', models.DateField()),
                ('salary', models.FloatField()),
                ('image', models.ImageField(blank=True, upload_to='images/employees')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
