from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # This controls the "Edit User" page
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'phone', 'is_verified')}),
    )
    
    # This controls the "Add User" page (which you are currently looking at)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'phone', 'is_verified')}),
    )

    list_display = ('username', 'email', 'role', 'is_staff', 'is_verified')
    list_filter = ('role', 'is_verified', 'is_staff')