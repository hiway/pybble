from pybble import console, UI, websocket


class WebsocketTest(object):
    def __init__(self):
        self.socket = None
        self.connected = False

    def connect(self, url):
        self.socket = websocket(url)
        self.socket.onerror = self.on_error
        self.socket.onopen = self.on_open
        self.socket.onclose = self.on_close
        self.socket.onmessage = self.on_message

    def on_error(self, error):
        self.connected = False
        console.log('Failed to connect.')
        console.log('Error: \n{}'.format(error))

    def on_open(self, event):
        self.connected = True
        console.log('Connected')
        self.send('Hello Websockets!')

    def on_close(self, event):
        self.connected = False
        console.log('Disconnected')

    def send(self, message):
        console.log('SEND: '.format(message))
        self.socket.send(message)

    def on_message(self, message):
        console.log('RECV: '.format(message.data))
        msg = UI.Card(title='RECV', body=message.data)
        msg.show()


wsecho = WebsocketTest()

home = UI.Card(title='Pybble!', subtitle='Python Apps for Pebble')
home.body('Click SELECT to connect to Echo websocket, and UP/DOWN'
          'buttons to send messages to test the connection.')

home.on('click', 'up', lambda e: wsecho.send('WS: Up was clicked'))
home.on('click', 'select', lambda e: wsecho.connect('wss://echo.websocket.org'))
home.on('click', 'down', lambda e: wsecho.send('WS: Down was clicked'))

home.show()
