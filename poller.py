import time
from datetime import datetime

from api import get_campground_availability
from config import MONITORED_CAMPGROUNDS, POLLING_INTERVAL_MINUTES
from processor import extract_available_data, format_availability_display


# reads campground list from config, loops thru each location, checks avail, waits X minutes, repeats
def poll_campground(campground, month):
    """
    Check avail for 1 campground for 1 month
    """
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
            "sites_info": sites_info,
        }

    return None


def poll_once():
    # run one polling cycle, returns list of dict w availability resutls
    print(f"\n{'='*60}")
    print(
        f"🔍 Starting polling cycle at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )
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

        print()  # blank line
    return results


def get_available_dates_set(sites_info):
    # extract all available dates into a set to compare
    dates = set()
    for site_id, site_data in sites_info.items():
        dates.update(site_data["available_dates"])
    return dates


def find_new_availability(current_results, prev_results):
    # compare, return only new
    prev_lookup = {}
    for prev in prev_results:
        key = f"{prev['campground_id']}_{prev['month']}"
        prev_lookup[key] = get_available_dates_set(prev["sites_info"])

    new_results = []

    for current in current_results:
        key = f"{current['campground_id']}_{current['month']}"
        current_dates = get_available_dates_set(current["sites_info"])

        if key not in prev_lookup:
            new_results.append(current)
            continue
        # find new availabilities
        prev_dates = prev_lookup[key]
        new_dates = current_dates - prev_dates

        if new_dates:
            filtered_sites = {}
            for site_id, site_data in current["sites_info"].items():
                new_dates_for_site = [
                    date for date in site_data["available_dates"] if date in new_dates
                ]
                if new_dates_for_site:
                    filtered_sites[site_id] = {
                        **site_data,
                        "available_dates": new_dates_for_site,
                    }
            if filtered_sites:
                new_results.append({**current, "sites_info": filtered_sites})
    return new_results


def display_results(results, is_new=False):
    # display results found in cycle
    if not results:
        print("😴 No new available sites found in this cycle\n")
        return

    header = "🎉 New availability detected!" if is_new else "Available sites found"

    print(f"\n{'='*60}")
    print(f"🎉{header} -- {len(results)} campground(s)")
    print(f"{'='*60}\n")

    for result in results:
        import calendar

        month_name = calendar.month_name[result["month"]]

        message = format_availability_display(
            result["sites_info"], result["campground_id"], month_name
        )
        print(message)
        print()
        # TODO: send notificaiton here


def run_poller():
    # main poling loop, runs until stopped ctrl+c
    print("\n" + "=" * 60)
    print("🏕️  CAMPGROUND AVAILABILITY POLLER")
    print("=" * 60)
    print(f"Monitoring {len(MONITORED_CAMPGROUNDS)} campground(s)")
    print(f"Checking every {POLLING_INTERVAL_MINUTES} minute(s)")
    print("Press Ctrl+C to stop")
    print("=" * 60 + "\n")

    cycle_count = 0
    prev_results = []

    try:
        while True:
            cycle_count += 1
            print(f"Cycle #{cycle_count}")

            # run 1 cycle
            current_results = poll_once()
            # 1st cycle: show all
            if cycle_count == 1:
                print("\n Initial scan - showing all current availability:")
                display_results(current_results, is_new=False)
            else:
                # only show new availabiliity
                new_availability = find_new_availability(current_results, prev_results)
                display_results(new_availability, is_new=True)

            # store current results for comparision
            prev_results = current_results
            # wait before next cycle
            print(
                f"⏳ Waiting {POLLING_INTERVAL_MINUTES} minute(s) until next check..."
            )
            print(f"{'='*60}\n")

            time.sleep(POLLING_INTERVAL_MINUTES * 60)  # Convert minutes to seconds
    except KeyboardInterrupt:
        print("\n\n Polling stopped by user")
        print(f"Total cycles completed: {cycle_count}")
        print("Goodbye! \n")


if __name__ == "__main__":
    run_poller()
