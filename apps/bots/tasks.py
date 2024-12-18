import requests
from bs4 import BeautifulSoup

from core.celery import app
from apps.bots.models import CarBrand, CarModel

from celery import shared_task

BRAND_API_URL = "https://panel.auto.uz/api/v1/car/makes/top/?limit=500"
MODEL_API_URL_TEMPLATE = "https://panel.auto.uz/api/v1/car/{brand_id}/models/?limit=100"


@app.task
def getting_car_brands():
    """
    Fetch car brands and their models from the APIs and save them to the database.
    """
    try:
        # Step 1: Fetch car brands
        brand_response = requests.get(BRAND_API_URL)
        if brand_response.status_code != 200:
            raise Exception(
                f"Failed to fetch car brands. Status code: {brand_response.status_code}"
            )
        brand_data = brand_response.json().get("results", [])

        for brand_item in brand_data:
            brand_name = brand_item.get("name")
            brand_slug = brand_item.get("slug")
            brand_id = brand_item.get("id")

            # Ensure brand exists or create a new one
            brand, created = CarBrand.objects.get_or_create(
                name=brand_name, slug=brand_slug
            )

            # Step 2: Fetch car models for each brand
            model_api_url = MODEL_API_URL_TEMPLATE.format(brand_id=brand_id)
            model_response = requests.get(model_api_url)
            if model_response.status_code != 200:
                print(
                    f"Failed to fetch models for brand {brand_name}. Status code: {model_response.status_code}"
                )
                continue
            model_data = model_response.json().get("results", [])

            for model_item in model_data:
                model_name = model_item.get("name")
                model_slug = f"{brand_slug}-{model_name.lower().replace(' ', '-')}"  # Generate a slug for the model

                # Ensure model exists under the correct brand
                CarModel.objects.get_or_create(
                    name=model_name, slug=model_slug, brand=brand
                )

        print("Car brands and models fetched and saved successfully.")

    except Exception as e:
        print(f"Error while fetching and saving car data: {e}")
