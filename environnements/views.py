from django.contrib.auth.models import User
from rest_framework import generics, permissions

from .models import Environnement, Type
from .serializers import EnvironnementSerializer, TypeSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET']) 
def api_root(request, format=None):
    return Response({
        'environnement': reverse('environnement-list', request=request, format=format),
        'type': reverse('type-list', request=request, format=format),
    })

class EnvironnementList(generics.ListCreateAPIView):
    queryset = Environnement.objects.all()
    serializer_class = EnvironnementSerializer

class EnvironnementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Environnement.objects.all()
    serializer_class = EnvironnementSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TypeList(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class TypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)