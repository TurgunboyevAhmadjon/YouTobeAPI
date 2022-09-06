from rest_framework import serializers
from .models import *

class PleylistSer(serializers.ModelSerializer):
    class Meta:
        model = Pleylist
        fields = '__all__'

class AccountSer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class VideoSer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class ObunaSer(serializers.ModelSerializer):
    class Meta:
        model = Obuna
        fields = '__all__'

class HistorySer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class LikeSer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'