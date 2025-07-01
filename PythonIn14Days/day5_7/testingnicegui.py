from nicegui import ui

ui.label('Hello Beautiful World!')
ui.button('Click Me', on_click=lambda: ui.notify('Clicked!'))

ui.run()
