from django.apps import AppConfig


class DjangoEnumsAppConfig(AppConfig):
    """
    Django app config for the django_enums app.
    """
    name = 'django_enums'

    def ready(self):
        # Make sure the custom serializer is registered
        from . import migrations
