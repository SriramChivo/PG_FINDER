from django.contrib import admin
from .models import UserProfiles, UserFiles
# from django.core.exceptions import ObjectDoesNotExist
# Register your models here.
admin.site.register(UserFiles)
@admin.register(UserProfiles)
class UserAdmin(admin.ModelAdmin):

    list_display = ("username", "user_Address", "user_phone_number", "email")

    def username(self, instance):
        try:
            get_username = instance.user_id.username
            return get_username
        except instance.__class__.DoesNotExist:
            raise ValueError("User is not available")

    def email(self, instance):
        try:
            get_username = instance.user_id.email
            return get_username
        except instance.__class__.DoesNotExist:
            raise ValueError("User is not available")
