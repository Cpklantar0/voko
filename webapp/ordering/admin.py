from django.contrib import admin
from django.db.models.loading import get_models, get_app
from .models import Order, OrderProduct

for model in get_models(get_app('ordering')):
    if model == Order:
        continue
    admin.site.register(model)
    
class OrderProductInline(admin.StackedInline):
    model = OrderProduct
    
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderProductInline,
    ]
    
admin.site.register(Order, OrderAdmin)
