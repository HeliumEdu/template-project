from django.conf import settings
from django.contrib.admin import ModelAdmin, sites

__author__ = "Alex Laird"
__copyright__ = "Copyright 2018, Helium Edu"
__version__ = "1.0.2"


class AdminSite(sites.AdminSite):
    """
    Creates a base AdminSite for this project. Models and URLs should be attached to an instance of this class.
    """
    site_header = settings.PROJECT_NAME + " Administration"
    site_title = site_header
    index_title = settings.PROJECT_NAME


class BaseModelAdmin(ModelAdmin):
    """
    All Models that inherit from BaseModel should also inherit from this BaseModelAdmin, which makes sure the common
    attributes are properly rendered in the admin area.
    """
    list_display = ("created_at", "updated_at",)
    ordering = ("-updated_at",)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ("created_at", "updated_at",)

        return self.readonly_fields


# Instantiate the Admin site
admin_site = AdminSite()
