# Think Like a Software Architect (40-Part Complete Masterclass)

This workspace contains the complete production-grade source code, formatted chapters, and compiled publications for **"Think Like a Software Architect"**.

Designed as a zero-to-expert blueprint for software engineers making the leap to architectural leadership, this curriculum progresses from your very first day on the job (surviving without tickets, escaping resume-driven development, mastering tradeoffs) up to advanced enterprise systems, zero-trust security, FinOps, distributed consensus, and Generative AI architecture.

Written in an engaging, humorous, and battle-tested style full of realistic war stories from the trenches, it is fully optimized for **Google NotebookLM** audio podcast generation and **Udemy** video course publishing.

---

## 📚 Deliverables & Quick Access

| Deliverable | Location / Clickable Link | Description |
| :--- | :--- | :--- |
| **Master Complete Book PDF (107 Pages)** | [output/Think_Like_a_Software_Architect_Complete_Guide.pdf](file:///Users/aliturgutbozkurt/Desktop/Software%20Architect/output/Think_Like_a_Software_Architect_Complete_Guide.pdf) | Complete 107-page master textbook with luxury obsidian cover, full table of contents, 10 section splash pages, all 40 chapters, and the Architect's Survival Cheatsheet Appendix. |
| **Master Complete Markdown Book** | [output/Think_Like_a_Software_Architect_Complete_Guide.md](file:///Users/aliturgutbozkurt/Desktop/Software%20Architect/output/Think_Like_a_Software_Architect_Complete_Guide.md) | Full unified Markdown source text for full-book ingestion into NotebookLM or e-book publishing (179 KB). |
| **40 Standalone Chapter PDFs** | [output/individual_pdfs/](file:///Users/aliturgutbozkurt/Desktop/Software%20Architect/output/individual_pdfs/) | 40 individually styled, numbered PDFs ready to attach as downloadable lecture materials on Udemy. |
| **40 Standalone Markdown Chapters** | [chapters/](file:///Users/aliturgutbozkurt/Desktop/Software%20Architect/chapters/) | 40 modular markdown chapters optimized for batch-uploading into Google NotebookLM for audio podcast generation. |
| **Udemy & NotebookLM Master Guide** | [course_guide/UDEMY_AND_NOTEBOOKLM_GUIDE.md](file:///Users/aliturgutbozkurt/Desktop/Software%20Architect/course_guide/UDEMY_AND_NOTEBOOKLM_GUIDE.md) | Detailed dual-host podcast prompts, 5-slide lecture outlines, quiz generation templates, and Udemy marketing recommendations. |

---

## 📑 Curriculum Architecture: 10 Sections & 40 Modules

### Section 1: The Great Awakening — The First Day as an Architect
- **Part 01:** The Day the Code Stopped Being Enough: What Does an Architect Actually Do?
- **Part 02:** Escaping Resume-Driven Development: Boredom vs. Business Reality
- **Part 03:** The Art of the Tradeoff: There Are No Solutions, Only Compromises
- **Part 04:** The Architect's Notebook: Documenting Decisions with ADRs (Before Everyone Forgets)

### Section 2: Blueprints and Boundaries — Deconstructing Complexity
- **Part 05:** The Monolith Strikes Back: When to Stay Unified and When to Split
- **Part 06:** Domain-Driven Design Without the Academic Headache: Bounded Contexts Made Human
- **Part 07:** Coupling and Cohesion: The Twin Forces That Make or Break Systems
- **Part 08:** API Design as a Sacred Contract: REST, gRPC, and GraphQL Demystified

### Section 3: Data Architecture — Where State Lives, Dies, and Lies
- **Part 09:** Polyglot Persistence: Choosing the Right Weapon for Your Data
- **Part 10:** The Database Bottleneck: Indexing, Sharding, and Read Replicas
- **Part 11:** The ACID vs. BASE Showdown: Consistency Models in the Real World
- **Part 12:** Caching Strategies: The Two Hard Things in Computer Science

### Section 4: Asynchronous Horizons — Event-Driven Architecture
- **Part 13:** Synchronous Hell to Asynchronous Bliss: Queues, Topics, and Streams
- **Part 14:** Kafka Without the Tears: Partitions, Offsets, and Consumer Groups
- **Part 15:** Eventual Consistency in Action: The Saga Pattern vs. Two-Phase Commit
- **Part 16:** Event Sourcing and CQRS: When the History Matters More Than the Present

### Section 5: Scalability and Elasticity — Handling the Stampede
- **Part 17:** Horizontal Scaling: Statelessness and the Twelve-Factor App
- **Part 18:** Load Balancing, Gateways, and Reverse Proxies
- **Part 19:** Content Delivery Networks (CDNs) and Edge Computing
- **Part 20:** Rate Limiting and Traffic Shaping: Protecting Your Castle

### Section 6: Reliability and Fault Tolerance — Designing for Failure
- **Part 21:** Everything Fails, All the Time: The Resilient Architect's Mindset
- **Part 22:** Circuit Breakers, Bulkheads, and Retries with Exponential Backoff
- **Part 23:** Chaos Engineering: Breaking Production on Purpose (Before It Breaks You)
- **Part 24:** Zero-Downtime Deployments: Blue-Green, Canary, and Feature Flags

### Section 7: Security and Zero Trust — Defending the Kingdom
- **Part 25:** The Zero Trust Architecture: Never Trust, Always Verify
- **Part 26:** Authentication & Authorization at Scale: OAuth2, OIDC, and RBAC vs. ABAC
- **Part 27:** Secrets Management, Encryption, and Data Privacy
- **Part 28:** Supply Chain Security and Threat Modeling

### Section 8: Observability and Operational Excellence — Seeing in the Dark
- **Part 29:** The Observability Triad: Metrics, Logs, and Distributed Tracing
- **Part 30:** Service Level Objectives: SLAs, SLOs, and Error Budgets
- **Part 31:** FinOps and Cloud Economics: Architecture That Doesn't Bankrupt the Company
- **Part 32:** Incident Management and Blameless Post-Mortems

### Section 9: The Human Architecture — Leading Without Authority
- **Part 33:** Conway's Law and Team Topologies: Structuring Teams to Mirror Architecture
- **Part 34:** Managing Technical Debt: When to Pay, When to Refactor, When to Rebuild
- **Part 35:** The Art of Influence: Selling Architectural Vision to Non-Engineers
- **Part 36:** Mentoring Senior Engineers into Emerging Architects

### Section 10: Modern Frontiers — AI-Era Architecture & Enterprise Mastery
- **Part 37:** Architecting for Generative AI: RAG, Vector Databases, and Agents
- **Part 38:** Distributed Consensus and Planetary Scale
- **Part 39:** The Legacy Modernization Playbook: Strangling the Dinosaur
- **Part 40:** The Architect's North Star: Wisdom, Humility, and the Timeless Craft

---

## 🛠️ Recompilation Commands

Whenever you edit chapter contents or templates, re-run the master build script from the project root:

```bash
python3 scripts/build_all.py
```

This single command will automatically:
1. Regenerate all 40 modular Markdown chapters in `chapters/`.
2. Generate Typst source files in `typst_sources/`.
3. Compile all 40 individual chapter PDFs into `output/individual_pdfs/`.
4. Compile the unified 107-page master book PDF into `output/Think_Like_a_Software_Architect_Complete_Guide.pdf`.
5. Update the master Markdown book in `output/` and the course production guide in `course_guide/`.
