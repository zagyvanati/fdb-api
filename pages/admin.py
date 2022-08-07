from django.contrib import admin
from .models import Page
from .forms import PageForm

class PagesAdmin(admin.ModelAdmin):
    list_display = ['slug', 'title', 'edited']
    form = PageForm
  
admin.site.register(Page, PagesAdmin)