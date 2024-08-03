import requests
from . import package_configs

def get_nasa():
    print("fetching nasa APOD...")
    config_nasa = package_configs()
    nasa_url = f'https://api.nasa.gov/planetary/apod?api_key={config_nasa["NASA_KEY"]}'
    try:
        nasa_response = requests.get(nasa_url)
        if nasa_response.status_code == 200:
            nasa_data = nasa_response.json()
            nasa_image = nasa_data["url"]
            nasa_explanation = nasa_data["explanation"]
            return {"nasa_image": nasa_image, "nasa_explanation": nasa_explanation}
        else:
            return {"nasa_image": f"nasa api error with response: {nasa_response}","nasa_explanation": "nasa api error"}
    except:
        print("Fetching failed! There is something wrong with request to the NASA API.")
        return {"nasa_image": "image fetching failed with unknown", "nasa_explanation": "explanation fetching failed"}
