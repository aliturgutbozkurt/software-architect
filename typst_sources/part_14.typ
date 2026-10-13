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
  part-num: 14,
  section-title: "Section 4: Asynchronous Horizons — Event-Driven Architecture",
  title: "Kafka Without the Tears: Partitions, Offsets, and Consumer Groups",
  subtitle: "Demystifying distributed event logs so you can scale data pipelines without losing sleep.",
  reading-time: "9 min"
)

#war-story(
  title: "WAR STORY FROM THE TRENCHES",
  [A ride-sharing company deployed Apache Kafka to track driver GPS coordinates in real time. The topic was created with a single partition. As the number of active drivers grew from 500 to 50,000, the single partition broker became saturated. To fix this, an engineer spun up 10 new consumer servers. To his bewilderment, only ONE consumer server was doing any work; the other 9 sat completely idle at 0% CPU! Desperate, another engineer changed the partition key from `driver_id` to random UUIDs. Suddenly, the GPS points for Driver 42 were scattered across 20 partitions. A ride ended up being calculated as: 1) Driver arrived, 2) Driver accepted ride, 3) Driver dropped off rider—in completely reversed order! Passengers were billed \$0 for trips and charged \$400 for rides that never started.]
)

== The Paradigm Shift: From Coder to Architect Mindset
Kafka is not a traditional message queue; it is a distributed, partitioned, replicated append-only commit log. The fundamental unit of scalability in Kafka is the *Partition*, and the fundamental rule of Kafka consumption is: *You can never have more active consumers in a consumer group than you have partitions in the topic.* If you want 10 consumers working in parallel, you must have at least 10 partitions. And if you care about message ordering, messages with the same business key MUST hash to the same partition.

== Core Architectural Principles & Mental Models
=== The Core Mechanics of Kafka
- *Partitions & Keys:* Kafka uses `hash(key) % num_partitions`. All events for `order_123` land on Partition 2 in strict chronological order. Total ordering across the entire topic does NOT exist; ordering is guaranteed ONLY within a single partition.
- *Offsets:* The sequential ID of each message in a partition. Consumers track their progress by committing their offset (`I have processed up to offset 402`).
- *Consumer Groups:* A set of cooperating workers. Kafka automatically balances partitions among group members. If a consumer dies, Kafka triggers a *rebalance* to reassign its partitions.

=== Delivery Guarantees: At-Least-Once vs. Exactly-Once
By default, distributed systems achieve *At-Least-Once* delivery. If a consumer processes a message and crashes before committing the offset, the replacement consumer will read that message again! Your consumers MUST be idempotent.

== Common Anti-Patterns & Traps to Avoid
- *The Rebalance Storm:* Setting consumer heartbeat timeouts too aggressively, causing long-running tasks to be declared dead, triggering constant partition rebalancing that halts all processing.
- *The Random Key Trap:* Forgetting to set a partition key on ordered events, causing related state updates to arrive out of order on different partitions.
- *The Giant Message Antipattern:* Sending 20-megabyte video files or giant PDF documents through Kafka messages instead of sending a lightweight metadata pointer to an S3 bucket.

#architect-playbook(
  title: "THE ARCHITECT'S PLAYBOOK: ACTION STEPS THIS WEEK",
  [
    - *Step 1:* Partition Sizing: Size your topic partitions based on target throughput (aim for 1-2 MB/sec per partition as a safe rule of thumb).
    - *Step 2:* Always set the partition key to the business entity ID that requires strict ordering (e.g., `user_id`, `account_id`).
    - *Step 3:* Design all event handlers to be strictly idempotent: use unique event IDs and database unique constraints so duplicate deliveries cause zero harm.
  ]
)

== Architectural Takeaways & Cheatsheet
- Kafka guarantees ordering ONLY within a partition, never across the whole topic.
- Adding more consumers than partitions is useless; the extra consumers will sit idle.
- Never assume messages arrive exactly once; design every consumer to survive duplicate deliveries.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM DISCUSSION PROMPT",
  [
    *Course Reflection & Hands-on Assignment:* If your consumer crashes right after executing a database update but before committing its message offset to Kafka, what happens when it restarts? Does your code handle this safely?
  ]
)