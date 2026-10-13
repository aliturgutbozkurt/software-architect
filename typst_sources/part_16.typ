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
  part-num: 16,
  section-title: "Section 4: Asynchronous Horizons — Event-Driven Architecture",
  title: "Event Sourcing and CQRS: When the History Matters More Than the Present",
  subtitle: "How to build an audit-proof system of record without drowning in architectural complexity.",
  reading-time: "9 min"
)

#war-story(
  title: "WAR STORY FROM THE TRENCHES",
  [A multinational banking institution had an account management system that simply updated a `balance` column in a SQL table: `UPDATE accounts SET balance = balance - 500 WHERE id = 12`. One morning, an enterprise client called screaming: 'Our balance was \$1.2 million yesterday, and today it says \$450,000! Where did the money go?' The DBA searched the logs, but the database only showed the current state: \$450,000. There was no record of which transactions, automated fees, or wire transfers produced that number. The bank had to pay a \$250,000 regulatory fine for failing financial audit standards. They were forced to re-architect using Event Sourcing, storing every credit and debit as an immutable historical event.]
)

== The Paradigm Shift: From Coder to Architect Mindset
Traditional CRUD architectures discard history: when you update a row, the old state is erased forever. *Event Sourcing* inverts this: the source of truth is not the current state, but an immutable append-only log of domain events (`AccountOpened`, `MoneyDeposited`, `MoneyWithdrawn`). The current state is simply a mathematical projection calculated by replaying those events. Pair this with *CQRS (Command Query Responsibility Segregation)*, where writes (Commands) go to the event store, while reads (Queries) are served from fast, pre-aggregated projection tables.

== Core Architectural Principles & Mental Models
=== The Anatomy of CQRS & Event Sourcing
- *Command Side:* Validates business rules against the current aggregate, generates new events, and appends them to the Event Store.
- *Event Store:* Append-only database (e.g., EventStoreDB, or PostgreSQL with strict append tables). Events are never updated or deleted.
- *Projection / Read Model:* Asynchronous listeners read events and update read-optimized tables (e.g., Elasticsearch for search, Redis for key lookups, Postgres for dashboards).
- *Snapshotting:* To avoid replaying 100,000 events to compute an aggregate's current state, take a snapshot every 100 events.

=== When NOT to Use Event Sourcing (The Pragmatic Warning)
Event Sourcing has massive cognitive overhead: schema evolution of events over 5 years is notoriously hard (what happens when an event schema changes?), eventual consistency between write and read sides confuses developers, and GDPR 'Right to be Forgotten' requires cryptographic erasure tricks. Use it for core ledgers, insurance claims, and medical tracking; avoid it for basic CRUD.

== Common Anti-Patterns & Traps to Avoid
- *The Universal Event Sourcing Hammer:* Applying Event Sourcing to a simple blog, marketing site, or user settings page where basic CRUD is 100x simpler.
- *The Mutable Event Bug:* Attempting to update or delete an already-persisted event in the event store because of a bug in the projection.
- *The Missing Snapshot:* Replaying 5 million historical events from the beginning of time every time an aggregate is loaded into memory, causing 30-second API latencies.

#architect-playbook(
  title: "THE ARCHITECT'S PLAYBOOK: ACTION STEPS THIS WEEK",
  [
    - *Step 1:* Reserve Event Sourcing for domains where the audit trail IS the product (financial ledgers, legal compliance, inventory tracking).
    - *Step 2:* Define your event schemas defensively: make event attributes optional or version them (`OrderPlacedV1`, `OrderPlacedV2`).
    - *Step 3:* Implement snapshotting from Day 1 to ensure aggregate reconstruction remains under 10 milliseconds.
  ]
)

== Architectural Takeaways & Cheatsheet
- CRUD records current state; Event Sourcing records the journey of how you got there.
- CQRS decouples the write model from the read model, letting you optimize both independently.
- Event Sourcing is an architectural Ferrari: incredible performance and power, but high maintenance and expensive to drive.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM DISCUSSION PROMPT",
  [
    *Course Reflection & Hands-on Assignment:* Which domain in your business would benefit most from an immutable audit trail? What is the biggest risk of introducing CQRS into your existing tech stack?
  ]
)