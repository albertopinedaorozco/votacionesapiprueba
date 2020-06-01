from django.shortcuts import render

#rest_framework
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .permissions import IsAdmin
from .serializers import (
    UserSerializer,
    #UserModelSerializer,
    UserSignUpSerializer
)


class UserList(generics.ListCreateAPIView):
    permission_classes = (IsAdmin,) 
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdmin,) 
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserSignUpAPIView(APIView):
    permission_classes = (IsAdmin,)
    
    def post(self,request,*args,**kwargs):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserSerializer(user).data
        print(type(data))

        return Response(data, status=status.HTTP_201_CREATED)
