# TBD entry point for chronjob
import calendar

from api import get_campground_availability, search_campground_by_name
from config import LOCATIONS
from processor import (
    extract_available_data,
    extract_search_results,
    format_availability_display,
)


def main():
    # Step 1: Hardcoded campground for now
    campground_id = LOCATIONS[0]["campground_id"]
    campground_name = LOCATIONS[0]["name"]

    # todo: make this dynamic
    print("\n=== Rec.gove Availability Checker 2026 ===\n")
    # Step 2: get campground name from user
    name_search_input = input("Enter campground name to search for: ")
    print(f"Searching for: {name_search_input}...")
    # validate?
    # get data from api and display results
    name_data = search_campground_by_name(name_search_input)
    if not name_data:
        print("Failed to fetch")
        return
    name_dict = extract_search_results(name_data)

    print(f"Name data results: {name_dict}")




    # Step 3: get month from user
    # NOTE: maybe a date picker?
    month_input = input("Enter month to search for, eg. 4 for April: ")
    # validate month
    try:
        month = int(month_input)
        if month < 1 or month > 12:
            print("Error: Month must be between 1-12")
            return
    except ValueError:
        print("Error: Please enter a number between 1 and 12")
        return
    # get month name
    month_name = calendar.month_name[month]

    print(f"\n Checking availabilty for {campground_name} for { month_name}...\n")

    # Step 3: get data from api
    data = get_campground_availability(campground_id, month_input)

    if not data:
        print("Failed to fetch data")
        return

    # Step 4: Process data
    campsites_info = extract_available_data(data)

    if campsites_info:
        # Step 5: format and display
        message = format_availability_display(campsites_info, campground_id, month_name)
        print(message)
        # Step 6: TBD notificaiotns
    else:
        print(f"No available sites found for {campground_name} in {month_name}")

    # for location in LOCATIONS:
    #     print(f"\nChecking: {location['name']}")

    #     data = get_campground_availability(location["campground_id"], location["date"])

    #     if data:
    #         avail = extract_available_data(data)
    #         if avail:
    #             print(f"Available! {location['name']}")
    #             print(avail)
    #             # TODO: send notificaiton here
    #         else:
    #             print(f"Not available")
    #     else:
    #         print(f"Failed to fetch data")


if __name__ == "__main__":
    main()
