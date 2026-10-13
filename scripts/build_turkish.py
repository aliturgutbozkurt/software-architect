#!/usr/bin/env python3
"""
Bir Yazılım Mimarı Gibi Düşünmek - Türkçe Derleme ve Üretim Motoru
1. 40 Bağımsız Türkçe Markdown Bölümü (chapters_tr/)
2. 40 Bağımsız Türkçe Typst Kaynağı ve PDF (output_tr/individual_pdfs/)
3. Birleşik Türkçe Ana Kitap Markdown (output_tr/Bir_Yazilim_Mimari_Gibi_Dusunmek_Tam_Rehber.md)
4. Birleşik Türkçe Ana Kitap PDF (output_tr/Bir_Yazilim_Mimari_Gibi_Dusunmek_Tam_Rehber.pdf)
5. Türkçe Udemy & NotebookLM Kurs Yapım Kılavuzu (course_guide/UDEMY_VE_NOTEBOOKLM_TURKCE_REHBER.md)
"""

import os
import re
import subprocess
import sys

# Local scripts directory in sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from content_data_tr.section_01_tr import SECTION_1_TR
from content_data_tr.section_02_tr import SECTION_2_TR
from content_data_tr.section_03_tr import SECTION_3_TR
from content_data_tr.section_04_tr import SECTION_4_TR
from content_data_tr.section_05_tr import SECTION_5_TR
from content_data_tr.section_06_tr import SECTION_6_TR
from content_data_tr.section_07_tr import SECTION_7_TR
from content_data_tr.section_08_tr import SECTION_8_TR
from content_data_tr.section_09_tr import SECTION_9_TR
from content_data_tr.section_10_tr import SECTION_10_TR

SECTIONS_TR = [
    SECTION_1_TR, SECTION_2_TR, SECTION_3_TR, SECTION_4_TR, SECTION_5_TR,
    SECTION_6_TR, SECTION_7_TR, SECTION_8_TR, SECTION_9_TR, SECTION_10_TR
]

BASE_DIR = os.path.dirname(SCRIPT_DIR)
CHAPTERS_TR_DIR = os.path.join(BASE_DIR, "chapters_tr")
TYPST_TR_DIR = os.path.join(BASE_DIR, "typst_sources_tr")
OUTPUT_TR_PDFS_DIR = os.path.join(BASE_DIR, "output_tr", "individual_pdfs")
OUTPUT_TR_DIR = os.path.join(BASE_DIR, "output_tr")
COURSE_GUIDE_DIR = os.path.join(BASE_DIR, "course_guide")

os.makedirs(CHAPTERS_TR_DIR, exist_ok=True)
os.makedirs(TYPST_TR_DIR, exist_ok=True)
os.makedirs(OUTPUT_TR_PDFS_DIR, exist_ok=True)
os.makedirs(OUTPUT_TR_DIR, exist_ok=True)
os.makedirs(COURSE_GUIDE_DIR, exist_ok=True)


def tr_slugify(text):
    text = text.lower()
    mapping = {
        'ç': 'c', 'ğ': 'g', 'ı': 'i', 'ö': 'o', 'ş': 's', 'ü': 'u',
        'Ç': 'c', 'Ğ': 'g', 'İ': 'i', 'Ö': 'o', 'Ş': 's', 'Ü': 'u'
    }
    for k, v in mapping.items():
        text = text.replace(k, v)
    text = re.sub(r'[^a-z0-9]+', '_', text)
    return text.strip('_')


def tr_clean_filename(text):
    parts = text.split(':')
    main_title = parts[0].strip()
    mapping = {
        'ç': 'c', 'ğ': 'g', 'ı': 'i', 'ö': 'o', 'ş': 's', 'ü': 'u',
        'Ç': 'C', 'Ğ': 'G', 'İ': 'I', 'Ö': 'O', 'Ş': 'S', 'Ü': 'U'
    }
    for k, v in mapping.items():
        main_title = main_title.replace(k, v)
    return re.sub(r'[^a-zA-Z0-9]+', '_', main_title).strip('_')


def typst_escape_text(text):
    if not text:
        return ""
    text = text.replace("$", "\\$")
    text = text.replace("@", "\\@")
    text = text.replace("<", "\\<")
    text = text.replace(">", "\\>")
    # Convert markdown bold **text** to Typst *text*
    text = re.sub(r'\*\*(.+?)\*\*', r'*\1*', text)
    return text


def typst_format_block(text):
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
    lines.append(f"# Parça {part['part_num']:02d}: {part['title']}")
    lines.append(f"**Bölüm {sec['section_num']}: {sec['section_title']}**  ")
    lines.append(f"*Tahmini Süre / Sesli Özet: {part.get('duration', '8 dk')}*  ")
    lines.append(f"*{part['subtitle']}*\n")
    lines.append("---\n")

    lines.append("## 🎙️ Mimarın Sahasından Yaşanmış Kriz Hikayesi\n")
    lines.append(f"> {part['war_story']}\n")

    lines.append("## 🧠 Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa\n")
    lines.append(f"{part['paradigm_shift']}\n")

    lines.append("## 📐 Temel Mimari İlkeler ve Zihinsel Modeller\n")
    for concept in part['core_concepts']:
        lines.append(f"### {concept['heading']}")
        lines.append(f"{concept['text']}\n")

    lines.append("## ⚠️ Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar\n")
    for ap in part['anti_patterns']:
        lines.append(f"- {ap}")
    lines.append("")

    lines.append("## 🎯 Mimarın Eylem Planı: Bu Haftaki Somut Adımlar\n")
    for step in part['playbook']:
        lines.append(f"- {step}")
    lines.append("")

    lines.append("## 📌 Mimari Çıkarımlar ve Hile Tablosu\n")
    for takeaway in part['takeaways']:
        lines.append(f"- {takeaway}")
    lines.append("")

    lines.append("## 💡 Udemy Kursu & NotebookLM Tartışma ve Ödev Sorusu\n")
    lines.append(f"**Ödev / Yansıtma Sorusu:** {part['udemy_prompt']}\n")

    return "\n".join(lines)


def generate_typst_single_chapter(sec, part):
    sec_num = sec['section_num']
    part_num = part['part_num']
    title_escaped = typst_escape_text(part['title'])
    subtitle_escaped = typst_escape_text(part['subtitle'])
    sec_title_escaped = typst_escape_text(sec['section_title'])
    duration = part.get('duration', '8 dk')

    out = []
    out.append('#import "/templates/book_style_tr.typ": *')
    out.append("")
    out.append('#set page(')
    out.append('  paper: "a4",')
    out.append('  margin: (top: 2.2cm, bottom: 2.2cm, left: 2.2cm, right: 2.2cm),')
    out.append('  header: align(right)[#text(size: 8pt, fill: rgb("#94a3b8"))[Bir Yazılım Mimarı Gibi Düşünmek • Masterclass]],')
    out.append('  footer: [')
    out.append('    #align(center)[')
    out.append('      #context text(size: 8.5pt, fill: rgb("#64748b"))[')
    out.append('        Sayfa #counter(page).display("1 / 1", both: true)')
    out.append('      ]')
    out.append('    ]')
    out.append('  ]')
    out.append(')')
    out.append('#set text(font: ("Avenir", "Helvetica Neue", "Arial"), size: 10pt, fill: rgb("#0f172a"))')
    out.append('#set par(justify: true, leading: 0.72em)')
    out.append("")
    out.append('#chapter-header(')
    out.append(f'  part-num: {part_num},')
    out.append(f'  section-title: "Bölüm {sec_num}: {sec_title_escaped}",')
    out.append(f'  title: "{title_escaped}",')
    out.append(f'  subtitle: "{subtitle_escaped}",')
    out.append(f'  reading-time: "{duration}"')
    out.append(')')
    out.append("")

    # War story
    war_story_escaped = typst_escape_text(part['war_story'])
    out.append('#war-story(')
    out.append('  title: "SAHADAN YAŞANMIŞ KRİZ HİKAYESİ",')
    out.append(f'  [{war_story_escaped}]')
    out.append(')')
    out.append("")

    # Paradigm shift
    out.append("== Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa")
    out.append(typst_format_block(part['paradigm_shift']))
    out.append("")

    # Core concepts
    out.append("== Temel Mimari İlkeler ve Zihinsel Modeller")
    for concept in part['core_concepts']:
        out.append(f"=== {typst_escape_text(concept['heading'])}")
        out.append(typst_format_block(concept['text']))
        out.append("")

    # Anti-patterns
    out.append("== Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar")
    for ap in part['anti_patterns']:
        out.append(f"- {typst_format_block(ap)}")
    out.append("")

    # Playbook
    out.append('#architect-playbook(')
    out.append('  title: "MİMARIN EYLEM PLANI: BU HAFTAKİ SOMUT ADIMLAR",')
    out.append('  [')
    for step in part['playbook']:
        out.append(f"    - {typst_format_block(step)}")
    out.append('  ]')
    out.append(')')
    out.append("")

    # Takeaways
    out.append("== Mimari Çıkarımlar ve Hile Tablosu")
    for takeaway in part['takeaways']:
        out.append(f"- {typst_format_block(takeaway)}")
    out.append("")

    # Udemy corner
    udemy_prompt_escaped = typst_escape_text(part['udemy_prompt'])
    out.append('#udemy-corner(')
    out.append('  title: "UDEMY & NOTEBOOKLM TARTIŞMA VE ÖDEV SORUSU",')
    out.append('  [')
    out.append(f'    *Ders Değerlendirmesi ve Ödev:* {udemy_prompt_escaped}')
    out.append('  ]')
    out.append(')')

    return "\n".join(out)


def generate_master_book_typst():
    out = []
    out.append('#import "/templates/book_style_tr.typ": *')
    out.append("")
    out.append('#set document(title: "Bir Yazılım Mimarı Gibi Düşünmek: Sıfırdan Uzmanlığa", author: "İleri Yazılım Mimarisi Enstitüsü")')
    out.append('#set text(font: ("Avenir", "Helvetica Neue", "Arial"), size: 10pt, fill: rgb("#0f172a"))')
    out.append('#set par(justify: true, leading: 0.72em)')
    out.append("")

    # Luxury Executive Cover Page
    out.append("""
// ==================== LÜKS TÜRKÇE KAPAK SAYFASI ====================
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
          İLERİ YAZILIM MİMARİSİ SERİSİ
        ]
      ]
      #v(22pt)
      #text(fill: white, size: 34pt, weight: "bold", tracking: -0.02em)[
        BİR YAZILIM\\
        MİMARI GİBİ\\
        DÜŞÜNMEK
      ]
      #v(14pt)
      #text(fill: rgb("#38bdf8"), size: 15pt, weight: "medium")[
        Sıfırdan Uzmanlığa Sistem Tasarımı ve Liderlik Rehberi
      ]
      #v(8pt)
      #text(fill: rgb("#94a3b8"), size: 11pt, style: "italic")[
        İlk Günkü Geliştiriciden Gezegensel Ölçek ve Yapay Zekaya
      ]
      #v(32pt)
      #line(length: 12cm, stroke: 1.5pt + rgb("#334155"))
      #v(32pt)
      #grid(
        columns: (auto, auto, auto),
        gutter: 16pt,
        [
          #rect(stroke: 1pt + rgb("#334155"), radius: 4pt, inset: (x: 10pt, y: 8pt))[
            #text(fill: white, size: 9pt, weight: "bold")[40 Ana Ders Modülü]
          ]
        ],
        [
          #rect(stroke: 1pt + rgb("#334155"), radius: 4pt, inset: (x: 10pt, y: 8pt))[
            #text(fill: white, size: 9pt, weight: "bold")[10 Stratejik Bölüm]
          ]
        ],
        [
          #rect(stroke: 1pt + rgb("#334155"), radius: 4pt, inset: (x: 10pt, y: 8pt))[
            #text(fill: white, size: 9pt, weight: "bold")[NotebookLM & Udemy Uyumlu]
          ]
        ]
      )
    ]
    #place(bottom + left, dx: 3.5cm, dy: -3cm)[
      #text(fill: rgb("#64748b"), size: 9.5pt)[
        İleri Yazılım Mimarisi Enstitüsü Yayınları • Tam Türkçe Sürüm 2026
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
          [#text(size: 8pt, fill: rgb("#94a3b8"), weight: "bold")[BİR YAZILIM MİMARI GİBİ DÜŞÜNMEK]],
          [#text(size: 8pt, fill: rgb("#94a3b8"))[SIFIRDAN UZMANLIĞA]]
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
          [#text(size: 8pt, fill: rgb("#94a3b8"))[40 Parçalık Tam Müfredat]],
          [#text(size: 8.5pt, fill: rgb("#475569"), weight: "bold")[#counter(page).display("1")]]
        )
      ]
    }
  ]
)

// ==================== İTHAF VE MANİFESTO ====================
#pagebreak()
#v(35pt)
#align(center)[
  #text(fill: rgb("#0f172a"), size: 22pt, weight: "bold")[Yazılım Mimarının Manifestosu]
  #v(16pt)
  #block(width: 82%)[
    #text(fill: rgb("#475569"), size: 11pt, style: "italic")[
      "Sen mümkün olan en karmaşık sistemi kurasın diye mimar yapılmadın.\\
      Sen karmaşığı sade, dayanıklı ve kalıcı kılasın diye mimar yapıldın.\\
      Her seçimin bir bedel istediği o zor anlarda ödünleşmeleri ustalıkla yönetesin diye.\\
      Ekiplere netlik, empati ve alçakgönüllülükle rehberlik edesin diye.\\
      Ve sen gittikten çok sonra bile trafiğe, arızalara ve zamana meydan okuyan sistemler inşa edesin diye."
    ]
  ]
]

#v(25pt)
== Bu Kitap NotebookLM ve Udemy Eğitimi İçin Nasıl Kullanılır?

Bu 40 parçalık başvuru eseri çift yönlü kullanım için özel olarak tasarlanmıştır:

1. *Kapsamlı Bir Yazılım Mimarisi El Kitabı Olarak:* İlk günkü bilet karmaşasından başlayıp; modüler monolitler, domain-driven design, dağıtık veritabanları, asenkron akışlar, sıfır güven, FinOps, ekip topolojileri ve üretken yapay zeka mimarilerine kadar sıfırdan uzmanlığa uzanan eksiksiz bir rehber.
2. *Google NotebookLM ve Udemy İçin Üretim Kütüphanesi Olarak:* 40 bölümün her biri sahada yaşanmış gerçek bir kriz hikayesi (war story), açık zihniyet dönüşümleri, temel mimari zihinsel modeller, kaçınılması gereken tuzaklar, haftalık eylem planları ve tartışma soruları içerir. Bu metinleri NotebookLM'e yükleyerek:
   - Her ders için anında çift sunuculu derinlemesine *Sesli Podcast'ler (Audio Overview)* üretebilirsiniz.
   - 5 slaytlık video sunum taslakları ve konuşmacı notları çıkarabilirsiniz.
   - Udemy öğrencileri için zorlayıcı, gerçekçi çoktan seçmeli sınav soruları üretebilirsiniz.

#pagebreak()
// ==================== İÇİNDEKİLER ====================
#v(20pt)
#text(fill: rgb("#0f172a"), size: 22pt, weight: "bold")[İçindekiler Tablosu]
#v(10pt)
#outline(title: none, indent: 1.5em, depth: 2)

#pagebreak()
""")

    # Loop over all sections and parts
    for sec in SECTIONS_TR:
        sec_num = sec['section_num']
        sec_title = typst_escape_text(sec['section_title'])
        sec_desc = typst_escape_text(sec['section_desc'])

        # Section Splash Page
        out.append(f"""
// ==================== BÖLÜM {sec_num} KAPAK ====================
#pagebreak()
#v(60pt)
#rect(
  width: 100%,
  fill: rgb("#090d16"),
  radius: 8pt,
  inset: (x: 24pt, y: 24pt),
  [
    #text(fill: rgb("#38bdf8"), size: 11pt, weight: "bold", tracking: 0.15em)[
      ANA BÖLÜM {sec_num}
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
#text(size: 11pt, weight: "bold", fill: rgb("#334155"))[Bu Bölümdeki Ders Modülleri:]
""")
        for part in sec['parts']:
            p_title = typst_escape_text(part['title'])
            out.append(f"- *Parça {part['part_num']:02d}:* {p_title}")

        out.append("\n#pagebreak()\n")

        # Section Level Heading for TOC
        out.append(f"= Bölüm {sec_num}: {sec_title}\n")

        # Now the 4 chapters of this section
        for part in sec['parts']:
            p_num = part['part_num']
            p_title = typst_escape_text(part['title'])
            p_sub = typst_escape_text(part['subtitle'])
            duration = part.get('duration', '8 dk')

            out.append(f"== Parça {p_num:02d}: {p_title}\n")
            out.append(f"""
#rect(
  width: 100%,
  fill: rgb("#f1f5f9"),
  radius: 4pt,
  inset: (x: 12pt, y: 8pt),
  [
    #grid(
      columns: (1fr, auto),
      [#text(weight: "bold", fill: rgb("#0f172a"))[Modül {p_num:02d}: {p_title}]],
      [#text(size: 8.5pt, fill: rgb("#0284c7"), weight: "bold")[⏱ {duration} • UDEMY DERSİ]]
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
            out.append('  title: "SAHADAN YAŞANMIŞ KRİZ HİKAYESİ",')
            out.append(f'  [{war_story_escaped}]')
            out.append(')')
            out.append("")

            # Paradigm shift
            out.append("=== Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa")
            out.append(typst_format_block(part['paradigm_shift']))
            out.append("")

            # Core concepts
            out.append("=== Temel Mimari İlkeler ve Zihinsel Modeller")
            for concept in part['core_concepts']:
                out.append(f"==== {typst_escape_text(concept['heading'])}")
                out.append(typst_format_block(concept['text']))
                out.append("")

            # Anti-patterns
            out.append("=== Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar")
            for ap in part['anti_patterns']:
                out.append(f"- {typst_format_block(ap)}")
            out.append("")

            # Playbook
            out.append('#architect-playbook(')
            out.append('  title: "MİMARIN EYLEM PLANI: BU HAFTAKİ SOMUT ADIMLAR",')
            out.append('  [')
            for step in part['playbook']:
                out.append(f"    - {typst_format_block(step)}")
            out.append('  ]')
            out.append(')')
            out.append("")

            # Takeaways
            out.append("=== Mimari Çıkarımlar ve Hile Tablosu")
            for takeaway in part['takeaways']:
                out.append(f"- {typst_format_block(takeaway)}")
            out.append("")

            # Udemy corner
            udemy_prompt_escaped = typst_escape_text(part['udemy_prompt'])
            out.append('#udemy-corner(')
            out.append('  title: "UDEMY & NOTEBOOKLM TARTIŞMA VE ÖDEV SORUSU",')
            out.append('  [')
            out.append(f'    *Ders Değerlendirmesi ve Ödev:* {udemy_prompt_escaped}')
            out.append('  ]')
            out.append(')')
            out.append("\n#pagebreak()\n")

    # Appendix: The Software Architect's Survival Cheatsheet
    out.append("""
// ==================== EK: MİMARIN HİLE TABLOSU ====================
#pagebreak()
#v(30pt)
#text(fill: rgb("#0f172a"), size: 24pt, weight: "bold")[Ek: Yazılım Mimarının Hayatta Kalma Kılavuzu & Zihinsel Modeller]
#v(14pt)

Bu özet başvuru bölümü, modern yazılım mimarisini yöneten temel matematiksel kuralları, yasaları ve formülleri tek bir yerde toplamaktadır.

== 1. Temel Dağıtık Sistem Yasaları
- *Conway Yasası:* Sistem mimarisi organizasyonun iletişim şemasını kopyalar.
- *Little Yasası:* $L = lambda times W$ (Sistemdeki ortalama istek = Geliş Hızı × Harcanan Süre).
- *Amdahl Yasası:* Paralelleştirmeden elde edilecek hız artışı, işin sıralı yapılmak zorunda olan kısmıyla kesin olarak sınırlıdır.
- *CAP Teoremi (Brewer):* Ağ bölünmesi anında Tutarlılık (CP) ya da Erişilebilirlik (AP) arasında seçim yapılmalıdır.
- *PACELC Teoremi (Abadi):* Bölünme varsa (*P*) Erişilebilirlik mi Tutarlılık mı? Yoksa (*E*) Gecikme mi Tutarlılık mı?

== 2. Yüksek Erişilebilirlik ve Kesinti Süresi Tablosu
#table(
  columns: (2fr, 2fr, 3fr),
  fill: (col, row) => if row == 0 { rgb("#0f172a") } else if calc.even(row) { rgb("#f8fafc") } else { white },
  stroke: 0.5pt + rgb("#cbd5e1"),
  align: (left, center, left),
  [#text(fill: white, weight: "bold")[Erişilebilirlik SLA]],
  [#text(fill: white, weight: "bold")[İzin Verilen Kesinti / Ay]],
  [#text(fill: white, weight: "bold")[Tipik Mimari Sınıfı]],
  [%99.0 (İki Dokuz)], [7.2 saat], [Tek sanal sunucu ve manuel yeniden başlatma],
  [%99.9 (Üç Dokuz)], [43.2 dakika], [Çok bölgeli auto-scale durumsuz pod'lar + RDS replica],
  [%99.99 (Dört Dokuz)], [4.32 dakika], [Çok bölgeli aktif-pasif otomatik yük devretme],
  [%99.999 (Beş Dokuz)], [25.9 saniye], [Çok bölgeli aktif-aktif dağıtık mutabakat (Spanner)]
)

== 3. Her Mimarın Ezbere Bilmesi Gereken Gecikme Rakamları
- *L1 CPU Önbelleği:* ~1 nanosaniye
- *L2 CPU Önbelleği:* ~4 nanosaniye
- *RAM Ana Bellek Okuma:* ~100 nanosaniye
- *NVMe / SSD Rastgele Okuma:* ~10-100 mikrosaniye (0.01 - 0.1 ms)
- *Aynı Veri Merkezinde Ağ Turu (LAN):* ~0.5 milisaniye
- *Kıtalararası Ağ Turu (İstanbul - New York):* ~75 milisaniye
- *Okyanus Tabanında Işık Hızı Turu (İstanbul - Sidney):* ~180 milisaniye

== 4. 1 Sayfalık Örnek ADR Şablonu (Michael Nygard Standardı)
```markdown
# ADR-[Numara]: [Kararın Kısa ve Net Başlığı]
**Durum:** [Önerildi | Kabul Edildi | İptal Edildi | ADR-XXXX ile Değiştirildi]
**Tarih:** YYYY-AA-GG
**Karar Vericiler:** [Mimar, Takım Lideri, İlgili Mühendisler]

## Bağlam ve Problem Tanımı
Hangi iş veya teknik zorunluluk bizi bu karara mecbur bıraktı? Kısıtlarımız nelerdi?

## Karar Sonucu
Seçilen çözüm: [Çözüm Adı], çünkü [Temel Gerekçe].

## Değerlendirilen Seçenekler ve Ödünleşmeler
- **1. Seçenek (Seçilen):** [Artıları ve Eksileri]
- **2. Seçenek (Elenen):** [Elenme Gerekçesi]
- **3. Seçenek (Elenen):** [Elenme Gerekçesi]

## Sonuçlar ve Kabul Edilen Riskler
- Olumlu Kazanımlar: [Sisteme kazandırılan yetenekler]
- Olumsuz Bedel / Sürekli Vergi: [Kabul edilen karmaşıklık, gecikme veya maliyet]
```
""")

    return "\n".join(out)


def generate_course_guide_tr():
    guide = []
    guide.append("# Bir Yazılım Mimarı Gibi Düşünmek: Türkçe Udemy & NotebookLM Kurs Yapım Kılavuzu\n")
    guide.append("**Bu 40 Parçalık Başvuru Eserini Sektörün Lideri Video ve Sesli Eğitimine Dönüştürme Rehberi**\n")
    guide.append("---\n")

    guide.append("## 1. Eğitimin Sistem Mimarisi\n")
    guide.append("Bu çalışma alanı, Udemy'de veya şirket içi kurumsal akademilerde premium bir mimarlık eğitimi yayınlamak için gereken her şeyi içerir:\n")
    guide.append("- **40 Modüler Bölüm:** Her biri 8-12 dakikalık video veya sesli dersler için ideal uzunlukta.")
    guide.append("- **10 Yapılandırılmış Bölüm:** İlk günden ileri kurumsal ölçeğe ve Generative AI'a uzanan doğal pedagojik akış.")
    guide.append("- **NotebookLM'e Hazır Dosyalar:** `chapters_tr/` klasöründe tek tek veya topluca yüklenebilir Markdown formatı.")
    guide.append("- **40 İndirilebilir Bağımsız PDF:** `output_tr/individual_pdfs/` klasöründe, her Udemy dersine ek kaynak olarak eklenebilir.")
    guide.append("- **Birleşik Tam Kitap PDF'i:** `output_tr/Bir_Yazilim_Mimari_Gibi_Dusunmek_Tam_Rehber.pdf` resmi eğitim ders kitabı olarak hazır.\n")

    guide.append("## 2. NotebookLM ile Ses ve Video Üretim İş Akışı\n")
    guide.append("### Adım A: Kaynakları Yükleme\n")
    guide.append("1. [Google NotebookLM](https://notebooklm.google.com/) adresine gidin.")
    guide.append("2. **'Bir Yazılım Mimarı Gibi Düşünmek'** başlıklı yeni bir defter açın.")
    guide.append("3. `chapters_tr/` klasöründeki bölümleri deftere yükleyin (bölüm bölüm veya 40 dosyayı birden).\n")

    guide.append("### Adım B: Çift Sunuculu Sesli Podcast (Audio Overview) Üretimi\n")
    guide.append("1. Bir bölüm seçin (Örn: `parca_01_kod_yazmanin_yetmedigi_gun.md`).")
    guide.append("2. **'Audio Overview (Deep Dive)'** butonuna tıklayın ve özel istemi (Customize) girin:\n")
    guide.append("```text")
    guide.append("Sahada yıllarca pişmiş iki deneyimli yazılım mimarı ve mühendislik lideri olarak enerjik, esprili ve derinlemesine bir Türkçe podcast yürütün. Bölümdeki kriz hikayesini (war story), zihniyet dönüşümünü ve temel mimari ilkeleri tartışın. Acemi yazılımcı hataları ile usta mimar bilgeliğini karşılaştırın. Somut analojiler kullanın, ödünleşmeleri tartışın ve yazılımcılar için uygulanabilir altın tavsiyelerle bitirin.")
    guide.append("```\n")
    guide.append("3. Üretilen `.m4a` ses dosyasını indirin.")
    guide.append("4. Bu sesi doğrudan **Udemy Podcast Dersi** olarak yükleyebilir veya slaytlarınızın arkasına seslendirme olarak koyabilirsiniz!\n")

    guide.append("### Adım C: Video Slaytları ve Ders Metinleri Çıkarma\n")
    guide.append("NotebookLM sohbetine şu istemi yazın:\n")
    guide.append("```text")
    guide.append("Parça [X]'e dayanarak Udemy için 5 slaytlık bir video sunum taslağı hazırla:")
    guide.append("Slayt 1: Başlık ve Giriş Kriz Hikayesi (Hook)")
    guide.append("Slayt 2: Zihniyet Dönüşümü (Yazılımcı vs Mimar Bakışı)")
    guide.append("Slayt 3: Temel Mimari İlkeler ve Modeller")
    guide.append("Slayt 4: Kaçınılması Gereken Tehlikeli Tuzaklar (Anti-Patterns)")
    guide.append("Slayt 5: Mimarın Haftalık Kontrol Listesi ve Öğrenci Ödevi")
    guide.append("Her slayt için konuşmacının söyleyeceği detaylı ders anlatım metnini ekle.")
    guide.append("```\n")

    guide.append("### Adım D: Udemy İçin Çoktan Seçmeli Quiz Üretme\n")
    guide.append("NotebookLM'e yazın:\n")
    guide.append("```text")
    guide.append("Bu bölümdeki bilgilere dayanarak Udemy öğrencileri için 5 adet zorlayıcı, gerçekçi çoktan seçmeli sınav sorusu üret. Her soru sahada yaşanmış gerçek bir kurumsal mimari senaryoya dayansın, 4 makul şık içersin, doğru cevabı belirtsin ve diğer 3 şıkkın neden tehlikeli acemi tuzakları olduğunu ayrıntılı açıklasın.")
    guide.append("```\n")

    guide.append("## 3. 40 Modüllük Tam Türkçe Müfredat Haritası\n")
    for sec in SECTIONS_TR:
        guide.append(f"### Bölüm {sec['section_num']}: {sec['section_title']}")
        guide.append(f"*{sec['section_desc']}*\n")
        for part in sec['parts']:
            guide.append(f"- **Modül {part['part_num']:02d}:** {part['title']} ({part.get('duration', '8 dk')})")
        guide.append("")

    guide.append("## 4. Udemy Pazarlama ve Paketleme Tavsiyeleri\n")
    guide.append("- **Kurs Başlığı:** Bir Yazılım Mimarı Gibi Düşünmek: Sıfırdan Uzmanlığa (Gezegensel Ölçek ve Yapay Zeka)")
    guide.append("- **Alt Başlık:** Sistem tasarımı, monolit vs mikroservis, dağıtık veritabanları, Kafka, sıfır güven, FinOps, SRE hata bütçeleri ve kurumsal GenAI mimarisi.")
    guide.append("- **Kategori:** Geliştirme > Yazılım Mühendisliği / Yazılım Mimarisi")
    guide.append("- **Hedef Kitle:** Kıdemli geliştiriciler, teknik liderler, yeni mimarlar ve Staff+ mühendislik liderliğine adım atmak isteyenler.")
    guide.append("- **İndirilebilir Materyaller:** Her dersin altına `output_tr/individual_pdfs/` klasöründeki bağımsız PDF'leri ders notu olarak; `output_tr/Bir_Yazilim_Mimari_Gibi_Dusunmek_Tam_Rehber.pdf` dosyasını da ana ders kitabı olarak ekleyin!")

    return "\n".join(guide)


def main():
    print("=" * 70)
    print("BİR YAZILIM MİMARI GİBİ DÜŞÜNMEK - TÜRKÇE DERLEME VE ÜRETİM MOTORU")
    print("=" * 70)

    # 1. 40 Bağımsız Türkçe Markdown Bölümü
    print("\n[1/5] 40 Bağımsız Türkçe Markdown Bölümü Üretiliyor...")
    for sec in SECTIONS_TR:
        for part in sec['parts']:
            p_num = part['part_num']
            slug = tr_slugify(part['title'].split(':')[0])
            filename = f"parca_{p_num:02d}_{slug}.md"
            filepath = os.path.join(CHAPTERS_TR_DIR, filename)
            content = generate_markdown_chapter(sec, part)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
    print(f" -> {CHAPTERS_TR_DIR} klasöründe 40 Türkçe Markdown dosyası oluşturuldu.")

    # 2. 40 Bağımsız Türkçe Typst Kaynağı ve PDF
    print("\n[2/5] 40 Bağımsız Türkçe Typst Kaynağı ve PDF Derleniyor...")
    pdf_count = 0
    for sec in SECTIONS_TR:
        for part in sec['parts']:
            p_num = part['part_num']
            short_title = tr_clean_filename(part['title'])
            typst_filename = f"parca_{p_num:02d}.typ"
            pdf_filename = f"Parca_{p_num:02d}_{short_title}.pdf"

            typst_path = os.path.join(TYPST_TR_DIR, typst_filename)
            pdf_path = os.path.join(OUTPUT_TR_PDFS_DIR, pdf_filename)

            typst_content = generate_typst_single_chapter(sec, part)
            with open(typst_path, 'w', encoding='utf-8') as f:
                f.write(typst_content)

            # Typst ile derle
            cmd = ["typst", "compile", "--root", BASE_DIR, typst_path, pdf_path]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode != 0:
                print(f"Parça {p_num} derlenirken hata: {res.stderr}")
                sys.exit(1)
            pdf_count += 1
            if pdf_count % 10 == 0:
                print(f"    Derlenen Türkçe PDF: {pdf_count}/40...")

    print(f" -> Tüm 40 bağımsız Türkçe PDF başarıyla {OUTPUT_TR_PDFS_DIR} klasörüne derlendi.")

    # 3. Birleşik Türkçe Ana Kitap Markdown
    print("\n[3/5] Birleşik Türkçe Ana Kitap Markdown Üretiliyor...")
    combined_md = []
    combined_md.append("# Bir Yazılım Mimarı Gibi Düşünmek: Sıfırdan Uzmanlığa\n")
    combined_md.append("**Sistem Tasarımı, Dağıtık Mimariler ve Teknik Liderlik Rehberi**  ")
    combined_md.append("*İlk Günkü Mühendisten Gezegensel Ölçek ve Yapay Zekaya*\n")
    combined_md.append("---\n")
    combined_md.append("## İçindekiler Tablosu\n")
    for sec in SECTIONS_TR:
        combined_md.append(f"### Bölüm {sec['section_num']}: {sec['section_title']}")
        for part in sec['parts']:
            combined_md.append(f"- [Parça {part['part_num']:02d}: {part['title']}](#parca-{part['part_num']:02d}-{tr_slugify(part['title'].split(':')[0])})")
        combined_md.append("")
    combined_md.append("---\n")

    for sec in SECTIONS_TR:
        combined_md.append(f"# Bölüm {sec['section_num']}: {sec['section_title']}\n")
        combined_md.append(f"> {sec['section_desc']}\n\n---\n")
        for part in sec['parts']:
            combined_md.append(generate_markdown_chapter(sec, part))
            combined_md.append("\n\n---\n\n")

    master_md_path = os.path.join(OUTPUT_TR_DIR, "Bir_Yazilim_Mimari_Gibi_Dusunmek_Tam_Rehber.md")
    with open(master_md_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(combined_md))
    print(f" -> Birleşik Türkçe Markdown kaydedildi: {master_md_path}")

    # 4. Birleşik Türkçe Master Typst Kaynağı ve PDF
    print("\n[4/5] Birleşik Türkçe Ana Kitap PDF Derleniyor...")
    master_typst_content = generate_master_book_typst()
    master_typst_path = os.path.join(TYPST_TR_DIR, "bir_yazilim_mimari_gibi_dusunmek_tam.typ")
    with open(master_typst_path, 'w', encoding='utf-8') as f:
        f.write(master_typst_content)

    master_pdf_path = os.path.join(OUTPUT_TR_DIR, "Bir_Yazilim_Mimari_Gibi_Dusunmek_Tam_Rehber.pdf")
    cmd = ["typst", "compile", "--root", BASE_DIR, master_typst_path, master_pdf_path]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Türkçe Ana Kitap PDF derlenirken hata: {res.stderr}")
        sys.exit(1)

    print(f" -> Birleşik Türkçe Ana Kitap PDF başarıyla derlendi: {master_pdf_path}")

    # 5. Türkçe Udemy & NotebookLM Kılavuzu
    print("\n[5/5] Türkçe Udemy & NotebookLM Kurs Yapım Kılavuzu Üretiliyor...")
    guide_content = generate_course_guide_tr()
    guide_path = os.path.join(COURSE_GUIDE_DIR, "UDEMY_VE_NOTEBOOKLM_TURKCE_REHBER.md")
    with open(guide_path, 'w', encoding='utf-8') as f:
        f.write(guide_content)
    print(f" -> Türkçe Kurs Kılavuzu kaydedildi: {guide_path}")

    print("\n" + "=" * 70)
    print("TÜM 40 TÜRKÇE BÖLÜM VE ANA ÇIKTILAR BAŞARIYLA TAMAMLANDI!")
    print("=" * 70)


if __name__ == "__main__":
    main()
