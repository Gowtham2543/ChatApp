from api.models import db
from api.app import app

with app.app_context():
    db.drop_all()