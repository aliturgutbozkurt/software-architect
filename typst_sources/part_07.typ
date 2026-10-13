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
  part-num: 7,
  section-title: "Section 2: Blueprints and Boundaries — Deconstructing Complexity",
  title: "Coupling and Cohesion: The Twin Forces That Make or Break Systems",
  subtitle: "Why changing a button color in the frontend shouldn't crash the warehouse packaging line.",
  reading-time: "8 min"
)

#war-story(
  title: "WAR STORY FROM THE TRENCHES",
  [A popular retail app had an incident during a flash sale. The marketing team wanted to change the wording of a promotional banner from 'Free Shipping' to 'Zero Delivery Fee.' A frontend developer updated the string and triggered a deployment. Ten minutes later, the automated robotic cranes in the physical warehouse ground to a halt. Why? The warehouse barcode scanning engine parsed the raw JSON payload of the cart, including the UI banner string, to calculate shipping weight categories! Because the string didn't match the regex `*Shipping*`, the warehouse system threw an unhandled exception. The entire logistics supply chain was brought down by a marketing copy edit.]
)

== The Paradigm Shift: From Coder to Architect Mindset
Coupling is the degree of interdependence between software modules; cohesion is how closely related the functions within a single module are. The holy grail of software architecture has never changed since Larry Constantine coined it in 1974: *High Cohesion, Loose Coupling.* If things that change together don't live together, you have low cohesion. If changing one line in Module A requires you to modify or redeploy Module B, you have tight coupling.

== Core Architectural Principles & Mental Models
=== Types of Coupling (From Innocent to Toxic)
- *Data Coupling (Healthy):* Modules pass only primitive data types needed to do the job.
- *Control Coupling (Suspicious):* Module A passes a boolean flag (`doExtraLogging=true`) that dictates internal execution logic of Module B.
- *Common / Database Coupling (Dangerous):* Multiple modules read and write to the same shared mutable global state or database tables.
- *Content Coupling (Catastrophic):* Module A reaches into Module B's private internals to modify private state.

=== The Law of Demeter (Principle of Least Knowledge)
Never talk to strangers: `order.getCustomer().getAddress().getZipCode().calculateTaxes()` couples the caller to 4 levels of internal object hierarchy. Instead, expose `order.calculateTaxes()` and let the aggregate handle internal navigation.

== Common Anti-Patterns & Traps to Avoid
- *The Shotgun Surgery:* Making one small conceptual change to a feature requires you to touch 18 different files across 5 different services.
- *The Tramp Data Anti-Pattern:* Passing a 50-field `OrderContext` object through 12 layers of functions just because one function at the bottom needs a single user ID.
- *The Utility Junk Drawer:* Creating a `CommonUtils` or `SharedHelpers` class with 40,000 lines of unrelated code imported by every single module in the company.

#architect-playbook(
  title: "THE ARCHITECT'S PLAYBOOK: ACTION STEPS THIS WEEK",
  [
    - *Step 1:* Run a git churn analysis: Find the top 5 files that are touched in almost every single pull request. Those are your toxic coupling hot spots.
    - *Step 2:* Refactor the worst hot spot by introducing an interface or an event-driven boundary.
    - *Step 3:* Kill the `Common` or `Utils` package. Break it up into domain-specific packages that are co-located with their actual owners.
  ]
)

== Architectural Takeaways & Cheatsheet
- Tight coupling is the primary reason why systems slow down over time as team size increases.
- Cohesion is about focus: a class or service should do one business job and do it completely.
- If two modules always need to be deployed together, they are not two services; they are one service split across a network cable.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM DISCUSSION PROMPT",
  [
    *Course Reflection & Hands-on Assignment:* Inspect your codebase's repository history. What is the most frequently edited file in the last 6 months? What makes it attract changes from so many different features?
  ]
)