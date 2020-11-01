from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import History
from .serializer import HistorySerializer

class HistoryListView(generics.ListAPIView,generics.CreateAPIView):
    serializer_class = HistorySerializer
    queryset = History.objects.all()
#
# class CreateHistory(generics.CreateAPIView):
#     queryset = History.objects.all()
#     serializer_class = HistorySerializer