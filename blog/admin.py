from django.contrib import admin
from .models import Post

# 관리자 사이트에서 post 모델을 보기위해 추가해준다.
admin.site.register(Post)
