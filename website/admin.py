from django.contrib import admin

from .models import Page, MenuItem, Projects, Author, Entry
# Register your models here.
admin.site.register(Page)
admin.site.register(MenuItem)
admin.site.register(Projects)
admin.site.register(Author)
admin.site.register(Entry)