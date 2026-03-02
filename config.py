# API Config
API_BASE_URL = "https://www.recreation.gov/api"
AVAILABILITY_PATH = "camps/availability/campground"
# todo: remove query and make dynamic
SEARCH_PATH = "search?fq=entity_type:campground&size=5"

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

RESERVE_BASE_URL = "https://www.recreation.gov/camping/campgrounds"
