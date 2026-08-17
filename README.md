# Recreation.gov Reservation Alert

## What

An interactive CLI with a Python polling script that monitors Recreation.gov for campsite availability by specified campsite and month.
Sends email notifications when reservations become available while polling is active.

## Why

Popular campsites on Recreation.gov book up months in advance and it's frustrating to be constantly refreshing and checking their site manually. This script was a personal project to continuously check for cancellations so I can find cancellations or general availability.

## Built With

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

- **Env:** Miniconda
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

4. Run the Interactive CLI from the root:

```bash
python3 cli.main
```

5. Follow the prompts:

- Enter a campground name to search for
- Choose the campground by number
- Enter the month number to check availability
- Choose 1 time search or enter email for polling to begin with email notifications of results.

CLI One time search
![CLI screenshot](/assets/cli-single-search.png)

---

### CLI Polling with Notifications

(Keeping this code here for easy testing to just run poller with hard-coded values from config.py outside of interactivity)

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

_Terminal Screenshot_
![CLI poller screenshot](/assets/poller-cli.png)

_Email content screenshot_
![email notification](/assets/email-notification.png)

---

## Stretch Goals WIP: Move logic to FastAPI, backend and simple frontend WedApp

### Moving past the CLI: Local setup

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
- [x] Configuration file for user preferences

### Phase 3: Polling loop and Notifications

- [x] Polling loop (check every X minutes)
- [x] Basic notification system: email

### Phase 4: Future Enhancements

- [ ] Create chron job
- [ ] Save success results to file
- [ ] Search by location (zip?) and specific date range (if even possible via API)
- [ ] Web app interface
- [ ] SMS notifications (not free)

---

## Notes

- Official RIDB API at https://ridb.recreation.gov/docs does not include availability data
- Endpoints discovered via browser network inspection and other open-source projects on github.
