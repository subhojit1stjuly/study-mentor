---
name: database-mastery
description: "Use when: studying databases, learning SQL, practicing SQL queries, understanding database indexing, learning schema design, studying normalization, learning NoSQL, understanding transactions, ACID properties, query optimization, studying distributed databases, learning PostgreSQL MySQL MongoDB Redis, database interview preparation, ER diagrams, studying data modeling."
argument-hint: "Topic or phase (e.g., 'window functions', 'indexing', 'Phase 2 NoSQL')"
---

# Database Mastery Roadmap

A structured roadmap for mastering databases — from SQL fundamentals through distributed database internals.

## When to Use

- Starting or resuming database learning
- Preparing for database-heavy interview questions
- Learning SQL query writing and optimization
- Understanding database internals (indexing, transactions, replication)
- Choosing between SQL vs NoSQL for a project
- Studying distributed database concepts

## How This Skill Works

1. **Assess** → Determine the user's current database knowledge level
2. **Teach** → Concepts with theory, diagrams, and hands-on SQL practice
3. **Practice** → Write real queries against sample schemas
4. **Build** → Design schemas for real-world scenarios
5. **Optimize** → Learn to read execution plans and optimize queries
6. **Scale** → Understand sharding, replication, and distributed patterns

---

## Phase 0: SQL Foundations

> **Goal**: Write correct, readable SQL and understand relational concepts.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 0.1 | Relational Model | Tables, rows, columns, primary keys, foreign keys, constraints (NOT NULL, UNIQUE, CHECK, DEFAULT) |
| 0.2 | Basic Queries | SELECT, WHERE, ORDER BY, LIMIT, DISTINCT, aliases, LIKE, IN, BETWEEN, NULL handling (IS NULL, COALESCE) |
| 0.3 | Joins | INNER JOIN, LEFT/RIGHT/FULL OUTER JOIN, CROSS JOIN, self-join, natural join, join conditions vs WHERE |
| 0.4 | Aggregation | GROUP BY, HAVING, COUNT, SUM, AVG, MIN, MAX, aggregate with joins |
| 0.5 | Subqueries | Scalar subqueries, column subqueries, table subqueries, correlated subqueries, EXISTS vs IN |
| 0.6 | Data Modification | INSERT, UPDATE, DELETE, UPSERT (INSERT ON CONFLICT), MERGE, TRUNCATE vs DELETE |

### Checkpoint
- Write a query joining 3+ tables with filtering and aggregation
- Explain the difference between WHERE and HAVING
- Convert a correlated subquery to a JOIN

---

## Phase 1: Intermediate SQL

> **Goal**: Master advanced SQL features used in real-world analytics and applications.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 1.1 | Window Functions | ROW_NUMBER, RANK, DENSE_RANK, NTILE, LEAD/LAG, FIRST_VALUE/LAST_VALUE, SUM/AVG OVER, PARTITION BY, framing (ROWS/RANGE BETWEEN) |
| 1.2 | CTEs & Recursion | Common Table Expressions (WITH), recursive CTEs (hierarchical data, org charts, bill of materials), CTE vs subquery vs temp table |
| 1.3 | Set Operations | UNION, UNION ALL, INTERSECT, EXCEPT, combining result sets |
| 1.4 | Advanced Functions | CASE expressions, string functions, date/time functions, CAST/CONVERT, COALESCE, NULLIF, conditional aggregation |
| 1.5 | Views & Procedures | Views, materialized views, stored procedures, functions, triggers, cursors — when to use each |

### Checkpoint
- Write a query using window functions to calculate running totals and rankings
- Use a recursive CTE to traverse a tree structure (employee → manager hierarchy)
- Create a materialized view and explain when to choose it over a regular view

---

## Phase 2: Schema Design & Modeling

> **Goal**: Design correct, efficient database schemas for real-world applications.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 2.1 | ER Diagrams | Entities, attributes, relationships (1:1, 1:N, M:N), cardinality, participation constraints, ER to relational mapping |
| 2.2 | Normalization | 1NF (atomic values), 2NF (no partial dependencies), 3NF (no transitive dependencies), BCNF, 4NF, 5NF — with examples |
| 2.3 | Denormalization | When and why to denormalize, read optimization, precomputed columns, materialized aggregates, trade-offs |
| 2.4 | Schema Patterns | Star schema, snowflake schema, data vault, slowly changing dimensions (SCD Type 1/2/3), audit trails |
| 2.5 | Real-World Design | E-commerce schema, social media schema, booking system schema, chat application schema, multi-tenant schema |

### Checkpoint
- Design a normalized schema for an e-commerce platform (users, products, orders, reviews)
- Identify normalization violations in a given schema and fix them
- Design a star schema for an analytics dashboard

---

## Phase 3: Indexing & Query Optimization

> **Goal**: Make queries fast — understand how databases execute queries and how to optimize them.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 3.1 | How Indexes Work | B-tree indexes, hash indexes, index pages, clustered vs non-clustered, covering indexes, composite indexes (column order matters!) |
| 3.2 | Index Types | Partial indexes, expression indexes, GIN indexes (for JSONB/arrays), GiST indexes (spatial), full-text indexes, bitmap indexes |
| 3.3 | Query Plans | EXPLAIN / EXPLAIN ANALYZE, sequential scan vs index scan vs bitmap scan, join algorithms (nested loop, hash join, merge join), sort operations |
| 3.4 | Optimization Techniques | Index selection strategy, query rewriting, avoiding SELECT *, using EXISTS vs IN, pagination (offset vs cursor), partitioning (range, hash, list) |
| 3.5 | Common Pitfalls | N+1 query problem, implicit type casting killing indexes, functions on indexed columns, over-indexing, bloat |

### Checkpoint
- Read an EXPLAIN ANALYZE output and identify the bottleneck
- Choose the right indexes for a given query workload
- Optimize a slow query from 5 seconds to under 100ms (with explanation)

---

## Phase 4: Transactions & Concurrency

> **Goal**: Understand how databases handle concurrent access safely.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 4.1 | ACID Properties | Atomicity, Consistency, Isolation, Durability — what each means mechanically |
| 4.2 | Isolation Levels | Read Uncommitted, Read Committed, Repeatable Read, Serializable — anomalies each prevents (dirty read, non-repeatable read, phantom read) |
| 4.3 | Concurrency Control | Pessimistic locking (SELECT FOR UPDATE), optimistic locking (version columns), MVCC (how PostgreSQL does it), deadlocks, lock granularity |
| 4.4 | WAL & Recovery | Write-ahead logging, checkpoints, crash recovery, point-in-time recovery, backup strategies |

### Checkpoint
- Explain what anomaly each isolation level prevents with concrete examples
- Implement optimistic locking for a bank transfer scenario
- Explain how MVCC works in PostgreSQL

---

## Phase 5: NoSQL Databases

> **Goal**: Understand NoSQL paradigms and when to choose each.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 5.1 | Document Stores | MongoDB (collections, documents, embedded vs referenced, aggregation pipeline), schema design patterns for document DBs |
| 5.2 | Key-Value Stores | Redis (data types, persistence, pub/sub, Lua scripting, caching patterns), DynamoDB (partition keys, sort keys, GSI/LSI) |
| 5.3 | Column-Family | Cassandra (partition key, clustering key, write-optimized, eventual consistency), HBase, wide-column modeling |
| 5.4 | Graph Databases | Neo4j (Cypher queries, nodes, relationships, properties), use cases (social networks, recommendations, fraud detection) |
| 5.5 | Search Engines | Elasticsearch (inverted index, mapping, analyzers, full-text search, aggregations), use cases |
| 5.6 | Time-Series | InfluxDB, TimescaleDB, time-series data modeling, downsampling, retention policies |

### Checkpoint
- Model the same data in MongoDB, Redis, and Cassandra — explain the trade-offs
- Write a Cypher query to find friends-of-friends in Neo4j
- Design a caching layer with Redis for a high-traffic API

---

## Phase 6: Distributed Databases

> **Goal**: Understand how databases work at internet scale.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 6.1 | Replication | Leader-follower, multi-leader, leaderless, synchronous vs asynchronous, replication lag, read-after-write consistency |
| 6.2 | Sharding | Range-based, hash-based, directory-based, shard key selection, resharding, cross-shard queries, hotspots |
| 6.3 | Consensus | Paxos, Raft (leader election, log replication), distributed consensus challenges, split-brain problem |
| 6.4 | Distributed Transactions | Two-phase commit (2PC), three-phase commit, saga pattern (choreography vs orchestration), compensating transactions |
| 6.5 | Conflict Resolution | Last-writer-wins, vector clocks, CRDTs, Lamport timestamps, causal ordering |
| 6.6 | Data Warehousing | OLTP vs OLAP, columnar storage, ETL/ELT, data lakes, data lakehouses, Apache Spark basics |

### Checkpoint
- Explain Raft consensus step by step
- Design a sharding strategy for a user table with 1 billion rows
- Compare saga pattern (choreography vs orchestration) for an e-commerce order flow

---

## Progress Tracking

- Save notes under `databases/` folder
- Create `databases/progress.md` to track completed modules
- Save SQL practice queries with explanations
- Track schema designs as separate files

## Recommended Resources

| Resource | Type | Best For |
|----------|------|----------|
| SQLZoo / SQLBolt | Interactive | SQL practice (beginner) |
| LeetCode Database | Platform | SQL interview problems |
| Use The Index, Luke | Book (free) | Indexing deep dive |
| Designing Data-Intensive Applications | Book | Distributed DB theory |
| CMU Database Course (Andy Pavlo) | Video | Database internals |
| PostgreSQL Documentation | Reference | Production-grade SQL reference |
