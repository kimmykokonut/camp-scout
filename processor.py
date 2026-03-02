from datetime import datetime

from config import RESERVE_BASE_URL

# param: json api response for multiple locations, returns sites, availability dict
# def check_multiple_sites_availability(data):
#     """
#     Check if any site has available sites
#     Returns: dict with {site_id: availability_dict, ...}
#     """
#     if not data or "campsites" not in data:
#         return {}

#     available_sites = {}
#     for site_id, site_data in data["campsites"].items():
#         availability = site_data.get("availabilities", {})
#         # filter to only available dates
#         available_dates = {
#             date: status
#             for date, status in availability.items()
#             if status == "Available"
#         }
#         if available_dates:
#             available_sites[site_id] = available_dates

#     return available_sites

# check availability for 1 site by id and month
def extract_available_data(response_data):
    # core logic, returns structured_dict.
    # takes raw API response, returns dict of multiple sites with available dates.
    if not response_data or "campsites" not in response_data:
        return None

    campsites = response_data["campsites"]
    if not campsites:
        return None
    # process all campsites
    available_sites = {}

    for site_id, site_data in campsites.items():
        availabilities = site_data.get("availabilities", {})
        available_dates = [
            date for date, status in availabilities.items() if status == "Available"
        ]
        if available_dates:
            available_sites[site_id] = {
                "site_id": site_id,
                "site_name": site_data.get("site"),
                "campsite_type": site_data.get("campsite_type"),
                "available_dates": available_dates
    }
    return available_sites if available_sites else None

def format_availability_display(campsite_data, campground_id, month_name):
    """
    Format availability display for console display
    Returns: string with formatted availability
    """
    if not campsite_data:
        return None
    # build message
    campsite_count = len(campsite_data)
    message = f"\nFound {campsite_count} site(s) with availablility \n"

    for campsite_id, campsite_info in campsite_data.items():
        name = campsite_info["site_name"]
        dates = campsite_info["available_dates"]
        campsite_type = campsite_info.get("campsite_type", "Unknown")

        #format dates
        formatted_dates = []
        for date in dates:
            # Parse "2026-04-01T00:00:00Z" -> extract month and day
            date_part = date.split("T")[0] # 2026-4-01
            year, month, day = date_part.split("-")
            # remove lead zeros
            formatted_dates.append(f"{int(month)}/{int(day)}")

        message += f"{name} ({campsite_type})\n"
        message += f" Available Dates ({len(formatted_dates)}) for {month_name}: {', '.join(formatted_dates)}\n\n"

    message += f" To reserve, go to: {RESERVE_BASE_URL}/{campground_id}"
    return message

# NOTIFICATIONS TBD
def format_email_message():
    return None

def format_sms_message():
    return None

def format_json_response():
    return None
    # return all?