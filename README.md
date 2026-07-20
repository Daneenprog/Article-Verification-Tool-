# Article-Verification-Tool-
A digital signature system for verifying authenticity of news article using SHA-256 and ECDSA

When you read a news article online, how do you know it actually came from the source it claims? And how do you know nobody changed it after it was published? This project explores how digital signatures can answer both of those questions.

## What This Does

ArticleVerify lets you sign any article using real cryptography and verify later whether it has been tampered with. If even one word changes after signing, the system catches it immediately.

It also runs four attack simulations to demonstrate exactly how the system holds up when someone tries to break it.

## How To Run It

Clone the repository, then run:

pip install flask cryptography

python app.py

Open http://localhost:5000 in your browser.

## How It Works

- SHA-256 turns the article into a unique fingerprint
- ECDSA signs that fingerprint using a private key
- Verification recomputes the fingerprint and checks the signature
- If anything is changed after signing, verification fails immediately

## The Four Attacks It Simulates

1. Content Tampering : a word is changed in the article after signing
2. Signature Replay : a valid signature is taken from one article and applied to another
3. Wrong Public Key :verification is attempted using a fake publisher's key
4. Impersonation : an attacker signs the article under a fake identity

All four are blocked every time.

## Honest Limitations
It can proves authenticity but not the truth, a signed article can still contain misinformation
Private keys are not stored permanently in this demo version

This tool proves that an article came from who signed it and has not been changed since signing. It does not prove the article is true. A publisher can sign and distribute false information and it will verify correctly. Cryptography solves authenticity — not truth.
