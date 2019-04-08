from django import forms
from .models import Dersler


class DersForm(forms.ModelForm):
    class Meta:
        model = Dersler
        fields = [
            'Id_ders',
            'ders_adi',
            'ogretmen',
        ]
