---
id: 20260507-7d9a2f-postgresql-config
name: PostgreSQL 本地配置
slug: postgresql-config
cwd: /home/loviya
summary: 配置本地 PostgreSQL 服务供开发使用。
tags:
  - postgresql
  - database
  - local-dev
priority: normal
---

# PostgreSQL 本地配置

## 当前快照

- 状态: 已完成
- 目标: 安装本地 PostgreSQL，启动服务，并配置可用的本地角色和数据库。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-07 12:40:10 +0800

## 关键结果

- 已安装 Ubuntu PostgreSQL 16.13 软件包：`postgresql`、`postgresql-contrib` 和 PostgreSQL 16 client/server 依赖。
- 已创建并启动 cluster `16/main`，端口为 `5432`；`postgresql` 已设置为开机启动。
- 已创建 PostgreSQL role `loviya`，随后改为 `SUPERUSER`。
- 已创建 database `loviya`，owner 为 role `loviya`。
- 已用 `psql -d loviya` 验证普通本地使用，返回 `current_user = loviya` 和 `current_database = loviya`。
- 已用 `show is_superuser;` 验证 `loviya` 是 superuser，返回 `on`。
- 已用 `pg_isready` 验证就绪状态：`/var/run/postgresql:5432 - accepting connections`。

## 配置本地 PostgreSQL

- 更新时间: 2026-05-07 12:40:00 +0800
- 工作目录: `/home/loviya`
- 来源指令: `# PostgreSQL 帮我配置一下这个`
- 问题:
  - 这台机器需要一套可用的本地 PostgreSQL 环境，但当时看起来还没有安装 PostgreSQL。
- 改进:
  - 使用系统包管理器和服务管理器，而不是临时二进制文件。
  - 优先使用与本地 Linux 用户同名的 PostgreSQL role/database，方便通过 Unix socket 免密码开发访问。
- 结果:
  - PostgreSQL 16.13 已安装并在本地运行。
  - 用户可以通过 `psql -d loviya` 连接。
  - 临时表 insert/select 测试成功，用户为 `loviya`.
- 下一步:
  - 无待处理步骤。

## 提升本地角色为超级用户

- 更新时间: 2026-05-07 12:40:10 +0800
- 工作目录: `/home/loviya`
- 来源指令: `改成superuser`
- 问题:
  - 本地 PostgreSQL role `loviya` 需要 superuser 权限，以便不受限制地进行本地开发。
- 改进:
  - 已执行 `ALTER ROLE loviya WITH SUPERUSER;`。
- 结果:
  - `psql -d loviya -tAc "select current_user, usesuper from pg_user where usename = current_user;"` 返回 `loviya|t`.
  - `psql -d loviya -c "show is_superuser;"` 返回 `on`.
- 下一步:
  - 无待处理步骤。

## 命令

- 安装软件包: `sudo apt-get install -y postgresql postgresql-contrib`
- 检查就绪状态: `pg_isready`
- 检查开机启用状态: `systemctl is-enabled postgresql`
- 以本地用户连接: `psql -d loviya`
- 管理员连接: `sudo -u postgres psql`
