---
title: PostgreSQL 本地配置
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

# PostgreSQL 本地配置

## 结果

- PostgreSQL 16.13 已通过 Ubuntu 24.04 软件包安装。
- Cluster `16/main` 运行在端口 `5432`。
- `postgresql` 已设置为开机启动。
- 本地角色 `loviya` 已存在，并且是 PostgreSQL 超级用户。
- 本地数据库 `loviya` 归属用户为 `loviya`。

## 日常使用

- 以普通本地用户连接：

```bash
psql -d loviya
```

- 检查服务就绪状态：

```bash
pg_isready
```

- 管理员 shell：

```bash
sudo -u postgres psql
```

## 验证

- `psql -d loviya -c "select current_user, current_database();"` 返回 `loviya | loviya`。
- `pg_isready` 返回 `/var/run/postgresql:5432 - accepting connections`。
- 临时表 insert/select 测试成功，用户为 `loviya`。
- `psql -d loviya -c "show is_superuser;"` 返回 `on`。
