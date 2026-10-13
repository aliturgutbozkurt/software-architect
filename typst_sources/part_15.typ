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
  part-num: 15,
  section-title: "Section 4: Asynchronous Horizons — Event-Driven Architecture",
  title: "Eventual Consistency in Action: The Saga Pattern vs. Two-Phase Commit",
  subtitle: "How to execute complex multi-service business transactions without locking up the universe.",
  reading-time: "9 min"
)

#war-story(
  title: "WAR STORY FROM THE TRENCHES",
  [A travel booking platform needed to book a Flight, a Hotel, and a Rental Car as a single package. In their initial microservice architecture, the architect implemented a distributed transaction using Two-Phase Commit (2PC). During a holiday rush, a customer initiated a booking. The 2PC coordinator placed a row lock on the Flight seat in the airline DB and a row lock on the Hotel room in the hotel DB. Then, the Rental Car API had a network hiccup and took 42 seconds to respond. For those 42 seconds, that flight seat and hotel room were completely locked, blocking 300 other booking requests. When the car API finally timed out, the coordinator had to orchestrate a rollback across all 3 databases. The entire booking engine froze into a cascading deadlock.]
)

== The Paradigm Shift: From Coder to Architect Mindset
Two-Phase Commit (2PC) does not scale in modern cloud architectures. It relies on locking distributed resources across network boundaries, turning the slowest network link into the bottleneck for the entire company. The modern distributed transaction pattern is the *Saga Pattern*: a sequence of local transactions where each step updates its local database and publishes an event. If a step fails, the saga executes a series of *Compensating Transactions* that undo the changes made by earlier steps.

== Core Architectural Principles & Mental Models
=== Choreography vs. Orchestration Sagas
- *Choreography (Event-Driven):* Each service listens to events and decides when to act: `OrderService` emits `OrderCreated` -\> `PaymentService` listens and emits `PaymentAuthorized` -\> `InventoryService` listens and emits `StockReserved`. Simple for 2-3 services, but hard to trace and debug as complexity grows.
- *Orchestration (Command-Driven):* A central Saga Orchestrator (e.g., Temporal, AWS Step Functions) explicitly commands each service: 'Charge payment.' If success: 'Reserve inventory.' If failure: 'Refund payment.' Clear, centralized state machine with visual observability.

=== Compensating Transactions: Undo Is Not Rollback
In a database, a rollback wipes the change from existence as if it never happened. In a Saga, you cannot un-ring a bell: the email was already sent, the credit card was already charged. A compensating transaction creates a new compensating action: issuing a refund credit, sending a cancellation email.

== Common Anti-Patterns & Traps to Avoid
- *The Missing Compensation Path:* Designing the happy path of a Saga brilliantly, but having zero automated compensation logic when the third step fails.
- *The Non-Idempotent Compensator:* Retrying a refund compensation without an idempotency key, resulting in the customer receiving two refunds for one failed order.
- *The Circular Choreography Nightmare:* In choreographies with 8 services, circular event dependencies where Service D triggers Service B, which triggers Service D in an infinite loop.

#architect-playbook(
  title: "THE ARCHITECT'S PLAYBOOK: ACTION STEPS THIS WEEK",
  [
    - *Step 1:* Choose Orchestration over Choreography whenever a business workflow exceeds 3 steps or involves financial transactions.
    - *Step 2:* Explicitly write down the Happy Path and the Failure Path for every step in the transaction before writing code.
    - *Step 3:* Use workflow engines like Temporal.io or AWS Step Functions to manage saga retries, timeouts, and state persistence automatically.
  ]
)

== Architectural Takeaways & Cheatsheet
- Never use 2-Phase Commit across microservices; distributed locks are a recipe for cascading gridlock.
- Sagas trade ACID atomicity for business-level eventual consistency and resilience.
- For complex workflows, an explicit Orchestrator beats event choreography every single time.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM DISCUSSION PROMPT",
  [
    *Course Reflection & Hands-on Assignment:* Draw out a multi-step workflow in your product (e.g., checkout, onboarding). What happens if step 3 fails after step 1 and step 2 have succeeded? Is the rollback automated or manual?
  ]
)