from django.urls import path
from .views import UserList, UserDetail, UserSignUpAPIView


urlpatterns = [
    path('', UserList.as_view(),name='login'), 
    path('<int:pk>/', UserDetail.as_view(), name='detail'), 
    path('signup/', UserSignUpAPIView.as_view(), name='signup'), 
]