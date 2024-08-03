# initialize
import dotenv
import os
print("initializing...")

def package_configs():
    # can use prd or uat for differ configs
    dotenv.load_dotenv()
    return {
        "NASA_KEY": os.getenv("NASA_KEY_V1", os.getenv("NASA_KEY"))
    }