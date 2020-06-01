
from django.urls import path

from .views import (
    DepartamentoList,
    DepartamentoDetail,
    MunicipioList,
    MunicipioDetail,
    PuestoVotacionList,
    PuestoVotacionDetail
)

urlpatterns = [
    path('departamentos/lista/', DepartamentoList.as_view()),
    path('departamentos/<int:pk>/', DepartamentoDetail.as_view()),
    path('municipios/lista/', MunicipioList.as_view()),
    path('municipios/<int:pk>/', MunicipioDetail.as_view()),
    path('puestovotaciones/lista/', PuestoVotacionList.as_view()),
    path('puestovotaciones/<int:pk>/', PuestoVotacionDetail.as_view())
]