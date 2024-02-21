from django.contrib import admin

from .models import Package, Subcribtion


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['title', 'sku', 'is_enable', 'price', 'duration']

@admin.register(Subcribtion)
class SubscriptionAdmin(admin.ModelAdmin):
    list_admin = ['user', 'package', 'created_time', 'expire_time']
