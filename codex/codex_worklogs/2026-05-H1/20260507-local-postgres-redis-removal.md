---
id: 20260507-local-postgres-redis-removal
name: Local PostgreSQL And Redis Removal
slug: local-postgres-redis-removal
cwd: /home/loviya/sub2api/deploy
summary: 移除宿主机安装的 PostgreSQL 和 Redis，让 Sub2API 改用部署目录管理的服务。
tags:
  - postgresql
  - redis
  - cleanup
  - sub2api
priority: normal
---

# 本地 PostgreSQL And Redis Removal

## 当前快照

- 状态: 已完成
- 目标: 移除宿主机安装的 PostgreSQL 和 Redis 服务/包。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-07 13:15:00 +0800

## 关键结果

- Initial check found PostgreSQL 16 installed and `postgresql@16-main` running on port `5432`.
- Initial check found no `redis-server.service` and no Redis listener on port `6379`.
- Purged apt packages `postgresql`, `postgresql-16`, `postgresql-client-16`, `postgresql-common`, `postgresql-contrib`, and remaining `postgresql-client-common` config.
- Redis packages `redis-server` and `redis-tools` were not installed.
- Verified `psql`, `redis-server`, and `redis-cli` are no longer present in PATH.
- Verified `postgresql.service`, `postgresql@16-main.service`, and `redis-server.service` are not found by systemd.
- Verified no listeners on ports `5432`, `6379`, or `8080`.
- Deployment precheck found `docker`, `docker-compose`, and `podman` are not installed or not in PATH.
- 已安装 Ubuntu packages `docker.io` and `docker-compose-v2`.
- Docker service is enabled and running.
- Verified `Docker version 29.1.3` and `Docker Compose version 2.40.3`.
- 已新增 user `loviya` to group `docker`.
- Verified `docker compose config --services` parses the deploy file and reports `postgres`, `redis`, and `sub2api`.
- 已诊断 a non-sudo Docker permission error: `loviya` is in group `docker`, `/var/run/docker.sock` 归属用户为 `root:docker`, but the current terminal session had not refreshed group membership.
- Sub2API deployment started successfully 带 Docker Compose.
- `docker compose ps` reports `sub2api`, `sub2api-postgres`, and `sub2api-redis` as `Up` and `healthy`.
- Sub2API logs report successful database connection, Redis connection, database initialization, admin user creation, and server start on `0.0.0.0:8080`.
- 已测试 a generated Sub2API `sk-...` client key against the Gemini endpoint; the gateway 返回 `403 Insufficient account balance`.

## Remove 宿主机 Database Services

- 更新时间: 2026-05-07 12:51:00 +0800
- 工作目录: `/home/loviya/sub2api/deploy`
- 来源指令: `PostgreSQL 或 Redis把本机自带的这两个全部删掉`
- 问题:
  - Host-installed PostgreSQL can conflict 带 Sub2API deployment-managed database configuration.
- 改进:
  - Remove apt-installed PostgreSQL packages and verify Redis is not present locally.
- 结果:
  - Host PostgreSQL was removed.
  - Host Redis was already absent.
  - No local PostgreSQL/Redis port conflict remains.
- 下一步:
  - Open a new shell or re-login for non-sudo Docker access, then run `docker compose up -d`.

## 检查 Compose Port Conflict 风险

- 更新时间: 2026-05-07 12:55:04 +0800
- 工作目录: `/home/loviya/sub2api/deploy`
- 来源指令: `检查一下我需不需要担心这个`
- 问题:
  - Sub2API's `docker-compose.yml` maps app/PostgreSQL/Redis to host ports `8080`, `5432`, and `6379`.
- 改进:
  - 已检查 current TCP listeners after host PostgreSQL removal.
  - 已检查 container tooling availability.
- 结果:
  - Ports `8080`, `5432`, and `6379` are not currently occupied.
  - `docker`, `docker-compose`, and `podman` are not available in PATH, so deployment cannot run yet.
- 下一步:
  - Open a new shell or re-login for non-sudo Docker access, then run `docker compose up -d` and `docker compose ps`.

## 安装 Docker And Compose

- 更新时间: 2026-05-07 12:56:56 +0800
- 工作目录: `/home/loviya/sub2api/deploy`
- 来源指令: `那么是不是需要安装一下docker`
- 问题:
  - The deployment instructions require `docker compose`, but no Docker-compatible runtime was installed.
- 改进:
  - 已安装 `docker.io` and `docker-compose-v2` from Ubuntu 24.04 repositories.
  - 已新增 `loviya` to the `docker` group.
- 结果:
  - `docker --version` reports Docker 29.1.3.
  - `docker compose version` reports Compose 2.40.3.
  - `docker.service` is active and enabled.
  - `sudo docker compose config --services` 返回 `postgres`, `redis`, and `sub2api`.
- 下一步:
  - Start a new shell or re-login so group membership applies 不带 `sudo`.
  - Run `docker compose up -d` from `/home/loviya/sub2api/deploy`.

## Refresh Docker Group Membership

- 更新时间: 2026-05-07 12:59:00 +0800
- 工作目录: `/home/loviya/sub2api/deploy`
- 来源指令: Docker daemon socket permission denied after running `docker compose up -d`
- 问题:
  - `docker compose` failed 带 permission denied on `/var/run/docker.sock`.
- 改进:
  - Verified `getent group docker` includes `loviya`.
  - Verified the real Docker socket is `root:docker` 带 group write permission.
  - Verified `sudo docker compose ps` can access the daemon.
- 结果:
  - Docker is installed correctly; the active shell needs `newgrp docker` or a new login session.
- 下一步:
  - Run `newgrp docker`, then retry `docker compose up -d`.

## Deploy Sub2API Containers

- 更新时间: 2026-05-07 13:00:22 +0800
- 工作目录: `/home/loviya/sub2api/deploy`
- 来源指令: User ran `docker compose ps` and reported all services healthy.
- 问题:
  - 需要 confirm whether the Docker Compose deployment actually started cleanly.
- 改进:
  - 已检查 `sudo docker compose ps`.
  - 已检查 recent `sub2api` logs.
- 结果:
  - Containers are running:
    - `sub2api`: healthy, mapped `0.0.0.0:8080->8080/tcp`.
    - `sub2api-postgres`: healthy, mapped `5432`.
    - `sub2api-redis`: healthy, mapped `6379`.
  - Logs show successful DB/Redis setup and `Server started on 0.0.0.0:8080`.
  - Warnings observed: URL allowlist disabled, trusted proxies empty, CORS origins not configured. These are configuration warnings, not startup blockers.
- 下一步:
  - Open `http://localhost:8080` and sign in 带 the configured admin email/password.

## 测试 已生成 Client API Key

- 更新时间: 2026-05-07 13:15:00 +0800
- 工作目录: `/home/loviya/sub2api/deploy`
- 来源指令: `直接执行`
- 问题:
  - 需要 verify whether a generated Sub2API `sk-...` client key can call the Gemini-compatible endpoint.
- 改进:
  - Sent a minimal `generateContent` request to `http://localhost:8080/v1beta/models/gemini-2.5-flash:generateContent`.
  - Did not record the raw key in the worklog.
- 结果:
  - HTTP status: `403`.
  - Response: `Insufficient account balance`.
  - This indicates the key reached Sub2API, but the associated user/account has no usable balance.
- 下一步:
  - Add balance to the owning user in the Admin UI, or switch the deployment to simple mode if billing should be bypassed for private use.
