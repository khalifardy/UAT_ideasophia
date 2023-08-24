from django.urls import re_path
from .views import DataUser, ViewUser

urlpatterns = [
    re_path(r'^user/fetch$',
            DataUser.as_view(), name='fetch_data'),
    re_path(r'^user/$',
            ViewUser.as_view(), name='data_user'),
    re_path(r'^user/(?P<id>\d+)',
            ViewUser.as_view(), name='user_detail'),

]
