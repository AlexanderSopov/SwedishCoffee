from django.contrib import admin
from tinymce.widgets import TinyMCE
from django import forms


from .models import Page, MenuItem, Projects, Author, Entry, EmailContact
# Register your models here.
# Minor change to be pushed



class EntryPageForm(forms.ModelForm):
    body_text = forms.CharField(widget=TinyMCE(attrs={'cols': 120, 'rows': 30,}, mce_attrs={'theme': 'advanced'}))


class EntryAdmin(admin.ModelAdmin):
    form = EntryPageForm


admin.site.register(Page)
admin.site.register(MenuItem)
admin.site.register(Projects)
admin.site.register(Author)
admin.site.register(EmailContact)
admin.site.register(Entry, EntryAdmin)