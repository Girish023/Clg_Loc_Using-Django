from django.contrib import admin
from .models import DjangoVarity, PojectReview, subjects, Certificate
# Register your models here.


class Projectline(admin.TabularInline):
    model=PojectReview
    extra=2

class DjangoVarietyAdmin(admin.ModelAdmin):
    list_display=('name','type','date_added')
    inlines=[Projectline]


class subjectsAdmin(admin.ModelAdmin):
    list_display=('name','location')
    filter_horizontal=('sub_variety',)

class CertificateAdmin(admin.ModelAdmin):
    list_display=('Certi','certificate_number')
admin.site.register(DjangoVarity,DjangoVarietyAdmin)
admin.site.register(subjects,subjectsAdmin)
admin.site.register(Certificate,CertificateAdmin)
