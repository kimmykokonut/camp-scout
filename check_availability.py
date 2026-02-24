import requests

# test individual api calls

# todo: add search to get campground id by name (new api call)
campground_id = "10277125"  # entire campground

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# todo: add date range selection (new api call)
response = requests.get(
    f"https://www.recreation.gov/api/camps/availability/campground/{campground_id}/month?start_date=2026-04-01T00%3A00%3A00.000Z",
    headers=headers,
)

response_dict = response.json()

campsite_count = len(response_dict["campsites"])
campsite_id = response_dict["campsites"]
# print(f'site id: {campsite_id}')
print(f"campsite count: {campsite_count}")

print(f"Status Code: {response.status_code}")
# print(f"Response Text: {response.text}")
print(f"Site name: {response_dict['campsites']['10277126']['site']}")

availability_dict = response_dict["campsites"]["10277126"]["availabilities"]

if len(availability_dict) > 0:
    print("Site is available! \n ")
    print(availability_dict)
else:
    print("Site is not available.")
