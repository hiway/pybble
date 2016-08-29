from pybble.pebblejs import UI
from pybble.pebblejs.vector2 import Vector2

txt_time = UI.TimeText(
    position=Vector2(0, 40),
    size=Vector2(144, 50),
    text='%H:%M',
    font='BITHAM_42_LIGHT',
    color='black',
    textAlign='center',
    backgroundColor='white'
)

txt_date = UI.TimeText(
    position=Vector2(0, 90),
    size=Vector2(144, 30),
    text='%a %d %b',
    font='GOTHIC_24',
    color='black',
    textAlign='center',
    backgroundColor='white'
)


window = UI.Window(fullscreen=True, backgroundColor='white')

window.add(txt_time)
window.add(txt_date)
window.show()
