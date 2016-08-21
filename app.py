from pybble import console, UI, websocket


def test_websock():
    console.log('creating websocket')
    socket = websocket('ws://192.168.1.204:8000/chat/')
    socket.onopen = lambda e: console.log(
        'Connected. {}'.format(e))
    socket.onerror = lambda e: console.log(
        'Unable to connect. Error: {}'.format(e))


def on_click_up(event):
    """
    A normal function for callback.
    """
    console.log('Up was clicked.')


home = UI.Card(title='Home')  # Initialize the card

# This works, because at runtime, this *is* Javascript
home.body('Use it (almost) like they show in Pebble.js API :)')

# A regular function as callback for click
home.on('click', 'up', on_click_up)

# A nameless function/ lambda for callback
home.on('click', 'select', lambda e: console.log('Select was clicked.'))

# Test webhook
home.on('click', 'up', test_websock)

home.show()  # Show the Card
