import os
from dotenv import load_dotenv

load_dotenv()

# API Config
API_BASE_URL = "https://www.recreation.gov/api"
AVAILABILITY_PATH = "camps/availability/campground"
# TODO: remove query and make dynamic
SEARCH_PATH = "search?fq=entity_type:campground&size=5"

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

RESERVE_BASE_URL = "https://www.recreation.gov/camping/campgrounds"

# Polling Config
POLLING_INTERVAL_MINUTES = 1
YEAR = 2026  # hardcoded for now

# Notification
EMAIL_ENABLED = True
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# campgrounds to monitor
MONITORED_CAMPGROUNDS = [
    {"name": "Gotchen Guard Station", "campground_id": 10277125, "months": [4, 5, 6]},
    {"name": "Fivemile Butte Lookout", "campground_id": 234248, "months": [4]},
]
