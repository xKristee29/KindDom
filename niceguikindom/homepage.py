from nicegui import ui,app

app.add_static_files("/static", "static")

ui.add_head_html('''
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/static/homepage.css">
    <link rel="stylesheet" href="/static/navbar.css">
    <title>Document</title>
''')

"""
ui.add_body_html(''' <div class="navbar">

            <p class="logo">Logo</p>

            <div class="infos-container">
                <div class="info">Activities</div>
                <div class="info">Resources</div>
                <div class="info">About Us</div>   
            </div>

            <div class="user-container">
                <div class="user-info">Username</div>
                <div class="user-info">PFP</div>
            </div>

        </div>
        <div class="homepage">
            <div class="first">
                <div class="label-container">
                    <div class="title">TITLU</div>
                    <div class="subtitle">My nigga is black</div>
                </div>
                <div class="image">
                    <img class="homepage-image" src="https://media.discordapp.net/attachments/880529479515115580/1094231477862023289/firstPanel.jpg?width=1005&height=670">
                </div>
            </div>

        </div>''')"""
with ui.header().classes('navbar'):
    with ui.element('p').classes('logo'):
        ui.label('Logo')
    with ui.element('div').classes('infos-container'):
        with ui.element('div').classes('info'):
            ui.label('Activities')
        with ui.element('div').classes('info'):
            ui.label('Resources')
        with ui.element('div').classes('info'):
            ui.label('About Us')
    with ui.element('div').classes('user-container'):
        with ui.element('div').classes('user-info'):
            ui.label('Username')
        with ui.element('div').classes('user-info'):
            ui.label('PFP')
            
def render_homepage():
    ui.add_body_html('''
    <br/>
    <div class="homepage">
            <div class="first">
                <div class="label-container">
                    <div class="title">TITLU</div>
                    <div class="subtitle">My nigga is black</div>
                </div>
                <div class="image">
                    <img class="homepage-image" src="https://media.discordapp.net/attachments/880529479515115580/1094231477862023289/firstPanel.jpg?width=1005&height=670">
                </div>
            </div>

        </div>''')



ui.run(title="Kindoom")