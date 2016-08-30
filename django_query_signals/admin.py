"""
Default admin interface setup.
"""
from django.contrib import admin
from .tools import models

# First define custom admin on required models.

# Now register the remaining with the default settings.
for key in models.ALL:
    subject = models.ALL[key]

    if not admin.site.is_registered(subject):
        admin.site.register(subject)