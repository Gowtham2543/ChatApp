from api.models import db
from api.app import app

with app.app_context():
    db.create_all()