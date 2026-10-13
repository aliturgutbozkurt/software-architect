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
  part-num: 29,
  section-title: "Section 8: Observability and Operational Excellence — Seeing in the Dark",
  title: "The Observability Triad: Metrics, Logs, and Distributed Tracing",
  subtitle: "How OpenTelemetry context propagation lets you pinpoint the exact 200ms slowdown across 15 microservices.",
  reading-time: "9 min"
)

#war-story(
  title: "WAR STORY FROM THE TRENCHES",
  [An online broker had a microservices ecosystem with 40 distinct services. During morning market open, users complained that submitting trade orders took 8 seconds instead of 150 milliseconds. The operations team stared at 40 different terminal windows scrolling unstructured text logs at 50,000 lines per second. Every service logged: `Error: Connection timeout` or `Waiting for downstream response`. But WHICH service was the culprit? The engineers spent four hours arguing: the order team blamed the account team, the account team blamed the risk team, and the risk team blamed the database team. When an architect finally implemented OpenTelemetry distributed tracing with a unified `trace_id`, they discovered the real cause within 30 seconds: a forgotten junior engineer's geo-IP lookup service was attempting to reverse-DNS look up the broker's IP address on every single trade!]
)

== The Paradigm Shift: From Coder to Architect Mindset
Monitoring tells you when a system is broken ('CPU is at 95%'); Observability allows you to infer the internal state of a system based on its external outputs and ask arbitrary questions you never anticipated. In a monolithic system, you could read a single stack trace. In a distributed architecture, you cannot debug with `grep`. You need the *Observability Triad*: Metrics to tell you there is a fire, Logs to tell you what the fire smells like, and Distributed Tracing to show you the exact match that lit the fire.

== Core Architectural Principles & Mental Models
=== The Observability Triad Defined
- *Metrics (Prometheus, Datadog):* Aggregatable numeric data over time (counters, gauges, histograms). Extremely cheap to store, fast to alert on, but lacks individual request context.
- *Structured Logs (JSON via FluentBit / Elasticsearch):* Rich textual event descriptions. Must include timestamps, log level, and contextual metadata (`user_id`, `tenant_id`).
- *Distributed Traces (OpenTelemetry, Jaeger):* Follows a single request across network boundaries. Every request receives a globally unique `trace_id` and each hop receives a `span_id`. Spans record parent-child relationships and start/end timestamps, generating a visual waterfall diagram of latency.

=== The Cardinality Trap in Metrics
Never add high-cardinality fields (like `user_id` or `email`) as labels or tags in Prometheus metrics! A label with 1 million distinct values will blow up your metric database's memory and cost \$30,000/month in SaaS ingestion fees. High-cardinality belongs in logs and traces, never in metric dimensions.

== Common Anti-Patterns & Traps to Avoid
- *Unstructured String Logging:* Writing `console.log('User logged in: ' + user.id)` instead of structured JSON `{"event": "user_login", "user_id": 42}`, making log queries impossible without slow regexes.
- *The Missing Trace Context:* Calling a downstream microservice via HTTP without forwarding the `traceparent` W3C header, breaking the distributed trace into disconnected fragments.
- *Alert Fatigue (Crying Wolf):* Configuring 300 PagerDuty alerts for trivial warning logs, training engineers to mute notifications until a critical production disaster is completely missed.

#architect-playbook(
  title: "THE ARCHITECT'S PLAYBOOK: ACTION STEPS THIS WEEK",
  [
    - *Step 1:* Adopt OpenTelemetry (OTel) SDKs as the vendor-neutral standard for metrics and distributed tracing across all services.
    - *Step 2:* Ensure your API Gateway generates a `trace_id` on every inbound request and injects it into response headers (`X-Trace-Id`).
    - *Step 3:* Convert all application logs to structured JSON format and automatically attach the current `trace_id` to every log line.
  ]
)

== Architectural Takeaways & Cheatsheet
- Without distributed tracing, debugging microservices is like searching for a needle in 40 different haystacks.
- Metrics show what is happening; traces show where it is happening; logs explain why it happened.
- Keep metrics dimensions low-cardinality; put high-cardinality metadata into traces and logs.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM DISCUSSION PROMPT",
  [
    *Course Reflection & Hands-on Assignment:* Can you take a single user request in your production environment and view the complete end-to-end trace of every network hop and database query it made? If not, what is missing?
  ]
)