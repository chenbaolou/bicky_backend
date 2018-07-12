from django.shortcuts import render
from rest_framework import generics, filters
from ap.serializers import APTypeSerializer, APSerializer
from ap.models import APType, AP
from common.pagination import StandardResultsSetPagination
from django_filters.rest_framework import DjangoFilterBackend

class APTypeList(generics.ListAPIView):
    queryset = APType.objects.all()
    pagination_class = None
    serializer_class = APTypeSerializer

class APList(generics.ListCreateAPIView):
    queryset = AP.objects.all()
    serializer_class = APSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('apname','basemac',)

    def perform_create(self, serializer):
        serializer.save()

class APDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AP.objects.all()
    serializer_class = APSerializer
