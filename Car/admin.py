from django.contrib import admin
from .models import Car, Brand, Order, Comment
class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'quantity', 'price']
    list_filter = ['brand']
    search_fields = ['name', 'description']

admin.site.register(Car, CarAdmin)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'quantity', 'order_date')
    search_fields = ('user__username', 'car__name')
    list_filter = ('order_date',)

admin.site.register(Comment)



