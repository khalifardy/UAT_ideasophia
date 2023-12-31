from django.db import models
from django.db import models
#from django.contrib.auth.models import User

#third party imports
from django_extensions.db.models import TimeStampedModel
# Create your models here.

class Penerbit(models.Model):

    code_penerbit = models.CharField(max_length=100, default="")
    nama = models.CharField(max_length=100,default="")
    email = models.CharField(max_length=100, null=True, blank=True)
    telpn = models.CharField(max_length=100, null=True, blank=True)
    asal = models.CharField(max_length=100,null=True,blank=True)

    class Meta:
        app_label = "inventory"
        verbose_name = "Penerbit"
        verbose_name_plural = "Penerbit"
    
    def __str__(self):
        return self.nama

class Buku(TimeStampedModel):
    isbn = models.CharField(max_length=100, default="")
    judul = models.CharField(max_length=100, default="")
    tahun_terbit = models.IntegerField(default=1991)
    pengarang = models.CharField(max_length=100,default="",blank=True,null=True)
    penerbit = models.ForeignKey(Penerbit,on_delete=models.CASCADE, blank=True, null=True)
    url_image = models.CharField(max_length=500, null=True, blank=True)
    kategori = models.CharField(max_length=500, null=True, blank=True)
    sub_kategori = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        app_label = "inventory"
        verbose_name = "Buku"
        verbose_name_plural = "Buku"
    
    def __str__(self):
        return self.judul

class Stock(TimeStampedModel):
    buku = models.ForeignKey(Buku,on_delete=models.CASCADE,null=True, blank=True)
    jumlah_stock = models.IntegerField()
    
    

    class Meta:
        app_label = "inventory"
        verbose_name = "Stock"
        verbose_name_plural = "Stock"
    
    def __str__(self) -> str:
        return self.buku.judul

