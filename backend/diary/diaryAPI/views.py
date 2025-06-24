from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers
from . import filters


def index(request):
    return render(request, "home.html")


class TagsView(generics.ListCreateAPIView):
    queryset = models.Tags.objects.all()
    serializer_class = serializers.TagsSerializer


class DiaryView(generics.ListCreateAPIView):
    queryset = models.Diary.objects.all()
    serializer_class = serializers.DiarySerializer
    filterset_class = filters.DiaryFilter


class SingleDiaryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Diary.objects.all()
    serializer_class = serializers.SingleDiarySerializer
