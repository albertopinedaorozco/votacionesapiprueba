from django.urls import path

from .views import VotanteList, VotanteDetail

urlpatterns = [
    path('lista/', VotanteList.as_view()),
    path('<int:pk>/', VotanteDetail.as_view()),
]