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
  part-num: 20,
  section-title: "Section 5: Scalability and Elasticity — Handling the Stampede",
  title: "Rate Limiting and Traffic Shaping: Protecting Your Castle",
  subtitle: "Algorithms and architectures to survive scrapers, runaway loops, and malicious volumetric assaults.",
  reading-time: "9 min"
)

#war-story(
  title: "WAR STORY FROM THE TRENCHES",
  [A weather forecasting API had a generous free tier. On a sunny Tuesday morning, a developer at a third-party smart sprinkler company wrote a Python script to check soil weather. Unfortunately, he placed the API call inside an infinite `while True:` loop without a sleep interval. His script ran on 500 home sprinkler controllers, bombarding the weather startup with 45,000 requests per second. The weather API had no rate limiting. Within 60 seconds, the database connection pool was exhausted, legitimate mobile users were receiving 504 Gateway Timeouts, and the company's AWS cloud bill incurred \$4,500 in egress fees in two hours. The entire business was held hostage by one junior developer's bug.]
)

== The Paradigm Shift: From Coder to Architect Mindset
In a distributed world, unmetered access is an existential liability. Even friendly consumers will accidentally DDoS you with buggy retry loops, infinite polling scripts, and automated scrapers. Rate limiting is not just a monetization tool for enterprise API tiers; it is the fundamental immune system of your architecture. An architect designs traffic shaping to enforce boundaries and protect core resources under all conditions.

== Core Architectural Principles & Mental Models
=== The Classic Rate Limiting Algorithms
- *Token Bucket:* Tokens are added to a bucket at a constant rate up to a max capacity. Each request consumes a token. Allows bursts up to bucket capacity while enforcing average rate. (Industry standard for APIs).
- *Leaky Bucket:* Requests enter a queue and are processed at a steady, fixed rate. Smooths out spiky traffic into a constant stream. Ideal for traffic shaping.
- *Sliding Window Log:* Stores timestamps of every request in a sorted set (Redis ZSET). 100% accurate, but memory-intensive for high volume.
- *Sliding Window Counter:* Approximates requests in the current window using a weighted sum of previous and current intervals. Low memory footprint, 99.9% accuracy.

=== Rate Limiting Architecture at Scale
Never implement distributed rate limiting by querying your primary relational database! Use an in-memory Redis cluster with atomic Lua scripts or edge gateways (Cloudflare/Kong) that evaluate limits in sub-millisecond time.

== Common Anti-Patterns & Traps to Avoid
- *The IP-Only Rate Limit:* Limiting purely by client IP address, which accidentally blocks an entire university or corporate office containing 5,000 legitimate users behind a single NAT gateway.
- *The Missing Retry-After Header:* Returning a raw HTTP `429 Too Many Requests` without an informative `Retry-After: 30` header, causing desperate clients to hammer you even harder.
- *The Database-Driven Rate Limiter:* Writing an `INSERT INTO api_logs` for every single request, meaning an incoming DDoS attack crashes the database before the rate limiter can even block it.

#architect-playbook(
  title: "THE ARCHITECT'S PLAYBOOK: ACTION STEPS THIS WEEK",
  [
    - *Step 1:* Implement multi-tiered rate limiting: tier by IP address for anonymous visitors, tier by API key/User ID for authenticated clients.
    - *Step 2:* Use the standard RFC 6585 headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`, and `Retry-After` on 429 responses.
    - *Step 3:* Deploy rate limiting at the perimeter (Reverse Proxy / CDN / Gateway) so blocked requests never consume application or database resources.
  ]
)

== Architectural Takeaways & Cheatsheet
- If your API does not have rate limiting, your production stability is at the mercy of your most careless client.
- Token Bucket is the gold standard algorithm for flexible, burst-tolerant API rate limiting.
- Block malicious traffic at the outer perimeter; never let rogue requests reach your internal databases.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM DISCUSSION PROMPT",
  [
    *Course Reflection & Hands-on Assignment:* What happens if a client hits your API 10,000 times in 10 seconds right now? Does your system throttle them, or does it try to execute all 10,000 queries?
  ]
)