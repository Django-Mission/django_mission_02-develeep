# Generated by Django 4.0.4 on 2022-04-16 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, verbose_name='질문')),
                ('cartegori', models.CharField(choices=[('account', '계정'), ('general', '일반'), ('other', '기타')], default='general', max_length=8, verbose_name='카테고리')),
                ('answer', models.TextField(blank=True, verbose_name='답변')),
                ('created', models.CharField(blank=True, max_length=10, verbose_name='생성자')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('last_updated', models.CharField(blank=True, max_length=10, verbose_name='최종수정자')),
                ('last_updated_at', models.DateTimeField(auto_now=True, verbose_name='최종수정일')),
            ],
        ),
    ]
