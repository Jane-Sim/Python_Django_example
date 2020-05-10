from django.conf import settings
from django.db import models
from django.utils import timezone

# models.Model 을 통해, 장고는 post가 데이터베이스에 저장되는걸 알게 된다.
# CharField - 글자수 제한된 텍스트 정의
# TextField - 글자수 제한없는 텍스트 정의
# DateTImeField - 날짜와 시간을 의미
# ForeignKey - 다른 모델에 대한 링크
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
