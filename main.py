from Database import Database
from Models.StatusReport import StatusReport
import requests
from requests.exceptions import HTTPError
import time

db = Database()

def fetch_and_store_latest():
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

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    

while (True):
    fetch_and_store_latest()
    print("ran")
    time.sleep(1200) # Every 20 minutes, poll the api

