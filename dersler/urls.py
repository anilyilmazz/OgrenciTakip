from django.urls import path, re_path
from .views import *

app_name = 'dersler'

urlpatterns = [

    path('listele', ders_Listele, name='listele'),
    path('ekle', ders_Ekle, name='ekle'),
    path('duzenle/<Id_ders>/', ders_Duzenle, name='duzenle'),
    path('sil/<Id_ders>/', ders_Sil, name='sil'),

    path('dersogrencilistele', dersogrenci_Listele, name='dersogrencilistele'),
    path('dersogrenciekle', dersogrenci_Ekle, name='dersogrenciekle'),
    path('dersogrenciduzenle/<Id_dersogrenci>/', dersogrenci_Duzenle, name='dersogrenciduzenle'),
    path('dersogrencisil/<Id_dersogrenci>/', dersogrenci_Sil, name='dersogrencisil'),

]
