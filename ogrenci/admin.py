from django.contrib import admin

# Register your models here.
from ogrenci.models import Ogrenci


class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Ogrenci


admin.site.register(Ogrenci, PostAdmin)
