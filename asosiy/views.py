from .models import *
from .serializer import *
from rest_framework import generics

class PleylistView(generics.ListCreateAPIView):
    serializer_class =PleylistSer
    queryset =  Pleylist.objects.all()

class AccountView(generics.ListCreateAPIView):
    serializer_class = AccountSer
    queryset = Account.objects.all()

class VideoView(generics.ListCreateAPIView):
    serializer_class = VideoSer
    queryset = Video.objects.all()

class ObunaView(generics.ListCreateAPIView):
    serializer_class = ObunaSer
    queryset = Obuna.objects.all()

class HistoryView(generics.ListCreateAPIView):
    serializer_class = HistorySer
    queryset = History.objects.all()

class LikeView(generics.ListCreateAPIView):
    serializer_class = LikeSer
    queryset = Like.objects.all()
