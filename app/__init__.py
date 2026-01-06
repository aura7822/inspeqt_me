from flask import Flask
from app.extensions import db
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler
from app.tasks import scrape_and_store
from app.scheduler import start_scheduler

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///jobs.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    
    from app.routes import main
    app.register_blueprint(main)


    with app.app_context():
        from app import models
        db.create_all()

        return app

def start_scheduler(app):
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        scrape_and_store,
        trigger="interval",
        hours=6,
        id="job_Scrapper",
        replace_existing = True
    )
    scheduler.start()

    start_scheduler()    
