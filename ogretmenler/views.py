from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import OgretmenForm
from django.contrib import messages
from .models import Ogretmenler


# Create your views here.


def ogretmen_ekle(request):
    forms = OgretmenForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        messages.success(request, 'Kayıt Eklendi')
        return HttpResponseRedirect('')
    context = {'forms': forms}
    return render(request, 'ogretmenler/EkleForm.html', context=context)


def ogretmen_Listele(request):
    ogretmenler = Ogretmenler.objects.all()
    context = {'ogretmenler': ogretmenler}
    return render(request, 'ogretmenler/ogretmenListele.html', context=context)


def ogretmen_duzenle(request, IDogretmen):
    # if not request.user.is_authenticated:
    #     return Http404()

    ogretmen = get_object_or_404(Ogretmenler, IDogretmen=IDogretmen)
    forms = OgretmenForm(request.POST or None, instance=ogretmen)

    if forms.is_valid():
        forms.save()
        messages.success(request, 'Başarılı Bir Şekilde Güncellediniz.')

        return HttpResponseRedirect(ogretmen.get_list_url())
    context = {'forms': forms, 'ogretmen': ogretmen}
    return render(request, 'ogretmenler/ogretmenUpdateForm.html', context)
