import requests
import base64
import re


def convert_image_to_base64(image_url):
    response = requests.get(image_url)
    return base64.b64encode(response.content).decode("utf-8")


def convert_duration_to_minutes(duration_str):
    match = re.search(r"(?:(\d+)h)?\s*(?:(\d+)m)?", duration_str)
    hours = int(match.group(1)) if match.group(1) else 0
    minutes = int(match.group(2)) if match.group(2) else 0
    return hours * 60 + minutes


def convert_country_code(country_url):
    match = re.search(r"country_of_origin=([A-Z]+)", country_url)
    return match.group(1)
