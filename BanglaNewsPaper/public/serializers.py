from rest_framework import serializers

from .models import News


# class NewsSerializers(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     author = serializers.CharField(max_length=50)
#     author_location = serializers.CharField(max_length=40)
#     published_date = serializers.DateTimeField()
#     description = serializers.CharField(max_length=2500)
#     is_active = serializers.NullBooleanField(default=False)
#     is_delete = serializers.NullBooleanField(default=False)
#     created = serializers.DateTimeField()
#     modified = serializers.DateTimeField()
#
#     def create(self, validated_data):
#         return News.objects.create(validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.author_location = validated_data.get('author_location', instance.author_location)
#         instance.published_date = validated_data.get('published_date', instance.published_date)
#         instance.description = validated_data.get('description', instance.description)
#         instance.is_active = validated_data.get('is_active', instance.is_active)
#         instance.is_delete = validated_data.get('is_delete', instance.is_delete)
#         instance.created = validated_data.get('created', instance.created)
#         instance.modified = validated_data.get('modified', instance.modified)
#         instance.save()
#         return instance


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'author', 'description']