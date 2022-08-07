from django.contrib import admin
from .models import Page
#from .forms import PageForm
from django.db import models
from tinymce.widgets import TinyMCE

class PagesAdmin(admin.ModelAdmin):
    list_display = ['slug', 'title', 'edited']
    formfield_overrides = {
    models.TextField: {'widget': TinyMCE()}
    }
    #form = PageForm
  
admin.site.register(Page, PagesAdmin)