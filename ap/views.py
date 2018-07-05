from django.shortcuts import render
from rest_framework import generics, filters
from ap.serializers import APSerializer
from ap.models import AP
from common.pagination import StandardResultsSetPagination
from django_filters.rest_framework import DjangoFilterBackend

class APList(generics.ListCreateAPIView):
    queryset = AP.objects.all()
    serializer_class = APSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('apIndex','apname',)

    def perform_create(self, serializer):
        serializer.save()

class APDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AP.objects.all()
    serializer_class = APSerializer
