// Think Like a Software Architect - Typst Styling Engine
#let brand-dark = rgb("#090d16")       // Deep Obsidian Midnight
#let brand-primary = rgb("#0f172a")    // Deep Slate Navy
#let brand-accent = rgb("#0284c7")     // Architectural Cyan/Sky
#let brand-emerald = rgb("#059669")    // System Health Emerald
#let brand-amber = rgb("#d97706")      // Tradeoff Amber
#let brand-rose = rgb("#e11d48")       // Failure Mode Rose
#let brand-violet = rgb("#7c3aed")     // Strategy Violet
#let brand-bg = rgb("#f8fafc")         // Clean Studio Canvas
#let brand-border = rgb("#e2e8f0")     // Crisp Border Slate
#let brand-text = rgb("#0f172a")       // High-contrast Charcoal
#let brand-muted = rgb("#64748b")      // Slate Metadata

// Callout Box Components
#let callout(title: "NOTE", icon: "💡", body, border-color: brand-accent, bg-color: rgb("#f0f9ff")) = [
  #block(
    width: 100%,
    stroke: (left: 4pt + border-color),
    fill: bg-color,
    radius: (right: 4pt),
    inset: (x: 14pt, y: 12pt),
    outset: 0pt,
    spacing: 14pt,
    [
      #text(weight: "bold", fill: border-color, size: 9.5pt)[#icon #upper(title)]
      #v(4pt)
      #text(fill: brand-text, size: 9.8pt, style: "normal")[#body]
    ]
  )
]

#let war-story(title: "WAR STORY FROM THE TRENCHES", body) = [
  #callout(
    title: title,
    icon: "🔥",
    body,
    border-color: rgb("#ea580c"),
    bg-color: rgb("#fff7ed")
  )
]

#let architect-playbook(title: "THE ARCHITECT'S PLAYBOOK: ACTION STEPS", body) = [
  #callout(
    title: title,
    icon: "🎯",
    body,
    border-color: rgb("#16a34a"),
    bg-color: rgb("#f0fdf4")
  )
]

#let udemy-corner(title: "UDEMY & NOTEBOOKLM DISCUSSION PROMPT", body) = [
  #callout(
    title: title,
    icon: "🎙️",
    body,
    border-color: rgb("#7c3aed"),
    bg-color: rgb("#faf5ff")
  )
]

#let chapter-header(part-num: 1, section-title: "", title: "", subtitle: "", reading-time: "8 min read") = [
  #v(8pt)
  #rect(
    width: 100%,
    fill: rgb("#090d16"),
    radius: 6pt,
    inset: (x: 18pt, y: 16pt),
    [
      #grid(
        columns: (1fr, auto),
        align: (left, right),
        [
          #text(fill: rgb("#38bdf8"), size: 8.5pt, weight: "bold", tracking: 0.12em)[
            #upper(section-title)
          ]
        ],
        [
          #text(fill: rgb("#a7f3d0"), size: 8.5pt, weight: "bold")[
            ⏱ #reading-time • MODULE #part-num
          ]
        ]
      )
      #v(6pt)
      #text(fill: white, size: 18pt, weight: "bold")[
        Part #part-num: #title
      ]
      #if subtitle != "" [
        #v(4pt)
        #text(fill: rgb("#cbd5e1"), size: 10.5pt, style: "italic")[
          #subtitle
        ]
      ]
    ]
  )
  #v(14pt)
]
