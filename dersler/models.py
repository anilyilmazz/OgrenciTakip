from django.db import models

# Create your models here.

"""
 ders_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ders_adi varchar(25) NOT NULL,
    ogretmen int,
    dersyili Date,
   FOREIGN KEY(ogretmen) REFERENCES ogretmen(ogretmen_id) on delete cascade
    """


class Dersler(models.Model):
    Id_ders = models.AutoField(verbose_name='Ders Id', primary_key=True)
    ders_adi = models.CharField(verbose_name='Ders', max_length='20')
    ders_yili = models.DateField(auto_now_add=True, verbose_name='Ders Yılı')
    ogretmen = models.ForeignKey('auth.User', verbose_name='Öğretmen', on_delete=models.CASCADE, related_name='ogr')
