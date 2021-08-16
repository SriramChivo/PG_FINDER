from .base import *
INSTALLED_APPS += [
    "user_accounts.apps.UserAccountConfig",
    "paying_guest.apps.PayingGuestConfig",
    "base.apps.BaseConfig",
    "django_celery_beat"
]
