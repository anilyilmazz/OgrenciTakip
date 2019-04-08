from django.db import models

# Create your models here.
from django.urls import reverse


class Dersler(models.Model):
    Id_ders = models.AutoField(verbose_name='Ders Id', primary_key=True)
    ders_adi = models.CharField(verbose_name='Ders', max_length=25)
    ders_yili = models.DateField(auto_now_add=True, verbose_name='Ders Yılı')
    ogretmen = models.ForeignKey('auth.User', verbose_name='Öğretmen', on_delete=models.CASCADE, related_name='ders',
                                 limit_choices_to={'groups__name': "ogretmenler"})
    # limit_choices_to={'groups__name': "ogretmenler"} sadece öğretmen grubuna dahil kişileri eklenebilir yapar.

    def __str__(self):
        return self.ders_adi

    @property
    def get_list_url(self):
        return reverse('dersler:listele')

    def get_sil_url(self):
        return reverse('dersler:sil', kwargs={'Id_ders': self.Id_ders})

    def get_update_url(self):
        return reverse('dersler:duzenle', kwargs={'Id_ders': self.Id_ders})
