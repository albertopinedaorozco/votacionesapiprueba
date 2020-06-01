
#rest_framework
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

#serializers
from .serializers import (
    DepartamentoSerializer,
    MunicipioSerializer,
    PuestoVotacionSerializer
)

#permissions custom
from .permissions import IsAdmin


from .models import Departamento, Municipio, PuestoVotacion

class DepartamentoList(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser, )
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class DepartamentoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class MunicipioList(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser, )
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer

class MunicipioDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer

class PuestoVotacionList(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser, )
    queryset = PuestoVotacion.objects.all()
    serializer_class = PuestoVotacionSerializer

class PuestoVotacionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )
    queryset = PuestoVotacion.objects.all()
    serializer_class = PuestoVotacionSerializer
    


