from django.contrib import admin
from .models import*
# Register your models here.

admin.site.register(User)

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name','product_image','price','description','category']

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id','name']


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display= ['name', 'email', 'subject', 'message']