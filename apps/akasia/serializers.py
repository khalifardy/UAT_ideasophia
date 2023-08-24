from rest_framework import serializers
from .models import User


class UserAkasiaSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'id_asal', 'email',
                  'first_name', 'last_name', 'avatar']
