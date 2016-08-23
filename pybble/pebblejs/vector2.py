_vector2 = require('vector2')

__pragma__('kwargs')

def Vector2(**kwargs):
    return __new__(_vector2, kwargs)

__pragma__('nokwargs')
