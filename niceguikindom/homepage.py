from nicegui import ui,app
import random

app.add_static_files("/static", "static")

tasks = []

with open('tasks.txt', 'r') as f:
    for line in f:
        tasks.append(line)

def render_navbar():
    with ui.header().classes('navbar'):
        with ui.element('p').classes('logo'):
            ui.html('<a href="/home">Logo</a>')
        with ui.element('div').classes('infos-container'):
            with ui.element('div').classes('info'):
                ui.html('<a href="/activities">Activities</a>')
            with ui.element('div').classes('info'):
                ui.html('<a href="/resources">Resources</a>')
            with ui.element('div').classes('info'):
                ui.html('<a href="/aboutus">About Us</a>')
        with ui.element('div').classes('user-container'):
            with ui.element('div').classes('user-info'):
                ui.html('<a href="/profile">Username</a>')
            with ui.element('div').classes('user-info'):
                ui.html('<a href="/profile">PFP</a>')

@ui.page('/activities')
def render_activities():
    ui.add_head_html('''
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="/static/activities.css">
        <link rel="stylesheet" href="/static/navbar.css">
    ''')

    render_navbar()
    
    cont = ui.column()

    with cont:
        ui.html('<h1 class="kindom">Kindness Roulette</h1>')
        ui.button('Tasks', on_click=lambda: go_to_task_roulette(cont))

def go_to_task_roulette(cont):
    cont.clear()
    ui.open('/task_roulette')
    
@ui.page('/task_roulette')
def render_roulette():
    ui.add_head_html('''
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="/static/activities.css">
        <link rel="stylesheet" href="/static/navbar.css">
        <script>
            function remelem(id){
                document.getElementById(id).remove();
            }
        </script>
    ''')

    render_navbar()

    ui.html('<h1 class="kindom">Kindness Roulette</h1>')
    cont = ui.column()
    with cont:
        ui.button('GENERATE TASKS', on_click=lambda: generate_tasks(cont))

def generate_tasks(cont):
    cont.clear()
    picked = random.sample(tasks, 7)
    with cont:
        ui.html('<p class="text-task">Those are your tasks for today!</p>')
        for i,task in enumerate(picked):
            ui.html(f'<div id="task{i}" class="tasks">{task} <button class="remove" onclick="remelem(\'task{i}\')">X</button></div>')

@ui.page('/home')
def render_homepage():
    ui.add_head_html('''
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="/static/homepage.css">
        <link rel="stylesheet" href="/static/navbar.css">
    ''')

    render_navbar()

    ui.add_body_html('''
    <br/>
    <div class="homepage">
            <div class="first">
                <div class="link-container">
                    <div class="title">TITLU</div>
                    <div class="subtitle">My nigga is black</div>
                </div>
                <div class="image">
                    <img class="homepage-image" src="https://media.discordapp.net/attachments/880529479515115580/1094231477862023289/firstPanel.jpg?width=1005&height=670">
                </div>
            </div>

        </div>''')

ui.button('REDIRECT', on_click=lambda: ui.open('/home'))

ui.run(title="Kindoom")