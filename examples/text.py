from pybble.pebblejs import UI
from pybble.pebblejs.vector2 import Vector2

window = UI.Window()


text = UI.Text(
    position=Vector2(0, 50),
    size=Vector2(144,20),
    textAlign='center',
    font='gothic-24',    
    text="Hello, World!",
    color='white',
    )

window.add(text)
window.show()
