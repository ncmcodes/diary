import django_filters
from . import models


class DiaryFilter(django_filters.FilterSet):
    year = django_filters.NumberFilter(field_name="created", lookup_expr="year")

    class Meta:
        model = models.Diary
        fields = ["year"]
