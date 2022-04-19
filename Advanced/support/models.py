from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class Inquiry(models.Model):
    category = [
        ('account', '계정'),
        ('general', '일반'),
        ('other', '기타'),
    ]
    title_category = models.CharField(
        verbose_name="문의분류", max_length=8, choices=category, default='general')
    title = models.TextField(verbose_name="제목", max_length=30, blank=True)
    email = models.EmailField(
        verbose_name="이메일", max_length=254, default='honggildong@example.com')
    email_btn = models.BooleanField(verbose_name="이메일로답변수신", default=False)
    message = models.CharField(
        verbose_name="전화번호", max_length=11, default='-없이 입력해 주세요')
    message_btn = models.BooleanField(verbose_name="문자메세지수신", default=False)
    content = models.TextField(verbose_name="내용", blank=True)
    image = models.ImageField(verbose_name="이미지", null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="생성시간", auto_now_add=True)
    last_updated_at = models.DateTimeField(
        verbose_name="최종 수정 일자", auto_now=True)
    writer = models.ForeignKey(
        to=User, verbose_name="생성자", on_delete=models.CASCADE)
    last_updater = models.CharField(verbose_name="최종수정자", max_length=10)
    finish = models.BooleanField(verbose_name="답변완료여부", default=False)


class Answer(models.Model):
    content = models.TextField(verbose_name="답변내용", blank=True)
    reference = models.TextField(verbose_name="참조 문의글", blank=True)
    created_at = models.DateTimeField(verbose_name="생성일시", auto_now_add=True)
    last_updated_at = models.DateTimeField(
        verbose_name="최종수정일시", auto_now=True)
    last_updater = models.CharField(verbose_name="최종수정자", max_length=10)
    Inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE)
    writer = models.ForeignKey(
        to=User, verbose_name="작성자", on_delete=models.CASCADE)
