from core.http import render_template

from sqlalchemy.orm import Session
from app.migartions import engine
from app.models import User, Post
from sqlalchemy import select
from session.sessions import create_session

def index(request):
    context = {'title': 'Home', 'message': 'Welcome to the Home Page'}
    return render_template('index.html', context)


def about(request):
    context = {'title': 'About', 'message': 'This is the About Page'}
    return render_template('about.html', context)


def register(request):
    if request.command == "POST":
        data = request.POST

        with Session(engine) as session:
            user = User(
                username=data['username'],
                password=data['password1'],
                email=data['email']
                # addresses=[Address(email_address="spongebob@sqlalchemy.org")],
            )
            session.add(user)
            session.commit()
        return render_template('register.html', {'message':f'user {data["username"]} is registered successfully!'})
        
        
    elif request.command == "GET":
        return render_template('register.html', {})


def login(request):
    """Show the login page or handle login submission."""
    if request.command == 'POST':
        data=request.POST
        username = data.get('username')
        password = data.get('password')
        if username is not None and password is not None:
            with Session(engine) as session:
                query = select(User).where(User.username==username,User.password==password)
                user=session.scalar(query)
                if user:
                    session_id = create_session(user.id)
                    request.send_response(302)
                    request.set_cookie('session_id', session_id)
                    request.send_header('Location', '/')
                    request.end_headers()
                    return ""

            return render_template('login.html', {'error': 'Invalid credentials'})

    return render_template('login.html', {})





def posts_view(request):
    contex = {}
    if request.command == "POST":
        new_post = request.POST.get('new_post')
        # do save model and return response
        return render_template('posts.html', contex)

    elif request.command == "GET":
        return render_template('posts.html', contex)
