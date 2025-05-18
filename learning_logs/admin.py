from django.contrib import admin

from .models import Topic, Entry
"""使用者の権限管理"""
admin.site.register(Topic)
admin.site.register(Entry)

