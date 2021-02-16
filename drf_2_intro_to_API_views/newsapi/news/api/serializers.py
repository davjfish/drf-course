from django.utils import timezone
from django.utils.timesince import timesince
from rest_framework import serializers
from .. import models



class ArticleSerializer(serializers.ModelSerializer):
    time_since_publication = serializers.SerializerMethodField()
    # author = JournalistSerializer()
    class Meta:
        model = models.Article
        # fields = "__all__"
        # fields = ("title", "description")
        exclude = ("id", "created_date", "updated_date")

    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = timezone.now()
        time_delta = timesince(publication_date, now)
        return time_delta

    # used for object level validation
    def validate(self, data):
        """check to see that title and description are different"""
        if data["title"] == data["description"]:
            raise serializers.ValidationError("title and description cannot be the same")
        return data

    # used for field level validation
    def validate_title(self, value):
        """check to see that title and description are different"""
        if len(value) < 60:
            raise serializers.ValidationError("title must be longer than 60 chars")
        return value


class JournalistSerializer(serializers.ModelSerializer):
    # articles = ArticleSerializer(read_only=True, many=True)
    articles = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name="article-detail")
    class Meta:
        model = models.Journalist
        fields = "__all__"



# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_date = serializers.DateTimeField(read_only=True)
#     updated_date = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_data):
#         return models.Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.body = validated_data.get('body', instance.body)
#         instance.location = validated_data.get('location', instance.location)
#         instance.publication_date = validated_data.get('publication_date', instance.publication_date)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     # used for object level validation
#     def validate(self, data):
#         """check to see that title and description are different"""
#         if data["title"] == data["description"]:
#             raise serializers.ValidationError("title and description cannot be the same")
#         return data
#
#     # used for field level validation
#     def validate_title(self, value):
#         """check to see that title and description are different"""
#         if len(value) < 60:
#             raise serializers.ValidationError("title must be longer than 60 chars")
#         return value
