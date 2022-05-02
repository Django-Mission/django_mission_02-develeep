# 장고 2차 미션
## Basic
### 미션 내용 : 고객센터 앱과 FAQ 모델 만들기

- 사용자에게 자주묻는질문 제공을 위한 고객센터앱, 자주묻는질문 모델 생성

### 목표

- 장고 ORM Models, Fields에 대한 이해

### 요구사항

- 고객센터 앱 생성
    - 앱명 : `support`
- FAQ 모델 생성
    - 모델명 : `Faq`
    - 필드 : 질문, 카테고리, 답변, 생성자, 생성일시, 최종 수정자, 최종 수정일시
### model code
``` python
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
        to=User,verbose_name='작성자',  on_delete=models.CASCADE,related_name="writer_name")
    last_updated_user = models.ForeignKey(to=User,verbose_name="최종 작성자", on_delete=models.CASCADE,related_name="last_updater_name")
```
## challenge 미션
고객센터 1:1 문의, 답글 모델 만들기

### 미션 내용 : 고객센터 앱에 1:1 문의, 답변 모델 만들기

### 목표

- 예시 화면 기반의 모델링 진행
    - 모델링 : 어떠한 데이터를 저장할 것인지 판단하여 모델 생성, 구성하는 작업
- 데이터베이스, 모델 관계 구성 이해

### 요구사항

- 1:1 문의, 답변 모델 생성

문의 모델 : 제목, 제목카테고리, 메일, 메일답변수신, 메세지, 메세지수진, 내용, 이미지, 생성시간, 최종수정시간, 생성자, 최종수정자, 답변완료여부 구현


![Inquirys_page](https://user-images.githubusercontent.com/83402978/164141880-ad4c7e58-63a2-40eb-9d5e-ddb2b438fec8.png)


```python
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
        to=User, verbose_name="생성자", on_delete=models.CASCADE,related_name="writer_name")
    last_updater = models.ForeignKey(to=User,verbose_name="최종 작성자", on_delete=models.CASCADE,related_name="last_updater_name")
    finish = models.BooleanField(verbose_name="답변완료여부", default=False)
```

답변 모델 : 1:N 구조. 답변내용, 참조문의글, 생성일시, 최종수정일시, 최종수정자, 작성자 구현

```python
class Answer(models.Model):
    content = models.TextField(verbose_name="답변내용", blank=True)
    Inquiry = models.ForeignKey(Inquiry,verbose_name="참조문의글", on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="생성일시", auto_now_add=True)
    last_updated_at = models.DateTimeField(
        verbose_name="최종수정일시", auto_now=True)
    last_updater = models.ForeignKey(to=User,verbose_name="최종 작성자", on_delete=models.CASCADE,related_name="Answer_last_updater")
    
    writer = models.ForeignKey(
        to=User, verbose_name="작성자", on_delete=models.CASCADE,related_name="Answer_writer_name")
```


