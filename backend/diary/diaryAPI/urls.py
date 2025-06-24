from django.urls import path
from . import views

urlpatterns = [
    # TODO: tags/?tag=<name_1+...+name_n>
    path("tags/", views.TagsView.as_view(), name="tags"),
    path("diary/", views.DiaryView.as_view(), name="diary"),
    path("diary/<int:pk>", views.SingleDiaryView.as_view(), name="single-diary"),
]
