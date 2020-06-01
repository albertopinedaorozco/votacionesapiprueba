from django.shortcuts import render

#rest_framework
from rest_framework import generics


from .models import Votante 
from .permissions import IsLiderWhoRegistred
from .serializers import VotanteSerializer


class VotanteList(generics.ListCreateAPIView):
    permission_classes = (IsLiderWhoRegistred,)
    queryset = Votante.objects.all()
    serializer_class = VotanteSerializer

class VotanteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsLiderWhoRegistred,)
    queryset = Votante.objects.all()
    serializer_class = VotanteSerializer
