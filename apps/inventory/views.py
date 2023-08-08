from django.shortcuts import render
from django.conf import settings
import os
from datetime import datetime

#django-rest-framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

#library internal
from library.auth import IsTokenValid

#models
from .models import Buku,Penerbit,Stock
from .serializers import BukuSerializers
# Create your views here.

class CrudBuku(APIView):
    permission_classes = (IsTokenValid,)

    def post(self,request):
        judul = request.data.get("judul")
        pengarang = request.data.get("pengarang")
        isbn = request.data.get("isbn")
        tahun = request.data.get("tahun")
        penerbit = request.data.get("penerbit")
        kategori = request.data.get("kategori",None)
        sub = request.data.get("sub_kategori",None)
        image = request.FILES.get("img",None)

        path = settings.MEDIA_ROOT + 'inventory/buku/images'

        if image :
            if not os.path.exists(path):
                os.makedirs(path)
            try:
                upload_path = os.path.join(
                    path, "image_"+judul+".jpg"
                )

                with open(upload_path, 'wb+') as destination:
                    for chunk in image.chunks():
                        destination.write(chunk)
            except Exception as e:
                print(str(e))
        
        try:
            id_penerbit = Penerbit.objects.get(nama=penerbit)
            if not image and not kategori and not sub:
                Buku.objects.create(
                    isbn=isbn, judul=judul, penerbit=id_penerbit,
                    pengarang=pengarang,tahun_terbit= tahun
                )
            elif not kategori and not sub and image:
                Buku.objects.create(
                    isbn=isbn, judul=judul, penerbit=id_penerbit,
                    pengarang=pengarang,tahun_terbit= tahun, url_image=image
                )
            elif not image and not sub and kategori:
                Buku.objects.create(
                    isbn=isbn, judul=judul, penerbit=id_penerbit,
                    pengarang=pengarang,tahun_terbit= tahun, kategori=kategori
                )
            elif not image and not kategori and sub:
                Buku.objects.create(
                    isbn=isbn, judul=judul, penerbit=id_penerbit,
                    pengarang=pengarang,tahun_terbit= tahun, sub_kategori=sub
                )
            elif not image and kategori and sub:
                Buku.objects.create(
                    isbn=isbn, judul=judul, penerbit=id_penerbit,
                    pengarang=pengarang,tahun_terbit= tahun, kategori=kategori,
                    sub_kategori=sub
                )
            elif not sub and image and kategori :
                Buku.objects.create(
                    isbn=isbn, judul=judul, penerbit=id_penerbit,
                    pengarang=pengarang,tahun_terbit= tahun, kategori=kategori,
                    url_image=upload_path
                )
            elif not kategori and image and sub :
                Buku.objects.create(
                    isbn=isbn, judul=judul, penerbit=id_penerbit,
                    pengarang=pengarang,tahun_terbit= tahun, sub_kategori=sub,
                    url_image=upload_path
                )
            else:
                Buku.objects.create(
                    isbn=isbn, judul=judul, penerbit=id_penerbit,
                    pengarang=pengarang,tahun_terbit= tahun, kategori=kategori,
                    url_image=upload_path, sub_kategori=sub
                )
        except Exception as e:
            return Response({'msg':str(e)},status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'msg':"Menambahkan Buku sukses"},status=status.HTTP_200_OK)
    
    def put(self,request):
        id_ = request.data.get("id")
        isbn = request.data.get("isbn",None)
        judul = request.data.get("judul",None),
        pengarang = request.data.get("pengarang",None)
        tahun = request.data.get("tahun",None)
        penerbit = request.data.get("penerbit",None)
        kategori = request.data.get("kategori",None)
        sub = request.data.get("sub_kategori",None)
        image = request.FILES.get("img",None)
        print(judul)
        print(isbn)

        try:
            id_buku = Buku.objects.filter(id=int(id_))

            if penerbit:
                objek_penerbit = Penerbit.objects.get(nama=penerbit)
                id_buku.update(penerbit=objek_penerbit)
        
            if judul and judul != ('',):
                id_buku.update(judul=judul[0])
        
            if pengarang:
                id_buku.update(pengarang=pengarang)

            if tahun:
                id_buku.update(tahun_terbit=tahun)

            if kategori:
                id_buku.update(kategori=kategori)

            if sub:
                id_buku.update(sub_kategori=sub) 
            
            if image:
                time = datetime.now().strftime("%Y-%m-%d")
                path = settings.MEDIA_ROOT + 'inventory/buku/images'
                
                
                upload_path = os.path.join(
                    path, "image_"+id_buku[0].judul+"_"+time+".jpg"
                )

                with open(upload_path, 'wb+') as destination:
                    for chunk in image.chunks():
                        destination.write(chunk)
                
                id_buku.update(url_image=upload_path)
            
            if isbn:
                id_buku.update(isbn=isbn)
            
            respon ={"msg":"update sukses"}
            
        except Exception as e:
            respon ={"msg":str(e)}
            
        
        return Response(respon,status=status.HTTP_200_OK)
    
    def delete(self,request):
        id_buku = request.data.get("id")

        try:
            obj = Buku.objects.get(id=id_buku)
            obj.delete()
            respon = {"msg":"Buku Berhasil Di hapus"}
        except Exception as e:
            respon = {"msg":str(e)}
        
        return Response(respon,status=status.HTTP_200_OK)

class ViewBuku(APIView,PageNumberPagination):

    permission_classes = (IsTokenValid,)
    page_size = 20
    max_page_size = 20

    def get_queryset(self,query):

        """
        fungsi untuk mengolah data/query menjadi halaman (pagination)
        """
        return self.paginate_queryset(query, self.request,view=self)

    def post(self,request):

        isbn = request.data.get("isbn",None)
        judul = request.data.get("judul",None),
        pengarang = request.data.get("pengarang",None)
        tahun = request.data.get("tahun",None)
        penerbit = request.data.get("penerbit",None)
        kategori = request.data.get("kategori",None)
        sub = request.data.get("sub_kategori",None)

        query_buku = Buku.objects.all()

        if isbn:
            query_buku=query_buku.filter(isbn=isbn)
        
        if judul and judul != ('',) :
            query_buku =query_buku.filter(judul=judul[0])
        
        if pengarang:
            query_buku=query_buku.filter(pengarang=pengarang)
        
        if tahun:
            query_buku=query_buku.filter(tahun_terbit=int(tahun))
        
        if penerbit:
            query_buku=query_buku.filter(penerbit__nama=penerbit)
        
        if kategori:
            query_buku=query_buku.filter(kategori=kategori)
        
        if sub:
            query_buku=query_buku.filter(sub_kategori=sub)
        
        record = self.get_queryset(query_buku)
        serializer =BukuSerializers(record,many=True)

        return self.get_paginated_response(serializer.data)
    






        
        




        
