from rest_framework import generics

from .models import History
from .serializer import HistorySerializer


class HistoryListView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = HistorySerializer
    queryset = History.objects.all().order_by('-pk')
