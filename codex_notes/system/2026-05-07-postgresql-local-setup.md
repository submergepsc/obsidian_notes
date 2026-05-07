---
title: PostgreSQL Local Setup
date: 2026-05-07
area: system
importance: normal
tags:
  - postgresql
  - database
  - local-dev
source_worklog: /home/loviya/.codex/worklogs/2026-05-07/20260507-7d9a2f-postgresql-config.md
requested_by_user: false
---

# PostgreSQL Local Setup

## Result

- PostgreSQL 16.13 is installed from Ubuntu 24.04 packages.
- Cluster `16/main` runs on port `5432`.
- `postgresql` is enabled for startup.
- Local role `loviya` exists and is a PostgreSQL superuser.
- Local database `loviya` is owned by `loviya`.

## Daily Use

- Connect as the normal local user:

```bash
psql -d loviya
```

- Check service readiness:

```bash
pg_isready
```

- Admin shell:

```bash
sudo -u postgres psql
```

## Verification

- `psql -d loviya -c "select current_user, current_database();"` returned `loviya | loviya`.
- `pg_isready` returned `/var/run/postgresql:5432 - accepting connections`.
- A temporary table insert/select test succeeded as `loviya`.
- `psql -d loviya -c "show is_superuser;"` returned `on`.
