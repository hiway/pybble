# pybble


## Python (almost) on Pebble

It's a hack; it works. Here's a barely-even-barebones proof of concept.

### Hello

```python
    from pybble.pebblejs import console, UI

    home = UI.Card(title='Pybble', subtitle='Says', body='Hello, world!')

    home.show()
```

### Watchface

```python

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
```

### Websocket

```python
    from pybble.pebblejs import console, UI, websocket

    class WebsocketTest(object):
        def __init__(self):
            self.socket = None
            self.connected = False

        def connect(self, url):
            self.socket = websocket.Websocket(url)
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
```

## Huh?

You can write an app for your Pebble watch using your knowledge of 
Python. In the background it gets converted into Javascript
by Transcrypt, This Javascript version of your app gets compiled by 
CloudPebble.net and installed to your phone + watch. Your app 
runs on your phone paired to the Pebble, and sends the UI to and
gets events such as button presses from the watch through Bluetooth. 

This unfortunately makes the interface slightly sluggish compared 
to a native Pebble app. However, you get fewer limits on memory
and better processing speed for heavy lifting behind the 
interface - on your phone.

I recently stumbled into this possiblity and was able to make a hello
world app run. This repository is an exploration-in-progress of 
what else is possible. Star and stick around, fork, tinker and
send pull requests if this sort of thing interests you :)

## But Why?

Because, why not?

  - No real reason except my bias towards Python for being the most versatile 
    proverbial hammer that I use *all the nails* in the world.
  - Because writing Python makes me happy, and reading Python makes me happier.

## You will need:
### A Pebble Watch or Emulator

  - Watch: https://www.pebble.com/
  - Emulator:  https://cloudpebble.net


### PebbleJS

  https://github.com/pebble/pebblejs

Pebble.js lets you write Javascript apps that run on your Phone and
display on your Pebble, giving us freedom to experiment with
pure Python or Javascript libraries.


### Transcrypt

  http://transcrypt.org/

Transcrypt takes your Python code and 'transpiles' it into Javascript
code that is optimized to run inside a Javascript execution engine,
which is what we get when we run a Pebble.js script.

Since it is compiled to JS and does not have a Python runtime like
Brython gives, we have limited access to Python standard library.
However, by substituting them with native Javascript libraries and
writing a little bit of glue code, you can close your eyes and
pretend we're still in Python world. These tradeoffs are what allow
diverse use cases.


### Pybble

  https://github.com/hiway/pybble/

Pybble is an experiment to see if Pebble.js can be used with the help
of Transcrypt to make more than hello world apps.


## What works?

So far:
 - Can create Cards
 - Can hook to button clicks
 - Ajax requests work as expected
 - Websockets work as expected

## What doesn't work?

 - Websockets to LAN won't work on CloudPebble's emulator ;)

## Installation

    git clone https://github.com/hiway/pybble.git
    cd pybble
    pip install --editable . # Don't miss that last dot


## Usage

  - Edit app.py in your preferred editor
  - In terminal, run `pybble build app.py --copy`
  - Head over to https://cloudpebble.net/, create a new Pebble.JS project
  - Replace contents of app.js on cloudpebble with the minified,
    auto-generated javascript code from your computer - which was
    automatically copied to your clipboard by the previous command.
  - Tap 'Run'
