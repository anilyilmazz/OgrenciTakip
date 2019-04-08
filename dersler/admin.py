from django.contrib import admin

# Register your models here.
from .models import Dersler


class DersAdmin(admin.ModelAdmin):
    class Meta:
        model = Dersler


admin.site.register(Dersler, DersAdmin)
