---
id: 20260507-sub2api-env-config
name: Sub2API Deploy Env Configuration
slug: sub2api-env-config
cwd: /home/loviya/sub2api/deploy
summary: Configure Sub2API deployment environment secrets and required runtime settings.
tags:
  - sub2api
  - deploy
  - env
priority: normal
---

# Sub2API Deploy Env Configuration

## Current Snapshot

- status: 已完成
- goal: Update `/home/loviya/sub2api/deploy/.env` with required web, database, Redis, admin, JWT, and TOTP settings.
- blocker: 无。
- next: 无。
- updated: 2026-05-07 12:44:05 +0800

## Key Results

- Set `SERVER_PORT=8080`.
- Restored password fields after the user clarified they will set passwords themselves.
- Kept `ADMIN_EMAIL=admin@sub2api.local`.
- Left admin password management to the user.
- Set `JWT_SECRET` from the 64-character value provided by the user.
- Set `TOTP_ENCRYPTION_KEY` from the 64-character value provided by the user.
- Verified required value lengths without printing secrets:
  - `SERVER_PORT`: 4
  - `POSTGRES_PASSWORD`: 27
  - `REDIS_PASSWORD`: 0
  - `ADMIN_EMAIL`: 19
  - `ADMIN_PASSWORD`: 8
  - `JWT_SECRET`: 64
  - `TOTP_ENCRYPTION_KEY`: 64

## Configure Deploy .env

- updated: 2026-05-07 12:42:31 +0800
- cwd: `/home/loviya/sub2api/deploy`
- source instruction: `修改一下.env`
- problem:
  - Sub2API deployment `.env` still had default or empty secret values.
- improvement:
  - Updated only the requested environment keys.
  - Avoided recording raw secret values in worklogs or notes.
- result:
  - `/home/loviya/sub2api/deploy/.env` now has the requested runtime port and required secrets populated.
- next:
  - No pending step.

## Leave Passwords For User Configuration

- updated: 2026-05-07 12:44:05 +0800
- cwd: `/home/loviya/sub2api/deploy`
- source instruction: `搞错了,password不要修改,我自己设置`
- problem:
  - Generated password values should not remain in `.env` because the user wants to set passwords manually.
- improvement:
  - Restored `POSTGRES_PASSWORD`, `REDIS_PASSWORD`, and `ADMIN_PASSWORD` to their pre-change values.
  - Kept `SERVER_PORT`, `JWT_SECRET`, and `TOTP_ENCRYPTION_KEY` configured.
- result:
  - Password fields are available for the user to edit directly.
- next:
  - Explain how PostgreSQL password configuration works for Docker Compose versus host PostgreSQL.
