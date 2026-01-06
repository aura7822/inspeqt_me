from flask import render_template
from flask import Blueprint, request, jsonify
from flask import request
from sqlalchemy import or_
from datetime import date, timedelta
from app.models import Job
from app import db
from app.scraper.simple_site import scrape_jobs

main = Blueprint("main", __name__)
@main.route("/")
def dashboard():
    return render_template("dashboard.html")

@main.route("/")
def home():
    return "Inspector is running"
@main.route("/jobs")
def list_jobs():
    jobs=Job.query.all()
    return{
        "count":len(jobs),
        "jobs":[j.title for j in jobs]
    }
@main.route("/scrape")
def scrape():
    jobs = scrape_jobs()
    added = 0

    for j in jobs:
        exists = Job.query.filter_by(url=j["url"]).first()
        if exists:
            continue

        job = Job(
            title=j["title"],
            company=j["company"],
            location=j["location"],
            url=j["url"],
            posted_date=j["posted_date"]
        )

        db.session.add(job)
        added += 1

    db.session.commit()
    return f"Scraping terminated. {added} new jobs added."

@main.route("/jobs/recent")
def recent_jobs():
    keyword = request.args.get("keyword")
    days = int(request.args.get("days",5))

    cutoff = date.today() - timedelta(days=5)
    keyword = request.args.get("q","").strip()
    query = Job.query.filter(Job.posted_date >= cutoff)

    if keyword:
     query = query.filter(Job.tite.ilike(f"%{keyword}%"))

     jobs = query.order_by(Job.posted_date.desc()).all()
     
     return jsonify([
         {
      
        "title":j.title,
        "company":j.company,
        "location":j.location,
        "url":j.url,
        "posted_date":j.posted_date.isoformat()
         }
        for j in jobs 
    
     ])