from django.contrib import admin
from .models import Coupon

@admin.register(Coupon)
class Couponadmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to', 'discount', 'active']
    list_filter = ['active', 'valid_from', 'valid_to']
    seach_fields = ['code']