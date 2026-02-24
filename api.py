import requests
from config import API_BASE_URL, HEADERS

# todo: add api call to search by name, grab ID (&other info?)

def get_campground_availability(campground_id, start_date):
  """
  Fetch data from recreation.gov
  Returns: dict with campsites data or None if error
  """
  url = f"{API_BASE_URL}/{campground_id}/month?start_date={start_date}T00%3A00%3A00.000Z"

  try:
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()
  except requests.exceptions.RequestException as e:
    print(f"API Error: {e}")
    return None