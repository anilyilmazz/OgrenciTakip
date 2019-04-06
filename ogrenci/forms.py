from django import forms
from .models import Ogrenci


class OgrenciForm(forms.ModelForm):
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


class ExcelIceAktar(forms.Form):
    dosya = forms.FileField(label='Excel Dosyasını Seçiniz!')
