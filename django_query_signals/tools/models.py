"""
Fetching models via app.
"""
from django.apps import apps as _apps
from .. import __info__

# pylint: disable=no-member, protected-access
# We go through this effort so that we can use this everywhere and don't have
# to be concerned about import conflicts during django start-up.
ALL = dict()
for _ in _apps.get_app_config(__info__.LABELS['name']).get_models():
    if _._meta.app_label == __info__.LABELS['name']:
        ALL[_.__name__] = _
        globals()[_.__name__] = _


