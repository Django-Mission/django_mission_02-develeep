# Generated by Django 4.0.4 on 2022-04-19 06:43

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0007_alter_faq_last_updated_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='last_updated_user',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=10, verbose_name='최종수정자'),
        ),
    ]
