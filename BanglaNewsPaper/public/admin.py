import datetime

from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = (
    'title', 'author', 'author_location', 'published_date', 'description', 'news_image', 'is_active', 'is_delete',
    'created', 'modified')
    list_filter = ("title",)
    exclude = ('created', 'published_date', 'modified')

    def save_model(self, request, obj, form, change):
        if change:
            obj.modified = datetime.datetime.now()
            obj.modified_by = request.user
        else:
            obj.created = datetime.datetime.now()
            obj.created_by = request.user
        obj.save()


admin.site.register(News, NewsAdmin)

# Register your models here.
