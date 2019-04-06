from django.db import models
from django.urls import reverse


class Ogretmenler(models.Model):
    IDogretmen = models.AutoField(primary_key=True, unique=True)
    ad = models.CharField(verbose_name='İsim', max_length=50)
    tel = models.CharField(verbose_name='Tel', max_length=10)
    kullaniciAdi = models.CharField(verbose_name='Kullanıcı Adı', max_length=25)
    password = models.CharField(verbose_name='Parola', max_length=30)
    aktif = models.BooleanField(default=True, null=False)

    def __str__(self):
        return self.ad

    def get_update_url(self):
        return reverse('ogretmen:duzenle', kwargs={'IDogretmen': self.IDogretmen})

    @staticmethod
    def get_list_url():
        return reverse('ogretmen:ogretmenListele')

    # def get_delete_url(self):
    #     return reverse('ogrenci:sil', kwargs={'tc': self.tc})

    # ders = models.CharField(verbose_name='Dersler', )
    # ogretmen_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    # adisoyadi varchar(50) NOT NULL,
    # ogretmen_tel char(10),
    # ogretmen_kullaniciadi varchar(30),
    # ogretmen_sifre varchar(30),
    # ogretmen_ders varchar(25),
    # aktif int DEFAULT 1
