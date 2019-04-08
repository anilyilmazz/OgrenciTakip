from django.urls import path, re_path
from .views import *

app_name = 'dersler'

urlpatterns = [

    path('listele', ders_Listele, name='listele'),
    path('ekle', ders_Ekle, name='ekle'),
    path('duzenle/<Id_ders>/', ders_Duzenle, name='duzenle'),
    path('sil/<Id_ders>/', ders_Sil, name='sil'),

]
