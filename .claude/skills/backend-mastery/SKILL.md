---
name: backend-mastery
description: "Use when: studying backend development, learning API development, building REST APIs, learning server frameworks, studying Node.js Express Django FastAPI, understanding authentication, learning microservices, studying message queues, learning Docker Kubernetes, backend architecture, server-side programming, building backend projects, studying DevOps CI/CD, understanding cloud deployment."
argument-hint: "Topic or phase (e.g., 'REST API design', 'authentication', 'Phase 3 microservices')"
---

# Backend Mastery Roadmap

A structured roadmap for mastering backend engineering — from building REST APIs through deploying microservices at scale.

## When to Use

- Starting or resuming backend development learning
- Building APIs and server-side applications
- Learning backend frameworks (Node.js, Python, Go, Java)
- Understanding authentication, authorization, and security
- Learning to deploy and scale backend services

---

## Phase 0: Backend Fundamentals

> **Goal**: Understand how backend systems work.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 0.1 | How the Web Works | HTTP request lifecycle, client-server model, DNS resolution, TCP/IP basics, ports, status codes (2xx, 3xx, 4xx, 5xx) |
| 0.2 | HTTP Deep Dive | HTTP methods (GET, POST, PUT, PATCH, DELETE), headers, cookies, caching (ETag, Cache-Control), content negotiation, CORS |
| 0.3 | API Paradigms | REST, GraphQL, gRPC, WebSockets, SSE — trade-offs, when to use each |
| 0.4 | Data Formats | JSON, XML, Protocol Buffers, MessagePack, YAML — serialization/deserialization |

---

## Phase 1: Building APIs

> **Goal**: Build production-quality REST APIs.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 1.1 | REST API Design | Resource naming, URL structure, versioning (URL, header, query), pagination (offset, cursor), filtering, sorting, HATEOAS |
| 1.2 | Framework (Python) | FastAPI (routes, request/response models, dependency injection, middleware, background tasks), Django REST Framework, Flask |
| 1.3 | Framework (Node.js) | Express.js (routes, middleware, error handling), Nest.js (modules, services, controllers, decorators) |
| 1.4 | Database Integration | ORMs (SQLAlchemy, Prisma, TypeORM), query builders, connection pooling, migrations, seeding |
| 1.5 | Validation & Error Handling | Input validation (Pydantic, Zod, Joi), error response formats (RFC 7807), global error handlers, custom exceptions |
| 1.6 | Documentation | OpenAPI/Swagger, auto-generated docs (FastAPI), API documentation best practices |

### Projects
- CRUD REST API with database, validation, and error handling
- Blog API with user authentication and authorization
- E-commerce API with product catalog, cart, and orders

---

## Phase 2: Authentication & Security

> **Goal**: Implement secure authentication and authorization.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 2.1 | Password Auth | Hashing (bcrypt, Argon2), salting, registration flow, login flow, password reset |
| 2.2 | JWT & Sessions | JWT (access/refresh tokens, rotation, blacklisting), session-based auth (cookies, Redis store), trade-offs |
| 2.3 | OAuth 2.0 | Authorization code flow + PKCE, social login (Google, GitHub), token management, scopes |
| 2.4 | Authorization | RBAC implementation, middleware/guards, resource-level permissions, policy engines |
| 2.5 | API Security | Rate limiting (token bucket), input sanitization, CORS configuration, security headers (Helmet.js), HTTPS enforcement |

---

## Phase 3: Advanced Backend

> **Goal**: Build scalable, production-grade backend systems.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 3.1 | Caching | Redis (strings, hashes, lists, sorted sets, pub/sub), caching strategies (cache-aside, write-through), cache invalidation, TTL |
| 3.2 | Message Queues | RabbitMQ (exchanges, queues, bindings), Kafka (topics, partitions, consumer groups), background job processing (Celery, BullMQ) |
| 3.3 | Real-time | WebSocket implementation, Socket.io, Server-Sent Events, pub/sub for real-time notifications |
| 3.4 | File Handling | File uploads (multipart), cloud storage (S3), image processing/resizing, streaming large files |
| 3.5 | Microservices | Service decomposition, API gateway, service discovery, inter-service communication (sync vs async), circuit breaker, saga pattern |
| 3.6 | GraphQL Server | Schema definition, resolvers, N+1 problem (DataLoader), subscriptions, authentication, caching |

---

## Phase 4: DevOps & Deployment

> **Goal**: Deploy and operate backend services in production.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 4.1 | Containers | Docker (Dockerfile, multi-stage builds, volumes, networking), Docker Compose, container best practices |
| 4.2 | CI/CD | GitHub Actions (workflows, jobs, steps), testing in CI, automated deployment, semantic versioning |
| 4.3 | Cloud Deployment | AWS (EC2, ECS, Lambda, RDS, S3, SQS), Vercel, Railway, managed databases, environment management |
| 4.4 | Kubernetes | Pods, services, deployments, ConfigMaps, secrets, Helm, horizontal pod autoscaler, health checks |
| 4.5 | Observability | Structured logging, application metrics (Prometheus), distributed tracing, error tracking (Sentry), alerting |
| 4.6 | Infrastructure as Code | Terraform basics, CloudFormation, infrastructure provisioning, state management |

---

## Progress Tracking

- Save notes under `web-dev/backend/` folder
- Create `web-dev/backend/progress.md` to track completed modules
- Save project code under `web-dev/projects/`

## Recommended Resources

| Resource | Type | Best For |
|----------|------|----------|
| FastAPI Docs | Docs | Python API development |
| Node.js Docs | Docs | Node.js fundamentals |
| roadmap.sh/backend | Roadmap | Visual backend path |
| Hussein Nasser (YouTube) | Video | Backend concepts explained |
| Docker Docs | Docs | Containerization |
| The Twelve-Factor App | Reference | Modern app methodology |
