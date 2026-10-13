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
  part-num: 27,
  section-title: "Section 7: Security and Zero Trust — Defending the Kingdom",
  title: "Secrets Management, Encryption, and Data Privacy",
  subtitle: "How to handle API keys, database credentials, and customer PII without ending up in the news.",
  reading-time: "9 min"
)

#war-story(
  title: "WAR STORY FROM THE TRENCHES",
  [A fast-moving startup engineer was debugging an urgent database timeout at 2:30 AM. To speed up testing, he pasted the production database password and AWS master access keys directly into `config.js`. He fixed the bug, committed the change, and pushed it to GitHub. Unfortunately, the company's repository was open-source. Within 8 minutes, automated malicious botnets crawling GitHub commits picked up the AWS credentials. By 3:15 AM, the attackers had spun up 400 GPU instances across 12 AWS regions mining Monero cryptocurrency. When the CTO woke up at 7:00 AM, the company had accumulated a \$42,000 AWS bill and all customer database records had been cloned to an external server in Eastern Europe.]
)

== The Paradigm Shift: From Coder to Architect Mindset
Hardcoding secrets in source code, committing them to git, or storing them in unencrypted configuration files is the digital equivalent of taping your house key to your front door. Git commit histories are permanent. An architect designs systems where secrets are dynamically injected at runtime from a secure vault, rotated automatically, and where customer data is protected with Envelope Encryption both at rest and in transit.

== Core Architectural Principles & Mental Models
=== The Hierarchy of Secrets Management
- *Level 0 (Suicide):* Hardcoded in source code or `.env` files committed to git.
- *Level 1 (Basic):* Injected via CI/CD environment variables at deployment time.
- *Level 2 (Modern Standard):* Dedicated Secret Stores (HashiCorp Vault, AWS Secrets Manager, Doppler). Secrets are fetched dynamically at runtime via IAM authentication.
- *Level 3 (Zero Trust):* Dynamic Ephemeral Credentials. Vault generates temporary database credentials valid for only 60 minutes and revokes them automatically.

=== Envelope Encryption & KMS
Encrypting a 5-gigabyte database backup with a master key across the network is slow. Envelope Encryption uses a two-tier key model:
+ A local *Data Encryption Key (DEK)* encrypts the data directly.
+ The *Key Management Service (KMS)* encrypts only the DEK using a master Key Encryption Key (KEK).
+ Only the encrypted DEK is stored alongside the encrypted data.

== Common Anti-Patterns & Traps to Avoid
- *The Secret in the Docker Image:* Baking database passwords or API keys into Dockerfile layers (`ENV DB_PASS=secret123`), making secrets accessible to anyone who can pull the Docker image.
- *Logging Sensitive PII:* Printing user passwords, credit card numbers, or social security numbers into application logs (`logger.info('Processing order: ' + user)`), exposing PII to Datadog or Splunk.
- *The Unrotated Master Key:* Using the exact same database password or API token for six consecutive years across 20 different former employees.

#architect-playbook(
  title: "THE ARCHITECT'S PLAYBOOK: ACTION STEPS THIS WEEK",
  [
    - *Step 1:* Run git-secrets or Trufflehog across your entire repository history to detect leaked credentials.
    - *Step 2:* Migrate all static config secrets into a centralized secret manager (AWS Secrets Manager or Vault).
    - *Step 3:* Implement automated log scrubbing to sanitize credit cards, passwords, and tokens before logs leave the application boundary.
  ]
)

== Architectural Takeaways & Cheatsheet
- Source control is for code, never for secrets. A committed secret must always be considered compromised.
- Automated secret rotation is the ultimate defense against credential leakage.
- Mask PII at the logging boundary; your observability platform should never contain unencrypted customer personal data.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM DISCUSSION PROMPT",
  [
    *Course Reflection & Hands-on Assignment:* Run a search in your codebase for words like `password`, `secret`, or `apiKey`. Are any values hardcoded? What is your procedure for rotating your production database password?
  ]
)