# Uber Clone Backend

A production-style backend for a ride-hailing platform, built from scratch to learn backend engineering and system design — not a tutorial clone, every design decision is deliberate and documented.

## Tech Stack
- **API:** FastAPI
- **Database:** PostgreSQL (via SQLAlchemy ORM)
- **Migrations:** Alembic
- **Auth:** JWT (python-jose) + bcrypt password hashing
- **Infra (local):** Docker / Docker Compose

## Status
🚧 In progress — Phase 2 (ride lifecycle)

## Phases
- [x] **Phase 1** — Project setup, PostgreSQL + SQLAlchemy, User/Driver/Rider models, JWT auth
- [ ] **Phase 2** — Ride requests, driver availability, ride lifecycle state machine, ride history
- [ ] **Phase 3** — WebSockets, live location, maps, nearby driver search
- [ ] **Phase 4** — Redis caching, Docker Compose (full stack), logging
- [ ] **Phase 5** — Kafka, notifications, mock payments, event-driven architecture
- [ ] **Phase 6** — AWS deployment, CI/CD, monitoring, scaling

## Setup

```bash
python -m venv venv
venv\Scripts\Activate.ps1   # Windows
pip install -r requirements.txt
docker-compose up -d
alembic upgrade head
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for interactive API docs.

## Architecture Notes
See `PHASE_1_DOCUMENTATION.md` for detailed design decisions and reasoning (schema design, connection pooling, JWT auth, etc.). Updated at the end of each phase.