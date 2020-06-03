from django.db.models import Count
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import viewsets, filters
from rest_framework.filters import SearchFilter
from django.db.models import Q

from .serializers import *
from .filters import *


class AdListAPIView(ListAPIView):
    serializer_class = AdSerializer
    queryset = serializer_class.Meta.model.objects.all()
    filter_backends = (filters.DjangoFilterBackend,SearchFilter,)
    filterset_class = AdFilter
    ordering_fields = ['id']
    search_fields = ('year', 'make','model')


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = serializer_class.Meta.model.objects.all()
