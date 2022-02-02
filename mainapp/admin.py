from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from common.models import User
from mainapp.models.customer import Customer


admin.site.register(User, UserAdmin)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
    )
    search_fields = (
        "name",
        "email",
    )
    ordering = ("name",)
