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
  part-num: 36,
  section-title: "Section 9: The Human Architecture — Leading Without Authority",
  title: "Mentoring Senior Engineers into Emerging Architects",
  subtitle: "How to scale your impact by teaching systems thinking, tradeoff evaluation, and the Staff+ engineering ladder.",
  reading-time: "8 min"
)

#war-story(
  title: "WAR STORY FROM THE TRENCHES",
  [A brilliant Principal Architect was the single point of failure for an entire engineering organization of 150 developers. Every architectural decision, schema change, and technology evaluation had to cross his desk for personal approval. He worked 70 hours a week, attended 35 review meetings, and reviewed 40 design docs weekly. When he took a two-week vacation for his wedding, engineering velocity ground to a dead halt: 12 teams had PRs blocked waiting for his sign-off. When he returned, exhausted, the VP of Engineering pulled him aside: 'You are the most brilliant engineer in this company, but you are also our biggest bottleneck. Your job is not to make every architectural decision; your job is to build an army of engineers who can make architectural decisions without you.']
)

== The Paradigm Shift: From Coder to Architect Mindset
The measure of an architect's greatness is not the brilliance of their individual decisions, but how many engineers around them have learned how to think like architects. If you are the only person who can solve complex problems in your company, you haven't built a resilient architecture—you've built an architectural monarchy. True leadership is about delegating decision-making authority, teaching mental models, and cultivating the Staff+ engineering ladder.

== Core Architectural Principles & Mental Models
=== The Four Archetypes of the Staff+ Engineer (Tanya Reilly)
- *The Tech Lead:* Partners with an engineering manager to lead execution on a critical team or initiative.
- *The Architect:* Responsible for the direction, quality, and coherence of architecture across multiple teams or the entire organization.
- *The Solver:* A deep specialist who parachutes into the organization's hardest, most existential technical problems to fix them.
- *The Right Hand:* Partners with executive leadership (CTO/VP) to evaluate organizational and technological strategy.

=== Teaching Systems Thinking & Tradeoffs
When a senior engineer asks you: 'Should we use Redis or PostgreSQL for this feature?', NEVER answer directly! Instead, ask Socratic questions: 'What are our access patterns? What is our data durability requirement? What happens if this node crashes?' Train them to evaluate the tradeoff matrix themselves.

== Common Anti-Patterns & Traps to Avoid
- *The Hero Gatekeeper:* Insisting on personally reviewing and approving every technical design document in the company.
- *The Knowledge Hoarder:* Keeping architectural context in your head as a form of job security rather than writing documentation and coaching others.
- *The Punitive Reviewer:* Leaving harsh, sarcastic comments on design docs instead of using reviews as educational coaching moments.

#architect-playbook(
  title: "THE ARCHITECT'S PLAYBOOK: ACTION STEPS THIS WEEK",
  [
    - *Step 1:* Establish an Architecture Review Working Group: Rotate senior engineers through the committee so they learn how to evaluate cross-cutting designs.
    - *Step 2:* When mentoring, use the Socratic method: Guide engineers to uncover tradeoffs rather than handing down answers.
    - *Step 3:* Sponsor a rising senior engineer: Have them co-author your next major architectural blueprint and lead the executive presentation.
  ]
)

== Architectural Takeaways & Cheatsheet
- Your ultimate legacy as an architect is the decision-making caliber of the people you leave behind.
- Stop giving answers; start asking the right questions that illuminate hidden tradeoffs.
- If your architecture falls apart when you take a vacation, you haven't built a system; you've built a dependency on yourself.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM DISCUSSION PROMPT",
  [
    *Course Reflection & Hands-on Assignment:* Who is the most promising senior engineer on your team today? What is one architectural responsibility or design document you can delegate to them this month with your coaching?
  ]
)