from django.db.migrations.serializer import BaseSerializer, serializer_factory, Serializer

from .enums import Choices


class ChoicesSerializer(BaseSerializer):
    """
    Custom serializer for enumerations.

    Code lifted from https://github.com/django/django/blob/master/django/db/migrations/serializer.py.
    """
    def serialize(self):
        return serializer_factory(self.value.value).serialize()


# Register the custom serializer
Serializer.register(Choices, ChoicesSerializer)
# It is important that the ChoicesSerializer appears before the EnumSerializer in the registry
# The registry is an ordered dict in Django 2.2, so all we can do is move it to the beginning
Serializer._registry.move_to_end(Choices, last=False)
