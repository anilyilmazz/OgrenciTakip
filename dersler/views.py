from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Dersler
from .forms import DersForm
from django.contrib.auth.decorators import login_required, user_passes_test


def is_member_yonetici(user):
    return user.groups.filter(name__in=['yonetici']).exists()


@login_required
@user_passes_test(is_member_yonetici)
def ders_Listele(request):
    dersler = Dersler.objects.all()
    return render(request, 'dersler/listele.html', context={'dersler': dersler})


@login_required
@user_passes_test(is_member_yonetici)
def ders_Ekle(request):
    forms = DersForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        messages.success(request, 'Kayıt Eklendi.')
        return redirect('dersler:listele')
    context = {'forms': forms}
    return render(request, 'dersler/Forms.html', context=context)


@login_required
@user_passes_test(is_member_yonetici)
def ders_Duzenle(request, Id_ders):
    ders = get_object_or_404(Dersler, Id_ders=Id_ders)
    forms = DersForm(request.POST or None, instance=ders)
    if forms.is_valid():
        forms.save()
        messages.success(request, 'Başarılı Bir Şekilde Güncellediniz.')
        return redirect('dersler:listele')
    context = {'forms': forms, 'ders': ders}
    return render(request, 'dersler/Forms.html', context=context)


@login_required
@user_passes_test(is_member_yonetici)
def ders_Sil(request, Id_ders):
    ders = get_object_or_404(Dersler, Id_ders=Id_ders)
    ders.delete()
    messages.success(request, 'Kayıt Silindi.')
    return redirect('dersler:listele')
