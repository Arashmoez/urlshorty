from django.contrib import admin
from .models import MoezUrl
# Register your models here.
class MoezUrlAdmin(admin.ModelAdmin):
    fields = ['url' , 'shortcode']
    list_display = ['url' , 'shortcode']

admin.site.register(MoezUrl , MoezUrlAdmin)