from django.contrib import admin

from .forms import OrderItemForm
from .models import (AllowedCombination, Actor, Room, Order, OrderItem,
                     Prepod)


class PrepodAdmin(admin.ModelAdmin):
    list_display = ['name_prepod', ]


class ActorAdmin(admin.ModelAdmin):
    list_display = ['name_actor', ]


class RoomAdmin(admin.ModelAdmin):
    list_display = ['room', ]


admin.site.register(Actor, ActorAdmin)
admin.site.register(Prepod, PrepodAdmin)
admin.site.register(Room, RoomAdmin)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    #form = OrderItemForm
    
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['date',]


admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    form = OrderItemForm




admin.site.register(OrderItem, OrderItemAdmin)


class AllowedCombinationAdmin(admin.ModelAdmin):
    list_display = ['cat', 'subcat', 'good', ]




admin.site.register(AllowedCombination, AllowedCombinationAdmin)
