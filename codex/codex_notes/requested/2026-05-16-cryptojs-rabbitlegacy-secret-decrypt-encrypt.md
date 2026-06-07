---
requested_by_user: true
importance: user-requested
review_priority: high
tags:
  - user-requested
  - important
  - cryptojs
  - rabbitlegacy
  - secrets
source_worklog: 20260514-mimo-api-runtime-home
created: 2026-05-16
---

# CryptoJS RabbitLegacy Secret 解密与加密

## 问题

一些共享 API tokens 可能以 CryptoJS/OpenSSL-compatible encrypted text 的形式发布，而不是 plaintext。密文通常是 base64 text，解码后以 `Salted__` header 开头。

在 MiMo key rotation 场景中，可见 metadata 是：

- algorithm: Rabbit
- 实际兼容实现: CryptoJS `RabbitLegacy`
- passphrase: `linux.do`
- format: CryptoJS/OpenSSL salted base64 ciphertext

不要把 plaintext API keys 写入 notes、worklogs、screenshots 或聊天回复。

## 关键结果

对于这种 Linux.do 风格的 encrypted token format，应使用 `CryptoJS.RabbitLegacy`，不要使用 `CryptoJS.Rabbit`。普通 Rabbit decryptor 可能因为 malformed UTF-8 或不可读 plaintext 失败，而 `RabbitLegacy` 会返回预期的 API token。

在本机，`crypto-js` 已可通过 OpenClaw 使用：

```bash
NODE_PATH=/home/loviya/.npm-global/lib/node_modules/openclaw/node_modules node
```

## 解密

使用占位符表示 encrypted value 和 passphrase：

```bash
NODE_PATH=/home/loviya/.npm-global/lib/node_modules/openclaw/node_modules node - <<'NODE'
const CryptoJS = require('crypto-js');

const encrypted = 'PASTE_ENCRYPTED_BASE64_HERE';
const passphrase = 'PASTE_PASSPHRASE_HERE';

const plaintext = CryptoJS.RabbitLegacy
  .decrypt(encrypted, passphrase)
  .toString(CryptoJS.enc.Utf8)
  .trim();

if (!plaintext) {
  throw new Error('decrypt failed');
}

console.log(plaintext);
NODE
```

处理 secret 时，避免打印 plaintext。只打印 metadata：

```bash
NODE_PATH=/home/loviya/.npm-global/lib/node_modules/openclaw/node_modules node - <<'NODE'
const CryptoJS = require('crypto-js');

const encrypted = 'PASTE_ENCRYPTED_BASE64_HERE';
const passphrase = 'PASTE_PASSPHRASE_HERE';
const plaintext = CryptoJS.RabbitLegacy.decrypt(encrypted, passphrase).toString(CryptoJS.enc.Utf8).trim();

if (!plaintext) {
  throw new Error('decrypt failed');
}

console.log(`ok len=${plaintext.length} prefix=${plaintext.slice(0, 3)} sha256=${CryptoJS.SHA256(plaintext).toString().slice(0, 12)}`);
NODE
```

## 加密

创建同样风格的可共享 encrypted token：

```bash
NODE_PATH=/home/loviya/.npm-global/lib/node_modules/openclaw/node_modules node - <<'NODE'
const CryptoJS = require('crypto-js');

const plaintext = 'PASTE_SECRET_TOKEN_HERE';
const passphrase = 'PASTE_PASSPHRASE_HERE';

const encrypted = CryptoJS.RabbitLegacy.encrypt(plaintext, passphrase).toString();
console.log(encrypted);
NODE
```

分享前验证 round trip：

```bash
NODE_PATH=/home/loviya/.npm-global/lib/node_modules/openclaw/node_modules node - <<'NODE'
const CryptoJS = require('crypto-js');

const plaintext = 'PASTE_SECRET_TOKEN_HERE';
const passphrase = 'PASTE_PASSPHRASE_HERE';
const encrypted = CryptoJS.RabbitLegacy.encrypt(plaintext, passphrase).toString();
const decrypted = CryptoJS.RabbitLegacy.decrypt(encrypted, passphrase).toString(CryptoJS.enc.Utf8);

if (decrypted !== plaintext) {
  throw new Error('round trip failed');
}

console.log(`round-trip ok encrypted_len=${encrypted.length}`);
NODE
```

## 安全轮换流程

1. 修改前备份当前 active env file：

```bash
cp /home/loviya/.codex-api-mimo-pay-self/mimo.env /home/loviya/.codex-api-mimo-pay-self/mimo.env.bak-$(date +%Y%m%d-%H%M%S)
```

2. 解密 token，尽量不要打印 plaintext。

3. 只替换 key 行：

```bash
# Edit this line only:
export MIMO_API_KEY="DECRYPTED_TOKEN_HERE"
```

4. 在不暴露 token 的情况下验证：

```bash
stat -c '%a %n' /home/loviya/.codex-api-mimo-pay-self/mimo.env
awk -F'"' '/^export MIMO_API_KEY=/{print length($2), substr($2,1,3)}' /home/loviya/.codex-api-mimo-pay-self/mimo.env
sed -n '1,5p' /home/loviya/.codex-api-mimo-pay-self/mimo.env | sed 's/MIMO_API_KEY=".*"/MIMO_API_KEY="***redacted***"/'
```

secret env files 的预期权限是 `600`。

## 注意事项

- 为了兼容 CryptoJS，需要使用 `RabbitLegacy`；仅名为 `Rabbit` 的实现可能无法正确解密同一密文。
- 本机 OpenSSL 没有暴露可用的 Rabbit cipher，因此 `openssl enc` 不适合这个场景。
- 分享 secrets 时，将 passphrase 和 encrypted token 分开保存。
- 不要把 decrypted key 存入 `codex_notes`、worklogs、screenshots 或最终回复。
