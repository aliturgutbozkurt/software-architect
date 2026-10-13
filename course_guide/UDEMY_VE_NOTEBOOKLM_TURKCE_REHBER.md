# Bir Yazılım Mimarı Gibi Düşünmek: Türkçe Udemy & NotebookLM Kurs Yapım Kılavuzu

**Bu 40 Parçalık Başvuru Eserini Sektörün Lideri Video ve Sesli Eğitimine Dönüştürme Rehberi**

---

## 1. Eğitimin Sistem Mimarisi

Bu çalışma alanı, Udemy'de veya şirket içi kurumsal akademilerde premium bir mimarlık eğitimi yayınlamak için gereken her şeyi içerir:

- **40 Modüler Bölüm:** Her biri 8-12 dakikalık video veya sesli dersler için ideal uzunlukta.
- **10 Yapılandırılmış Bölüm:** İlk günden ileri kurumsal ölçeğe ve Generative AI'a uzanan doğal pedagojik akış.
- **NotebookLM'e Hazır Dosyalar:** `chapters_tr/` klasöründe tek tek veya topluca yüklenebilir Markdown formatı.
- **40 İndirilebilir Bağımsız PDF:** `output_tr/individual_pdfs/` klasöründe, her Udemy dersine ek kaynak olarak eklenebilir.
- **Birleşik Tam Kitap PDF'i:** `output_tr/Bir_Yazilim_Mimari_Gibi_Dusunmek_Tam_Rehber.pdf` resmi eğitim ders kitabı olarak hazır.

## 2. NotebookLM ile Ses ve Video Üretim İş Akışı

### Adım A: Kaynakları Yükleme

1. [Google NotebookLM](https://notebooklm.google.com/) adresine gidin.
2. **'Bir Yazılım Mimarı Gibi Düşünmek'** başlıklı yeni bir defter açın.
3. `chapters_tr/` klasöründeki bölümleri deftere yükleyin (bölüm bölüm veya 40 dosyayı birden).

### Adım B: Çift Sunuculu Sesli Podcast (Audio Overview) Üretimi

1. Bir bölüm seçin (Örn: `parca_01_kod_yazmanin_yetmedigi_gun.md`).
2. **'Audio Overview (Deep Dive)'** butonuna tıklayın ve özel istemi (Customize) girin:

```text
Sahada yıllarca pişmiş iki deneyimli yazılım mimarı ve mühendislik lideri olarak enerjik, esprili ve derinlemesine bir Türkçe podcast yürütün. Bölümdeki kriz hikayesini (war story), zihniyet dönüşümünü ve temel mimari ilkeleri tartışın. Acemi yazılımcı hataları ile usta mimar bilgeliğini karşılaştırın. Somut analojiler kullanın, ödünleşmeleri tartışın ve yazılımcılar için uygulanabilir altın tavsiyelerle bitirin.
```

3. Üretilen `.m4a` ses dosyasını indirin.
4. Bu sesi doğrudan **Udemy Podcast Dersi** olarak yükleyebilir veya slaytlarınızın arkasına seslendirme olarak koyabilirsiniz!

### Adım C: Video Slaytları ve Ders Metinleri Çıkarma

NotebookLM sohbetine şu istemi yazın:

```text
Parça [X]'e dayanarak Udemy için 5 slaytlık bir video sunum taslağı hazırla:
Slayt 1: Başlık ve Giriş Kriz Hikayesi (Hook)
Slayt 2: Zihniyet Dönüşümü (Yazılımcı vs Mimar Bakışı)
Slayt 3: Temel Mimari İlkeler ve Modeller
Slayt 4: Kaçınılması Gereken Tehlikeli Tuzaklar (Anti-Patterns)
Slayt 5: Mimarın Haftalık Kontrol Listesi ve Öğrenci Ödevi
Her slayt için konuşmacının söyleyeceği detaylı ders anlatım metnini ekle.
```

### Adım D: Udemy İçin Çoktan Seçmeli Quiz Üretme

NotebookLM'e yazın:

```text
Bu bölümdeki bilgilere dayanarak Udemy öğrencileri için 5 adet zorlayıcı, gerçekçi çoktan seçmeli sınav sorusu üret. Her soru sahada yaşanmış gerçek bir kurumsal mimari senaryoya dayansın, 4 makul şık içersin, doğru cevabı belirtsin ve diğer 3 şıkkın neden tehlikeli acemi tuzakları olduğunu ayrıntılı açıklasın.
```

## 3. 40 Modüllük Tam Türkçe Müfredat Haritası

### Bölüm 1: Büyük Uyanış — Mimar Olarak İlk Gün
*Akıllı algoritmalar yazmaktan; insanlara, ölçeğe ve zamana meydan okuyan dayanıklı sistemler tasarlamaya uzanan zihinsel ve teknik sıçrama.*

- **Modül 01:** Kod Yazmanın Yetmediği Gün: Bir Yazılım Mimarı Aslında Ne Yapar? (8 dk)
- **Modül 02:** CV Odaklı Geliştirmeden (RDD) Kaçış: Sıkıcılık vs. İş Gerçekleri (8 dk)
- **Modül 03:** Ödünleşme (Trade-off) Sanatı: Çözüm Yoktur, Yalnızca Tavizler Vardır (9 dk)
- **Modül 04:** Mimarın Not Defteri: Kararları ADR ile Belgelemek (Herkes Unutmadan Önce) (8 dk)

### Bölüm 2: Planlar ve Sınırlar — Karmaşıklığı Parçalara Ayırmak
*Yazılım sistemlerinin temel geometrisinde ustalaşmak: sınırları çizmek, monolitleri modülerleştirmek, pratik alan odaklı tasarım (DDD) ve bozulmaz API sözleşmeleri üretmek.*

- **Modül 05:** Monolit Geri Dönüyor: Ne Zaman Birleşik Kalmalı, Ne Zaman Bölünmeli? (9 dk)
- **Modül 06:** Akademik Baş Ağrısı Olmadan Domain-Driven Design: İnsan Dilinde Bounded Context (9 dk)
- **Modül 07:** Bağlaşıklık ve Uyum (Coupling vs. Cohesion): Sistemleri Yaşatan veya Öldüren İkiz Güç (8 dk)
- **Modül 08:** Kutsal Bir Sözleşme Olarak API Tasarımı: REST, gRPC ve GraphQL Karşılaştırması (9 dk)

### Bölüm 3: Veri Mimarisi — Durumun Yaşadığı, Öldüğü ve Yalan Söylediği Yer
*İş dünyasının durum temelini tasarlamak: doğru depolama motorlarını seçmek, indeksleme ve kopyalarla darboğazları kırmak, tutarlılık modellerini yönetmek ve önbellek canavarını evcilleştirmek.*

- **Modül 09:** Çoklu Veri Kalıcılığı (Polyglot Persistence): Veriniz İçin Doğru Silahı Seçmek (9 dk)
- **Modül 10:** Veritabanı Darboğazı: İndeksleme, Parçalama (Sharding) ve Okuma Kopyaları (9 dk)
- **Modül 11:** ACID vs. BASE Karşılaşması: Gerçek Dünyada Tutarlılık Modelleri (9 dk)
- **Modül 12:** Önbellekleme Stratejileri: Bilgisayar Biliminin İki Zor Şeyinden Biri (9 dk)

### Bölüm 4: Asenkron Ufuklar — Olay Odaklı Mimari
*Senkron HTTP zincirlerinin prangalarından kurtulmak: olay odaklı sistemler tasarlamak, Kafka mekaniğinde ustalaşmak, dağıtık Saga işlemlerini yönetmek ve Event Sourcing / CQRS dengesini kurmak.*

- **Modül 13:** Senkron Cehennemden Asenkron Huzura: Kuyruklar, Konular ve Akışlar (9 dk)
- **Modül 14:** Gözyaşı Dökmeden Kafka: Bölümler (Partitions), Offsetler ve Tüketici Grupları (9 dk)
- **Modül 15:** Pratikte Eventual Consistency: Saga Kalıbı vs. İki Aşamalı İşleme (2PC) (9 dk)
- **Modül 16:** Event Sourcing ve CQRS: Geçmiş, Şimdiki Zamandan Daha Önemli Olduğunda (9 dk)

### Bölüm 5: Ölçeklenebilirlik ve Esneklik — İzdihamı Yönetmek
*Patlayıcı kullanıcı artışlarına mimari hazırlık: durumsuz on iki faktörlü uygulamalar tasarlamak, Layer 4/7 yük dengeleyiciler ve API ağ geçitleri kurmak, küresel uçta (Edge) önbellekleme yapmak ve hız sınırlama ile sistemi korumak.*

- **Modül 17:** Yatay Ölçekleme: Durumsuzluk (Statelessness) ve 12-Faktör Uygulama (9 dk)
- **Modül 18:** Yük Dengeleme, Ağ Geçitleri ve Tersine Vekil Sunucular (Reverse Proxies) (9 dk)
- **Modül 19:** İçerik Dağıtım Ağları (CDN) ve Uç Nokta Bilişim (Edge Computing) (8 dk)
- **Modül 20:** Hız Sınırlama (Rate Limiting) ve Trafik Şekillendirme: Kalenizi Korumak (9 dk)

### Bölüm 6: Güvenilirlik ve Hata Toleransı — Çöküş İçin Tasarlamak
*Kaosun içinde ayakta kalan sistemler inşa etmek: Werner Vogels'ın hata felsefesi, devre kesiciler ve bölmelerle hasar yarıçapını izole etmek, kaos mühendisliğini silahlandırmak ve kesintisiz dağıtım yapmak.*

- **Modül 21:** Her Şey Her An Çöker: Dayanıklı Mimarın Zihniyeti (9 dk)
- **Modül 22:** Devre Kesiciler (Circuit Breakers), Bölmeler (Bulkheads) ve Üstel Geri Çekilme (Exponential Backoff) (9 dk)
- **Modül 23:** Kaos Mühendisliği (Chaos Engineering): Sistem Sizi Çökertmeden Önce Onu Bilerek Bozmak (9 dk)
- **Modül 24:** Sıfır Kesintili Dağıtımlar: Mavi-Yeşil (Blue-Green), Kanarya (Canary) ve Özellik Bayrakları (Feature Flags) (9 dk)

### Bölüm 7: Güvenlik ve Sıfır Güven — Krallığı Savunmak
*Derinlemesine savunma mimarisi: Sıfır Güven (Zero Trust) ve mTLS ile kale yanılsamalarını yıkmak, RBAC ve ABAC ile dinamik yetkilendirme kurmak, anahtarları korumak ve tedarik zinciri tehditlerini modellemek.*

- **Modül 25:** Sıfır Güven Mimarisi (Zero Trust): Asla Güvenme, Daima Doğrula (9 dk)
- **Modül 26:** Ölçekte Kimlik ve Yetkilendirme: OAuth2, OIDC ve RBAC vs. ABAC (9 dk)
- **Modül 27:** Gizli Anahtar Yönetimi, Şifreleme ve Veri Gizliliği (9 dk)
- **Modül 28:** Tedarik Zinciri Güvenliği ve Tehdit Modellemesi (STRIDE) (9 dk)

### Bölüm 8: Gözlemlenebilirlik ve Operasyonel Mükemmellik — Karanlıkta Görmek
*Kör sistemleri şeffaf cam kutulara dönüştürmek: OpenTelemetry metrikleri, logları ve dağıtık izleri; Google SRE hata bütçeleri; FinOps ile bulut israfını budamak ve suçlamasız post-mortem kültürü.*

- **Modül 29:** Gözlemlenebilirlik Üçlüsü: Metrikler, Loglar ve Dağıtık İzleme (Tracing) (9 dk)
- **Modül 30:** Hizmet Seviyesi Hedefleri: SLA, SLO ve Hata Bütçesi (Error Budget) (9 dk)
- **Modül 31:** FinOps ve Bulut Ekonomisi: Şirketi İflas Ettirmeyen Mimari (9 dk)
- **Modül 32:** Kriz Yönetimi ve Suçlamasız Olay İncelemesi (Blameless Post-Mortem) (9 dk)

### Bölüm 9: İnsan Mimarisi — Yetki Olmadan Liderlik Etmek
*Sistemlerin sosyo-teknik gerçekliğinde ustalaşmak: Conway Yasası'nı Ekip Topolojileriyle lehinize çevirmek, teknik borcu finansal kaldıraç gibi yönetmek, resmi makam gücü olmadan yöneticileri ikna etmek ve yeni mimarlar yetiştirmek.*

- **Modül 33:** Conway Yasası ve Ekip Topolojileri (Team Topologies): Ekipleri Mimariyi Yansıtacak Şekilde Yapılandırmak (9 dk)
- **Modül 34:** Teknik Borç Yönetimi: Ne Zaman Ödemeli, Ne Zaman Refactor Etmeli, Ne Zaman Sıfırdan Yazmalı? (9 dk)
- **Modül 35:** İkna Sanatı: Mimari Vizyonu Mühendis Olmayan Yöneticilere Satmak (9 dk)
- **Modül 36:** Kıdemli Mühendisleri Geleceğin Mimarlarına Dönüştürmek (8 dk)

### Bölüm 10: Modern Ufuklar — Yapay Zeka Çağında Mimarlık ve Kurumsal Ustalık
*Modern teknolojinin en ön cephesini fethetmek: RAG ve vektör depolarıyla üretime hazır Generative AI sistemleri tasarlamak, gezegensel ölçekte dağıtık mutabakatı (Raft/Spanner) yönetmek, dinozor monolitleri boğarak modernize etmek ve zamansız mimari bilgeliği korumak.*

- **Modül 37:** Üretken Yapay Zeka (GenAI) Mimarisi: RAG, Vektör Veritabanları ve Ajanlar (9 dk)
- **Modül 38:** Dağıtık Mutabakat (Consensus) ve Gezegensel Ölçek (9 dk)
- **Modül 39:** Eski Sistemleri Modernleştirme Kitabı: Dinozoru Boğmak (Strangler Fig) (9 dk)
- **Modül 40:** Mimarın Kutup Yıldızı: Bilgelik, Alçakgönüllülük ve Zamansız Zanaat (8 dk)

## 4. Udemy Pazarlama ve Paketleme Tavsiyeleri

- **Kurs Başlığı:** Bir Yazılım Mimarı Gibi Düşünmek: Sıfırdan Uzmanlığa (Gezegensel Ölçek ve Yapay Zeka)
- **Alt Başlık:** Sistem tasarımı, monolit vs mikroservis, dağıtık veritabanları, Kafka, sıfır güven, FinOps, SRE hata bütçeleri ve kurumsal GenAI mimarisi.
- **Kategori:** Geliştirme > Yazılım Mühendisliği / Yazılım Mimarisi
- **Hedef Kitle:** Kıdemli geliştiriciler, teknik liderler, yeni mimarlar ve Staff+ mühendislik liderliğine adım atmak isteyenler.
- **İndirilebilir Materyaller:** Her dersin altına `output_tr/individual_pdfs/` klasöründeki bağımsız PDF'leri ders notu olarak; `output_tr/Bir_Yazilim_Mimari_Gibi_Dusunmek_Tam_Rehber.pdf` dosyasını da ana ders kitabı olarak ekleyin!