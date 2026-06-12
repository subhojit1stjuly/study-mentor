# System Design Domain

This domain provides specialized templates and guidance for mastering system design - the art of designing scalable, reliable distributed systems.

## What is System Design?

System design is the process of defining the architecture, components, modules, interfaces, and data for a system to satisfy specified requirements. It's essential for:
- Senior+ engineering roles
- Technical leadership positions
- Building scalable products
- System design interviews (FAANG, etc.)

## Key Skills

1. **Fundamentals**: Scalability, reliability, availability, latency, throughput
2. **Architecture Patterns**: Monolith, microservices, event-driven, serverless
3. **Databases**: SQL vs NoSQL, sharding, replication, consistency
4. **Caching**: Redis, Memcached, CDN strategies
5. **Load Balancing**: Algorithms, health checks, failover
6. **Message Queues**: Kafka, RabbitMQ, SQS
7. **System Components**: API Gateway, service mesh, reverse proxy
8. **Trade-offs**: CAP theorem, consistency models, cost vs performance

## Learning Progression

### Phase 1: Foundation (Beginner)
- Basic system design concepts
- Client-server architecture
- REST APIs and HTTP
- Databases (relational vs non-relational)
- Caching basics
- Load balancing concepts
- Simple system designs (URL shortener)

### Phase 2: Development (Intermediate)
- Horizontal vs vertical scaling
- Database sharding and replication
- Microservices architecture
- Message queues and event-driven design
- CDNs and caching strategies
- API design and versioning
- Medium complexity systems (Twitter, Instagram)

### Phase 3: Mastery (Advanced)
- Distributed systems theory
- Consistency and consensus (Paxos, Raft)
- Complex trade-off analysis
- Multi-region deployments
- Performance optimization at scale
- Real-world production incidents and solutions
- Complex systems (YouTube, Netflix, Uber)

## Recommended Resources

1. **Books**
   - "Designing Data-Intensive Applications" by Martin Kleppmann
   - "System Design Interview" by Alex Xu (Vol 1 & 2)
   - "Building Microservices" by Sam Newman

2. **Courses**
   - Grokking System Design Interview
   - System Design Primer (GitHub)
   - ByteByteGo (YouTube)

3. **Practice**
   - Mock interviews with peers
   - Study real-world architectures
   - Read engineering blogs (Netflix, Uber, Meta)

## Learning Strategy

1. **Case Studies**: Study how real companies solve problems
2. **Draw Diagrams**: Always sketch architecture diagrams
3. **Trade-off Analysis**: No perfect solution, understand trade-offs
4. **Scale Thinking**: Start simple, then scale gradually
5. **Numbers Matter**: Learn back-of-the-envelope calculations
6. **Mock Interviews**: Practice explaining designs verbally

## Core Topics

### 1. Scalability
- Horizontal vs vertical scaling
- Load balancing strategies
- Database sharding
- Caching at multiple layers
- CDN for static assets

### 2. Reliability & Availability
- Redundancy and replication
- Failover strategies
- Health checks and monitoring
- Disaster recovery
- SLAs, SLOs, SLIs

### 3. Performance
- Latency vs throughput
- Bottleneck identification
- Database query optimization
- Caching strategies
- Asynchronous processing

### 4. Data Storage
- SQL vs NoSQL trade-offs
- Database types (relational, document, key-value, graph)
- Data partitioning and sharding
- Replication (master-slave, master-master)
- Consistency models (strong, eventual, causal)

### 5. Networking
- TCP vs UDP
- HTTP/HTTPS, WebSockets
- DNS and load balancing
- API Gateway patterns
- Rate limiting and throttling

### 6. Messaging & Queues
- Pub/Sub vs message queues
- Kafka, RabbitMQ, SQS
- Event-driven architecture
- Stream processing

### 7. Caching
- Cache invalidation strategies
- Cache-aside, write-through, write-back
- Redis, Memcached
- CDN (CloudFlare, CloudFront)
- Application-level caching

### 8. Microservices
- Service decomposition
- Service communication (REST, gRPC)
- Service discovery
- API Gateway
- Distributed tracing

### 9. Monitoring & Observability
- Logging (ELK stack)
- Metrics (Prometheus, Grafana)
- Distributed tracing (Jaeger)
- Alerting strategies

## Common System Design Questions

### Beginner Level
- Design a URL shortener (bit.ly)
- Design a pastebin (pastebin.com)
- Design a rate limiter

### Intermediate Level
- Design Twitter
- Design Instagram
- Design Uber
- Design WhatsApp
- Design YouTube

### Advanced Level
- Design Netflix
- Design Google Search
- Design Amazon
- Design Ticketmaster
- Design a distributed cache

## Interview Framework (RADIO)

1. **Requirements** clarification
   - Functional requirements
   - Non-functional requirements (scale, latency, availability)
   - Assumptions

2. **Architecture** high-level design
   - Draw major components
   - Data flow
   - APIs

3. **Deep Dive** into components
   - Database schema
   - Caching strategy
   - Scaling approach

4. **Identify** bottlenecks
   - What breaks at scale?
   - How to fix it?

5. **Optimization** and trade-offs
   - Performance improvements
   - Cost optimization
   - Trade-off justifications

## Back-of-Envelope Calculations

Know these numbers:
- 1 million requests/day ≈ 12 requests/second
- 1 billion users ≈ need to shard database
- Typical cache hit ratio: 80-90%
- Network latency: 1-100ms depending on distance
- Disk seek: ~10ms
- SSD read: ~1ms
- Memory access: ~100ns

## Assessment Focus

For system design assessments:
- **Conceptual**: Explain trade-offs, CAP theorem, consistency models
- **Applied**: Design systems from requirements
- **Pattern Recognition**: Choose appropriate patterns for scenarios
- **Teaching**: Justify design decisions clearly

## Time Commitment

- **Beginner to Interview-Ready**: 3-6 months with 2 hours/day
- **Interview-Ready to Expert**: 2-3 years of building real systems
- **Maintenance**: Read engineering blogs, study incidents weekly

## Success Metrics

- ✅ Can design common systems (Twitter, Instagram, etc.)
- ✅ Explain trade-offs clearly
- ✅ Know when to use which database, cache, queue
- ✅ Perform back-of-envelope calculations
- ✅ Pass system design interviews
- ✅ Anticipate failure modes
- ✅ Design for scale from the start

## Resources

### Engineering Blogs (Learn from the best)
- Netflix Tech Blog
- Uber Engineering
- Meta Engineering
- AWS Architecture Blog
- Google Cloud Blog
- Martin Fowler's blog

### YouTube Channels
- ByteByteGo
- Gaurav Sen
- Tech Dummies Narendra L
- System Design Interview

### Communities
- r/systemdesign
- Blind (for interview experiences)
- High Scalability blog

## Domain-Specific Considerations

**No Perfect Answer**: System design is about trade-offs, not right/wrong.

**Start Simple**: Begin with basic solution, then optimize.

**Scale Numbers**: Always discuss scale - 100 users vs 100M users.

**Real-World Examples**: Reference how actual companies solve problems.

**Draw It Out**: Visualizations are critical in system design.

**Failure Modes**: Think about what can go wrong and how to handle it.

**Cost Aware**: Mention cost implications of design decisions.

---

Use the templates in this directory for system design-specific learning paths.
