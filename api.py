from fastapi import FastAPI
from poller import poll

from dotenv import load_dotenv, find_dotenv
from Database import Database

from DB_Models.StatusReport import StatusReport
import requests
from requests.exceptions import HTTPError
import time
import schedule
from threading import Thread

# Load the env
load_dotenv(find_dotenv())

# Init the database
db = Database()

# Init the API
api = FastAPI()

# Init the scheduler for the poller
schedule.every(15).minutes.do(poll, db)

# Start a new thread to manage the poller
def manage_poller():
    while True:
        schedule.run_pending()
        time.sleep(1)
thread = Thread(target=manage_poller)
thread.start()


@api.get("/")
async def root():
    return {"message": "API is alive!"}

@api.get("/all")
async def all_status_reports():
    all = db.session.query(StatusReport).order_by(StatusReport.timestamp.desc()).all()
    reports_json = []
    for report in all:
        reports_json.append(report.to_dict())
    return {"message": "Successfully fetched all status reports", "reports": reports_json}