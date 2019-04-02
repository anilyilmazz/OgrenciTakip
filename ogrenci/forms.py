from django import forms
from .models import Ogrenci


class ogrenci_Ekle_form(forms.ModelForm):
    class Meta:
        model = Ogrenci
        fields = [
            'tc',
            'adSoyad',
            'dogum_tarihi',
            'tel',
            'aolNo',
            'veli_ad',
            'veli_tel',
            'adres',
            'aktif',
        ]


class Excel_Deneme(forms.Form):
    dosya = forms.FileField(label='Excel Dosyasını Seçiniz!')
