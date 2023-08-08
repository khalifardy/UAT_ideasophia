from rest_framework import serializers
from .models import Buku, Stock

class BukuSerializers(serializers.ModelSerializer):
    
    penerbit = serializers.SerializerMethodField(method_name='get_penerbit') 

    class Meta:
        model = Buku
        fields = [
            'id','isbn','judul','tahun_terbit','pengarang','url_image',
            'penerbit','kategori','sub_kategori'
        ]
    
    def get_penerbit(self,obj):
        try:
            return obj.penerbit.nama
        except Exception as _:
            return "-"

class StockSerializer(serializers.ModelSerializer):
    buku = BukuSerializers()

    class Meta:
        model = Stock
        fields = ['id','buku','jumlah_stock']