---
id: 20260507-7d9a2f-postgresql-config
name: PostgreSQL Local Configuration
slug: postgresql-config
cwd: /home/loviya
summary: Configure a local PostgreSQL service for development use.
tags:
  - postgresql
  - database
  - local-dev
priority: normal
---

# PostgreSQL Local Configuration

## Current Snapshot

- status: 已完成
- goal: Install local PostgreSQL, start the service, and configure a usable local role/database.
- blocker: 无。
- next: 无。
- updated: 2026-05-07 12:40:10 +0800

## Key Results

- Installed Ubuntu PostgreSQL 16.13 packages: `postgresql`, `postgresql-contrib`, and PostgreSQL 16 client/server dependencies.
- Created and started cluster `16/main` on port `5432`; `postgresql` is enabled for startup.
- Created PostgreSQL role `loviya`, then changed it to `SUPERUSER`.
- Created database `loviya` owned by role `loviya`.
- Verified normal local usage with `psql -d loviya`, returning `current_user = loviya` and `current_database = loviya`.
- Verified `loviya` is a superuser with `show is_superuser;`, returning `on`.
- Verified readiness with `pg_isready`: `/var/run/postgresql:5432 - accepting connections`.

## Configure Local PostgreSQL

- updated: 2026-05-07 12:40:00 +0800
- cwd: `/home/loviya`
- source instruction: `# PostgreSQL 帮我配置一下这个`
- problem:
  - The machine needs a usable local PostgreSQL setup, but PostgreSQL does not appear to be installed yet.
- improvement:
  - Use the system package manager and service manager rather than ad hoc binaries.
  - Prefer a local Linux-user-matching PostgreSQL role/database for passwordless Unix-socket development access.
- result:
  - PostgreSQL 16.13 is installed and running locally.
  - The user can connect with `psql -d loviya`.
  - A temporary table insert/select test succeeded as `loviya`.
- next:
  - No pending step.

## Promote Local Role To Superuser

- updated: 2026-05-07 12:40:10 +0800
- cwd: `/home/loviya`
- source instruction: `改成superuser`
- problem:
  - The local PostgreSQL role `loviya` needed superuser privileges for unrestricted local development.
- improvement:
  - Ran `ALTER ROLE loviya WITH SUPERUSER;`.
- result:
  - `psql -d loviya -tAc "select current_user, usesuper from pg_user where usename = current_user;"` returned `loviya|t`.
  - `psql -d loviya -c "show is_superuser;"` returned `on`.
- next:
  - No pending step.

## Commands

- Install packages: `sudo apt-get install -y postgresql postgresql-contrib`
- Check readiness: `pg_isready`
- Check startup enablement: `systemctl is-enabled postgresql`
- Connect as local user: `psql -d loviya`
- Admin connection: `sudo -u postgres psql`
