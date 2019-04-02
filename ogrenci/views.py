import pandas

from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ogrenci
from .forms import ogrenci_Ekle_form


# Create your views here.


def home_view(request):
    return render(request, 'home.html', {'title': 'Anasayfa'})


def ogrenci_listele(request):
    ogrenciler = Ogrenci.objects.all()
    return render(request, 'ogrenci/listele.html', {'ogrenciler': ogrenciler})


def ogrenci_ekle(request):
    # if not request.user.is_authenticated:
    #     return Http404()
    forms = ogrenci_Ekle_form(request.POST or None)
    if forms.is_valid():
        forms.save()
        messages.success(request, 'Kayıt Eklendi', extra_tags='Mesaj Başarılı')
        return HttpResponseRedirect('')
    context = {'forms': forms}
    return render(request, 'ogrenci/form.html', context)


def Excel(request):
    if request.method == 'POST':
        # if request.FILES:
        upload_file = request.FILES['document']
        data = pandas.read_excel(io=upload_file, sheet_name=0)  # , encoding='utf-8'
        ogrenciler = []
        for index in range(len(data)):
            ogrenciler.append(Ogrenci())
            ogrenciler[index].tc = data.iloc[index, 0]
            ogrenciler[index].adSoyad = data.iloc[index, 1]

            ogrenciler[index].dogum_tarihi = data.iloc[index, 2]
            ogrenciler[index].tel = data.iloc[index, 3]
            ogrenciler[index].aolNo = data.iloc[index, 4]
            ogrenciler[index].veli_ad = data.iloc[index, 5]
            ogrenciler[index].veli_tel = data.iloc[index, 6]
            ogrenciler[index].adres = data.iloc[index, 7]
        for ogrenci in ogrenciler:
            ogrenci.save()
        return redirect('ogrenci:listele')

    return render(request, 'ogrenci/excelForm.html')


def ogrenci_detay(request, tc):
    ogrenci = get_object_or_404(Ogrenci, tc=tc)
    contex = {
        'ogrenci': ogrenci,
    }
    return render(request, 'ogrenci/detay.html', contex)


def ogrenci_duzenle(request, tc):
    # if not request.user.is_authenticated:
    #     return Http404()
    ogrenci = get_object_or_404(Ogrenci, tc=tc)
    forms = ogrenci_Ekle_form(request.POST or None, request.FILES or None, instance=ogrenci)
    if forms.is_valid():
        forms.save()
        # messages.success(request, 'Başarılı Bir Şekilde Güncellediniz.')
        return HttpResponseRedirect(ogrenci.get_absolute_url())
    context = {'forms': forms}
    return render(request, 'ogrenci/form.html', context)
