from django.urls import path

from ogrenci.views import *

app_name = 'ogrenci'
urlpatterns = [

    path('', home_view, name='home'),
    path('listele', ogrenci_listele, name='listele'),
    path('ekle', ogrenci_ekle, name='ekle'),
    path('ekle_excel', Excel, name='excel_Ekle'),
    path('duzenle/<tc>/', ogrenci_duzenle, name='duzenle'),
    path('sil/<tc>/', ogrenci_sil, name='sil'),

]
