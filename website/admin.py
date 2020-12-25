from django.contrib import admin

from website.models import UrlMapping

@admin.register(UrlMapping)
class UrlMappingAdmin(admin.ModelAdmin):
    """UrlMapping model admin."""
    pass
