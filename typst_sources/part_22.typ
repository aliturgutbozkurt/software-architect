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
  part-num: 22,
  section-title: "Section 6: Reliability and Fault Tolerance — Designing for Failure",
  title: "Circuit Breakers, Bulkheads, and Retries with Exponential Backoff",
  subtitle: "How to stop self-inflicted DDoS attacks and isolate failures like a naval battleship.",
  reading-time: "9 min"
)

#war-story(
  title: "WAR STORY FROM THE TRENCHES",
  [A major fintech company experienced a 100ms latency spike on their currency conversion microservice. The upstream payments service had an aggressive retry policy: on timeout, retry immediately up to 5 times. As latency grew, 1,000 incoming user requests turned into 6,000 simultaneous requests hammering the already struggling currency service. The currency service's CPU hit 100% and completely crashed. Now returning immediate 503 errors, the payments service continued retrying 5 times at full speed! Even when the currency service was rebooted, the incoming tidal wave of millions of queued retries crushed it before it could finish initialization. The engineering team had built a self-inflicted Distributed Denial of Service weapon against themselves.]
)

== The Paradigm Shift: From Coder to Architect Mindset
When a downstream dependency is struggling, retrying immediately and synchronously is the equivalent of beating a sick horse to make it run faster—you will kill it. Resilient distributed systems use *Exponential Backoff with Full Jitter* to space out retries, *Circuit Breakers* (Michael Nygard) to cut off requests to failing services, and *Bulkheads* to compartmentalize resources so a flood in one compartment doesn't sink the entire ship.

== Core Architectural Principles & Mental Models
=== The Circuit Breaker State Machine
- *Closed (Normal):* Requests flow through. Failures are counted.
- *Open (Tripped):* When error rate exceeds threshold (e.g., 50% failures over 10 seconds), the circuit trips OPEN. All requests fail FAST immediately without touching the downstream service, giving it room to recover.
- *Half-Open (Testing):* After a cooldown period (e.g., 30s), allow a small trickle of canary requests through. If they succeed, reset to Closed; if they fail, trip back to Open.

=== The Bulkhead Pattern (Ship Hull Isolation)
Just like a naval ship divides its hull into watertight compartments so one torpedo breach doesn't sink the vessel, software bulkheads divide thread pools, memory, and database connections. Never let background reporting share the same thread pool or connection pool as customer checkout.

=== Exponential Backoff with Jitter
Formula: \$\text{sleep} = \min(\text{max\_wait}, \text{base} \times 2^{\text{attempt}}) + \text{random\_jitter}\$. Jitter randomizes retry intervals across clients, breaking synchronization and preventing the thundering herd.

== Common Anti-Patterns & Traps to Avoid
- *The Immediate Naive Retry:* `while (error) { retry(); }` — the classic recipe for taking down any recovering system.
- *The Missing Timeout:* Making a network call without an explicit timeout configuration, meaning a hanging socket holds a thread open indefinitely.
- *The Shared Thread Pool Trap:* Using a single global async thread pool for both critical API processing and heavy PDF generation.

#architect-playbook(
  title: "THE ARCHITECT'S PLAYBOOK: ACTION STEPS THIS WEEK",
  [
    - *Step 1:* Implement Circuit Breakers (using Resilience4j, Polly, or Envoy) on all external third-party API calls.
    - *Step 2:* Update all retry logic to use Exponential Backoff with randomized Jitter.
    - *Step 3:* Partition your thread pools and connection pools into dedicated bulkheads based on critical priority.
  ]
)

== Architectural Takeaways & Cheatsheet
- Fail fast when a service is drowning; don't make your users wait 60 seconds to see a failure.
- Retries without jitter are just a distributed denial of service attack wearing a coat.
- Bulkheads protect your critical revenue flows from being starved by secondary features.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM DISCUSSION PROMPT",
  [
    *Course Reflection & Hands-on Assignment:* Check the HTTP client configurations in your codebase. Are there default timeouts specified on every call, or are they infinite? What is your current retry strategy on network failures?
  ]
)