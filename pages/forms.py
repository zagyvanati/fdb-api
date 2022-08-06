from django import forms
from .models import Page

class PageForm(forms.ModelForm):
  content = forms.CharField( widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
  class Meta:
    model = Page
    fields = ('__all__')