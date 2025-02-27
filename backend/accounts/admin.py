from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'last_name', 'phone')


admin.site.register(User, UserAdmin)