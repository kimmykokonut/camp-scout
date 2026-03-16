# Recreation.gov Reservation Alert

## What

A Python polling script that monitors Recreation.gov for campsite availability and sends notifications when reservations become available due to cancellations.

## Why

Popular campsites on Recreation.gov book up months in advance. This script continuously checks for cancellations so you can snag last-minute reservations that would otherwise be impossible to find manually.

## Tech Stack

- **Python 3.11**
- **Libraries:** `requests`, `python-dotenv`
- **API:** Recreation.gov API
- **Notifications:** TBD (SMS/Email)

---

## Roadmap

### Phase 1: MVP

- [x] Discover and test Recreation.gov API endpoints
- [x] Hardcoded search for specific lookout towers
- [x] Hardcoded date range (April 2026)

### Phase 2: Configurable

- [x] Make interactive console app
- [x] Results from user input month, year 2026 (No date range options)
- [x] User keyword search for name, display top 5, user selects 1, id used to get availability
- [x] Handle different campground types (guard stations vs multi-site campgrounds)
- [ ] Configuration file for user preferences

### Phase 3: Cron Job & Notifications

- [x] Polling loop (check every X minutes)
- [ ] Save success results to file
- [ ] Basic notification system
- [ ] Cron job setup

### Phase 4: Future Enhancements

- [ ] Search by location and specific date range (if possible via API)
- [ ] Web app interface or Mobile app

---

## Notes

- Uses undocumented Recreation.gov internal API endpoints
- Official RIDB API at https://ridb.recreation.gov/docs does not include availability data
- Endpoints discovered via browser network inspection and other open-source projects on github.
