from django.urls import re_path
from .views import Login,Logout

urlpatterns = [
    re_path(r'^login/$',Login.as_view(), name='login'),
    re_path(r'^logout/$',Logout.as_view(), name='logout'),
]