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
  part-num: 6,
  section-title: "Section 2: Blueprints and Boundaries — Deconstructing Complexity",
  title: "Domain-Driven Design Without the Academic Headache: Bounded Contexts Made Human",
  subtitle: "How to carve your architecture around business realities instead of database schemas.",
  reading-time: "9 min"
)

#war-story(
  title: "WAR STORY FROM THE TRENCHES",
  [A telecommunications company built an enterprise system centered around a giant database table named `tbl_User`. The Sales department defined a user as an anonymous lead with an email and marketing score. The Billing department defined a user as a legal entity with a VAT number and bank account. The Network Security team defined a user as an active SIM card and IMEI number. Whenever Sales wanted to make the email optional for kiosk leads, Billing's invoicing batch jobs crashed with NullPointerExceptions. Engineers spent nine months in committee meetings trying to construct the 'Universal Omnipresent User Object.' It had 142 database columns and satisfied nobody. The project was canceled after burning \$4M.]
)

== The Paradigm Shift: From Coder to Architect Mindset
There is no such thing as a single universal model of reality in a complex business. The core insight of Eric Evans' Domain-Driven Design (DDD) is that words only have precise meaning within a specific *Bounded Context*. To Billing, a customer is an invoice recipient; to Shipping, a customer is a delivery address; to Support, a customer is a ticket history. An architect's job is not to unify these concepts into one Frankenstein model, but to draw explicit boundaries and translate between them.

== Core Architectural Principles & Mental Models
=== The Core DDD Toolkit for Real Engineers
- *Ubiquitous Language:* The shared vocabulary agreed upon by domain experts and engineers. If the business calls it a 'Policy Cancellation,' never name the database column `is_deleted`.
- *Bounded Context:* The explicit boundary within which a domain model applies. Inside Context A, 'Product' means inventory stock; inside Context B, 'Product' means marketing copy.
- *Aggregate Root:* The gatekeeper entity that guarantees data integrity (e.g., an `Order` aggregate manages its `OrderLines`; external code cannot mutate an `OrderLine` directly).

=== Context Mapping & Anti-Corruption Layers (ACL)
When two bounded contexts communicate, never allow the messy internal data structures of one to bleed into the other. Put an Anti-Corruption Layer (a translator/adapter) between them so changes in one system don't infect the rest of your architecture.

== Common Anti-Patterns & Traps to Avoid
- *The God Object:* A single massive class (`User`, `Account`, `Order`) that touches 80% of the entire codebase and has 200 methods.
- *The Anemic Domain Model:* Classes that contain only getters and setters (dumb data bags), while business rules are scattered randomly across 50 controller services.
- *The Academic DDD Dogma:* Spending three months building value objects and repositories for a simple lookup table that just needed a basic SQL query.

#architect-playbook(
  title: "THE ARCHITECT'S PLAYBOOK: ACTION STEPS THIS WEEK",
  [
    - *Step 1:* Conduct an Event Storming workshop: Gather engineers and business stakeholders in front of a digital whiteboard to map business events in chronological order.
    - *Step 2:* Circle natural clusters of business events to discover your natural Bounded Contexts.
    - *Step 3:* Introduce an Anti-Corruption Layer immediately whenever integrating with legacy or third-party enterprise vendor APIs.
  ]
)

== Architectural Takeaways & Cheatsheet
- Models are not copies of the real world; they are tools designed to solve a specific problem within a specific boundary.
- Don't let the marketing team's definition of an entity break the accounting team's ledger.
- Speak the language of the business in your code, or spend your career translating tickets into English.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM DISCUSSION PROMPT",
  [
    *Course Reflection & Hands-on Assignment:* Find a class in your application that has more than 20 properties. Can you split it into two distinct models belonging to two different bounded contexts?
  ]
)