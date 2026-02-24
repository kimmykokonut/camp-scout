# entry point for chronjob
from config import LOCATIONS
from api import get_campground_availability
from availability import check_availability


def main():
    for location in LOCATIONS:
        print(f"\nChecking: {location['name']}")

        data = get_campground_availability(location["campground_id"], location["date"])

        if data:
            avail = check_availability(data)
            if avail:
                print(f"Available! {location['name']}")
                print(avail)
                # TODO: send notificaiton here
            else:
                print(f"Not available")
        else:
            print(f"Failed to fetch data")


if __name__ == "__main__":
    main()
