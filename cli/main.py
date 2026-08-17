import calendar
from cli.api import get_campground_availability, search_campground_by_name
from cli.processor import (
    extract_available_data,
    extract_search_results,
    format_availability_display,
)


# interactive CLI. searches 1 campground within 1 month (limitation of API). User can add polling/email notification.
def main():
    print("\n=== Rec.gov Availability Checker 2026 ===\n")
    while True:
        # get campground name from user
        search_query = input("👀 Enter campground name to search for: ")
        print(f"Searching for: {search_query}...")
        # get data from api and display results
        search_response = search_campground_by_name(search_query)
        if not search_response:
            print("Failed to fetch")
            return
        campground_options = extract_search_results(search_response)
        if not campground_options:
            print("🙈 No campgrounds found.  Try a a different name.")
            continue
        print(
            f"\n🎉 Found {len(campground_options)} campground(s) matching '{search_query}' \n"
        )
        for i, campground in enumerate(campground_options):
            print(f" {i + 1}. {campground['name']}")
            print("-" * 20)
        name_input = input("Enter the correct number for the campground: ")
        try:
            selection_index = int(name_input) - 1
            if selection_index < 0 or selection_index >= len(campground_options):
                print(
                    f"⚠️ Error: Please enter a number between 1 and {len(campground_options)}"
                )
                continue
            selected_campground_name = campground_options[selection_index]["name"]
            selected_campground_id = campground_options[selection_index]["id"]
        except ValueError:
            print("⚠️ Error: Please enter a valid number")
            continue
        print(f"\n✅ Selected: {selected_campground_name}\n")

        while True:
            # get month from user
            # TODO: maybe add a date picker?
            month_input = input("🗓️ Enter month to search for, eg. 4 for April: ")
            # validate month
            try:
                month = int(month_input)
                if month < 1 or month > 12:
                    print("Error: Month must be between 1-12")
                    continue
            except ValueError:
                print("Error: Please enter a number between 1 and 12")
                continue
            month_name = calendar.month_name[month]
            # option for one-time search or polling
            mode = input(
                "Mode: (1) Check once (2) Start polling and send email notifications:"
            )
            print(
                f"\n🔍 Checking availability for {selected_campground_name} in {month_name}...\n"
            )

            if mode == "2":
                email = input("Enter your email:")
                from cli.poller import poll_loop

                poll_loop(
                    selected_campground_id, selected_campground_name, month, email
                )
                return

            # one time check
            availability_response = get_campground_availability(
                selected_campground_id, month_input
            )

            if not availability_response:
                print("⚠️ Failed to fetch availability_response")
                return

            # Process availability_response
            campsites_info = extract_available_data(availability_response)

            if campsites_info:
                # format and display
                message = format_availability_display(
                    campsites_info, selected_campground_id, month_name
                )
                print(message)
                print("\n 👋 Goodbye! \n")
                return
            else:
                # NOTE: feature idea- possible to find next available date? button on website.
                print(
                    f"😭 No available sites found for {selected_campground_name} in {month_name}"
                )
                try_again = input("Try again? y or n:")
                if try_again == "y":
                    continue
                else:
                    print("👋 Goodbye! \n")
                    return


if __name__ == "__main__":
    main()
