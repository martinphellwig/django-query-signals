"""
Application Init
"""
import os

from django.apps import AppConfig as _APPCFG
from django.dispatch import receiver

from . import __info__
from .signals import (pre_update, post_update,
                      pre_delete, post_delete,
                      pre_bulk_create, post_bulk_create,
                      pre_get_or_create, post_get_or_create,
                      pre_update_or_create, post_update_or_create)

_ = os.path.abspath(__file__)
_ = os.path.dirname(_)
_ = os.path.split(_)[1]
__info__.LABELS['path'] = _

def _ready(self):
    return _APPCFG.ready(self)

_ = globals()

_[__info__.LABELS['class']] = \
    type(__info__. LABELS['class'], (_APPCFG,),
         {'ready':_ready, 'name':__info__.LABELS['name'],
          'verbose_name':__info__.LABELS['verbose_name']})

_['default_app_config'] = __info__.LABELS['path'] \
                          + '.' + __info__.LABELS['class']

