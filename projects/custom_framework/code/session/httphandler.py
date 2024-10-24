from http.cookies import SimpleCookie
from framework.routing import resolve
from framework.sessions import get_session
from jinja2 import Environment, FileSystemLoader
import os

class MyHandler(http.server.SimpleHTTPRequestHandler):

    def parse_cookies(self):
        """Parse cookies from request headers."""
        if 'Cookie' in self.headers:
            cookie = SimpleCookie(self.headers['Cookie'])
            if 'session_id' in cookie:
                return cookie['session_id'].value
        return None

    def get_current_user(self):
        """Retrieve the currently logged-in user from the session."""
        session_id = self.parse_cookies()
        if session_id:
            session = get_session(session_id)
            if session:
                return session['username']
        return None

    def do_GET(self):
        # Check if the requested URL is valid
        view_func, kwargs = resolve(self.path)
        if view_func:
            response = view_func(self, **kwargs)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(response.encode())
        else:
            self.send_error(404, "Page not found")

    def set_cookie(self, name, value):
        """Helper to set a cookie."""
        self.send_header('Set-Cookie', f'{name}={value}; HttpOnly; Path=/')

    def delete_cookie(self, name):
        """Helper to delete a cookie."""
        self.send_header('Set-Cookie', f'{name}=; Max-Age=0; Path=/')

    def render_template(self, template_name, context):
        template_dir = os.path.join(os.getcwd(), 'app', 'templates')
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template(template_name)
        return template.render(context)
