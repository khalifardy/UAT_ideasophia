from django.urls import re_path
from .views import CrudBuku

urlpatterns = [
    re_path(r'^crud_buku/$',CrudBuku.as_view(), name='crud_buku'),
    
]