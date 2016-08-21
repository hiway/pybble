"""
With Transcrypt, we are running in javascript environment, hence
pythonic introspection is not available at runtime, making do with
decorators instead.
"""

from pybble.pebblejs import console

tests = []


def test(wrapped):
    tests.append(wrapped)
    def wrapper():
        return wrapped
    return wrapper()


@test
def test_console():
    console.log('Hello from Console Test, let us begin.')



for run_test in tests:
    run_test()
