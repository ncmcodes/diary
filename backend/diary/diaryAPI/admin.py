from django.contrib import admin
from . import models

admin.site.register(models.Diary)
admin.site.register(models.Tags)
admin.site.register(models.DiaryTags)
