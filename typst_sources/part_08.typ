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
  part-num: 8,
  section-title: "Section 2: Blueprints and Boundaries — Deconstructing Complexity",
  title: "API Design as a Sacred Contract: REST, gRPC, and GraphQL Demystified",
  subtitle: "How to design interfaces that client applications can rely on without breaking on Friday afternoon.",
  reading-time: "9 min"
)

#war-story(
  title: "WAR STORY FROM THE TRENCHES",
  [A mobile banking app had 2 million active iOS and Android users. On Friday evening, a backend developer refactored the `/api/v1/accounts` endpoint, renaming the JSON response field `account_number` to `accountNumber` to match clean camelCase naming standards. The web frontend team updated their code and deployed seamlessly. But 1.4 million mobile app users who hadn't updated their iOS app through the Apple App Store woke up on Saturday morning to find their account balances showing \$0.00. The company's phone lines melted with panic. Because mobile apps cannot be forced to update instantly, the change required an emergency backend hotfix and a public apology from the CEO.]
)

== The Paradigm Shift: From Coder to Architect Mindset
An internal function signature belongs to you; a public API belongs to your consumers. Once an API is published to external clients, mobile apps, or third-party partners, it is an immutable, legally binding contract. You do not own the upgrade schedule of your users' phones. An architect designs APIs for evolution, strict backward compatibility, and defensive degradation.

== Core Architectural Principles & Mental Models
=== The Protocol Trifecta: Choosing the Right Transport
- *REST (JSON over HTTP/1.1 or HTTP/2):* Universal, easily debugged in curl/browser, perfect for public developer ecosystems and standard CRUD workflows.
- *gRPC (Protobuf over HTTP/2):* High performance, binary serialization, strict schema contracts, bi-directional streaming. The undisputed king of internal microservice-to-service communication.
- *GraphQL:* Client-specified data fetching, solves mobile over-fetching and under-fetching. Ideal for complex frontend dashboards aggregating data from multiple backend services.

=== The Golden Rules of API Evolution
+ *Additive Changes Only:* You may add new fields, but you may never delete or rename existing fields without a formal deprecation lifecycle.
+ *Tolerant Reader Pattern:* Consumers should ignore unknown fields in JSON/Protobuf responses.
+ *Idempotency Keys:* Every mutation API (`POST /charges`) must accept an `Idempotency-Key` header to safely allow network retries without duplicate charges.

== Common Anti-Patterns & Traps to Avoid
- *The Leaky Database API:* Directly exposing database table columns through your JSON API (`SELECT * FROM users` serialized to JSON), exposing internal database schemas and password hashes to the internet.
- *The GraphQL Wild West:* Exposing an open GraphQL endpoint to the public internet without query depth limits or cost analysis, allowing attackers to crash your servers with nested queries.
- *The Silent Breaking Change:* Changing the semantic behavior or data format of an API field (e.g., changing timestamp from ISO 8601 to epoch milliseconds) without changing the version.

#architect-playbook(
  title: "THE ARCHITECT'S PLAYBOOK: ACTION STEPS THIS WEEK",
  [
    - *Step 1:* Adopt OpenAPI / Swagger or Protobuf specs as the single source of truth before writing server code (API-First Design).
    - *Step 2:* Implement automated contract testing (e.g., Pact) in CI/CD to prevent breaking changes from ever reaching production.
    - *Step 3:* Mandate `Idempotency-Key` headers on all critical financial and state-altering API endpoints.
  ]
)

== Architectural Takeaways & Cheatsheet
- APIs are forever: once someone builds a mobile app on your endpoint, you will maintain that schema for years.
- Use gRPC for fast internal plumbing; use REST or GraphQL for external clients and user interfaces.
- Never let an internal database refactoring dictate a breaking change in an external API response.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM DISCUSSION PROMPT",
  [
    *Course Reflection & Hands-on Assignment:* Pick an API endpoint in your current company. How does it handle versioning? If a mobile client was built against it 3 years ago and never updated, would it still work today?
  ]
)