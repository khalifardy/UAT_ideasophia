from django.urls import re_path
from .views import CrudBuku,ViewBuku

urlpatterns = [
    re_path(r'^crud_buku/$',CrudBuku.as_view(), name='crud_buku'),
    re_path(r'^view_buku/$',ViewBuku.as_view(), name='view_buku'),
    
]