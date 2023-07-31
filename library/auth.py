"""
File berisi class-class atau modul yang diperlukan untuk
authetikasi/login/signup
"""
from rest_framework.permissions import BasePermission
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User

class IsTokenValid(BasePermission):
    """
    class yang dibutuhkan pada setiap views yang memerlukan 
    token JWT sebelum diakses 
    """

    def has_permission(self, request, view):
        try:
            try:
                token = request.auth.decode("utf-8")
            except Exception as e:
                token = request.META["HTTP_AUTHORIZATION"]
                token = token.replace("Bearer ","")
            
            if token is not None:
                is_allowed_user = True
                jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
                payload = jwt_decode_handler(token)
                user_id = payload['user_id']
                user = User.objects.get(id=user_id)
                request.user = user
            
            else:
                is_allowed_user = False
        except Exception as e:
            print("verify_token_error :" + str(e))
            is_allowed_user = False
            
        return is_allowed_user

