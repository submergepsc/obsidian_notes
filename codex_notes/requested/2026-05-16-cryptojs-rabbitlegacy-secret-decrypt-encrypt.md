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

# CryptoJS RabbitLegacy Secret Decrypt And Encrypt

## Problem

Some shared API tokens may be posted as CryptoJS/OpenSSL-compatible encrypted text instead of plaintext. The ciphertext often starts with base64 text that decodes to the `Salted__` header.

In the MiMo key rotation case, the visible metadata was:

- algorithm: Rabbit
- actual compatible implementation: CryptoJS `RabbitLegacy`
- passphrase: `linux.do`
- format: CryptoJS/OpenSSL salted base64 ciphertext

Do not put plaintext API keys into notes, worklogs, screenshots, or chat replies.

## Key Result

Use `CryptoJS.RabbitLegacy`, not `CryptoJS.Rabbit`, for this Linux.do-style encrypted token format. The normal Rabbit decryptor can fail with malformed UTF-8 or unreadable plaintext, while `RabbitLegacy` returns the expected API token.

On this machine, `crypto-js` is already available through OpenClaw:

```bash
NODE_PATH=/home/loviya/.npm-global/lib/node_modules/openclaw/node_modules node
```

## Decrypt

Use placeholders for the encrypted value and passphrase:

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

For secret-handling work, avoid printing the plaintext. Print only metadata:

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

## Encrypt

To create the same style of shareable encrypted token:

```bash
NODE_PATH=/home/loviya/.npm-global/lib/node_modules/openclaw/node_modules node - <<'NODE'
const CryptoJS = require('crypto-js');

const plaintext = 'PASTE_SECRET_TOKEN_HERE';
const passphrase = 'PASTE_PASSPHRASE_HERE';

const encrypted = CryptoJS.RabbitLegacy.encrypt(plaintext, passphrase).toString();
console.log(encrypted);
NODE
```

Validate the round trip before sharing:

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

## Safe Rotation Procedure

1. Back up the active env file before touching it:

```bash
cp /home/loviya/.codex-api-mimo/mimo.env /home/loviya/.codex-api-mimo/mimo.env.bak-$(date +%Y%m%d-%H%M%S)
```

2. Decrypt the token without printing plaintext if possible.

3. Replace only the key line:

```bash
# Edit this line only:
export MIMO_API_KEY="DECRYPTED_TOKEN_HERE"
```

4. Verify without exposing the token:

```bash
stat -c '%a %n' /home/loviya/.codex-api-mimo/mimo.env
awk -F'"' '/^export MIMO_API_KEY=/{print length($2), substr($2,1,3)}' /home/loviya/.codex-api-mimo/mimo.env
sed -n '1,5p' /home/loviya/.codex-api-mimo/mimo.env | sed 's/MIMO_API_KEY=".*"/MIMO_API_KEY="***redacted***"/'
```

Expected permission for secret env files is `600`.

## Caveats

- `RabbitLegacy` is needed for CryptoJS compatibility; implementations named only `Rabbit` may not decrypt the same ciphertext correctly.
- OpenSSL on this machine did not expose a usable Rabbit cipher, so `openssl enc` was not suitable for this case.
- Keep the passphrase separate from the encrypted token when sharing secrets.
- Never store the decrypted key in `codex_notes`, worklogs, screenshots, or final responses.
