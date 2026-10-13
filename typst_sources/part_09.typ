#import "/templates/book_style.typ": *

#set page(
  paper: "a4",
  margin: (top: 2.2cm, bottom: 2.2cm, left: 2.2cm, right: 2.2cm),
  header: align(right)[#text(size: 8pt, fill: rgb("#94a3b8"))[Think Like a Software Architect • Masterclass]],
  footer: [
    #align(center)[
      #context text(size: 8.5pt, fill: rgb("#64748b"))[
        Page #counter(page).display("1 of 1", both: true)
      ]
    ]
  ]
)
#set text(font: ("Avenir", "Helvetica Neue", "Arial"), size: 10pt, fill: rgb("#0f172a"))
#set par(justify: true, leading: 0.72em)

#chapter-header(
  part-num: 9,
  section-title: "Section 3: Data Architecture — Where State Lives, Dies, and Lies",
  title: "Polyglot Persistence: Choosing the Right Weapon for Your Data",
  subtitle: "Why forcing all your application data into a single SQL table or Mongo collection is architectural malpractice.",
  reading-time: "9 min"
)

#war-story(
  title: "WAR STORY FROM THE TRENCHES",
  [A social networking app stored everything inside a single PostgreSQL database. When they introduced a 'Friends of Friends' recommendation feature, the query required a 6-level recursive SQL join across 12 million user relationship rows. During peak hours, every time a user visited their feed, the database CPU spiked to 100%, locking the table for 15 seconds. Frustrated, a junior engineer suggested migrating the entire company from PostgreSQL to MongoDB 'because NoSQL is fast.' They spent three months migrating, only to discover that executing financial balance checks and user profile updates without ACID transactions caused user account balances to randomly drift by thousands of dollars. They had replaced a relational query bottleneck with a data integrity nightmare.]
)

== The Paradigm Shift: From Coder to Architect Mindset
Code is transient; data is permanent. Martin Fowler popularized the term *Polyglot Persistence*: using different data storage technologies to handle different data storage needs within the same overall architecture. You don't use a screwdriver to hammer a nail. Relational databases excel at transactional integrity and complex joins; Document stores excel at unstructured polymorphic catalogs; Key-Value stores excel at high-speed lookups; Graph databases excel at traversing connected networks.

== Core Architectural Principles & Mental Models
=== The Modern Data Weaponry Matrix
- *Relational (RDBMS - PostgreSQL, MySQL):* Structured, schema-enforced, ACID transactions, complex relational queries. Default choice for 90% of business domains.
- *Key-Value (Redis, DynamoDB, Memcached):* O(1) reads/writes, lightning-fast session state, caching, rate limiting, leaderboards.
- *Document (MongoDB, Couchbase):* Hierarchical JSON objects, flexible evolving schemas, content management, product catalogs with varying attributes.
- *Wide-Column / Time-Series (Cassandra, ScyllaDB, TimescaleDB, InfluxDB):* Append-heavy sensor telemetry, financial tick logs, write throughput measured in millions per second.
- *Graph (Neo4j, Amazon Neptune):* First-class relationships, fraud detection networks, social graphs, permission trees.

=== The Default Rule: PostgreSQL Until Proven Guilty
Never adopt a specialized NoSQL database until you can prove with telemetry that PostgreSQL (with JSONB, full-text search, and proper indexing) cannot handle the workload. Specialized databases add operational sprawl.

== Common Anti-Patterns & Traps to Avoid
- *The Golden Hammer:* Believing your favorite database (whether SQL or Mongo) is the best solution for every problem in computer science.
- *The Database Zoo:* Having 7 different database technologies maintained by a 6-person engineering team, resulting in zero deep operational expertise.
- *The Dual-Write Quagmire:* Writing to PostgreSQL and Elasticsearch in two consecutive application lines without transactional outbox or CDC, causing search results to become permanently desynchronized.

#architect-playbook(
  title: "THE ARCHITECT'S PLAYBOOK: ACTION STEPS THIS WEEK",
  [
    - *Step 1:* Audit your access patterns before selecting storage: Is this workload read-heavy, write-heavy, relationship-heavy, or text-search heavy?
    - *Step 2:* Profile query latencies under load: If relational joins exceed 500ms, evaluate whether a read-optimized projection or specialized store is needed.
    - *Step 3:* Use Change Data Capture (CDC via Debezium) to synchronize secondary search engines (like Elasticsearch/OpenSearch) from your primary source of truth.
  ]
)

== Architectural Takeaways & Cheatsheet
- Data models dictate system architecture far more than application programming languages.
- Default to a solid relational engine like PostgreSQL; break out into specialized stores only when specific query shapes demand it.
- If you write to two different datastores synchronously, you have built an eventually inconsistent distributed system.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM DISCUSSION PROMPT",
  [
    *Course Reflection & Hands-on Assignment:* Look at the data models in your company. Are there any queries where you are using SQL for graph traversals, or NoSQL for relational reporting? How is that impacting performance?
  ]
)