
nvm管理node,每个node带一个npm

## npm、pnpm、nvm、corepack 关系

- `npm` 和 `pnpm` 都是 JavaScript 包管理器，都是读取 `package.json` 来安装依赖、运行脚本、发布包
- `npm` 一般随 `Node.js` 一起安装，是官方默认方案
- `pnpm` 是第三方替代方案，和 `npm` 是并列关系，不是谁依赖谁

## nvm 和 npm

- `nvm` 管理的是 `Node.js` 版本
- 每个 Node 版本自带一套对应的 `npm`
- 所以切换 `nvm use 18`、`nvm use 22` 时，也是在切换对应的 `npm`
- `nvm` 不是单独管理 `npm`，而是通过切换 Node 间接切换 `npm`

## pnpm 和 nvm

- `pnpm` 不一定跟着 `nvm` 走
- 如果 `pnpm` 是单独全局安装的，比如装在 `~/.npm-global/bin/pnpm`
- 那么切换 Node/npm 以后，`pnpm` 可能还是原来那一份
- 所以一台机器上容易出现：`node` 和 `npm` 归 `nvm` 管，`pnpm` 走另一套独立路径

## corepack 是什么

- `corepack` 不是包管理器本身，而是包管理器版本调度器
- 它主要管理 `pnpm`、`yarn` 这类包管理器该用哪个版本
- 项目里如果写了 `"packageManager": "pnpm@10.33.1"`，`corepack` 会尽量保证执行的是这个版本
- 适合团队项目、CI、本地开发统一包管理器版本

## 实用理解

- `nvm` 管 `Node`
- `npm` 是 Node 自带包管理器
- `pnpm` 是替代型包管理器
- `corepack` 管包管理器版本选择

## 使用建议

- 单人项目：直接用 `npm` 或独立安装的 `pnpm` 也可以
- 团队项目：推荐在 `package.json` 里加 `packageManager` 字段，并配合 `corepack`
- 最好统一一种方式管理 `pnpm`
- 不要长期混用独立全局 `pnpm` 和 `corepack` 管理的 `pnpm`，否则容易搞不清实际执行的是哪一个
