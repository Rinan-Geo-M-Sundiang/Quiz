from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser


class MyUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )

    filter_horizontal = ('groups', 'user_permissions')
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'groups')

    search_fields = ('email', 'username')
    ordering = ('email',)

# Register the custom user model with the admin interface
admin.site.register(MyUser, MyUserAdmin)
