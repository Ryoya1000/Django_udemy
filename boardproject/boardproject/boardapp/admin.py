from django.contrib import admin
from .models import BoardModel

# Register your models here.

# 管理画面上に表示したいモデル情報を定義する
admin.site.register(BoardModel)