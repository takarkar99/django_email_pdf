from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomAdmin(UserAdmin):

    model = CustomUser
    list_display = ('email','is_active', 'is_superuser')

    ordering = ('email',)
    search_fields = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('permissions', {'fields': ('is_staff', 'is_active', 'email_is_verified')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    

admin.site.register(CustomUser, CustomAdmin)