from nicegui import ui

ui.label('CONTENT')
[ui.label(f'Line {i}') for i in range(100)]
with ui.header().classes('items-center justify-between'):
    ui.label('HEADER')

ui.run()