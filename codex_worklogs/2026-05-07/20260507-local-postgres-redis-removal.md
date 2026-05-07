---
id: 20260507-local-postgres-redis-removal
name: Local PostgreSQL And Redis Removal
slug: local-postgres-redis-removal
cwd: /home/loviya/sub2api/deploy
summary: Remove host-installed PostgreSQL and Redis services so Sub2API can rely on deploy-managed services instead.
tags:
  - postgresql
  - redis
  - cleanup
  - sub2api
priority: normal
---

# Local PostgreSQL And Redis Removal

## Current Snapshot

- status: 已完成
- goal: Remove host-installed PostgreSQL and Redis services/packages.
- blocker: 无。
- next: 无。
- updated: 2026-05-07 13:15:00 +0800

## Key Results

- Initial check found PostgreSQL 16 installed and `postgresql@16-main` running on port `5432`.
- Initial check found no `redis-server.service` and no Redis listener on port `6379`.
- Purged apt packages `postgresql`, `postgresql-16`, `postgresql-client-16`, `postgresql-common`, `postgresql-contrib`, and remaining `postgresql-client-common` config.
- Redis packages `redis-server` and `redis-tools` were not installed.
- Verified `psql`, `redis-server`, and `redis-cli` are no longer present in PATH.
- Verified `postgresql.service`, `postgresql@16-main.service`, and `redis-server.service` are not found by systemd.
- Verified no listeners on ports `5432`, `6379`, or `8080`.
- Deployment precheck found `docker`, `docker-compose`, and `podman` are not installed or not in PATH.
- Installed Ubuntu packages `docker.io` and `docker-compose-v2`.
- Docker service is enabled and running.
- Verified `Docker version 29.1.3` and `Docker Compose version 2.40.3`.
- Added user `loviya` to group `docker`.
- Verified `docker compose config --services` parses the deploy file and reports `postgres`, `redis`, and `sub2api`.
- Diagnosed a non-sudo Docker permission error: `loviya` is in group `docker`, `/var/run/docker.sock` is owned by `root:docker`, but the current terminal session had not refreshed group membership.
- Sub2API deployment started successfully with Docker Compose.
- `docker compose ps` reports `sub2api`, `sub2api-postgres`, and `sub2api-redis` as `Up` and `healthy`.
- Sub2API logs report successful database connection, Redis connection, database initialization, admin user creation, and server start on `0.0.0.0:8080`.
- Tested a generated Sub2API `sk-...` client key against the Gemini endpoint; the gateway returned `403 Insufficient account balance`.

## Remove Host Database Services

- updated: 2026-05-07 12:51:00 +0800
- cwd: `/home/loviya/sub2api/deploy`
- source instruction: `PostgreSQL 或 Redis把本机自带的这两个全部删掉`
- problem:
  - Host-installed PostgreSQL can conflict with Sub2API deployment-managed database configuration.
- improvement:
  - Remove apt-installed PostgreSQL packages and verify Redis is not present locally.
- result:
  - Host PostgreSQL was removed.
  - Host Redis was already absent.
  - No local PostgreSQL/Redis port conflict remains.
- next:
  - Open a new shell or re-login for non-sudo Docker access, then run `docker compose up -d`.

## Check Compose Port Conflict Risk

- updated: 2026-05-07 12:55:04 +0800
- cwd: `/home/loviya/sub2api/deploy`
- source instruction: `检查一下我需不需要担心这个`
- problem:
  - Sub2API's `docker-compose.yml` maps app/PostgreSQL/Redis to host ports `8080`, `5432`, and `6379`.
- improvement:
  - Checked current TCP listeners after host PostgreSQL removal.
  - Checked container tooling availability.
- result:
  - Ports `8080`, `5432`, and `6379` are not currently occupied.
  - `docker`, `docker-compose`, and `podman` are not available in PATH, so deployment cannot run yet.
- next:
  - Open a new shell or re-login for non-sudo Docker access, then run `docker compose up -d` and `docker compose ps`.

## Install Docker And Compose

- updated: 2026-05-07 12:56:56 +0800
- cwd: `/home/loviya/sub2api/deploy`
- source instruction: `那么是不是需要安装一下docker`
- problem:
  - The deployment instructions require `docker compose`, but no Docker-compatible runtime was installed.
- improvement:
  - Installed `docker.io` and `docker-compose-v2` from Ubuntu 24.04 repositories.
  - Added `loviya` to the `docker` group.
- result:
  - `docker --version` reports Docker 29.1.3.
  - `docker compose version` reports Compose 2.40.3.
  - `docker.service` is active and enabled.
  - `sudo docker compose config --services` returns `postgres`, `redis`, and `sub2api`.
- next:
  - Start a new shell or re-login so group membership applies without `sudo`.
  - Run `docker compose up -d` from `/home/loviya/sub2api/deploy`.

## Refresh Docker Group Membership

- updated: 2026-05-07 12:59:00 +0800
- cwd: `/home/loviya/sub2api/deploy`
- source instruction: Docker daemon socket permission denied after running `docker compose up -d`
- problem:
  - `docker compose` failed with permission denied on `/var/run/docker.sock`.
- improvement:
  - Verified `getent group docker` includes `loviya`.
  - Verified the real Docker socket is `root:docker` with group write permission.
  - Verified `sudo docker compose ps` can access the daemon.
- result:
  - Docker is installed correctly; the active shell needs `newgrp docker` or a new login session.
- next:
  - Run `newgrp docker`, then retry `docker compose up -d`.

## Deploy Sub2API Containers

- updated: 2026-05-07 13:00:22 +0800
- cwd: `/home/loviya/sub2api/deploy`
- source instruction: User ran `docker compose ps` and reported all services healthy.
- problem:
  - Need to confirm whether the Docker Compose deployment actually started cleanly.
- improvement:
  - Checked `sudo docker compose ps`.
  - Checked recent `sub2api` logs.
- result:
  - Containers are running:
    - `sub2api`: healthy, mapped `0.0.0.0:8080->8080/tcp`.
    - `sub2api-postgres`: healthy, mapped `5432`.
    - `sub2api-redis`: healthy, mapped `6379`.
  - Logs show successful DB/Redis setup and `Server started on 0.0.0.0:8080`.
  - Warnings observed: URL allowlist disabled, trusted proxies empty, CORS origins not configured. These are configuration warnings, not startup blockers.
- next:
  - Open `http://localhost:8080` and sign in with the configured admin email/password.

## Test Generated Client API Key

- updated: 2026-05-07 13:15:00 +0800
- cwd: `/home/loviya/sub2api/deploy`
- source instruction: `直接执行`
- problem:
  - Need to verify whether a generated Sub2API `sk-...` client key can call the Gemini-compatible endpoint.
- improvement:
  - Sent a minimal `generateContent` request to `http://localhost:8080/v1beta/models/gemini-2.5-flash:generateContent`.
  - Did not record the raw key in the worklog.
- result:
  - HTTP status: `403`.
  - Response: `Insufficient account balance`.
  - This indicates the key reached Sub2API, but the associated user/account has no usable balance.
- next:
  - Add balance to the owning user in the Admin UI, or switch the deployment to simple mode if billing should be bypassed for private use.
