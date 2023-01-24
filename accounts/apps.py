from django.apps import AppConfig


# Created when Django App created. Added connection to
# Django project settings.py file under INSTALLED_APPS
class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"
