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
  part-num: 1,
  section-title: "Section 1: The Great Awakening — The First Day as an Architect",
  title: "The Day the Code Stopped Being Enough: What Does an Architect Actually Do?",
  subtitle: "How to survive the existential crisis of having zero Jira tickets assigned to you on Monday morning.",
  reading-time: "8 min"
)

#war-story(
  title: "WAR STORY FROM THE TRENCHES",
  [Marcus was the ultimate 10x senior developer. He could refactor 4,000 lines of spaghetti TypeScript before lunch and benchmark database queries in his sleep. On Friday afternoon, the VP of Engineering patted him on the back: 'Marcus, you're our new Software Architect.' On Monday at 9:00 AM, Marcus sat down, opened his IDE, and checked the sprint board. There were no tickets assigned to him. None. He asked his team lead for work and was told: 'You tell us what to build.' Marcus spent three hours re-indenting an open-source library just to feel useful. By 2:00 PM, he realized the terrifying truth: nobody was going to give him a roadmap. He was now responsible for the roadmap.]
)

== The Paradigm Shift: From Coder to Architect Mindset
As a developer, your primary currency is code: pull requests merged, bugs squashed, functions written. As an architect, your currency is decision quality, system boundaries, and organizational alignment. Ralph Johnson famously defined architecture as 'the decisions that are hard to change later.' If you measure your day by how many lines of code you committed, you will feel permanently unemployed as an architect. Your job is not to build the engine anymore; your job is to make sure we aren't building a rocket engine to power a bicycle.

== Core Architectural Principles & Mental Models
=== The Three Pillars of Software Architecture
+ *Structure & Decomposition:* How a massive, incomprehensible problem is chopped into smaller, comprehensible chunks with clean boundaries.
+ *Characteristics & Quality Attributes (The '-ilities'):* Scalability, availability, maintainability, testability, security. A system can be functionally flawless and architecturally dead if it takes 14 seconds to respond under load.
+ *Tradeoff Governance:* Recognizing that every architectural choice is a package deal containing benefits and hidden maintenance taxes.

=== The Architect's Time Horizon
Developers live in the present sprint (1-2 weeks). Tech leads live in the quarter (3 months). Architects must live in the 1-to-3 year horizon. You must anticipate where traffic, team size, and regulatory requirements will be when the company succeeds, without falling into the trap of speculative over-engineering today.

== Common Anti-Patterns & Traps to Avoid
- *The Ivory Tower Astronaut:* Sitting in an isolated office producing 80-page Visio diagrams that nobody reads and that cannot be implemented in the real codebase.
- *The Shadow Coder:* Becoming secretly resentful of meetings and sneaking in at midnight to rewrite junior engineers' code because 'it was faster than explaining it.'
- *The Shiny Object Tourist:* Adopting every new technology trending on Hacker News, turning production into an unstable zoo of unproven alpha software.

#architect-playbook(
  title: "THE ARCHITECT'S PLAYBOOK: ACTION STEPS THIS WEEK",
  [
    - *Step 1:* Audit your system's current 'Hard-to-Change' decisions: List the database, the core messaging protocol, and the monolithic boundaries.
    - *Step 2:* Schedule 1-on-1 discovery sessions with the three most frustrated engineers on the team. Ask: 'Where does our codebase fight you every day?'
    - *Step 3:* Establish your primary metric: Architectural velocity—how quickly can new developers safely ship business value without triggering an outage?
  ]
)

== Architectural Takeaways & Cheatsheet
- Architecture is not about drawing pretty boxes; it is about choosing which problems you want to suffer from.
- Code is an asset to developers, but a liability to architects. Every line of code written is a line of code that must be maintained, patched, and debugged.
- The best architects write code to understand problems, not to hoard implementation tickets.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM DISCUSSION PROMPT",
  [
    *Course Reflection & Hands-on Assignment:* Think about your current primary application. What is the single architectural decision made 2 years ago that everyone complains about today? What made that decision seem sensible back then?
  ]
)