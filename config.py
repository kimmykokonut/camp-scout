# location dict/api endpoint, const
# later file to store results if 200?

# API Config
API_BASE_URL = "https://www.recreation.gov/api/camps/availability/campground"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# Locations to monitor
# later: put lat/long? or pull from future search? dog friendly? sleeps x ppl. season.
LOCATIONS = [
  {
    "name": "Gotchen Guard Station",
    "campground_id": 10277125,
    "date": "2026-04-01"
  },
  {
    "name": "Fivemile Butte Lookout",
    "campground_id": 234248,
    "date": "2026-04-01"
  },
  {
    "name": "Mineral Springs Guard Station",
    "campground_id": 234091,
    "date": "2026-04-01"
  },
  {
    "name": "Ditch Creek Guard Station",
    "campground_id": 234145,
    "date": "2026-04-01"
  },
  {
    "name": "Clear Lake Cabin Lookout",
    "campground_id": 234247,
    "date": "2026-04-01"
  },
]