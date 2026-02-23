# Recreation.gov Reservation Alert

## What

A Python polling script that monitors Recreation.gov for campsite availability and sends notifications when reservations become available due to cancellations.

## Why

Popular campsites on Recreation.gov book up months in advance. This script continuously checks for cancellations so you can snag last-minute reservations that would otherwise be impossible to find manually.

## Tech Stack

- **Python 3.11**
- **Libraries:** `requests`, `python-dotenv`
- **API:** Recreation.gov internal API
- **Notifications:** TBD (SMS/Email)

---

## Roadmap

### Phase 1: MVP

- [x] Discover and test Recreation.gov API endpoints
- [ ] Hardcoded search for specific lookout towers
- [ ] Hardcoded date range (April 2026)
- [ ] Polling loop (check every X minutes)
- [ ] Basic notification system
- [ ] Cron job setup

### Phase 2: Configurable

- [ ] Search by campground name
- [ ] Custom date range selection
- [ ] Handle different campground types (guard stations vs multi-site campgrounds)
- [ ] Configuration file for user preferences

### Phase 3: Future Enhancements

- [ ] Web app interface or Mobile app

---

## Notes

- Uses undocumented Recreation.gov internal API endpoints
- Official RIDB API at https://ridb.recreation.gov/docs does not include availability data
- Endpoints discovered via browser network inspection and open-source projects on github.
