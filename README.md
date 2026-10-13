# Think Like a Software Architect / Bir Yazılım Mimarı Gibi Düşünmek (40-Part Masterclass)

Bu çalışma alanı, **"Think Like a Software Architect"** kitabının ve Udemy / NotebookLM eğitim setinin hem **İngilizce (English Edition)** hem de **Türkçe (Turkish Edition)** tam sürümlerini içerir.

Proje, yazılımcılıktan mimarlığa geçen bir mühendisin ilk gününden başlayıp; sistem sınırları, Domain-Driven Design, mikroservisler vs monolitler, dağıtık veritabanları, Kafka, olay odaklı mimari, sıfır güven güvenliği, FinOps, SRE hata bütçeleri, gezegensel mutabakat ve üretime hazır Generative AI mimarisine kadar **sıfırdan uzmanlığa** uzanmaktadır.

Tüm bölümler sahadan gerçek kriz hikayeleri (War Stories), zihniyet dönüşümleri, anti-pattern'ler, pratik eylem planları ve Google NotebookLM podcast istemleri ile donatılmıştır.

---

## 🇹🇷 Türkçe Sürüm Çıktıları (Turkish Edition)

| Çıktı Türü | Konum / Dosya Linki | Açıklama |
| :--- | :--- | :--- |
| **Birleşik Ana Kitap PDF (107 Sayfa)** | [output_tr/Bir_Yazilim_Mimari_Gibi_Dusunmek_Tam_Rehber.pdf](file:///Users/aliturgutbozkurt/Desktop/Software%20Architect/output_tr/Bir_Yazilim_Mimari_Gibi_Dusunmek_Tam_Rehber.pdf) | Özel Obsidian & Cyan Türkçe kapak, içindekiler tablosu, 10 ana bölüm kapağı, 40 modül ve Mimarın Hile Tablosu (Appendix). |
| **Birleşik Türkçe Markdown Kaynak** | [output_tr/Bir_Yazilim_Mimari_Gibi_Dusunmek_Tam_Rehber.md](file:///Users/aliturgutbozkurt/Desktop/Software%20Architect/output_tr/Bir_Yazilim_Mimari_Gibi_Dusunmek_Tam_Rehber.md) | NotebookLM'e tek seferde yüklemek veya e-kitap olarak dağıtmak için 193 KB'lık tam Türkçe metin. |
| **40 Adet Bağımsız Türkçe PDF** | [output_tr/individual_pdfs/](file:///Users/aliturgutbozkurt/Desktop/Software%20Architect/output_tr/individual_pdfs/) | Her biri kendi başlığına, sayfa numarasına ve Udemy ders etiketine sahip 40 bağımsız Türkçe PDF. |
| **40 Adet Modüler Türkçe Markdown** | [chapters_tr/](file:///Users/aliturgutbozkurt/Desktop/Software%20Architect/chapters_tr/) | Google NotebookLM'e bölüm bölüm yükleyip çift sunuculu Türkçe podcast üretmek için optimize edilmiş 40 dosya. |
| **Türkçe Kurs & NotebookLM Kılavuzu** | [course_guide/UDEMY_VE_NOTEBOOKLM_TURKCE_REHBER.md](file:///Users/aliturgutbozkurt/Desktop/Software%20Architect/course_guide/UDEMY_VE_NOTEBOOKLM_TURKCE_REHBER.md) | Türkçe çift sunuculu podcast istemleri, 5 slaytlık sunum şablonları, Udemy sınav (quiz) çıkarma rehberi. |

---

## 🇬🇧 İngilizce Sürüm Çıktıları (English Edition)

| Çıktı Türü | Konum / Dosya Linki | Açıklama |
| :--- | :--- | :--- |
| **Master Complete Book PDF (107 Pages)** | [output/Think_Like_a_Software_Architect_Complete_Guide.pdf](file:///Users/aliturgutbozkurt/Desktop/Software%20Architect/output/Think_Like_a_Software_Architect_Complete_Guide.pdf) | Complete 107-page master book in English with luxury obsidian cover, TOC, 10 section splash pages, 40 parts, and Cheatsheet Appendix. |
| **Master Complete Markdown** | [output/Think_Like_a_Software_Architect_Complete_Guide.md](file:///Users/aliturgutbozkurt/Desktop/Software%20Architect/output/Think_Like_a_Software_Architect_Complete_Guide.md) | Full unified English source text for global NotebookLM ingestion and e-book distribution (179 KB). |
| **40 Standalone Chapter PDFs** | [output/individual_pdfs/](file:///Users/aliturgutbozkurt/Desktop/Software%20Architect/output/individual_pdfs/) | 40 individually styled, numbered PDFs ready to attach as downloadable lecture resources on Udemy. |
| **40 Standalone Markdown Chapters** | [chapters/](file:///Users/aliturgutbozkurt/Desktop/Software%20Architect/chapters/) | 40 modular markdown chapters optimized for batch uploading into NotebookLM. |
| **English Course & NotebookLM Guide** | [course_guide/UDEMY_AND_NOTEBOOKLM_GUIDE.md](file:///Users/aliturgutbozkurt/Desktop/Software%20Architect/course_guide/UDEMY_AND_NOTEBOOKLM_GUIDE.md) | Dual-host podcast prompts, lecture scripts, 5-slide outlines, and quiz generation templates. |

---

## 📑 10 Ana Bölüm (Müfredat Haritası)

1. **Bölüm 1: Büyük Uyanış — Mimar Olarak İlk Gün (Parça 01 – 04)**
   * Kod yazmanın yetmediği an, CV odaklı geliştirmeden kaçış, ödünleşme sanatı ve ADR tutma disiplini.
2. **Bölüm 2: Planlar ve Sınırlar — Karmaşıklığı Parçalara Ayırmak (Parça 05 – 08)**
   * Modüler monolit vs mikroservisler, insan dilinde DDD (Bounded Context), bağlaşıklık/uyum ve API sözleşmeleri.
3. **Bölüm 3: Veri Mimarisi — Durumun Yaşadığı, Öldüğü ve Yalan Söylediği Yer (Parça 09 – 12)**
   * Çoklu veri kalıcılığı (Polyglot persistence), indeksleme, parçalama (sharding), ACID vs BASE ve önbellek faciaları.
4. **Bölüm 4: Asenkron Ufuklar — Olay Odaklı Mimari (Parça 13 – 16)**
   * Kuyruklar ve akışlar, Kafka partition mekaniği, Saga telafi işlemleri ve Event Sourcing / CQRS.
5. **Bölüm 5: Ölçeklenebilirlik ve Esneklik — İzdihamı Yönetmek (Parça 17 – 20)**
   * Durumsuz 12-Faktör uygulamalar, Layer 4/7 yük dengeleme, CDN ve uç bilgi işlem (Edge), Hız sınırlama (Rate Limiting).
6. **Bölüm 6: Güvenilirlik ve Hata Toleransı — Çöküş İçin Tasarlamak (Parça 21 – 24)**
   * 'Her şey her an çöker' felsefesi, Circuit Breaker, Kaos Mühendisliği (Chaos Monkey) ve sıfır kesintili dağıtımlar.
7. **Bölüm 7: Güvenlik ve Sıfır Güven — Krallığı Savunmak (Parça 25 – 28)**
   * Sıfır Güven (Zero Trust) ve mTLS, OAuth2/OIDC yetkilendirme (RBAC/ABAC), gizli anahtar kasaları ve STRIDE tehdit modellemesi.
8. **Bölüm 8: Gözlemlenebilirlik ve Operasyonel Mükemmellik — Karanlıkta Görmek (Parça 29 – 32)**
   * OpenTelemetry (Metrik, Log, Trace), Google SRE SLO ve Hata Bütçeleri, FinOps bulut ekonomisi ve suçlamasız post-mortem.
9. **Bölüm 9: İnsan Mimarisi — Yetki Olmadan Liderlik Etmek (Parça 33 – 36)**
   * Conway Yasası ve Ekip Topolojileri, teknik borcu kaldıraç gibi yönetmek, C-Level ikna sanatı ve yeni mimarlar yetiştirmek.
10. **Bölüm 10: Modern Ufuklar — Yapay Zeka Çağında Mimarlık ve Kurumsal Ustalık (Parça 37 – 40)**
    * Kurumsal GenAI ve RAG mimarisi, gezegensel dağıtık mutabakat (Raft/Spanner), dinozor monolitleri boğma kalıbı ve zamansız bilgelik.

---

## 🛠️ Yeniden Derleme Komutları (Recompilation)

Herhangi bir metin, stil veya bölüm değişikliği yaptığınızda:

- **Türkçe Sürümü (40 PDF + Birleşik Kitap PDF) Yeniden Derlemek İçin:**
  ```bash
  python3 scripts/build_turkish.py
  ```
- **İngilizce Sürümü (40 PDF + Master Book PDF) Yeniden Derlemek İçin:**
  ```bash
  python3 scripts/build_all.py
  ```
