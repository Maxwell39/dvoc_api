from django.conf.urls import url 
from core import views 
 
urlpatterns = [ 
    url('voucher-check/(?P<pk>[0-9]+)$', views.CheckVoucher, name='checkvoucher'),
]