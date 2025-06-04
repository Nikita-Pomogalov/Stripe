from django.contrib import admin
from .models import Item, Tax, Discount, Order

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'currency')

class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ('items', )

admin.site.register(Item, ItemAdmin)
admin.site.register(Discount)
admin.site.register(Tax)
admin.site.register(Order, OrderAdmin)