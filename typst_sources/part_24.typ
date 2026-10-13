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
  part-num: 24,
  section-title: "Section 6: Reliability and Fault Tolerance — Designing for Failure",
  title: "Zero-Downtime Deployments: Blue-Green, Canary, and Feature Flags",
  subtitle: "Shipping code to production 50 times a day without terrifying your customers or your on-call team.",
  reading-time: "9 min"
)

#war-story(
  title: "WAR STORY FROM THE TRENCHES",
  [A SaaS human resources company had a scheduled maintenance window every Saturday at 2:00 AM. Developers dreaded it. One weekend, they deployed Release 4.2, which included a database migration that added a `NOT NULL` column to a table with 80 million rows. The migration locked the table. The web servers threw timeout errors. By 5:00 AM, the migration had stalled at 40%. The team panicked and attempted to roll back the release, but the rollback script failed because intermediate schema changes couldn't be cleanly reverted. The system stayed down until Monday at 11:00 AM. Thousands of enterprise clients couldn't run payroll. The company lost three enterprise contracts worth \$600,000.]
)

== The Paradigm Shift: From Coder to Architect Mindset
The concept of a 'maintenance window' is an obsolete relic of 1990s enterprise IT. Modern software architecture demands zero-downtime continuous deployment. Deploying software (copying bits to servers) must be completely decoupled from releasing software (making features visible to customers). Using *Blue-Green Deployments*, *Canary Releases*, and *Feature Flags*, you can ship code to production continuously while minimizing risk to near zero.

== Core Architectural Principles & Mental Models
=== The Zero-Downtime Deployment Strategies
- *Blue-Green Deployment:* Run two identical production environments (Blue and Green). Blue is live. Deploy new release to Green, run smoke tests. Switch router traffic instantly from Blue to Green. If anything fails, switch back in 2 seconds.
- *Canary Deployment:* Route 2% of real user traffic to the new version. Monitor error rates, latency, and CPU for 15 minutes. Gradually ramp to 10%, 50%, and 100% only if metrics stay healthy.
- *Feature Flags (Toggles):* Decouple deployment from release. Code is deployed into production dark (turned off). Product managers toggle features on for specific users or beta testers via a dashboard without touching server deployments.

=== The Expand and Contract Pattern (Parallel Schema Evolution)
Never rename a database column in a single migration! Follow 3 phases:
+ *Expand:* Add new column `full_name`. Write to both `name` and `full_name`.
+ *Migrate:* Backfill old records in background batches.
+ *Contract:* Point all reads to `full_name`, then drop the old `name` column in the next sprint.

== Common Anti-Patterns & Traps to Avoid
- *The Big Bang Release:* Bundling 45 features and 6 database migrations into a massive release deployed once every two months.
- *The Destructive Database Migration:* Renaming or dropping columns during active traffic, immediately breaking older running application pods.
- *Feature Flag Debt:* Leaving hundreds of dead feature flags in the codebase for years, turning conditional logic into unreadable spaghetti.

#architect-playbook(
  title: "THE ARCHITECT'S PLAYBOOK: ACTION STEPS THIS WEEK",
  [
    - *Step 1:* Implement Canary routing in your API Gateway or Kubernetes Ingress (route 5% of traffic to new pod replicas).
    - *Step 2:* Enforce backward-compatible database migrations using the Expand and Contract pattern.
    - *Step 3:* Adopt feature flags (LaunchDarkly, Unleash, or Flagsmith) for any feature that touches critical customer workflows.
  ]
)

== Architectural Takeaways & Cheatsheet
- Deploying code should be a boring, routine non-event, not a late-night crisis.
- Decouple technical deployment from business feature release using feature flags.
- Always make database schema changes backward-compatible with running application versions.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM DISCUSSION PROMPT",
  [
    *Course Reflection & Hands-on Assignment:* How does your team currently perform database migrations? If a migration fails halfway through, can you roll back without taking down production or losing data?
  ]
)