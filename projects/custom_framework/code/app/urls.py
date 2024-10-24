from app.views import (
    register, login,
    index, about, posts_view)

urlpatterns = [
    {"path": "/register", "view": register},
    {"path": "/login", "view": login},
    {"path": "/", "view": index},
    {"path": "/about", "view": about},
    {"path": "/posts", "view": posts_view},
]
