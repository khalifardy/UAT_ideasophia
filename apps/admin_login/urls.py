from django.urls import re_path
from .views import Login

urlpatterns = [
    re_path(r'^login/$',Login.as_view(), name='login')
]