from app.scraper.simple_site import scrape_jobs
from app.models import Job
from app import db
from datetime import datetime

def scrape_and_store():
    jobs=scrape_jobs()
    added=0

    for j in jobs:
        if not j.get("url"):
            continue

        exists = Job.query.filter_by(url=j["url"]).first()
        if exists:
            continue
            
            job = Job(
                title=j.get("title"),
                company=j.get("company"),
                location=j.get("location"),
                url=j.get("url"),
                posted_date=j.get("posted_date")
            )
            db.session.add(job)
            added += 1
            db.session.commit()
            print(f"[{datetime.now()}] Scrape terminated.{added}new jobs")
        