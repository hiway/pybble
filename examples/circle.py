from pybble.pebblejs import UI
from pybble.pebblejs.vector2 import Vector2

wind = UI.Window()
vect = Vector2(72, 84)

circle = UI.Circle(
    position=vect,
    radius=25,
    backgroundColor='white')

wind.add(circle)
wind.show()
