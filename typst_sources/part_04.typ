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
  part-num: 4,
  section-title: "Section 1: The Great Awakening — The First Day as an Architect",
  title: "The Architect's Notebook: Documenting Decisions with ADRs (Before Everyone Forgets)",
  subtitle: "How lightweight Architecture Decision Records prevent corporate amnesia and endless circular debates.",
  reading-time: "8 min"
)

#war-story(
  title: "WAR STORY FROM THE TRENCHES",
  [A healthcare SaaS company was conducting an architectural review of their patient intake portal. A newly hired principal engineer pointed at a bizarre caching layer that intercepted every query and duplicated data in both Redis and Memcached. 'Who wrote this garbage?' he laughed in front of 12 engineers. 'This is completely unmaintainable!' The room went dead quiet. The VP of Engineering leaned forward: 'That was put in place three years ago because our primary vendor experienced a 4-day outage during Hurricane Sandy, and state law mandates 100% intake continuity under penalty of criminal fines. It saved the company from a federal audit.' The engineer turned bright red. Nobody had written down why it was built. Three months later, someone refactored it away—and during the next regional fiber cut, the company violated compliance.]
)

== The Paradigm Shift: From Coder to Architect Mindset
Code tells you *how* something is implemented; it almost never tells you *why*. Six months after code is merged, the original context, business pressures, regulatory deadlines, and rejected alternatives vanish from human memory. Without Architecture Decision Records (ADRs), teams suffer from 'Chesterton's Fence' syndrome: tearing down fences without understanding why they were erected, only to be trampled by the bulls the fence was keeping out.

== Core Architectural Principles & Mental Models
=== The Anatomy of an ADR (Michael Nygard Standard)
A standard ADR is a simple Markdown document kept in the git repository (`/docs/adr/0004-choose-postgres.md`). It contains:
+ *Title & Number:* ADR-0014: Asynchronous Order Processing via SQS
+ *Status:* Proposed / Accepted / Deprecated / Superseded
+ *Context:* What business or technical constraint forced this decision?
+ *Decision:* Exactly what we chose to do.
+ *Consequences:* Positive, negative, and neutral tradeoffs accepted.

=== ADRs as Living History, Not Bureaucracy
An ADR must take no longer than 20 minutes to draft. If it feels like filling out an insurance claim, developers will stop writing them. Keep them in version control right next to the code so they evolve with pull requests.

== Common Anti-Patterns & Traps to Avoid
- *The Secret Conclave:* Making major architectural decisions in private Slack DMs and announcing them as decrees without context.
- *The Wiki Graveyard:* Writing comprehensive architectural blueprints on a dusty Confluence page that nobody ever visits or updates.
- *The Eternal Draft:* Leaving ADRs in 'Proposed' status for eight months while engineers argue over trivialities.

#architect-playbook(
  title: "THE ARCHITECT'S PLAYBOOK: ACTION STEPS THIS WEEK",
  [
    - *Step 1:* Create an `/adr` folder in your primary git repository today with an `0001-record-architecture-decisions.md` template.
    - *Step 2:* Whenever a team debate lasts longer than 30 minutes in a meeting or PR, halt the debate: 'Let's write a 1-page ADR comparing Option A and Option B.'
    - *Step 3:* Make reading the top 10 ADRs mandatory reading for every new developer during their first week of onboarding.
  ]
)

== Architectural Takeaways & Cheatsheet
- If an architectural decision isn't written down, it doesn't exist; it's just tribal folklore.
- Documenting the rejected alternatives in an ADR saves dozens of hours of re-debating the exact same topic next year.
- Never tear down a strange piece of architecture until you find out why it was put there.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM DISCUSSION PROMPT",
  [
    *Course Reflection & Hands-on Assignment:* Draft a 1-page ADR for the last major technical choice your team made (e.g., choosing a library, splitting a database, or picking an auth provider). Include at least two rejected alternatives and the negative consequences accepted.
  ]
)