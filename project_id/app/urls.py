from django.conf.urls import url
from rest_framework.documentation import include_docs_urls

from {%PROJECT_ID_LOWER%}.app.admin import admin_site
from {%PROJECT_ID_LOWER%}.app.views.apis.infoviews import InfoResourceView
from {%PROJECT_ID_LOWER%}.app.views.apis.statusviews import StatusResourceView

__author__ = "Alex Laird"
__copyright__ = "Copyright 2019, Helium Edu"
__version__ = "1.0.3"

urlpatterns = [
    # URLs for auto-generated resources
    url('admin/', admin_site.urls, name='admin'),
    url('docs/', include_docs_urls(title='{%PROJECT_NAME%} API Documentation'), name='docs'),

    ##############################
    # Unauthenticated URLs
    ##############################
    url('status/', StatusResourceView.as_view({'get': 'status'}), name='resource_status'),
    url('info/', InfoResourceView.as_view({'get': 'info'}), name='resource_info'),
]
