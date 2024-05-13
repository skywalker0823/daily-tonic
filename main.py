import base64
import functions_framework
import os, dotenv
from fastapi import FastAPI

dotenv.load_dotenv()

TEST = os.getenv("TEST")

def tester():
    print(TEST)

# Triggered from a message on a Cloud Pub/Sub topic.
@functions_framework.cloud_event
def start_daily(cloud_event):
    # Print out the data from Pub/Sub, to prove that it worked
    print("OK")
    print(base64.b64decode(cloud_event.data["message"]["data"]))


# if __name__=="__main__":
#     tester()