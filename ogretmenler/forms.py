from django import forms
from .models import Ogretmenler


class OgretmenForm(forms.ModelForm):
    class Meta:
        model = Ogretmenler
        fields = [
            'ad',
            'tel',
            'kullaniciAdi',
            'password',
            'aktif',
        ]
