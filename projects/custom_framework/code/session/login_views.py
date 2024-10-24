from core.http import render_template
from core.sessions import create_session, destroy_session

# Dummy user credentials (in real apps, use a database and hashed passwords)
USERS = {
    'admin': 'password123'
}

def login(request):
    """Show the login page or handle login submission."""
    if request.command == 'POST':
        content_length = int(request.headers['Content-Length'])
        post_data = request.rfile.read(content_length)
        post_params = parse_qs(post_data.decode('utf-8'))
        
        username = post_params.get('username', [''])[0]
        password = post_params.get('password', [''])[0]

        if USERS.get(username) == password:
            session_id = create_session(username)
            request.send_response(302)
            request.set_cookie('session_id', session_id)
            request.send_header('Location', '/')
            request.end_headers()
            return ""
        else:
            return render_template('login.html', {'error': 'Invalid credentials'})

    return render_template('login.html', {})

def logout(request):
    """Handle user logout."""
    session_id = request.parse_cookies()
    if session_id:
        destroy_session(session_id)
    request.send_response(302)
    request.delete_cookie('session_id')
    request.send_header('Location', '/')
    request.end_headers()

def index(request):
    """Home page."""
    user = request.get_current_user()
    context = {
        'title': 'Home',
        'message': 'Welcome to the Home Page',
        'user': user
    }
    return render_template('index.html', context)

def protected(request):
    """A protected page that requires login."""
    user = request.get_current_user()
    if not user:
        request.send_response(302)
        request.send_header('Location', '/login')
        request.end_headers()
        return ""
    
    context = {
        'title': 'Protected',
        'message': 'Welcome to the protected page!',
        'user': user
    }
    return render_template('protected.html', context)
