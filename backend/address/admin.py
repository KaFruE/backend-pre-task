from django.contrib import admin
from .models import AddressBook, Label

class AddressBookAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

class LabelAdmin(admin.ModelAdmin):
    list_display = ('name','id')

admin.site.register(AddressBook, AddressBookAdmin)
admin.site.register(Label, LabelAdmin)