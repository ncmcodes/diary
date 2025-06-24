from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tags
        fields = "__all__"


class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Diary
        fields = ["id", "entry", "created", "last_modified"]


class SingleDiarySerializer(serializers.ModelSerializer):
    created = serializers.DateField(read_only=True)

    class Meta:
        model = models.Diary
        fields = "__all__"
