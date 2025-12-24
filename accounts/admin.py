from django.contrib import admin
from .models import User
from core.models import Customer
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        ('Something', {"fields": ("phone_number", )}),
        (("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            'Something',
            {
                "classes": ("wide",),
                "fields": ['phone_number'],
            },
        ),
    )
    list_display = ("phone_number", "id", "first_name", "last_name", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("phone_number", "first_name", "last_name")
    ordering = ("id",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    
    
admin.site.register(Customer)