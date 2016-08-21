# pybble


## Python on Pebble

It's a hack; it works. Here's a barely-even-barebones proof of concept.

## Huh?

  - Transcrypt is a Python => Javascript transpiler
  - Pebble.js lets you write Javascript apps that run directly on your Phone and display on your Pebble
  - Pybble is a bunch of scripts that uses the above two to help you
      transpile a Python app to JS; you can run that on your Pebble smartwatch.
      Tested on a real Pebble Classic, and on emulator for some newer versions.
  - It will be interesting to try the same on rocky.js, and preferably use that.
      I'm using Pebble.js simply because I own an older watch which will not
      get v4 firmware with rocky.js.


## What works?

Mostly nothing - I have only tried what basic 'Hello World' tutorials implement.
I discovered a few hours ago that my Pebble smart watch is already capable of
running Python - this repo is an attempt at making sense of what that means :)

If further experiments are successful and if Python could be used for more than
toy programs, I will continue working on this project to get to feature
parity with Pebble.js (or Rocky.js, whichever works better, or at all)


## Installation

  - `git clone https://github.com/hiway/pybble.git`
  - `cd pybble`
  - `pip install --editable . # Don't miss that last dot`


## Usage

  - Edit app.py in your preferred editor
  - In terminal, run `./build.sh`
  - This will create an app.js file next to your app.py
  - Copy the content of app.js
  - Head over to https://cloudpebble.net/, create a new project
  - Replace contents of app.js on cloudpebble with the minified,
    auto-generated code from your computer.
  - Tap 'Run'

