# Recreation.gov Reservation Alert

## What

A personal Python polling script that monitors Recreation.gov for campsite availability by specified campsite and month. Sends email notifications when reservations become available while polling is active.

## Why

Popular campsites on Recreation.gov book up months in advance. This script continuously checks for cancellations so you can snag last-minute reservations that would otherwise be impossible to find manually.

## Tech Stack

- **Python 3.11**
- **Libraries:** `requests`, `python-dotenv`
- **API:** Recreation.gov internal API
- **Notifications:** TBD (Email)

---

## Setup

1. Create the Conda environment:

```bash
conda env create -f environment.yml
```

2. Activate it:

```bash
conda activate reservation-alert
```

3. Troubleshooting - If you get `ModuleNotFoundError`:

```bash
conda env update -f environment.yml --prune
```

4. Run the CLI:

```bash
python3 main.py
```

5. Follow the prompts:

- Enter a campground name to search for
- Choose the campground by number
- Enter the month number to check availability

CLI One time search
![CLI screenshot](/assets/cli-single-search.png)

---

## Roadmap

### Phase 1: MVP

- [x] Discover and test Recreation.gov API endpoints
- [x] Hardcoded search for specific sites
- [x] Hardcoded date range (April 2026)

### Phase 2: Configurable

- [x] Make interactive console app
- [x] Results from user input month, year 2026 (No date range options yet)
- [x] User keyword search for name, display top 5, user selects 1, id used to get availability
- [x] Handle different campground types (guard stations vs multi-site campgrounds)
- [ ] Configuration file for user preferences

### Phase 3: Cron Job & Notifications

- [x] Polling loop (check every X minutes)
- [ ] Save success results to file
- [x] Basic notification system: email
- [ ] Cron job setup

### Phase 4: Future Enhancements

- [ ] Search by location (zip?) and specific date range (if possible via API)
- [ ] Web app interface or Mobile app
- [ ] SMS notifications

---

## Notes

- Official RIDB API at https://ridb.recreation.gov/docs does not include availability data
- Endpoints discovered via browser network inspection and other open-source projects on github.
