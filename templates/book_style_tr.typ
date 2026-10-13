// Bir Yazılım Mimarı Gibi Düşünmek - Türkçe Typst Tasarım Motoru
#let brand-dark = rgb("#090d16")       // Derin Gece Laciverti
#let brand-primary = rgb("#0f172a")    // Koyu Arduvaz Lacivert
#let brand-accent = rgb("#0284c7")     // Mimari Camgöbeği
#let brand-emerald = rgb("#059669")    // Sistem Sağlığı Yeşili
#let brand-amber = rgb("#d97706")      // Ödünleşme Kehribarı
#let brand-rose = rgb("#e11d48")       // Hata Modu Kırmızısı
#let brand-violet = rgb("#7c3aed")     // Strateji Moru
#let brand-bg = rgb("#f8fafc")         // Temiz Stüdyo Beyazı
#let brand-border = rgb("#e2e8f0")     // Çerçeve Rengi
#let brand-text = rgb("#0f172a")       // Yüksek Kontrastlı Kömür Metin
#let brand-muted = rgb("#64748b")      // Sessiz Gri

// Vurgu Kutusu Bileşenleri
#let callout(title: "NOT", icon: "💡", body, border-color: brand-accent, bg-color: rgb("#f0f9ff")) = [
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

#let war-story(title: "SAHADAN YAŞANMIŞ KRİZ HİKAYESİ", body) = [
  #callout(
    title: title,
    icon: "🔥",
    body,
    border-color: rgb("#ea580c"),
    bg-color: rgb("#fff7ed")
  )
]

#let architect-playbook(title: "MİMARIN EYLEM PLANI: BU HAFTAKİ ADIMLAR", body) = [
  #callout(
    title: title,
    icon: "🎯",
    body,
    border-color: rgb("#16a34a"),
    bg-color: rgb("#f0fdf4")
  )
]

#let udemy-corner(title: "UDEMY & NOTEBOOKLM TARTIŞMA VE ÖDEV SORUSU", body) = [
  #callout(
    title: title,
    icon: "🎙️",
    body,
    border-color: rgb("#7c3aed"),
    bg-color: rgb("#faf5ff")
  )
]

#let chapter-header(part-num: 1, section-title: "", title: "", subtitle: "", reading-time: "8 dk okuma") = [
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
            ⏱ #reading-time • DERS #part-num
          ]
        ]
      )
      #v(6pt)
      #text(fill: white, size: 18pt, weight: "bold")[
        Parça #part-num: #title
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
