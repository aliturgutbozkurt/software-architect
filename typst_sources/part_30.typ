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
  part-num: 30,
  section-title: "Section 8: Observability and Operational Excellence — Seeing in the Dark",
  title: "Service Level Objectives: SLAs, SLOs, and Error Budgets",
  subtitle: "How Google SRE principles turn the eternal war between Product and Engineering into mathematical harmony.",
  reading-time: "9 min"
)

#war-story(
  title: "WAR STORY FROM THE TRENCHES",
  [At an enterprise SaaS company, Product and Engineering were at war. The VP of Product wanted to ship 10 new features this month to close a multimillion-dollar prospect. The VP of Engineering wanted to halt all feature work for an entire quarter to rewrite the database and refactor legacy code because 'the system is too unstable.' Every sprint planning meeting was an emotional shouting match. In the boardroom, the CEO asked: 'Is our uptime good enough?' The VP of Product answered: 'Yes, customers are happy!' The VP of Engineering answered: 'No, we are on the brink of collapse!' Neither executive had objective data, so the company was paralyzed by political gridlock.]
)

== The Paradigm Shift: From Coder to Architect Mindset
Demanding '100% uptime' is an expensive amateur mistake. 100% reliability is impossible, and pursuing it requires infinite budget while driving feature velocity to zero. The Google Site Reliability Engineering (SRE) framework resolves the tension between feature development and reliability through mathematics: *SLIs (Indicators)*, *SLOs (Objectives)*, and the *Error Budget*. An Error Budget turns downtime into a calculated asset to be spent on innovation.

== Core Architectural Principles & Mental Models
=== The SRE Holy Trinity
- *SLI (Service Level Indicator):* A quantifiable metric of performance: `Good Events / Total Events * 100%` (e.g., % of HTTP requests returning 200 with latency \< 300ms).
- *SLO (Service Level Objective):* The internal target agreed upon by Product and Engineering: `99.9% of requests must meet the SLI over a rolling 30-day window`.
- *SLA (Service Level Agreement):* The legal/contractual promise made to customers with financial penalty clauses (usually set looser than the SLO, e.g., 99.5%).

=== The Error Budget Equation
If your SLO is 99.9% uptime over 30 days, your Error Budget is 0.1% (which equals *43.2 minutes of allowable downtime or degraded performance*). If you have budget remaining, Product can deploy risky, innovative features at high speed! If the Error Budget is burned to zero, all feature deployments freeze automatically, and all engineering capacity shifts to stability and tech debt remediation.

== Common Anti-Patterns & Traps to Avoid
- *The Four-Nines Mirage:* Committing to 99.99% uptime in a customer SLA when your cloud infrastructure and dependencies only offer 99.9% uptime.
- *The Vanity SLI:* Measuring server CPU usage as an SLI instead of user-centric success metrics (e.g., failed checkouts or page load delays).
- *The Toothless Error Budget:* Burning 300% of the Error Budget and continuing to ship risky product features anyway because leadership ignores the policy.

#architect-playbook(
  title: "THE ARCHITECT'S PLAYBOOK: ACTION STEPS THIS WEEK",
  [
    - *Step 1:* Define 1-2 user-centric SLIs for your core customer journey (e.g., Checkout Success Rate, Search Latency \< 200ms).
    - *Step 2:* Negotiate an SLO with your Product Manager (e.g., 99.9%) and calculate your monthly Error Budget in minutes.
    - *Step 3:* Establish an explicit Error Budget Policy: If budget is exhausted, freeze non-essential feature releases until reliability is restored.
  ]
)

== Architectural Takeaways & Cheatsheet
- 100% uptime is the wrong target; it halts innovation and burns capital needlessly.
- SLOs transform emotional arguments between Product and Engineering into objective data-driven decisions.
- Error Budgets give engineering a legitimate mandate to fix technical debt without begging for permission.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM DISCUSSION PROMPT",
  [
    *Course Reflection & Hands-on Assignment:* What is the SLO of your primary user-facing service? If you don't have one, what percentage of failed requests in a 30-day period would make your customers legitimately angry?
  ]
)