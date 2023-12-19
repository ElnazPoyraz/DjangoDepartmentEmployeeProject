from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Personel, Departman
from .serializers import PersonelSerializer, DepartmanSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsStaffOrReadOnly


class DepartmanMVS(ModelViewSet):
    queryset = Departman.objects.all()
    serializer_class = DepartmanSerializer
    permission_classes = [IsStaffOrReadOnly]


class PersonelMVS(ModelViewSet):
    queryset = Personel.objects.all()
    serializer_class = PersonelSerializer
    permission_classes = [IsStaffOrReadOnly, IsAuthenticated]