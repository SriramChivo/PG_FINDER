from django.contrib import admin
from .models import PayingGuest, PgImage, PgCot, PgRoom, Comment
# Register your models here.
@admin.register(PayingGuest, PgImage, PgCot, PgRoom, Comment)
class PayingGuestAdmin(admin.ModelAdmin):
    pass
