from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    author_location = models.CharField(max_length=40)
    published_date = models.DateTimeField(auto_now_add=True, null=True)
    description = models.CharField(max_length=2500)
    news_image = models.FileField(upload_to='documents/news_image', blank=True, null=True)
    is_active = models.NullBooleanField(default=False)
    is_delete = models.NullBooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
