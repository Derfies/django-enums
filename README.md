# django-enums

This package provides a backport of the
[Enumeration Types](https://docs.djangoproject.com/en/3.0/ref/models/fields/#enumeration-types)
for Django model field types from Django 3.0 to Django 2.x.

## Installation

Install directly from GitHub:

```sh
pip install git+https://github.com/cedadev/django-enums.git
```

Add the `django_enums` app to `INSTALLED_APPS` in your `settings.py`:

```python
INSTALLED_APPS = [
    # Other apps
    'django_enums',
    # Other apps
]
```

## Usage

Use is as described in the
[Django 3.0 documentation](https://docs.djangoproject.com/en/3.0/ref/models/fields/#enumeration-types),
except that `Choices`, `TextChoices` and `IntegerChoices` are imported from `django_enum`.
