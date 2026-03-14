# reads campground list from config, loops thru each location, checks avail, waits X minutes, repeats
import time
from datetime import datetime

from api import get_campground_availability
from config import MONITORED_CAMPGROUNDS, POLLING_INTERVAL_MINUTES
from processor import extract_available_data, format_availability_display


def poll_campground(campground, month):
    '''
    Check avail for 1 campground for 1 month
    '''
    campground_id = campground["campground_id"]
    campground_name = campground["name"]

    print(f" Checking {campground_name} for month {month}...")

    # get avail data
    response = get_campground_availability(campground_id, month)

    if not response:
        print(f" Failed to fetch data for {campground_name}")
        return None

    sites_info = extract_available_data(response)

    if sites_info:
        return {
            "campground_name": campground_name,
            "campground_id": campground_id,
            "month": month,
            "sites_info": sites_info
        }

    return None

def poll_once():
    # run one polling cycle, returns list of dict w availability resutls
    print(f"\n{'='*60}")
    print(f"🔍 Starting polling cycle at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")

    results = []

    for campground in MONITORED_CAMPGROUNDS:
        campground_name = campground["name"]
        months = campground["months"]

        print(f"📍 {campground_name}")

        for month in months:
            availability = poll_campground(campground, month)

            if availability:
                results.append(availability)
                print("Found availability")
            else:
                print(f"No availability for month {month}")

        print() # blank line
    return results

def display_results(results):
    # display results found in cycle
    if not results:
        print("No available sites found in this cycle\n")
        return

    print(f"\n{'='*60}")
    print(f"🎉 FOUND {len(results)} CAMPGROUND(S) WITH AVAILABILITY!")
    print(f"{'='*60}\n")

    for result in results:
        import calendar
        month_name = calendar.month_name[result["month"]]

        message = format_availability_display(
            result["sites_info"],
            result["campground_id"],
            month_name
        )
        print(message)
        print()
        # TODO: send notificaiton here

def run_poller():
    # main poling loop, runs until stopped ctrl+c
    print("\n" + "="*60)
    print("🏕️  CAMPGROUND AVAILABILITY POLLER")
    print("="*60)
    print(f"Monitoring {len(MONITORED_CAMPGROUNDS)} campground(s)")
    print(f"Checking every {POLLING_INTERVAL_MINUTES} minute(s)")
    print("Press Ctrl+C to stop")
    print("="*60 + "\n")

    cycle_count = 0

    try:
        while True:
            cycle_count += 1
            print(f"Cycle #{cycle_count}")

            # run 1 cycle
            results = poll_once()
            # display results
            display_results(results)
            # wait before next cycle
            print(f"⏳ Waiting {POLLING_INTERVAL_MINUTES} minute(s) until next check...")
            print(f"{'='*60}\n")

            time.sleep(POLLING_INTERVAL_MINUTES * 60)  # Convert minutes to seconds
    except KeyboardInterrupt:
        print("\n\n Polling stopped by user")
        print(f"Total cycles completed: {cycle_count}")
        print("Goodbye! \n")

if __name__ == "__main__":
    run_poller()