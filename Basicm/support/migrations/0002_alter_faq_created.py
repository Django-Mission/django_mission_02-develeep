# Generated by Django 4.0.4 on 2022-04-16 07:05

import django.contrib.auth.base_user
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='created',
            field=models.CharField(blank=True, default=django.contrib.auth.base_user.AbstractBaseUser.get_username, max_length=10, verbose_name='생성자'),
        ),
    ]
