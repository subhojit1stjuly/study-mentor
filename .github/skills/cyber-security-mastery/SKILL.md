---
name: cyber-security-mastery
description: "Use when: studying cyber security, learning OWASP Top 10, understanding cryptography, learning network security, studying ethical hacking, learning authentication authorization, web application security, studying encryption, penetration testing concepts, security compliance, learning about firewalls, studying zero trust, preparing for security interviews, understanding TLS SSL."
argument-hint: "Topic or phase (e.g., 'OWASP XSS', 'cryptography basics', 'Phase 3 offensive')"
---

# Cyber Security Mastery Roadmap

A structured roadmap for mastering cyber security — from fundamentals through offensive and defensive security practices.

## When to Use

- Starting or resuming a security learning journey
- Studying for security-focused interview questions
- Understanding web application vulnerabilities
- Learning cryptography and secure communication
- Studying authentication, authorization, and identity
- Understanding offensive vs defensive security

---

## Phase 0: Security Foundations

> **Goal**: Understand core security principles and threat modeling.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 0.1 | CIA Triad | Confidentiality, Integrity, Availability — real examples, trade-offs |
| 0.2 | Security Principles | Defense in depth, least privilege, zero trust, security by design, fail-safe defaults, separation of duties |
| 0.3 | Threat Modeling | STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation), attack surface analysis, threat matrices, risk assessment |
| 0.4 | Security Landscape | Types of attackers (script kiddies → nation-states), attack lifecycle (MITRE ATT&CK), common CVE patterns |

---

## Phase 1: Cryptography

> **Goal**: Understand encryption, hashing, and secure communication.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 1.1 | Symmetric Encryption | AES (modes: ECB, CBC, CTR, GCM), DES (why broken), ChaCha20, block vs stream ciphers, key sizes |
| 1.2 | Asymmetric Encryption | RSA (key generation, encryption/signing), ECC (elliptic curves), Diffie-Hellman key exchange, key pair management |
| 1.3 | Hashing | SHA-256, SHA-3, MD5 (why broken), properties (collision resistance, preimage resistance), Merkle trees |
| 1.4 | Password Security | bcrypt, scrypt, Argon2 (why not plain SHA), salting, peppering, dictionary attacks, rainbow tables, password policies |
| 1.5 | TLS/SSL | TLS 1.3 handshake, certificate chain, X.509 certificates, PKI, certificate authorities, certificate pinning, HSTS |
| 1.6 | Digital Signatures | Signing vs encryption, HMACs, JWT signing (HS256 vs RS256), code signing, non-repudiation |

### Checkpoint
- Explain the TLS 1.3 handshake step by step
- Compare AES-GCM vs AES-CBC — when to use each
- Explain why bcrypt is better than SHA-256 for passwords

---

## Phase 2: Web Application Security (OWASP)

> **Goal**: Understand and defend against the most common web vulnerabilities.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 2.1 | Injection | SQL injection (classic, blind, union-based), NoSQL injection, command injection, LDAP injection — parameterized queries as defense |
| 2.2 | Broken Authentication | Credential stuffing, session fixation, session hijacking, brute force, weak password policies, MFA bypass |
| 2.3 | XSS | Reflected, Stored, DOM-based XSS — input validation, output encoding, Content Security Policy (CSP), sanitization libraries |
| 2.4 | CSRF & SSRF | Cross-Site Request Forgery (token-based defense, SameSite cookies), Server-Side Request Forgery (internal network access, cloud metadata) |
| 2.5 | Broken Access Control | IDOR, privilege escalation (vertical/horizontal), path traversal, forced browsing, RBAC vs ABAC |
| 2.6 | Security Misconfiguration | Default credentials, verbose error messages, unnecessary services, missing security headers, debug mode in production |
| 2.7 | Data Exposure | Sensitive data in URLs/logs, missing encryption at rest/in transit, PII handling, data classification |
| 2.8 | Insecure Deserialization | Java/PHP/.NET deserialization attacks, JSON/XML bombs, defense strategies |

### Checkpoint
- Demonstrate a SQL injection attack and its fix (parameterized query)
- Explain stored vs reflected XSS with examples and defenses
- Identify 5 security headers and what each prevents

---

## Phase 3: Authentication & Authorization

> **Goal**: Master identity, authentication, and access control at scale.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 3.1 | Authentication Methods | Username/password, MFA (TOTP, FIDO2/WebAuthn, SMS), biometrics, passwordless, magic links |
| 3.2 | OAuth 2.0 | Authorization code flow, PKCE, client credentials, refresh tokens, scopes, token validation |
| 3.3 | OpenID Connect | ID tokens, userinfo endpoint, discovery, OIDC vs OAuth, SSO implementation |
| 3.4 | JWT Deep Dive | Claims (iss, sub, exp, aud), signing algorithms, validation pitfalls (alg:none, key confusion), token storage, refresh strategy |
| 3.5 | Session Management | Server-side sessions, cookie security (HttpOnly, Secure, SameSite), session fixation, session revocation |
| 3.6 | Access Control | RBAC, ABAC, ReBAC, policy engines (OPA), least privilege in practice, API authorization patterns |

### Checkpoint
- Draw the OAuth 2.0 authorization code flow with PKCE
- Explain 3 common JWT security pitfalls and their fixes
- Design an access control system for a multi-tenant SaaS application

---

## Phase 4: Network Security

> **Goal**: Understand network-level security controls and attacks.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 4.1 | Firewalls | Stateful vs stateless, WAF, network firewalls, security groups (cloud), NACLs, iptables basics |
| 4.2 | IDS/IPS | Intrusion detection vs prevention, signature-based vs anomaly-based, SIEM, log analysis |
| 4.3 | DDoS | Types (volumetric, protocol, application-layer), mitigation (rate limiting, CDN, scrubbing centers, anycast) |
| 4.4 | VPN & Tunneling | IPsec, WireGuard, TLS VPN, split tunneling, zero trust network access (ZTNA) |
| 4.5 | DNS Security | DNS spoofing, DNSSEC, DNS over HTTPS (DoH), DNS over TLS (DoT), DNS sinkholing |

---

## Phase 5: Application Security (AppSec)

> **Goal**: Build and maintain secure software throughout the SDLC.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 5.1 | Secure SDLC | Security requirements, threat modeling in design, secure coding practices, security testing, security in CI/CD |
| 5.2 | SAST & DAST | Static analysis tools, dynamic analysis tools, integrating into CI/CD, false positives management |
| 5.3 | Dependency Security | SCA (Software Composition Analysis), CVE databases, Dependabot, Snyk, SBOM (Software Bill of Materials) |
| 5.4 | Secrets Management | Vault (HashiCorp), AWS Secrets Manager, environment variables (anti-pattern), rotation policies, never commit secrets |
| 5.5 | Secure API Design | Input validation, output encoding, rate limiting, API keys vs OAuth, CORS configuration, security headers |

---

## Phase 6: Offensive Security Concepts

> **Goal**: Think like an attacker to build better defenses.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 6.1 | Reconnaissance | OSINT, DNS enumeration, subdomain discovery, port scanning (Nmap), technology fingerprinting |
| 6.2 | Vulnerability Assessment | Common vulnerability types, CVSS scoring, vulnerability databases (NVD, CVE), scanning tools |
| 6.3 | Exploitation Concepts | How exploits work (buffer overflows, injection, deserialization), exploit chains, privilege escalation |
| 6.4 | Social Engineering | Phishing, pretexting, baiting, tailgating, security awareness training |
| 6.5 | MITRE ATT&CK | Tactics, techniques, procedures (TTPs), using ATT&CK for defense, threat intelligence |

---

## Phase 7: Compliance & Governance

> **Goal**: Understand regulatory requirements and security frameworks.

| Framework | Focus |
|-----------|-------|
| GDPR | Data privacy (EU), consent, right to erasure, DPO |
| HIPAA | Healthcare data protection, PHI, BAAs |
| SOC 2 | Trust service criteria (security, availability, confidentiality) |
| PCI-DSS | Payment card security, 12 requirements |
| ISO 27001 | Information security management system (ISMS) |
| NIST CSF | Cybersecurity framework (Identify, Protect, Detect, Respond, Recover) |

---

## Progress Tracking

- Save notes under `security/` folder
- Create `security/progress.md` to track completed modules
- Document security checklists and cheat sheets

## Recommended Resources

| Resource | Type | Best For |
|----------|------|----------|
| OWASP Top 10 | Reference | Web vulnerability overview |
| PortSwigger Web Security Academy | Interactive | Hands-on web security labs |
| Hack The Box | Platform | Offensive security practice |
| TryHackMe | Platform | Beginner-friendly security labs |
| Crypto101 (free book) | Book | Cryptography fundamentals |
| The Web Application Hacker's Handbook | Book | Web security deep dive |
