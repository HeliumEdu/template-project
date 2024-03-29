__copyright__ = "Copyright (c) 2024 Helium Edu"
__license__ = "MIT"

import copy
import sys
from concurrent.futures import ThreadPoolExecutor

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from health_check.plugins import plugin_dir
from rest_framework import status
from rest_framework.viewsets import ViewSet


def _run_checks(plugins):
    errors = []

    def _run(plugin):
        plugin.run_check()
        try:
            return plugin.errors
        finally:
            from django.db import connection
            connection.close()

    with ThreadPoolExecutor(max_workers=len(plugins) or 1) as executor:
        for plugin, ers in zip(plugins, executor.map(_run, plugins)):
            if plugin.critical:
                errors.extend(ers)

    return errors


def _build_components_status(plugins):
    components = {}
    system_level = sys.maxsize
    system_status = _("operational")
    for p in plugins:
        components[str(p.identifier())] = {
            "status": p.severity[1] if p.errors else _("operational"),
            "description": p.description,
            "took": round(getattr(p, "time_taken", -1), 4)
        }
        if p.critical and p.errors and p.severity[0] < system_level:
            system_level = p.severity[0]
            system_status = components[str(p.identifier())]["status"]

    return components, system_status


class StatusResourceView(ViewSet):
    """
    status:
    Check the status of the system and its dependencies.
    """

    @method_decorator(never_cache)
    def status(self, request, *args, **kwargs):
        plugins = sorted((
            plugin_class(**copy.deepcopy(options))
            for plugin_class, options in plugin_dir._registry
        ), key=lambda plugin: plugin.identifier())

        errors = _run_checks(plugins)

        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR if errors else status.HTTP_200_OK

        components, system_status = _build_components_status(plugins)

        return JsonResponse(
            {
                "components": components,
                "status": system_status
            },
            status=status_code
        )
