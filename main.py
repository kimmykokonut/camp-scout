# TBD entry point for chronjob
import calendar

from api import get_campground_availability, search_campground_by_name

# from config import LOCATIONS
from processor import (
    extract_available_data,
    extract_search_results,
    format_availability_display,
)


def main():
    # Current iteration: interactive console app
    print("\n=== Rec.gov Availability Checker 2026 ===\n")
    # Step 2: get campground name from user
    search_query = input("Enter campground name to search for: ")
    print(f"Searching for: {search_query}...")
    # validate?
    # get data from api and display results
    search_response = search_campground_by_name(search_query)
    if not search_response:
        print("Failed to fetch")
        return
    campground_options = extract_search_results(search_response)
    if not campground_options:
        print("No campgrounds found.  Try a a different name.")
        # restart prompt?
        return
    print(f"\n🎉Found {len(campground_options)} campground(s) matching '{search_query}' \n")
    for i, campground in enumerate(campground_options):
        print(f" {i + 1}. {campground['name']}")
        print("-" * 20)
    # get user input to confirm campground name
    name_input = input("Enter the correct number for the campground: ")
    try:
        selection_index = int(name_input) - 1
        if selection_index < 0 or selection_index >= len(campground_options):
            print(f"Error: Please enter a number between 1 and {len(campground_options)}")
            return
        selected_campground_name = campground_options[selection_index]["name"]
        selected_campground_id = campground_options[selection_index]["id"]
    except ValueError:
        print("Error: Please enter a valid number")
        return
    print(f"\n✅ Selected: {selected_campground_name}\n")

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

    print(f"\n🔍 Checking availability for {selected_campground_name} in {month_name}...\n")

    # Step 3: get data from api
    availability_response = get_campground_availability(selected_campground_id, month_input)

    if not availability_response:
        print("Failed to fetch availability_response")
        return

    # Step 4: Process availability_response
    campsites_info = extract_available_data(availability_response)

    if campsites_info:
        # Step 5: format and display
        message = format_availability_display(campsites_info, selected_campground_id, month_name)
        print(message)
        # Step 6: TBD notificaiotns
    else:
        # feature idea: possible to find next available date? button on website.
        print(f"😭No available sites found for {selected_campground_name} in {month_name}")

if __name__ == "__main__":
    main()
