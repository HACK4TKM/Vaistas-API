from django.shortcuts import render,get_object_or_404
from rest_framework import generics
# Create your views here.
from .models import History
from .serializer import HistorySerializer

class HistoryListView(generics.ListAPIView,generics.CreateAPIView):
    li = []
    serializer_class = HistorySerializer
    queryset = History.objects.all().order_by('-pk')

