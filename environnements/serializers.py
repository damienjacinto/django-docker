from rest_framework import serializers
from . models import Environnement, Type, Status

class EnvironnementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Environnement
        fields = ('id', 'name', )

class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ('id', 'name', )

class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ('id', 'environnement', 'type', 'result', 'date_exec')