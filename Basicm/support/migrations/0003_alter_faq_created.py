# Generated by Django 4.0.4 on 2022-04-16 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_alter_faq_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='created',
            field=models.CharField(blank=True, max_length=10, verbose_name='생성자'),
        ),
    ]
