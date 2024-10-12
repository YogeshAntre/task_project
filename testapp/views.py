from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Item
from testapp.seializers import ItemSerializers,UserSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from loggerConfig import logger
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
# Create your views here.
def m(request):
    return HttpResponse('<h1 style="color:red"> HI Yogesh GM</h1>')

class GetData(ListCreateAPIView):
    try:
        serializer_class= ItemSerializers
        queryset=Item.objects.all()
        #permission_class=[IsAuthenticated]
        permission_classes=[IsAuthenticated]
        authentication_classes=[JWTAuthentication]
    except Exception as e:
        logger.exception(f"exception found in ADD and POST API Views  {str(e)}")
        raise e

class RetriveData(RetrieveUpdateDestroyAPIView):
    try:
        serializer_class= ItemSerializers
        queryset=Item.objects.all()
        permission_classes=[IsAuthenticated]
        authentication_classes=[JWTAuthentication]
    except Exception as e:
        logger.exception(f"exception found in retrive delete update API Views  {str(e)}")
        raise e




class CustomAuthUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            data = request.data
            if User.objects.filter(username=data['username']).exists():
                return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create(
                username=data['username'],
            
                password=make_password(data['password'])
            )
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'username': user.username
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.exception(f"exception found in USER API Views  {str(e)}")
            raise e

class CustomAuthTokenView(APIView):
    permission_classes = [AllowAny]
    def post(self, request,*args, **kwargs):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            print(username,password)
            user = authenticate(username=username, password=password)
            print(user)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        'username': user.username
                    })
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            logger.exception(f"exception found in Login Views  {str(e)}")
            raise e




    