from apscheduler.schedulers.background import BackgroundScheduler
from app.tasks import scrape_and_store

scheduler = BackgroundScheduler()

def start_scheduler():
    if not scheduler.running:
        scheduler.add_job(
            scrape_and_store,
            trigger="interval",
            hours=6,
            id="job_scrapper,",
            replace_existing=True
            
        )
        scheduler.start()