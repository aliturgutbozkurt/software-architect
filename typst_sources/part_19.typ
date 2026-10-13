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
  part-num: 19,
  section-title: "Section 5: Scalability and Elasticity — Handling the Stampede",
  title: "Content Delivery Networks (CDNs) and Edge Computing",
  subtitle: "How to conquer the speed-of-light latency penalty and serve global users in under 50 milliseconds.",
  reading-time: "8 min"
)

#war-story(
  title: "WAR STORY FROM THE TRENCHES",
  [A SaaS analytics platform had its entire infrastructure hosted in a single AWS data center in Northern Virginia (`us-east-1`). They signed a major enterprise client in Sydney, Australia. The Australian executives immediately complained that the dashboard took 4.2 seconds to load. The engineering team spent three weeks optimizing SQL queries and compressing JSON, shaving off 100 milliseconds. But the page was still crawling. Why? The physical distance from Sydney to Virginia and back is 30,000 kilometers of fiber optic cable. The speed of light in glass introduces a mandatory 180ms round-trip latency. Loading the dashboard required 18 sequential HTTP requests for CSS, fonts, icons, and JavaScript bundles. That meant \$18 	imes 180	ext{ms} = 3.24	ext{ seconds}\$ spent purely traveling through ocean cables! When they put Cloudflare CDN in front, Sydney load time dropped to 380 milliseconds.]
)

== The Paradigm Shift: From Coder to Architect Mindset
You cannot optimize code to beat the speed of light. The only way to deliver fast digital experiences to a global audience is to move assets and computation physically closer to where the user lives. A modern Content Delivery Network (CDN) is not just a cache for JPEG images; it is a globally distributed programmable edge network with 300+ Points of Presence (PoPs) worldwide that can terminate TLS, execute serverless edge workers, and shield your origin servers from 95% of all web traffic.

== Core Architectural Principles & Mental Models
=== The Edge Hierarchy: Origin vs. Edge PoP
- *Edge Point of Presence (PoP):* Located in every major city worldwide (London, Tokyo, Sydney, São Paulo). Users connect to the edge server 5 milliseconds away.
- *Origin Server:* Your central database and compute in AWS/GCP.
- *Edge Caching Mechanics:* Governed by HTTP response headers:
- `Cache-Control: public, max-age=31536000, immutable` (for hashed static assets)
- `Cache-Control: s-maxage=60, stale-while-revalidate=300` (for dynamic API endpoints)

=== Edge Computing (Cloudflare Workers, Fastly Compute, Lambda\@Edge)
Running lightweight V8 JavaScript or WebAssembly directly at the edge PoP. Ideal for:
+ Geolocation redirects and localized currency display
+ A/B testing cookie evaluation
+ Edge authentication and token validation
+ Bot management and DDoS filtering

== Common Anti-Patterns & Traps to Avoid
- *The Unhashed Asset Trap:* Serving static JS/CSS bundles without content hashes in the filename (`app.js` instead of `app.7f8b2c.js`), forcing you to use low TTLs or suffer broken updates.
- *The Origin Pass-Through:* Forgetting to cache static API responses, allowing a sudden Reddit viral post to hit your origin database with 50,000 requests/second.
- *The Edge Heavyweight:* Attempting to run heavy database queries or long-running CPU calculations on edge workers, hitting execution timeouts.

#architect-playbook(
  title: "THE ARCHITECT'S PLAYBOOK: ACTION STEPS THIS WEEK",
  [
    - *Step 1:* Configure your build pipeline to generate content-hashed filenames for all frontend static bundles.
    - *Step 2:* Set `Cache-Control: public, max-age=31536000, immutable` on all hashed static assets.
    - *Step 3:* Use `stale-while-revalidate` on semi-dynamic public API endpoints to allow CDN edges to serve instant cached responses while fetching updates in the background.
  ]
)

== Architectural Takeaways & Cheatsheet
- You cannot refactor your way around the speed of light; move content to the edge.
- A well-configured CDN should absorb 80% to 95% of all incoming requests before they ever touch your origin servers.
- Cache invalidation at the edge is made trivial by content-hashed filenames.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM DISCUSSION PROMPT",
  [
    *Course Reflection & Hands-on Assignment:* Open your browser's Developer Tools network tab on your company's homepage. What is the `Cache-Control` header on your main JavaScript and CSS files? Are they served from a CDN edge or from origin?
  ]
)