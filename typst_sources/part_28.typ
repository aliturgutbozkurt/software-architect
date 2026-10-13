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
  part-num: 28,
  section-title: "Section 7: Security and Zero Trust — Defending the Kingdom",
  title: "Supply Chain Security and Threat Modeling",
  subtitle: "Defending against malicious npm packages, hijacked dependencies, and calculating STRIDE risks.",
  reading-time: "9 min"
)

#war-story(
  title: "WAR STORY FROM THE TRENCHES",
  [In 2018, an open-source JavaScript library named `event-stream` with 2 million weekly downloads had its repository ownership transferred by an exhausted, burned-out maintainer to a stranger who offered to help maintain it. The new maintainer quietly added a tiny dependency named `flatmap-stream`. Embedded inside this dependency was encrypted malicious code designed to detect and harvest private keys from the open-source Copay Bitcoin wallet. For months, developers blindly ran `npm install`, pulling the backdoor into dozens of commercial software products. Thousands of applications were running malware in production with zero code changes made by their own engineering teams.]
)

== The Paradigm Shift: From Coder to Architect Mindset
Modern software applications are not built from scratch; they are assembled from thousands of open-source dependencies. When you write 1,000 lines of custom code, you import 500,000 lines of third-party open-source code written by strangers on the internet. Your security perimeter is only as strong as the most vulnerable transitive dependency in your `node_modules` or `pom.xml`. Architectural security requires automated Software Bill of Materials (SBOM) tracking, continuous vulnerability scanning, and proactive *STRIDE Threat Modeling*.

== Core Architectural Principles & Mental Models
=== The STRIDE Threat Modeling Framework (Microsoft Standard)
Before building a system, analyze every component against six threat categories:
- *S - Spoofing:* Can an attacker impersonate another user or service?
- *T - Tampering:* Can data be altered in transit or in the database without detection?
- *R - Repudiation:* Can a user deny performing an action (lack of audit logging)?
- *I - Information Disclosure:* Can sensitive data be leaked or read by unauthorized eyes?
- *D - Denial of Service:* Can a service be overwhelmed by volumetric traffic or algorithmic complexity?
- *E - Elevation of Privilege:* Can an unprivileged user escalate to admin rights?

=== Supply Chain Defenses (SBOM & Lockfiles)
+ *Deterministic Lockfiles:* Always commit `package-lock.json`, `poetry.lock`, or `go.sum` to guarantee identical dependency trees.
+ *Automated Vulnerability Scanning:* Tools like Snyk, Dependabot, and Trivy running in CI pipelines.
+ *Private Artifact Caching:* Mirror approved open-source packages in an internal artifact repository (Artifactory, Nexus) rather than pulling live from public registries.

== Common Anti-Patterns & Traps to Avoid
- *Floating Dependency Versions:* Using `*` or `^` in dependency manifests without lockfiles, allowing an upstream hijacked package to install automatically during a production build.
- *Ignoring Vulnerability Alerts:* Treating Dependabot and security warnings as annoying spam and ignoring high-severity CVEs for months.
- *Blind Trust in Container Bases:* Using untrusted Docker base images (`FROM randomuser/python`) downloaded from public registries without scanning for rootkits.

#architect-playbook(
  title: "THE ARCHITECT'S PLAYBOOK: ACTION STEPS THIS WEEK",
  [
    - *Step 1:* Conduct a 1-hour STRIDE threat modeling session on your next major feature architecture diagram before writing code.
    - *Step 2:* Configure automated dependency vulnerability scanning in your CI/CD pipeline that blocks PRs containing Critical CVEs.
    - *Step 3:* Generate and audit a Software Bill of Materials (SBOM) for your production release artifacts.
  ]
)

== Architectural Takeaways & Cheatsheet
- You are responsible for the security of every line of third-party code you import into your binary.
- STRIDE provides a systematic mental model to uncover vulnerabilities during design rather than after an incident.
- Lock your dependencies, scan your artifacts, and treat every third-party package with healthy skepticism.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM DISCUSSION PROMPT",
  [
    *Course Reflection & Hands-on Assignment:* Run `npm audit` or `pip audit` on your current repository. How many vulnerabilities are reported? How many are classified as High or Critical?
  ]
)