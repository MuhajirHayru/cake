

from django.contrib import admin

from .models import  Item1, About, special,Gallaryy,Category





@admin.register(Item1)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name",  "price")

@admin.register(About)
class aboutAdmin(admin.ModelAdmin):
    list_display = ("id", "email")
    

@admin.register(special)
class specialAdmin(admin.ModelAdmin):
    list_display = ("id", "specialname", "price")

@admin.register(Gallaryy)
class gallary1Admin(admin.ModelAdmin):
    list_display = ("id", "gallaryname")
    
@admin.register(Category)
class gallary1Admin(admin.ModelAdmin):
    list_display = ("id", "Cname")

