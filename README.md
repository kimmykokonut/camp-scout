# Recreation.gov Reservation Alert

## What

A personal Python polling script that monitors Recreation.gov for campsite availability by specified campsite and month. Sends email notifications when reservations become available while polling is active.

## Why

Popular campsites on Recreation.gov book up months in advance. This script continuously checks for cancellations so you can snag last-minute reservations that would otherwise be impossible to find manually.

## Tech Stack

- **Python 3.11**
- **Libraries:** `requests`, `python-dotenv`
- **API:** Recreation.gov internal API
- **Notifications:** Email SMTP

---

## Setup

1. Create the Conda environment:

```bash
conda env create -f cli/environment.yml
```

2. Activate it:

```bash
conda activate reservation-alert
```

3. Troubleshooting - If you get `ModuleNotFoundError`:

```bash
conda env update -f environment.yml --prune
```

4. Run the CLI from the root:

```bash
python3 cli.main
```

5. Follow the prompts:

- Enter a campground name to search for
- Choose the campground by number
- Enter the month number to check availability

CLI One time search
![CLI screenshot](/assets/cli-single-search.png)

---

CLI Polling with Notifications (currently hardcoded)

1. Activate conda env:

```bash
conda activate reservation-alert
```

2. Run the CLI:

```bash
python3 cli/poller
```

3. Automated script:

- runs availability checker on set locations and dates from config.py
- returns results in CLI
- if availability, email sent.

![CLI poller screenshot](/assets/poller-cli.png)

![email notification](/assets/email-notification.png)

## Moving past the CLI: Local setup

### Backend

1. Activate venv

```bash
cd backend
python -m venv venv
source venv/bin/activate
```

2. Install packages
```bash
pip install -r requirements.txt
```

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
