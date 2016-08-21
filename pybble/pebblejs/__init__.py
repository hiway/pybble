def js_require(lib):
    return require(lib)

from .websocket import websocket
from .platform import Platform
from . import UI

__ALL__ = [UI, Platform, websocket]
