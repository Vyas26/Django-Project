from django.contrib import admin
from .models import sgv,RegIns,om,pj,saifee,bmart_keshav,saras,royal,priya,komal,chaat,panch,kundan,orders

# Register your models here.
class Adminsgv(admin.ModelAdmin):
    list_display = ['name','price']

class AdminRegIns(admin.ModelAdmin):
    list_display = ['name','mobile_no','email','password']

class Adminom(admin.ModelAdmin):
    list_display = ['name','price']

class Adminpj(admin.ModelAdmin):
    list_display = ['name','price']

class Adminsaifee(admin.ModelAdmin):
    list_display = ['name','price']

class Adminbmart_keshav(admin.ModelAdmin):
    list_display = ['name','price']

class Adminsaras(admin.ModelAdmin):
    list_display = ['name','price']

class Adminroyal(admin.ModelAdmin):
    list_display = ['name','price']

class Adminpriya(admin.ModelAdmin):
    list_display = ['name','price']

class Adminkomal(admin.ModelAdmin):
    list_display = ['name','price']

class Adminchaat(admin.ModelAdmin):
    list_display = ['name','price']

class Adminpanch(admin.ModelAdmin):
    list_display = ['name','price']

class Adminkundan(admin.ModelAdmin):
    list_display = ['name','price']

class Adminorders(admin.ModelAdmin):
    list_display = ['name','email','address']

admin.site.register(sgv,Adminsgv)
admin.site.register(RegIns,AdminRegIns)
admin.site.register(om,Adminom)
admin.site.register(pj,Adminpj)
admin.site.register(saifee,Adminsaifee)
admin.site.register(bmart_keshav,Adminbmart_keshav)
admin.site.register(saras,Adminsaras)
admin.site.register(royal,Adminroyal)
admin.site.register(priya,Adminpriya)
admin.site.register(komal,Adminkomal)
admin.site.register(chaat,Adminchaat)
admin.site.register(panch,Adminpanch)
admin.site.register(kundan,Adminkundan)
admin.site.register(orders,Adminorders)