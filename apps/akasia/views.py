from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_jwt.settings import api_settings
import requests
import json

from .models import User
from .serializers import UserAkasiaSerializers
# Create your views here.


class DataUser(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):

        page = request.GET.get('page')

        if page:
            url = "https://reqres.in/api/users"
            params = {
                'page': page
            }
            try:
                response = requests.get(url, params=params)
                id_tersimpan = []
                for i in response.json()["data"]:
                    id_ = i["id"]
                    email = i["email"]
                    first = i["first_name"]
                    last = i["last_name"]
                    avatar = i["avatar"]
                    cek_id = User.objects.filter(id_asal=id_)

                    if len(cek_id) == 0:
                        User.objects.create(id_asal=id_, email=email,
                                            first_name=first, last_name=last,
                                            avatar=avatar)
                        id_tersimpan.append(id_)

                obj = User.objects.filter(id_asal__in=id_tersimpan)
                data = UserAkasiaSerializers(obj, many=True)
                respon = {
                    "msg": "sukses",
                    'data': data.data
                }

            except Exception as e:
                return Response({"msg": str(e)})

        else:
            respon = {"msg": "parameter harus dimasukan"}

        return Response(respon, status=status.HTTP_200_OK)


class ViewUser(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, id=None):

        if id:

            usr = User.objects.filter(id=id)
        else:
            usr = User.objects.all()

        data = UserAkasiaSerializers(usr, many=True)

        return Response(data.data, status=status.HTTP_200_OK)

    def post(self, request):
        email = request.data.get('email')
        first = request.data.get('first_name')
        last = request.data.get('last_name')
        avatar = request.data.get('avatar', None)

        try:
            User.objects.create(
                email=email, first_name=first,
                last_name=last, avatar=avatar
            )

            respon = {"msg": "menambahkan user sukses"}

        except Exception as e:
            respon = {"msg": str(e)}

        return Response(respon, status=status.HTTP_200_OK)

    def put(self, request):
        id_ = request.data.get('id')
        email = request.data.get('email', None)
        first = request.data.get('first_name', None)
        last = request.data.get('last_name', None)
        avatar = request.data.get('avatar', None)

        try:
            obj = User.objects.filter(id=id_)

            if email:
                obj.update(email=email)

            if first:
                obj.update(first_name=first)

            if last:
                obj.update(last_name=last)

            if avatar:
                obj.update(avatar=avatar)

            respon = {"msg": "update user sukses"}

        except Exception as e:
            respon = {"msg": str(e)}

        return Response(respon, status=status.HTTP_200_OK)

    def delete(self, request):

        id_ = request.data.get("id")

        try:
            obj = User.objects.get(id=id_)
            obj.delete()
            respon = {
                'msg': "hapus user sukses"
            }
        except Exception as e:
            respon = {
                'msg': str(e)
            }

        return Response(respon, status=status.HTTP_200_OK)
