from django.contrib import admin
from .models import Buku,Penerbit,Stock

# Register your models here
admin.site.register([Buku,Penerbit,Stock])