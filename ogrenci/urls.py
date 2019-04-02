from django.urls import path

from ogrenci.views import *

app_name = 'ogrenci'
urlpatterns = [

    path('listele', ogrenci_listele, name='listele'),
    path('ekle', ogrenci_ekle, name='ekle'),
    path('', home_view, name='home'),
    path('detay/<tc>/', ogrenci_detay, name='detay'),
    path('duzenle/<tc>/', ogrenci_duzenle, name='duzenle'),
    path('ekle_excel', Excel, name='excel_Ekle'),


]
