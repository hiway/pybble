"""
Implements the UI class

https://pebble.github.io/pebblejs/#ui
"""

__UI = require('ui')

__pragma__('kwargs')


def Card(**kwargs):
    return __new__(__UI.Card(kwargs))


def Window(**kwargs):
    return __new__(__UI.Window(kwargs))


def Menu(**kwargs):
    return __new__(__UI.Menu(kwargs))


__pragma__('nokwargs')
