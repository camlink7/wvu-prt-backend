from dotenv import load_dotenv, find_dotenv
from Database import Database

from DB_Models.StatusReport import StatusReport
import requests
from requests.exceptions import HTTPError
import time


def poll(db):
    try:
        # Fetch the latest JSON from the api
        current_epoch = int(time.time())
        api_url = "https://prtstatus.wvu.edu/api/" + str(current_epoch) + "/?format=json"
        response = requests.get(api_url)
        response.raise_for_status()
        json = response.json()

        # Fetch and merge the latest status report
        latest = StatusReport(int(json["timestamp"]), int(json["status"]), str(json["message"]), int(json["bussesDispatched"]))
        db.session.merge(latest)
        db.session.commit()

        print("Polled PRT API @ " + str(int(time.time())))

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
<<<<<<< HEAD:main.py
    

while (True):
    fetch_and_store_latest()
    print("ran")
    time.sleep(1200) # Every 20 minutes, poll the api
=======
>>>>>>> 9208448acd5957a98aa125cc029b2fd17f0b8ac2:poller.py

