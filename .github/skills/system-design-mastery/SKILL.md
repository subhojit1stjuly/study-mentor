---
name: system-design-mastery
description: "Use when: studying system design, learning high-level design HLD, learning low-level design LLD, practicing system design interviews, understanding scalability, learning distributed systems, designing architectures, studying microservices, learning about load balancing, caching strategies, message queues, API design, preparing for senior engineer system design rounds."
argument-hint: "Topic or system to design (e.g., 'URL shortener', 'caching strategies', 'Phase 2')"
---

# System Design Mastery Roadmap

A structured, phase-based roadmap for mastering system design — from fundamentals through senior/staff-level interview readiness.

## When to Use

- Starting or resuming a system design study journey
- Preparing for system design interview rounds
- Learning to design scalable, reliable, available systems
- Understanding distributed systems concepts
- Practicing real-world system design problems

## How This Skill Works

1. **Assess** the user's current level
2. **Teach** concepts with theory, diagrams, and trade-off analysis
3. **Practice** with real-world system design problems
4. **Review** designs for completeness and depth
5. **Track** progress through phases

---

## Phase 0: Fundamentals

> **Goal**: Understand the building blocks of distributed systems.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 0.1 | Scalability | Vertical vs horizontal scaling, stateless services, auto-scaling, scaling databases |
| 0.2 | Availability & Reliability | SLAs/SLOs/SLIs, nines of availability, redundancy, failover, replication |
| 0.3 | Consistency Models | Strong consistency, eventual consistency, causal consistency, read-your-writes, linearizability |
| 0.4 | CAP & PACELC | CAP theorem deep dive, PACELC framework, practical implications, choosing the right trade-off |
| 0.5 | Back-of-Envelope | QPS estimation, storage estimation, bandwidth calculation, common numbers every engineer should know |

### Checkpoint
- Calculate QPS, storage, and bandwidth for a Twitter-like system
- Explain CAP theorem with 3 real database examples
- Explain the difference between availability and reliability

---

## Phase 1: Core Components

> **Goal**: Master the building blocks used in every system design.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 1.1 | Load Balancing | L4 vs L7, algorithms (round robin, least connections, consistent hashing, weighted), health checks, session affinity, GSLB |
| 1.2 | Caching | Cache-aside, read/write-through, write-behind, eviction (LRU, LFU, TTL), Redis, Memcached, CDN caching, cache invalidation, thundering herd |
| 1.3 | Databases at Scale | Replication (leader-follower, multi-leader, leaderless), sharding (range, hash, directory), partitioning, read replicas, connection pooling |
| 1.4 | Message Queues | Pub/sub, point-to-point, Kafka, RabbitMQ, SQS, delivery guarantees (at-least-once, at-most-once, exactly-once), dead letter queues, backpressure |
| 1.5 | API Design | REST (resource naming, versioning, pagination), GraphQL, gRPC, rate limiting (token bucket, sliding window), idempotency |
| 1.6 | Storage | Blob/object storage (S3), block storage (EBS), file storage (EFS), SQL vs NoSQL selection, LSM trees vs B-trees |
| 1.7 | Networking | DNS, CDNs, reverse proxies (Nginx, Envoy), API gateways, WebSockets, SSE, long polling |

### Checkpoint
- Design a caching strategy for a read-heavy e-commerce product catalog
- Explain when to use Kafka vs RabbitMQ vs SQS
- Design an API for a social media feed (REST)

---

## Phase 2: Architecture Patterns

> **Goal**: Understand and apply common architectural patterns.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 2.1 | Microservices | Monolith → microservices migration, service boundaries, service discovery, circuit breakers, saga pattern, sidecar pattern |
| 2.2 | Event-Driven Architecture | Event sourcing, CQRS, event bus, eventual consistency, compensating transactions |
| 2.3 | Data Patterns | Database per service, shared database, polyglot persistence, data replication, change data capture (CDC) |
| 2.4 | Observability | Structured logging, metrics (counters, gauges, histograms), distributed tracing (Jaeger, Zipkin), alerting, SLIs/SLOs |
| 2.5 | Security | Authentication at scale (OAuth, JWT, session), encryption (at rest, in transit), secrets management, API security, DDoS mitigation |

### Checkpoint
- Compare event sourcing vs CRUD with trade-offs
- Design a observability stack for a microservices architecture
- Explain the saga pattern with a concrete e-commerce example

---

## Phase 3: Real-World System Designs (Interview Practice)

> **Goal**: Practice designing 15+ real-world systems at interview quality.

### System Design Problems

| # | System | Key Focus Areas |
|---|--------|----------------|
| 3.1 | URL Shortener | Hashing, base62 encoding, database design, read-heavy optimization |
| 3.2 | Paste Bin | Object storage, expiration, content delivery |
| 3.3 | Rate Limiter | Token bucket, sliding window, distributed rate limiting |
| 3.4 | Notification System | Push, pull, pub/sub, priority, multi-channel delivery |
| 3.5 | Twitter/X Feed | Fan-out on read vs write, timeline generation, ranking |
| 3.6 | Instagram | Image storage, CDN, feed generation, stories |
| 3.7 | WhatsApp/Chat | WebSocket, message ordering, delivery receipts, group chat, E2E encryption |
| 3.8 | YouTube/Netflix | Video transcoding, adaptive bitrate, CDN, recommendation |
| 3.9 | Uber/Ride Sharing | Location tracking, matching, ETA, surge pricing, geospatial indexing |
| 3.10 | Google Maps | Graph algorithms, geospatial data, tile rendering, routing |
| 3.11 | Dropbox/Google Drive | File sync, chunking, deduplication, conflict resolution |
| 3.12 | Search Engine | Web crawler, indexer, ranking (PageRank), inverted index |
| 3.13 | Distributed Cache | Consistent hashing, replication, eviction, hot key handling |
| 3.14 | Ticket Booking (BookMyShow) | Seat locking, distributed locking, concurrency, payment |
| 3.15 | Payment System | Idempotency, distributed transactions, reconciliation, PCI compliance |
| 3.16 | Collaborative Editor (Google Docs) | OT vs CRDT, conflict resolution, real-time sync |
| 3.17 | Ad Click Aggregator | Stream processing, Lambda architecture, real-time analytics |
| 3.18 | Distributed Key-Value Store | Partitioning, replication, consistency, Dynamo paper |

### Interview Framework

For each system design, follow:
```
1. REQUIREMENTS    → Functional + non-functional (scale, latency, availability)
2. ESTIMATION      → Users, QPS, storage, bandwidth (back-of-envelope)
3. API DESIGN      → Key endpoints, request/response formats
4. DATA MODEL      → Schema, relationships, SQL vs NoSQL choice with justification
5. HIGH-LEVEL      → ASCII architecture diagram with component responsibilities
6. DEEP DIVES      → Pick 2-3 components (caching, DB design, message queue, etc.)
7. TRADE-OFFS      → Every decision has alternatives — discuss them proactively
8. BOTTLENECKS     → What breaks at 10x scale? How to address it?
```

---

## Phase 4: Low-Level Design (LLD)

> **Goal**: Master object-oriented design and class-level architecture.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 4.1 | OOP Principles | SOLID, DRY, KISS, YAGNI, composition over inheritance |
| 4.2 | Design Patterns | Creational (Singleton, Factory, Builder, Prototype), Structural (Adapter, Decorator, Facade, Proxy), Behavioral (Strategy, Observer, Command, State, Template Method) |
| 4.3 | LLD Problems | Parking lot, elevator system, library management, chess game, food delivery app, hotel booking, file system, logging framework, pub/sub system |

---

## Progress Tracking

- Save design notes under `system-design/` folder
- Create `system-design/progress.md` to track completed designs
- For each system designed, save the ASCII diagram and key decisions
- Practice each system design within a 45-minute timer

## Recommended Resources

| Resource | Type | Best For |
|----------|------|----------|
| System Design Interview (Alex Xu Vol 1 & 2) | Book | Core concepts + practice |
| Designing Data-Intensive Applications (Kleppmann) | Book | Deep distributed systems theory |
| ByteByteGo (YouTube) | Video | Visual system design explanations |
| Gaurav Sen (YouTube) | Video | Intuitive system design concepts |
| Grokking System Design | Course | Structured interview prep |
| System Design Primer (GitHub) | Reference | Quick reference for components |
