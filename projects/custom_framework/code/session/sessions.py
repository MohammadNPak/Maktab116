import hashlib
import random
import json
from app.models import Session as SessionModel
from datetime import datetime, timedelta


from sqlalchemy.orm import Session
from app.migartions import engine
from app.models import User, Post
from sqlalchemy import select


def generate_session_id():
    """Generate a random session ID."""
    return hashlib.sha256(f'{random.random()}'.encode()).hexdigest()


def create_session(user_id):
    """Create a session for a user and return the session ID."""
    session_id = generate_session_id()
    session_value = json.dumps({'user_id': user_id})

    with Session(engine) as session:

        session_model = SessionModel(
            session_id=session_id,
            session_value=session_value,
            expire_date=datetime.now()+timedelta(days=2))

        session.add(session_model)
        session.commit()

    return session_id


def get_session(session_id):
    """Retrieve session data based on the session ID."""

    with Session(engine) as session:
        query = select(SessionModel).where(
            SessionModel.session_id == session_id)
        session_model = session.scalar(query)
        if session_model is None:
            return None
        elif session_model.expire_date < datetime.now():
            return None
        
    return json.loads(session_model.session_value)


def destroy_session(session_id):
    """Remove a session by session ID."""
    if session_id in SESSIONS:
        del SESSIONS[session_id]
