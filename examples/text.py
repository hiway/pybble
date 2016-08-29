from pybble.pebblejs import UI
from pybble.pebblejs.vector2 import Vector2

wind = UI.Window()
vect = Vector2(72, 84)

text = UI.Text(
    position=vect,
    backgroundColor='white',
    text="Hello, World!",
    )

# circle = UI.Circle(
#     position=vect,
#     radius=50,
#     backgroundColor='white')

wind.add(text)
# wind.add(circle)
wind.show()
