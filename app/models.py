from datetime   import datetime
from app import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(200))
    company = db.Column(db.String(200))
    location = db.Column(db.String(200))
    url = db.Column(db.String(300), unique=True)
    posted_date = db.Column(db.Date)
    scraped_at = db.Column(db.DateTime, default=datetime.utcnow)