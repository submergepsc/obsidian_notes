---
id: 20260507-sub2api-env-config
name: Sub2API Deploy Env Configuration
slug: sub2api-env-config
cwd: /home/loviya/sub2api/deploy
summary: 配置 Sub2API 部署所需的环境密钥和运行时参数。
tags:
  - sub2api
  - deploy
  - env
priority: normal
---

# Sub2API Deploy Env 配置

## 当前快照

- 状态: 已完成
- 目标: 更新 `/home/loviya/sub2api/deploy/.env`，补齐 Web、数据库、Redis、管理员、JWT 和 TOTP 所需设置。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-07 12:44:05 +0800

## 关键结果

- Set `SERVER_PORT=8080`.
- Restored password fields after the user clarified they will set passwords themselves.
- Kept `ADMIN_EMAIL=admin@sub2api.local`.
- Left admin password management to the user.
- Set `JWT_SECRET` from the 64-character value provided by the user.
- Set `TOTP_ENCRYPTION_KEY` from the 64-character value provided by the user.
- Verified required value lengths 不带 printing secrets:
  - `SERVER_PORT`: 4
  - `POSTGRES_PASSWORD`: 27
  - `REDIS_PASSWORD`: 0
  - `ADMIN_EMAIL`: 19
  - `ADMIN_PASSWORD`: 8
  - `JWT_SECRET`: 64
  - `TOTP_ENCRYPTION_KEY`: 64

## 配置 Deploy .env

- 更新时间: 2026-05-07 12:42:31 +0800
- 工作目录: `/home/loviya/sub2api/deploy`
- 来源指令: `修改一下.env`
- 问题:
  - Sub2API deployment `.env` still had default or empty secret values.
- 改进:
  - 已更新 only the requested environment keys.
  - Avoided recording raw secret values in worklogs or notes.
- 结果:
  - `/home/loviya/sub2api/deploy/.env` now has the requested runtime port and required secrets populated.
- 下一步:
  - No pending step.

## Leave Passwords For User 配置

- 更新时间: 2026-05-07 12:44:05 +0800
- 工作目录: `/home/loviya/sub2api/deploy`
- 来源指令: `搞错了,password不要修改,我自己设置`
- 问题:
  - 已生成 password values should not remain in `.env` 因为 the user wants to set passwords manually.
- 改进:
  - Restored `POSTGRES_PASSWORD`, `REDIS_PASSWORD`, and `ADMIN_PASSWORD` to their pre-change values.
  - Kept `SERVER_PORT`, `JWT_SECRET`, and `TOTP_ENCRYPTION_KEY` configured.
- 结果:
  - Password fields are available for the user to edit directly.
- 下一步:
  - 解释how PostgreSQL password configuration works for Docker Compose versus host PostgreSQL.
