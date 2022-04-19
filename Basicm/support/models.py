
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Faq(models.Model):
    question_categori = [
        ('account', '계정'),
        ('general', '일반'),
        ('other', '기타'),
    ]
    question = models.TextField(verbose_name='질문', blank=True)
    cartegori = models.CharField(
        verbose_name='카테고리', max_length=8, choices=question_categori, default='general')
    answer = models.TextField(verbose_name="답변", blank=True)
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    last_updated_at = models.DateTimeField(verbose_name='최종수정일', auto_now=True)
    writer = models.ForeignKey(
        verbose_name='작성자', to=User, on_delete=models.CASCADE, null=True, blank=True)
    last_updated_user = models.CharField(
        verbose_name="최종수정자", max_length=10, null=True, blank=True)
