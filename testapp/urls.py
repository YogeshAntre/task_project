from .  import views

from django.urls import path
from testapp.views import m,GetData,RetriveData
from testapp.views import CustomAuthTokenView,CustomAuthUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [

    path('data/',views.m),
    path('items/',GetData.as_view()),
    path('items/<int:pk>/',RetriveData.as_view()),
    path('token/',CustomAuthTokenView.as_view()),
    path('register/',CustomAuthUserView.as_view()),
    path('obtain_token/',TokenObtainPairView.as_view()),
    path('token_refresh/', TokenRefreshView.as_view()),
]
  

