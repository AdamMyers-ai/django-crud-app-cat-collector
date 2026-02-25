from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from .models import Cat, Feeding

# Register your models here.
for model in (Cat, Feeding):
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        # Avoid autoreload crashes if a model is imported/registered twice.
        pass
