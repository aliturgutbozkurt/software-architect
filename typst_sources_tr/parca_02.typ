#import "/templates/book_style_tr.typ": *

#set page(
  paper: "a4",
  margin: (top: 2.2cm, bottom: 2.2cm, left: 2.2cm, right: 2.2cm),
  header: align(right)[#text(size: 8pt, fill: rgb("#94a3b8"))[Bir Yazılım Mimarı Gibi Düşünmek • Masterclass]],
  footer: [
    #align(center)[
      #context text(size: 8.5pt, fill: rgb("#64748b"))[
        Sayfa #counter(page).display("1 / 1", both: true)
      ]
    ]
  ]
)
#set text(font: ("Avenir", "Helvetica Neue", "Arial"), size: 10pt, fill: rgb("#0f172a"))
#set par(justify: true, leading: 0.72em)

#chapter-header(
  part-num: 2,
  section-title: "Bölüm 1: Büyük Uyanış — Mimar Olarak İlk Gün",
  title: "CV Odaklı Geliştirmeden (RDD) Kaçış: Sıkıcılık vs. İş Gerçekleri",
  subtitle: "45 kullanıcılı şirket içi bir admin panelinin neden Rust, Kafka ve CockroachDB kümesine ihtiyacı yoktur?",
  reading-time: "8 dk"
)

#war-story(
  title: "SAHADAN YAŞANMIŞ KRİZ HİKAYESİ",
  [Hızla büyüyen bir e-ticaret girişiminde, müşteri temsilcilerinin iade işlemlerini onayladığı 45 kişilik dahili bir portal vardı. Ekibin yeni lideri, Big Tech mülakatlarında havalı görünmek adına bu basit CRUD panelini Apache Kafka, Rust mikro-servisleri ve CockroachDB dağıtık veritabanı kullanarak 'olaya dayalı (event-driven)' mimariye geçirmeye ikna etti. Altı ay sonra bir ağ gecikmesi sırasında Kafka consumer offset'leri kilitlendi. Basit bir 100 TL'lik iade işlemi 48 dakika sürmeye başladı. Üstelik Rust bellek yönetimini anlayan tek geliştirici istifa edip bir kripto şirketine geçmişti! Sistem çöktü ve tüm panel iki haftasonunda basit bir Django uygulamasıyla sıfırdan yeniden yazılmak zorunda kaldı.]
)

== Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa
CV Odaklı Geliştirme (Resume-Driven Development - RDD), teknoloji şirketlerinin gizli katilidir. Deneyimsiz yazılımcılar zekalarını ve yetkinliklerini kanıtlamak için en karmaşık araçları seçer; bilge mimarlar ise bilgeliklerini kanıtlamak için en sade ve sıkıcı araçları seçer. Dan McKinley'in altın kuralı: 'Sıkıcı Teknolojiyi Seçin (Choose Boring Technology).' Bir şirketin harcayabileceği yalnızca 3 'İnovasyon Jetonu' vardır. O jetonları şirketinizi rakiplerinizden ayıran temel iş mantığına harcayın; oturum çerezlerini nasıl sakladığınıza değil.

== Temel Mimari İlkeler ve Zihinsel Modeller
=== İnovasyon Jetonu Bütçesi (Dan McKinley)
Her şirketin sınırlı bir operasyonel risk bütçesi vardır. Alışılmadık bir veritabanı seçtiğinde bir jeton harcarsın. Yeni ve popüler bir dil seçtiğinde bir jeton daha gider. Tüm jetonlarını altyapı borularına harcarsan, şirkete para kazandıracak yenilikçi özellikleri üretmeye sıfır jetonun kalır.

=== Toplam Sahip Olma Maliyeti (TCO)
Teknolojinin maliyeti asla lisans bedeli değildir. Asıl maliyet; gecenin 3'ünde çalan çağrı cihazları, o dilde mühendis bulma zorluğu ve yıllarca süren versiyon yükseltme sancılarıdır. Dünyada 50.000 mühendisin uzman olduğu sıkıcı bir PostgreSQL, GitHub'da üç akademisyenin geliştirdiği egzotik bir dağıtık graf veritabanından fersah fersah daha ucuzdur.

== Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar
- *LinkedIn İstifçisi:* Kararları salt Netflix veya Google'ın iş ilanlarında çok geçiyor diye alan mühendis.
- *Erken Gezegensel Ölçekleyici:* Henüz 300 aktif kullanıcısı varken sistemi 500 milyon eşzamanlı kullanıcı kaldıracak şekilde tasarlayan mimar.
- *Burada Üretilmedi (NIH) Sendromu:* Redis'in 'fazla hantal' olduğunu iddia edip şirket içinde kendi bellek içi önbellek motorunu yazmaya kalkanlar.

#architect-playbook(
  title: "MİMARIN EYLEM PLANI: BU HAFTAKİ SOMUT ADIMLAR",
  [
    - *1. Adım:* Canlı ortamındaki farklı programlama dillerini ve veritabanı türlerini listele. Sayı 4'ü aşıyorsa tehlike çanları çalıyor demektir.
    - *2. Adım:* Önerilen her yeni havalı teknolojiye 'Sıkıcı Teknoloji Testi' uygula: 'Bunu standart PostgreSQL ve basit kuyruklarla çözseydik ne kaybederdik?'
    - *3. Adım:* İşe alım hızını hesapla: Bu teknolojiyi yazan kıdemli yarın ayrılsa, yerine birini bulup adapte etmek kaç ay sürer?
  ]
)

== Mimari Çıkarımlar ve Hile Tablosu
- Usta bir mimarın alameti farikası, karmaşık problemleri basitleştirmesidir; basit problemleri karmaşıklaştırması değil.
- Sıkıcı teknoloji geceleri huzurla uyumanı sağlar; havalı teknoloji seni geceleri ücretsiz test kullanıcısına çevirir.
- Müşterinin tek ihtiyacı sağlam ahşap bir bank iken, üzerine dağıtık uzay istasyonu kurma.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM TARTIŞMA VE ÖDEV SORUSU",
  [
    *Ders Değerlendirmesi ve Ödev:* Şirketinizin mevcut teknoloji yığınına bakın. Sırf heyecan veya trend olduğu için seçilmiş ama operasyonel yük getiren bir araç var mı? Bugün olsa neyi seçerdiniz?
  ]
)