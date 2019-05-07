from django_filters import rest_framework as filters

from .models import Task


class TaskFilter(filters.FilterSet):
    name=filters.CharFilter(lookup_expr='contains')
    status=filters.CharFilter(lookup_expr="exact")
    # min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    # max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    class Meta:
        model = Task
        fields=('name','status',)
