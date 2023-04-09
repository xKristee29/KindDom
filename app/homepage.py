from nicegui import ui, app
import random
from tinydb import TinyDB, Query
import hashlib

app.add_static_files("/static", "static")

tasks = []

with open('tasks.txt', 'r') as f:
    for line in f:
        tasks.append(line)

db = TinyDB('db.json')
User = Query()

iduser = ""
username = ""


@ui.page("/loginfailed")
def login_failed():
    ui.add_head_html('''<meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta ="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/static/login.css">
    ''')
    ui.html('<h1 class="title">Login Failed</h1>')
    ui.html('<p class="text">The user or password you entered is incorrect.</p>')


def render_navbar():
    with ui.header().classes('navbar'):
        with ui.element('p').classes('logo'):
            ui.html('<a href="/home">Kindoom</a>')
        with ui.element('div').classes('infos-container'):
            with ui.element('div').classes('info'):
                ui.html('<a href="/activities">Activities</a>')
            with ui.element('div').classes('info'):
                ui.html('<a href="/home">Resources</a>')
            with ui.element('div').classes('info'):
                ui.html('<a href="/aboutus">About Us</a>')
        with ui.element('div').classes('user-container'):
            with ui.element('div').classes('user-info'):
                ui.html(f'<a href="/home">{username}</a>')
            with ui.element('div').classes('user-info'):
                ui.html('<a href="/home">PFP</a>')


@ui.page('/activities')
def render_activities():
    ui.add_head_html('''
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta ="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="/static/activities.css">
        <link rel="stylesheet" href="/static/navbar.css">
    ''')

    render_navbar()

    ui.add_body_html('''
        <div class="panel1">
    
            <div class="subpanel1">
                Be the best version of yourself!
                <button onClick = "location.href = '/task_roulette'" class="button1">
                    TASK GENERATOR
                </button>
            </div>

            </div>

        <div class='transition'>
        .
        </div>

            <div class="panel2">
                <div class='subpanel1'>
            <h1>
                More about yourself
            </h1>
            <p>Take A Survey Now</p>
            <button class="button1"> Personality Test </button>
            </div>
            </div>

            <div class='transition'>
        .
            </div>

            <div class="panel3">
        <div class='subpanel1'>
            <h1>
                Daily Journal
            </h1>
            <button class="button1">Write down your thoughts</button>
            </div>
            </div>

    </div>
    ''')


def go_to_task_roulette(cont):
    cont.clear()
    ui.open('/task_roulette')


@ui.page('/task_roulette')
def render_roulette():
    ui.add_head_html('''
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta ="viewport" content="width=device-width, initial-scale=1.0">
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
        for i, task in enumerate(picked):
            ui.html(
                f'<div id="task{i}" class="tasks">{task} <button class="remove" onclick="remelem(\'task{i}\')">X</button></div>')


@ui.page('/home')
def render_homepage():
    ui.add_head_html('''
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta ="viewport" content="width=device-width, initial-scale=1.0">
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
                    <div class="title">KINDOOM</div>
                    <div class="subtitle">Your companion on your self-improvement journey</div>
                </div>
                <div class="image">
                    <img class="homepage-image" src="https://media.discordapp.net/attachments/880529479515115580/1094231477862023289/firstPanel.jpg?width=1005&height=670">
                </div>
            </div>

        </div>''')

@ui.page('/aboutus')
def render_aboutus():
    ui.add_head_html('''
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta ="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="/static/aboutus.css">
        <link rel="stylesheet" href="/static/navbar.css">
    ''')

    render_navbar()

    ui.add_body_html('''
    <div class="about-container">
            <div class="title-about">DESPRE NOI</div>
            <div class="text-about">
                &nbsp;&nbsp;&nbsp;&nbsp;Scopul aplicației noastre este de a ajuta utilizatorii sa-si imbunatateasca viata prin indeplinirea sarcinilor zilnice sau saptamanale. 
                In plus, aplicatia este echipata cu o aplicatie de notite si resurse utile pentru gestionarea timpului si dezvoltarea personala. 
                <br/>
                <br/>
                &nbsp;&nbsp;&nbsp;&nbsp;Acest cod reprezinta un component React care genereaza sarcini zilnice sau saptamanale dintr-un array de provocari predefinite. 
                Aplicatia include, de asemenea, o functie pentru gestionarea notitelor si resurselor pentru dezvoltare personala.
                <br/>
                <br/>
                &nbsp;&nbsp;&nbsp;&nbsp;Array-ul provocari 
                contine o serie de provocari prestabilite. 
                <br/>
                Functia SelectTasks selecteaza un numar specificat de provocari in mod aleatoriu din array-ul provocari. 
                Pentru fiecare sarcina afisata, exista 
                si un buton "X" care permite utilizatorului sa elimine sarcina din lista. Componenta Tasks include, de asemenea, un stil CSS pentru a formata 
                lista de sarcini si butoanele asociate. 
            </div>
    </div>
    ''')

def login_checker(user, password):
    passhash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    result = db.search(User.user == user and User.password == passhash)
    if len(result) > 0:
        global iduser
        global username
        iduser = result[0]['id']
        username = result[0]['username']
        ui.open('/home')
        return True
    ui.open('/loginfailed')
    return False


def render_login():
    ui.add_head_html('''
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta ="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap" rel="stylesheet">
    ''')

    ui.add_body_html('''
    <link rel="stylesheet" href="/static/login.css">
    ''')

    with ui.element('div').classes('login-box'):
        ui.html('''<h1>Login</h1>''')
        with ui.element('div').classes('container'):
            userin = ui.input(placeholder='Enter Username', label='Username')
            pasin = ui.input(password=True, password_toggle_button=True,
                             placeholder='Enter Password', label='Password')
            ui.button('Login', on_click=lambda: login_checker(
                userin.value, pasin.value))


render_login()

ui.run(native=True, title="Kindoom")
