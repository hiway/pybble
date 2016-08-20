from pybble import console, UI

home = UI.Card(title='Home')
home.on('click', 'select', lambda e: console.log('Select was clicked.'))
home.show()
