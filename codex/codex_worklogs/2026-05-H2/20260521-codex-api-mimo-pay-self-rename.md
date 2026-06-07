---
id: 20260521-codex-api-mimo-pay-self-rename
name: codex-api-mimo-pay-self 账户重命名
slug: codex-api-mimo-pay-self-rename
cwd: /home/loviya
summary: 将三组 MiMo API home 和启动入口重命名为 pay/free 与 self/other 语义。
tags:
  - codex-api
  - mimo
  - rename
---

# codex-api-mimo-pay-self 账户重命名

## Current Snapshot

- workflow id: 20260521-codex-api-mimo-pay-self-rename
- current status: 已完成
- current goal: 将原 `codex-api-mimo`、`codex-api-mimo1`、`codex-api-mimo2` 改名为 `codex-api-mimo-pay-self`、`codex-api-mimo-free-self`、`codex-api-mimo-free-other`
- current blocker: none
- next step: none
- tags: codex-api, mimo, rename
- summary: 已完成三个 MiMo API home、启动入口、内部脚本、全局规则、worklogs 和 notes 的新命名迁移；旧入口不再解析，新入口和配置验证通过。

## Key Results

- `/home/loviya/.codex-api-mimo` -> `/home/loviya/.codex-api-mimo-pay-self`。
- `/home/loviya/.codex-api-mimo1` -> `/home/loviya/.codex-api-mimo-free-self`。
- `/home/loviya/.codex-api-mimo2` -> `/home/loviya/.codex-api-mimo-free-other`。
- `~/.local/bin` 启动入口改为 `codex-api-mimo-pay-self`、`codex-api-mimo-free-self`、`codex-api-mimo-free-other`；保留下划线兼容入口 `codex_api_mimo_free_self`、`codex_api_mimo_free_other`。
- 更新 `/home/loviya/.codex/AGENTS.md` 的 API home 清单和 `CODEX_HOME` 绑定规则。
- 批量更新 worklogs 和 codex_notes 中的持久引用；历史 `sessions/` 和 `log/` 审计记录未改写。

## Verification

- `CODEX_HOME=... codex debug models`：三个新 API home 均解析成功。
- 新启动器 `--version`：五个入口均返回 `codex-cli 0.132.0`。
- PATH 检查：旧 `codex-api-mimo`、`codex-api-mimo1`、`codex-api-mimo2` 不再解析；三个新 hyphen 命令可解析。
- 残留扫描：排除 `sessions/`、`log/`、`sqlite` 后，配置/脚本/文档中未发现旧命名残留或重复替换残留。
- `codex-api-mimo-free-other exec --skip-git-repo-check --sandbox read-only --json "只回复 ok"`：真实调用成功，返回 `ok`。
- `python3 -m py_compile`：pay-self 与 free-other 的 Responses proxy 语法检查通过。
