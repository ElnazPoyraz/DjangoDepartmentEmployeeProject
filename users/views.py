from django.shortcuts import render
from .serializers import RegisteSerializer
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

#  REGISTER
class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisteSerializer

# LOGOUT
@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({"message":"user logout:token deleted"})