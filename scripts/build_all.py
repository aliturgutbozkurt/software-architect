#!/usr/bin/env python3
"""
Think Like a Software Architect - Master Build & Compilation Engine
Generates:
1. 40 Individual Markdown Chapters (chapters/)
2. 40 Individual Typst Sources (typst_sources/) & 40 Standalone PDFs (output/individual_pdfs/)
3. Master Unified Complete Book Markdown (output/Think_Like_a_Software_Architect_Complete_Guide.md)
4. Master Unified Typst Master Source & PDF (output/Think_Like_a_Software_Architect_Complete_Guide.pdf)
5. Comprehensive Udemy & NotebookLM Production Guide (course_guide/UDEMY_AND_NOTEBOOKLM_GUIDE.md)
"""

import os
import re
import subprocess
import sys

# Ensure local scripts folder is in sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from content_data.section_01 import SECTION_1
from content_data.section_02 import SECTION_2
from content_data.section_03 import SECTION_3
from content_data.section_04 import SECTION_4
from content_data.section_05 import SECTION_5
from content_data.section_06 import SECTION_6
from content_data.section_07 import SECTION_7
from content_data.section_08 import SECTION_8
from content_data.section_09 import SECTION_9
from content_data.section_10 import SECTION_10

SECTIONS = [
    SECTION_1, SECTION_2, SECTION_3, SECTION_4, SECTION_5,
    SECTION_6, SECTION_7, SECTION_8, SECTION_9, SECTION_10
]

BASE_DIR = os.path.dirname(SCRIPT_DIR)
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")
TYPST_DIR = os.path.join(BASE_DIR, "typst_sources")
OUTPUT_PDFS_DIR = os.path.join(BASE_DIR, "output", "individual_pdfs")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
COURSE_GUIDE_DIR = os.path.join(BASE_DIR, "course_guide")

os.makedirs(CHAPTERS_DIR, exist_ok=True)
os.makedirs(TYPST_DIR, exist_ok=True)
os.makedirs(OUTPUT_PDFS_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(COURSE_GUIDE_DIR, exist_ok=True)


def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '_', text)
    return text.strip('_')


def clean_title_for_filename(text):
    parts = text.split(':')
    main_title = parts[0].strip()
    return re.sub(r'[^a-zA-Z0-9]+', '_', main_title).strip('_')


def typst_escape_text(text):
    if not text:
        return ""
    # Escape dollar sign for Typst (math mode)
    text = text.replace("$", "\\$")
    # Escape at symbol (citations / labels)
    text = text.replace("@", "\\@")
    # Escape angle brackets to prevent Typst label syntax error (<label>)
    text = text.replace("<", "\\<")
    text = text.replace(">", "\\>")
    # Convert markdown bold **text** to Typst *text*
    text = re.sub(r'\*\*(.+?)\*\*', r'*\1*', text)
    return text


def typst_format_block(text):
    """Formats multi-line text blocks with bullets or numbers for Typst."""
    if not text:
        return ""
    text = typst_escape_text(text)
    lines = text.split('\n')
    formatted = []
    for line in lines:
        line_s = line.strip()
        if line_s.startswith('- '):
            formatted.append('- ' + line_s[2:])
        elif re.match(r'^\d+\.\s+', line_s):
            m = re.match(r'^\d+\.\s+(.*)', line_s)
            formatted.append('+ ' + m.group(1))
        else:
            formatted.append(line)
    return '\n'.join(formatted)


def generate_markdown_chapter(sec, part):
    lines = []
    lines.append(f"# Part {part['part_num']:02d}: {part['title']}")
    lines.append(f"**Section {sec['section_num']}: {sec['section_title']}**  ")
    lines.append(f"*Estimated Duration / Audio Overview: {part.get('duration', '8 min')}*  ")
    lines.append(f"*{part['subtitle']}*\n")
    lines.append("---\n")

    lines.append("## 🎙️ The Architect's Hook & War Story from the Trenches\n")
    lines.append(f"> {part['war_story']}\n")

    lines.append("## 🧠 The Paradigm Shift: From Coder to Architect Mindset\n")
    lines.append(f"{part['paradigm_shift']}\n")

    lines.append("## 📐 Core Architectural Principles & Mental Models\n")
    for concept in part['core_concepts']:
        lines.append(f"### {concept['heading']}")
        lines.append(f"{concept['text']}\n")

    lines.append("## ⚠️ Common Anti-Patterns & Traps to Avoid\n")
    for ap in part['anti_patterns']:
        lines.append(f"- {ap}")
    lines.append("")

    lines.append("## 🎯 The Architect's Playbook: Action Steps This Week\n")
    for step in part['playbook']:
        lines.append(f"- {step}")
    lines.append("")

    lines.append("## 📌 Architectural Takeaways & Cheatsheet\n")
    for takeaway in part['takeaways']:
        lines.append(f"- {takeaway}")
    lines.append("")

    lines.append("## 💡 Udemy Course & NotebookLM Discussion Prompt\n")
    lines.append(f"**Assignment / Reflection Prompt:** {part['udemy_prompt']}\n")

    return "\n".join(lines)


def generate_typst_single_chapter(sec, part):
    sec_num = sec['section_num']
    part_num = part['part_num']
    title_escaped = typst_escape_text(part['title'])
    subtitle_escaped = typst_escape_text(part['subtitle'])
    sec_title_escaped = typst_escape_text(sec['section_title'])
    duration = part.get('duration', '8 min')

    out = []
    out.append('#import "/templates/book_style.typ": *')
    out.append("")
    out.append('#set page(')
    out.append('  paper: "a4",')
    out.append('  margin: (top: 2.2cm, bottom: 2.2cm, left: 2.2cm, right: 2.2cm),')
    out.append('  header: align(right)[#text(size: 8pt, fill: rgb("#94a3b8"))[Think Like a Software Architect • Masterclass]],')
    out.append('  footer: [')
    out.append('    #align(center)[')
    out.append('      #context text(size: 8.5pt, fill: rgb("#64748b"))[')
    out.append('        Page #counter(page).display("1 of 1", both: true)')
    out.append('      ]')
    out.append('    ]')
    out.append('  ]')
    out.append(')')
    out.append('#set text(font: ("Avenir", "Helvetica Neue", "Arial"), size: 10pt, fill: rgb("#0f172a"))')
    out.append('#set par(justify: true, leading: 0.72em)')
    out.append("")
    out.append('#chapter-header(')
    out.append(f'  part-num: {part_num},')
    out.append(f'  section-title: "Section {sec_num}: {sec_title_escaped}",')
    out.append(f'  title: "{title_escaped}",')
    out.append(f'  subtitle: "{subtitle_escaped}",')
    out.append(f'  reading-time: "{duration}"')
    out.append(')')
    out.append("")

    # War story
    war_story_escaped = typst_escape_text(part['war_story'])
    out.append('#war-story(')
    out.append('  title: "WAR STORY FROM THE TRENCHES",')
    out.append(f'  [{war_story_escaped}]')
    out.append(')')
    out.append("")

    # Paradigm shift
    out.append("== The Paradigm Shift: From Coder to Architect Mindset")
    out.append(typst_format_block(part['paradigm_shift']))
    out.append("")

    # Core concepts
    out.append("== Core Architectural Principles & Mental Models")
    for concept in part['core_concepts']:
        out.append(f"=== {typst_escape_text(concept['heading'])}")
        out.append(typst_format_block(concept['text']))
        out.append("")

    # Anti-patterns
    out.append("== Common Anti-Patterns & Traps to Avoid")
    for ap in part['anti_patterns']:
        out.append(f"- {typst_format_block(ap)}")
    out.append("")

    # Playbook
    out.append('#architect-playbook(')
    out.append('  title: "THE ARCHITECT\'S PLAYBOOK: ACTION STEPS THIS WEEK",')
    out.append('  [')
    for step in part['playbook']:
        out.append(f"    - {typst_format_block(step)}")
    out.append('  ]')
    out.append(')')
    out.append("")

    # Takeaways
    out.append("== Architectural Takeaways & Cheatsheet")
    for takeaway in part['takeaways']:
        out.append(f"- {typst_format_block(takeaway)}")
    out.append("")

    # Udemy corner
    udemy_prompt_escaped = typst_escape_text(part['udemy_prompt'])
    out.append('#udemy-corner(')
    out.append('  title: "UDEMY & NOTEBOOKLM DISCUSSION PROMPT",')
    out.append('  [')
    out.append(f'    *Course Reflection & Hands-on Assignment:* {udemy_prompt_escaped}')
    out.append('  ]')
    out.append(')')

    return "\n".join(out)


def generate_master_book_typst():
    out = []
    out.append('#import "/templates/book_style.typ": *')
    out.append("")
    out.append('#set document(title: "Think Like a Software Architect: The Complete Masterclass", author: "Advanced Software Architecture Institute")')
    out.append('#set text(font: ("Avenir", "Helvetica Neue", "Arial"), size: 10pt, fill: rgb("#0f172a"))')
    out.append('#set par(justify: true, leading: 0.72em)')
    out.append("")

    # Luxury Executive Cover Page
    out.append("""
// ==================== LUXURY EXECUTIVE COVER PAGE ====================
#page(
  paper: "a4",
  margin: 0cm,
  header: none,
  footer: none,
  fill: rgb("#090d16"),
  [
    #place(top + left, dx: 3.5cm, dy: 3.5cm)[
      #rect(fill: rgb("#0284c7"), radius: 3pt, inset: (x: 10pt, y: 6pt))[
        #text(fill: white, size: 9pt, weight: "bold", tracking: 0.15em)[
          MASTER SOFTWARE ARCHITECTURE SERIES
        ]
      ]
      #v(22pt)
      #text(fill: white, size: 36pt, weight: "bold", tracking: -0.02em)[
        THINK LIKE\\
        A SOFTWARE\\
        ARCHITECT
      ]
      #v(14pt)
      #text(fill: rgb("#38bdf8"), size: 15pt, weight: "medium")[
        The Zero-to-Expert Blueprint for Engineering Systems
      ]
      #v(8pt)
      #text(fill: rgb("#94a3b8"), size: 11pt, style: "italic")[
        From First-Day Architect to Planetary Scale & AI Frontiers
      ]
      #v(32pt)
      #line(length: 12cm, stroke: 1.5pt + rgb("#334155"))
      #v(32pt)
      #grid(
        columns: (auto, auto, auto),
        gutter: 16pt,
        [
          #rect(stroke: 1pt + rgb("#334155"), radius: 4pt, inset: (x: 10pt, y: 8pt))[
            #text(fill: white, size: 9pt, weight: "bold")[40 Master Modules]
          ]
        ],
        [
          #rect(stroke: 1pt + rgb("#334155"), radius: 4pt, inset: (x: 10pt, y: 8pt))[
            #text(fill: white, size: 9pt, weight: "bold")[10 Core Sections]
          ]
        ],
        [
          #rect(stroke: 1pt + rgb("#334155"), radius: 4pt, inset: (x: 10pt, y: 8pt))[
            #text(fill: white, size: 9pt, weight: "bold")[NotebookLM & Udemy Ready]
          ]
        ]
      )
    ]
    #place(bottom + left, dx: 3.5cm, dy: -3cm)[
      #text(fill: rgb("#64748b"), size: 9.5pt)[
        Published by Advanced Software Architecture Institute • Complete Edition 2026
      ]
    ]
  ]
)
""")

    # Inside Setup & Headers
    out.append("""
#set page(
  paper: "a4",
  margin: (top: 2.5cm, bottom: 2.5cm, left: 2.4cm, right: 2.4cm),
  header: [
    #context {
      let page_num = counter(page).get().first()
      if page_num > 2 [
        #grid(
          columns: (1fr, auto),
          align: (left, right),
          [#text(size: 8pt, fill: rgb("#94a3b8"), weight: "bold")[THINK LIKE A SOFTWARE ARCHITECT: ZERO TO EXPERT]],
          [#text(size: 8pt, fill: rgb("#94a3b8"))[COMPLETE MASTERCLASS]]
        )
        #v(-4pt)
        #line(length: 100%, stroke: 0.5pt + rgb("#e2e8f0"))
      ]
    }
  ],
  footer: [
    #context {
      let page_num = counter(page).get().first()
      if page_num > 1 [
        #line(length: 100%, stroke: 0.5pt + rgb("#e2e8f0"))
        #v(4pt)
        #grid(
          columns: (1fr, auto),
          align: (left, right),
          [#text(size: 8pt, fill: rgb("#94a3b8"))[Complete 40-Part Curriculum]],
          [#text(size: 8.5pt, fill: rgb("#475569"), weight: "bold")[#counter(page).display("1")]]
        )
      ]
    }
  ]
)

// ==================== DEDICATION & MANIFESTO ====================
#pagebreak()
#v(35pt)
#align(center)[
  #text(fill: rgb("#0f172a"), size: 22pt, weight: "bold")[The Software Architect's Manifesto]
  #v(16pt)
  #block(width: 82%)[
    #text(fill: rgb("#475569"), size: 11pt, style: "italic")[
      "You were not made an architect to build the most complicated system possible.\\
      You were made an architect to make the complex simple, resilient, and enduring.\\
      To master tradeoffs when every choice demands a sacrifice.\\
      To guide teams with clarity, empathy, and humility.\\
      And to build systems that survive traffic, failures, and time long after you are gone."
    ]
  ]
]

#v(25pt)
== How to Use This Book for NotebookLM & Udemy Course Production

This 40-part volume is engineered for immediate dual-use:

1. *As a Master Architecture Textbook:* A complete zero-to-expert curriculum taking you from your very first day as a software architect through boundaries, domain modeling, distributed data, asynchronous messaging, elasticity, fault tolerance, zero trust, observability, team topologies, and planetary AI scale.
2. *As a Production Source for Google NotebookLM & Udemy:* Each of the 40 chapters includes a hook war story, clear paradigm shifts, core architectural mental models, anti-patterns, action playbooks, and course assignments. When uploaded into NotebookLM:
   - Generate engaging dual-host *Audio Overviews (Podcasts)* for each module.
   - Generate slide outlines, video scripts, and interactive student discussions.
   - Generate challenging multiple-choice quizzes for Udemy module completion certificates.

#pagebreak()
// ==================== TABLE OF CONTENTS ====================
#v(20pt)
#text(fill: rgb("#0f172a"), size: 22pt, weight: "bold")[Table of Contents]
#v(10pt)
#outline(title: none, indent: 1.5em, depth: 2)

#pagebreak()
""")

    # Loop over all sections and parts
    for sec in SECTIONS:
        sec_num = sec['section_num']
        sec_title = typst_escape_text(sec['section_title'])
        sec_desc = typst_escape_text(sec['section_desc'])

        # Section Splash Page
        out.append(f"""
// ==================== SECTION {sec_num} SPLASH ====================
#pagebreak()
#v(60pt)
#rect(
  width: 100%,
  fill: rgb("#090d16"),
  radius: 8pt,
  inset: (x: 24pt, y: 24pt),
  [
    #text(fill: rgb("#38bdf8"), size: 11pt, weight: "bold", tracking: 0.15em)[
      SECTION {sec_num}
    ]
    #v(8pt)
    #text(fill: white, size: 24pt, weight: "bold")[
      {sec_title}
    ]
    #v(10pt)
    #text(fill: rgb("#cbd5e1"), size: 10.5pt)[
      {sec_desc}
    ]
  ]
)
#v(20pt)
#text(size: 11pt, weight: "bold", fill: rgb("#334155"))[Modules in this Section:]
""")
        for part in sec['parts']:
            p_title = typst_escape_text(part['title'])
            out.append(f"- *Part {part['part_num']:02d}:* {p_title}")

        out.append("\n#pagebreak()\n")

        # Section Level Heading for TOC
        out.append(f"= Section {sec_num}: {sec_title}\n")

        # Now the 4 chapters of this section
        for part in sec['parts']:
            p_num = part['part_num']
            p_title = typst_escape_text(part['title'])
            p_sub = typst_escape_text(part['subtitle'])
            duration = part.get('duration', '8 min')

            out.append(f"== Part {p_num:02d}: {p_title}\n")
            out.append(f"""
#rect(
  width: 100%,
  fill: rgb("#f1f5f9"),
  radius: 4pt,
  inset: (x: 12pt, y: 8pt),
  [
    #grid(
      columns: (1fr, auto),
      [#text(weight: "bold", fill: rgb("#0f172a"))[Module {p_num:02d}: {p_title}]],
      [#text(size: 8.5pt, fill: rgb("#0284c7"), weight: "bold")[⏱ {duration} • UDEMY READY]]
    )
    #v(2pt)
    #text(size: 9pt, fill: rgb("#64748b"), style: "italic")[{p_sub}]
  ]
)
#v(10pt)
""")
            # War story
            war_story_escaped = typst_escape_text(part['war_story'])
            out.append('#war-story(')
            out.append('  title: "WAR STORY FROM THE TRENCHES",')
            out.append(f'  [{war_story_escaped}]')
            out.append(')')
            out.append("")

            # Paradigm shift
            out.append("=== The Paradigm Shift: From Coder to Architect Mindset")
            out.append(typst_format_block(part['paradigm_shift']))
            out.append("")

            # Core concepts
            out.append("=== Core Architectural Principles & Mental Models")
            for concept in part['core_concepts']:
                out.append(f"==== {typst_escape_text(concept['heading'])}")
                out.append(typst_format_block(concept['text']))
                out.append("")

            # Anti-patterns
            out.append("=== Common Anti-Patterns & Traps to Avoid")
            for ap in part['anti_patterns']:
                out.append(f"- {typst_format_block(ap)}")
            out.append("")

            # Playbook
            out.append('#architect-playbook(')
            out.append('  title: "THE ARCHITECT\'S PLAYBOOK: ACTION STEPS THIS WEEK",')
            out.append('  [')
            for step in part['playbook']:
                out.append(f"    - {typst_format_block(step)}")
            out.append('  ]')
            out.append(')')
            out.append("")

            # Takeaways
            out.append("=== Architectural Takeaways & Cheatsheet")
            for takeaway in part['takeaways']:
                out.append(f"- {typst_format_block(takeaway)}")
            out.append("")

            # Udemy corner
            udemy_prompt_escaped = typst_escape_text(part['udemy_prompt'])
            out.append('#udemy-corner(')
            out.append('  title: "UDEMY & NOTEBOOKLM DISCUSSION PROMPT",')
            out.append('  [')
            out.append(f'    *Course Reflection & Hands-on Assignment:* {udemy_prompt_escaped}')
            out.append('  ]')
            out.append(')')
            out.append("\n#pagebreak()\n")

    # Appendix: The Software Architect's Survival Cheatsheet
    out.append("""
// ==================== APPENDIX ====================
#pagebreak()
#v(30pt)
#text(fill: rgb("#0f172a"), size: 24pt, weight: "bold")[Appendix: The Architect's Survival Cheatsheet & Mental Models Reference]
#v(14pt)

This reference summary consolidates the fundamental mathematical rules, formulas, and laws governing modern software architecture.

== 1. The Core Distributed Systems Laws
- *Conway's Law:* System architecture copies organizational communication charts.
- *Little's Law:* $L = lambda times W$ (Average requests in system = Arrival Rate × Average Time spent).
- *Amdahl's Law:* Speedup from parallelization is strictly bounded by the sequential fraction of the task.
- *CAP Theorem (Brewer):* Under network partition, choose Consistency (CP) or Availability (AP).
- *PACELC Theorem (Abadi):* If Partition: choose Availability or Consistency; Else: choose Latency or Consistency.

== 2. High Availability & Downtime Math
#table(
  columns: (2fr, 2fr, 3fr),
  fill: (col, row) => if row == 0 { rgb("#0f172a") } else if calc.even(row) { rgb("#f8fafc") } else { white },
  stroke: 0.5pt + rgb("#cbd5e1"),
  align: (left, center, left),
  [#text(fill: white, weight: "bold")[Uptime SLA]],
  [#text(fill: white, weight: "bold")[Allowed Downtime / Month]],
  [#text(fill: white, weight: "bold")[Typical Architecture Class]],
  [99.0% (Two Nines)], [7.2 hours], [Single VM with manual restart],
  [99.9% (Three Nines)], [43.2 minutes], [Multi-AZ auto-scaled stateless instances + RDS replica],
  [99.99% (Four Nines)], [4.32 minutes], [Multi-region active-passive with automated failover],
  [99.999% (Five Nines)], [25.9 seconds], [Multi-region active-active distributed consensus (Spanner)]
)

== 3. Latency Numbers Every Architect Must Know
- *L1 CPU Cache:* ~1 nanosecond
- *L2 CPU Cache:* ~4 nanoseconds
- *RAM Main Memory Read:* ~100 nanoseconds
- *SSD / NVMe Random Read:* ~10-100 microseconds (0.01 - 0.1 ms)
- *LAN Network Roundtrip (Same Datacenter):* ~0.5 milliseconds
- *WAN Transatlantic Roundtrip (NYC to London):* ~70 milliseconds
- *Speed of Light Roundtrip (NYC to Sydney):* ~180 milliseconds

== 4. The 1-Page ADR Template (Michael Nygard Standard)
```markdown
# ADR-[Number]: [Short Title of Architectural Decision]
**Status:** [Proposed | Accepted | Deprecated | Superseded by ADR-XXXX]
**Date:** YYYY-MM-DD
**Deciders:** [Names of Architects, Tech Leads, Stakeholders]

## Context & Problem Statement
What technical or business situation forced this decision? What were the constraints?

## Decision Outcome
Chosen option: [Option Name], because [Primary Justification].

## Considered Options & Tradeoffs
- **Option 1 (Chosen):** [Pros and Cons]
- **Option 2 (Rejected):** [Reason for Rejection]
- **Option 3 (Rejected):** [Reason for Rejection]

## Consequences & Accepted Risks
- Positive: [Capabilities unlocked]
- Negative / Ongoing Tax: [Complexity, cost, latency accepted]
```
""")

    return "\n".join(out)


def generate_course_guide():
    guide = []
    guide.append("# Think Like a Software Architect: Master Udemy & NotebookLM Production Guide\n")
    guide.append("**How to Transform This 40-Part Blueprint into an Industry-Leading Video & Audio Course**\n")
    guide.append("---\n")

    guide.append("## 1. System Architecture of the Course\n")
    guide.append("This repository contains everything needed to launch a premier engineering masterclass on Udemy, Coursera, or internal corporate academies:\n")
    guide.append("- **40 Modular Chapters:** Perfectly sized for 8-12 minute video or audio lectures.")
    guide.append("- **10 Structured Sections:** Natural progression from Day 1 on the job up to planetary scale and Generative AI architecture.")
    guide.append("- **Ready-to-Upload Markdown Files:** Formatted in `chapters/` for batch uploading into Google NotebookLM.")
    guide.append("- **40 Downloadable Standalone PDFs:** Located in `output/individual_pdfs/`, ready to attach to each Udemy lecture as student resources.")
    guide.append("- **Unified Complete Master PDF:** Located in `output/Think_Like_a_Software_Architect_Complete_Guide.pdf` as the official course handbook.\n")

    guide.append("## 2. NotebookLM Audio & Video Generation Workflow\n")
    guide.append("### Phase A: Uploading Sources\n")
    guide.append("1. Go to [Google NotebookLM](https://notebooklm.google.com/).")
    guide.append("2. Create a new notebook titled **'Think Like a Software Architect'**.")
    guide.append("3. Upload the chapters from `chapters/` (either in batches of 4-5 chapters per section, or all 40 chapters).\n")

    guide.append("### Phase B: Generating Dual-Host Audio Overviews (Podcasts)\n")
    guide.append("1. Select a chapter (e.g., `part_01_the_day_the_code_stopped_being_enough.md`).")
    guide.append("2. Click on **'Audio Overview (Deep Dive)'** and customize the prompt:\n")
    guide.append("```text")
    guide.append("Act as two veteran software architects and engineering leaders hosting an energetic, witty, and deeply insightful podcast. Discuss the war story, the paradigm shift, and the core architectural principles in this chapter. Contrast junior coder mistakes with battle-tested architectural wisdom. Use concrete analogies, debate tradeoffs, and end with the actionable takeaway for software engineers.")
    guide.append("```\n")
    guide.append("3. Download the generated `.m4a` or `.mp3` audio file.")
    guide.append("4. Use this audio directly as your **Udemy Podcast / Audio Lecture** or as the voiceover track for your slide presentations!\n")

    guide.append("### Phase C: Generating Lecture Slides & Video Scripts\n")
    guide.append("For each chapter, enter the following prompt into NotebookLM chat:\n")
    guide.append("```text")
    guide.append("Based on Part [X], create a 5-slide lecture presentation outline for Udemy:")
    guide.append("Slide 1: Title and The War Story Hook")
    guide.append("Slide 2: The Paradigm Shift (Coder Mindset vs. Architect Mindset)")
    guide.append("Slide 3: Core Architectural Principles & Mental Models")
    guide.append("Slide 4: Common Anti-Patterns & Traps to Avoid")
    guide.append("Slide 5: The Architect's Action Checklist & Student Reflection Assignment")
    guide.append("Include detailed presenter talking points for each slide.")
    guide.append("```\n")

    guide.append("### Phase D: Generating Multiple-Choice Quizzes for Udemy\n")
    guide.append("Prompt NotebookLM:\n")
    guide.append("```text")
    guide.append("Based on this section, generate 5 challenging, realistic multiple-choice quiz questions for Udemy students. Each question must feature a real-world corporate architectural scenario, 4 plausible options, the correct answer, and an in-depth explanation of why the other 3 options represent dangerous junior traps.")
    guide.append("```\n")

    guide.append("## 3. Complete 40-Module Udemy Course Curriculum Map\n")
    for sec in SECTIONS:
        guide.append(f"### Section {sec['section_num']}: {sec['section_title']}")
        guide.append(f"*{sec['section_desc']}*\n")
        for part in sec['parts']:
            guide.append(f"- **Module {part['part_num']:02d}:** {part['title']} ({part.get('duration', '8 min')})")
        guide.append("")

    guide.append("## 4. Udemy Marketing & Packaging Recommendations\n")
    guide.append("- **Course Title:** Think Like a Software Architect: The Complete Masterclass (From Zero to Planetary Scale)")
    guide.append("- **Subtitle:** Master system decomposition, microservices vs monoliths, distributed data, event-driven architectures, fault tolerance, zero trust, observability, and Generative AI systems.")
    guide.append("- **Category:** Development > Software Engineering / Software Architecture")
    guide.append("- **Target Audience:** Senior developers, tech leads, aspiring software architects, and engineering managers looking to make the leap to Staff+ architectural leadership.")
    guide.append("- **Pricing Strategy:** $84.99–$129.99 (position as premium career-transforming training).")
    guide.append("- **Included Downloadables:** Provide the 40 individual chapter PDFs (`output/individual_pdfs/`) as lecture handouts, and the complete unified PDF (`output/Think_Like_a_Software_Architect_Complete_Guide.pdf`) as the master course textbook!")

    return "\n".join(guide)


def main():
    print("=" * 70)
    print("THINK LIKE A SOFTWARE ARCHITECT - MASTER BUILD PIPELINE")
    print("=" * 70)

    # 1. Generate Individual Markdown Chapters
    print("\n[1/5] Generating 40 Individual Markdown Chapters...")
    for sec in SECTIONS:
        for part in sec['parts']:
            p_num = part['part_num']
            slug = slugify(part['title'].split(':')[0])
            filename = f"part_{p_num:02d}_{slug}.md"
            filepath = os.path.join(CHAPTERS_DIR, filename)
            content = generate_markdown_chapter(sec, part)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
    print(f" -> Generated 40 Markdown files in {CHAPTERS_DIR}")

    # 2. Generate Individual Typst Sources and Compile PDFs
    print("\n[2/5] Generating and Compiling 40 Standalone Chapter PDFs...")
    pdf_count = 0
    for sec in SECTIONS:
        for part in sec['parts']:
            p_num = part['part_num']
            short_title = clean_title_for_filename(part['title'])
            typst_filename = f"part_{p_num:02d}.typ"
            pdf_filename = f"Part_{p_num:02d}_{short_title}.pdf"

            typst_path = os.path.join(TYPST_DIR, typst_filename)
            pdf_path = os.path.join(OUTPUT_PDFS_DIR, pdf_filename)

            typst_content = generate_typst_single_chapter(sec, part)
            with open(typst_path, 'w', encoding='utf-8') as f:
                f.write(typst_content)

            # Compile with typst
            cmd = ["typst", "compile", "--root", BASE_DIR, typst_path, pdf_path]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode != 0:
                print(f"Error compiling Part {p_num}: {res.stderr}")
                sys.exit(1)
            pdf_count += 1
            if pdf_count % 10 == 0:
                print(f"    Compiled {pdf_count}/40 PDFs...")

    print(f" -> Successfully compiled all 40 individual PDFs into {OUTPUT_PDFS_DIR}")

    # 3. Generate Complete Combined Markdown Book
    print("\n[3/5] Generating Combined Complete Markdown Book...")
    combined_md = []
    combined_md.append("# Think Like a Software Architect: The Complete Masterclass\n")
    combined_md.append("**The Zero-to-Expert Blueprint for Engineering Systems**  ")
    combined_md.append("*From First-Day Architect to Planetary Scale & AI Frontiers*\n")
    combined_md.append("---\n")
    combined_md.append("## Table of Contents\n")
    for sec in SECTIONS:
        combined_md.append(f"### Section {sec['section_num']}: {sec['section_title']}")
        for part in sec['parts']:
            combined_md.append(f"- [Part {part['part_num']:02d}: {part['title']}](#part-{part['part_num']:02d}-{slugify(part['title'].split(':')[0])})")
        combined_md.append("")
    combined_md.append("---\n")

    for sec in SECTIONS:
        combined_md.append(f"# Section {sec['section_num']}: {sec['section_title']}\n")
        combined_md.append(f"> {sec['section_desc']}\n\n---\n")
        for part in sec['parts']:
            combined_md.append(generate_markdown_chapter(sec, part))
            combined_md.append("\n\n---\n\n")

    master_md_path = os.path.join(OUTPUT_DIR, "Think_Like_a_Software_Architect_Complete_Guide.md")
    with open(master_md_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(combined_md))
    print(f" -> Saved Complete Book Markdown to {master_md_path}")

    # 4. Generate Combined Master Typst Source & Compile Unified Book PDF
    print("\n[4/5] Generating and Compiling Master Complete Book PDF...")
    master_typst_content = generate_master_book_typst()
    master_typst_path = os.path.join(TYPST_DIR, "think_like_a_software_architect_complete.typ")
    with open(master_typst_path, 'w', encoding='utf-8') as f:
        f.write(master_typst_content)

    master_pdf_path = os.path.join(OUTPUT_DIR, "Think_Like_a_Software_Architect_Complete_Guide.pdf")
    cmd = ["typst", "compile", "--root", BASE_DIR, master_typst_path, master_pdf_path]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error compiling Master Book PDF: {res.stderr}")
        sys.exit(1)

    print(f" -> Successfully compiled Complete Master PDF to {master_pdf_path}")

    # 5. Generate Udemy & NotebookLM Guide
    print("\n[5/5] Generating Udemy & NotebookLM Production Guide...")
    guide_content = generate_course_guide()
    guide_path = os.path.join(COURSE_GUIDE_DIR, "UDEMY_AND_NOTEBOOKLM_GUIDE.md")
    with open(guide_path, 'w', encoding='utf-8') as f:
        f.write(guide_content)
    print(f" -> Saved Course Guide to {guide_path}")

    print("\n" + "=" * 70)
    print("ALL 40 CHAPTERS AND MASTER DELIVERABLES SUCCESSFULLY CREATED!")
    print("=" * 70)


if __name__ == "__main__":
    main()
