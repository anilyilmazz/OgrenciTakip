from django.urls import path

from ogretmenler.views import *

app_name = 'ogretmen'
urlpatterns = [

    path('ekle', ogretmen_ekle, name='ekle'),
    path('listele', ogretmen_Listele, name='ogretmenListele'),
    path('duzenle/<IDogretmen>/', ogretmen_duzenle, name='duzenle'),
    # path('sil/<tc>/', ogrenci_sil, name='sil'),

]
