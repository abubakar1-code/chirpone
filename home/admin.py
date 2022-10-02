from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .models import  *

class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff','phone', 'dob' 
        )
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser','groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('phone','dob') , #['phone] for singal field
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser','groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('phone','dob')
        })
    )

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register((Profile,Group,Feelings,BackPost,Post,PostMedia,Page,Story,PostUser,PostComment,PostLike,AddFriend,GroupMember,MchatTheme, MChat, MChatSms,Blockuser))