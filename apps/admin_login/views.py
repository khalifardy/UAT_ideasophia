from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

#django-rest-framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_jwt.settings import api_settings

#models
from .models import StaffProfile,Level
# Create your views here.

class Login(APIView):
    "API untuk Login Internal"
    permission_classes = (AllowAny,)

    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request,username=username, password=password)

        if user is not None:
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler  = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)

            try:
                role = Level.objects.get(user=user).tipe
            except Exception as _:
                role = "-"
            
            msg = {
                'role':role,
                'token':token
            }

            return Response(msg, status=status.HTTP_200_OK)
        else:
            return Response({"msg":"username atau password salah"}, status=status.HTTP_400_BAD_REQUEST)
        

        

