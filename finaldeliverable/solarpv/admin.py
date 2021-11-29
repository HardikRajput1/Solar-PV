from django.contrib import admin
from .models import User, Client, Location, Product, TestStandard, Certificate

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first', 'email']
    list_filter = ['choose_user', 'prefix']
    search_fields = ['first', 'middle', 'last']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['clientname', 'clienttype']
    list_filter = ['clienttype']
    search_fields = ['clientname', 'clienttype']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['city', 'pincode']
    list_filter = ['city', 'state']
    search_fields = ['city', 'pincode', 'state']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['modelnum', 'mname']
    search_fields = ['mname', 'cellmanu', 'modelnum']

@admin.register(TestStandard)
class TestStandardAdmin(admin.ModelAdmin):
    list_display = ['stdname', 'pubdate']
    list_filter = ['pubdate']
    search_fields = ['stdname', 'pubdate']

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    search_fields = ['reportnum', 'certissue']
    list_display = ['reportnum', 'certissue', 'modelnum']