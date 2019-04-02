# Generated by Django 2.1.7 on 2019-04-02 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ogrenci',
            fields=[
                ('tc', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='Kimlik No')),
                ('adSoyad', models.CharField(max_length=50, verbose_name='Adı')),
                ('dogum_tarihi', models.DateField(null=True, verbose_name='Doğum Tarihi')),
                ('tel', models.CharField(max_length=10, verbose_name='Telefon Numarası')),
                ('aolNo', models.CharField(max_length=10, verbose_name='AOL Numarası')),
                ('veli_ad', models.CharField(max_length=50, verbose_name='Veli Adı')),
                ('veli_tel', models.CharField(max_length=10, verbose_name='Veli Tel')),
                ('adres', models.TextField(null=True, verbose_name='Adres')),
                ('aktif', models.BooleanField(default=True)),
            ],
        ),
    ]
