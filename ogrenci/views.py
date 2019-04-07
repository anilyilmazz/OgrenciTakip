import pandas
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import OgrenciForm
from .models import Ogrenci


# Create your views here.

def is_member_list(user):
    return user.groups.filter(name__in=['ogretmenler', 'yonetici', 'root']).exists()


def is_member_yonetici(user):
    return user.groups.filter(name__in=['yonetici']).exists()


def home_view(request):
    return render(request, 'home.html', {'title': 'Anasayfa'})


@login_required
@user_passes_test(is_member_list)
def ogrenci_listele(request):
    # print(request.user.groups.all())
    ogrenciler = Ogrenci.objects.all()
    return render(request, 'ogrenci/listele.html', {'ogrenciler': ogrenciler})


@login_required
@user_passes_test(is_member_yonetici)
def ogrenci_ekle(request):
    forms = OgrenciForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        messages.success(request, 'Kayıt Eklendi', extra_tags='Mesaj Başarılı')
        return HttpResponseRedirect('')
    context = {'forms': forms}
    return render(request, 'ogrenci/form.html', context)


@login_required
@user_passes_test(is_member_yonetici)
def Excel(request):
    if request.method == 'POST':
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


@login_required
@user_passes_test(is_member_yonetici)
def ogrenci_duzenle(request, tc):

    ogrenci = get_object_or_404(Ogrenci, tc=tc)
    forms = OgrenciForm(request.POST or None, instance=ogrenci)

    if forms.is_valid():
        forms.save()
        messages.success(request, 'Başarılı Bir Şekilde Güncellediniz.')

        return HttpResponseRedirect(ogrenci.get_list_url())
    context = {'forms': forms, 'ogrenci': ogrenci}
    return render(request, 'ogrenci/updateForm.html', context)


@login_required
@user_passes_test(is_member_yonetici)
def ogrenci_sil(request, tc):
    ogrenci = get_object_or_404(Ogrenci, tc=tc)
    ogrenci.delete()
    return redirect('ogrenci:listele')
