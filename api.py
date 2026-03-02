import requests

from config import API_BASE_URL, AVAILABILITY_PATH, HEADERS, SEARCH_PATH


def search_campground_by_name(name):
  """
  Searches for campground by name
  Returns: dict with campground data for first 5 hits or None if error
  """
  url = f"{API_BASE_URL}/{SEARCH_PATH}&q={name}"

  try:
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()
  except requests.exceptions.RequestException as e:
    print(f"API Error: {e}")
    return None

def get_campground_availability(campground_id, month_input):
  """
  Fetch data from recreation.gov
  Returns: dict with campsites data or None if error
  """
  month_str = str(month_input).zfill(2) # 4-> 04
  url = f"{API_BASE_URL}/{AVAILABILITY_PATH}/{campground_id}/month?start_date=2026-{month_str}-01T00%3A00%3A00.000Z"

  try:
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()
  except requests.exceptions.RequestException as e:
    print(f"API Error: {e}")
    return None