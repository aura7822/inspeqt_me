import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_me():
    jobs=[]
    r= requests.get("https://www.myjobmag.co.ke/", headers={
        "User-Agent":"Mozilla/5.0"
    })

    soup = BeautifulSoup(r.text, "lxml.parser")

    for card in soup.select(".job"):
        posted = datetime.strptime(
            card.select_one(".date").textstrip(),
            "%d %b %Y"
        ).date()

        jobs.append({
            "title":card.select_one(".title").text.strip,
            "company":card.select_one(".company").text.strip(),
            "loction": "Remote",
            "posted_date": posted,
            "url":card.select_one("a")["href"]
        })
        return jobs