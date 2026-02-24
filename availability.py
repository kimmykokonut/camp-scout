def check_availability(data):
    """
    Check if any site has available sites
    Returns: dict with {site_id: availability_dict, ...}
    """
    if not data or "campsites" not in data:
        return {}

    available_sites = {}
    for site_id, site_data in data["campsites"].items():
        availability = site_data.get("availabilities", {})
        # filter to only available dates
        available_dates = {
            date: status
            for date, status in availability.items()
            if status == "Available"
        }
        if available_dates:
            available_sites[site_id] = available_dates

    return available_sites
