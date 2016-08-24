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


def Circle(**kwargs):
    circle = __new__(__UI.Circle(kwargs))
    return circle

def Text(**kwargs):
    text = __new__(__UI.Text(kwargs))
    return text

def TimeText(**kwargs):
    text = __new__(__UI.TimeText(kwargs))
    return text


# todo: Elements: Circle, Image, Line, Radial, Rect, Text, TimeText


def Accel():
    return require('ui/accel')


def Voice():
    return require('ui/voice')


def Vibe():
    return require('ui/vibe')


def Light():
    return require('ui/light')




__pragma__('nokwargs')
