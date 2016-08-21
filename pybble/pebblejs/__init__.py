def js_require(lib):
    return require(lib)


def websocket(url):
    return __new__(WebSocket(url))
