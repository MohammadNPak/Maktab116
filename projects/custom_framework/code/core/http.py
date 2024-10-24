import http.server
from jinja2 import Environment, FileSystemLoader
from core.routing import resolve
import os
from urllib.parse import parse_qsl, urlparse
from http.cookies import SimpleCookie
from session.sessions import get_session



class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        view_func, kwargs = resolve(self.path)
        if view_func:
            response = view_func(self, **kwargs)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(response.encode())
        else:
            self.send_error(404, "Page not found")

    def post_data(self):
        content_length = int(self.headers.get("Content-Length", 0))
        return self.rfile.read(content_length)

    def form_data(self):
        self.POST=dict(parse_qsl(self.post_data().decode("utf-8")))
    
    def do_POST(self):
        view_func, kwargs = resolve(self.path)
        if view_func:
            self.form_data()
            response = view_func(self, **kwargs)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(response.encode())
        else:
            self.send_error(404, "Page not found")
    
    
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
                return session['user_id']
        return None
    
    def set_cookie(self, name, value):
        """Helper to set a cookie."""
        self.send_header('Set-Cookie', f'{name}={value}; HttpOnly; Path=/')

    def delete_cookie(self, name):
        """Helper to delete a cookie."""
        self.send_header('Set-Cookie', f'{name}=; Max-Age=0; Path=/')

    
    
    
def run_server(urlpatterns):
    PORT = 8000
   
    with http.server.HTTPServer(("", PORT), MyHandler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()

def render_template(template_name, context):
    template_dir = os.path.join(os.getcwd(), 'app', 'templates')
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)
    return template.render(context)
