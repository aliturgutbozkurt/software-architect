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
  part-num: 38,
  section-title: "Bölüm 10: Modern Ufuklar — Yapay Zeka Çağında Mimarlık ve Kurumsal Ustalık",
  title: "Dağıtık Mutabakat (Consensus) ve Gezegensel Ölçek",
  subtitle: "Doktora tezi okumadan Paxos, Raft, CockroachDB ve Google Spanner mimarisini anlamak.",
  reading-time: "9 dk"
)

#war-story(
  title: "SAHADAN YAŞANMIŞ KRİZ HİKAYESİ",
  [Global bir oyun şirketi New York, Londra ve Tokyo veri merkezlerinde çalışan çevrim içi bir açık artırma sistemi kurdu. Hız kazanmak adına her bölgede bağımsız bir veritabanı çalıştırıldı ve bunlar arka planda asenkron eşitlendi. Londra'daki bir oyuncu efsanevi bir büyü kılıcını 50.000 altın bedelle satışa koydu. Tam o milisaniyede bir köpekbalığı Atlantik altındaki fiber optik kabloyu ısırdı ve 12 dakikalık bir ağ bölünmesi yaşandı. New York'taki bir oyuncu kılıcı 50.000 altına satın aldı. Aynı saniyede Tokyo'daki başka bir oyuncu da aynı kılıcı 50.000 altına satın aldı! Ağ düzeldiğinde iki oyuncuda da aynı kılıç vardı ve satıcının hesabına 100.000 altın geçmişti! Oyunun ekonomisi bir haftada hiperenflasyonla çöktü.]
)

== Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa
Mimariniz kıtalar arasına yayıldığında, ışık hızı ve ağ bölünmeleri geleneksel tek liderli veritabanlarını imkansız kılar. Dünyanın farklı köşelerindeki bağımsız sunucular, tek bir merkezi hata noktası olmadan işlemlerin sırası üzerinde nasıl anlaşır? Cevap *Dağıtık Mutabakat Algoritmaları*'dır: Paxos ve Raft. Modern NewSQL sistemleri (Google Spanner, CockroachDB) çoğunluk oylaması (Quorum) ve atomik saatlerle küresel boyutta ACID işlemlerinin mümkün olduğunu kanıtlamıştır.

== Temel Mimari İlkeler ve Zihinsel Modeller
=== Raft Mutabakat Algoritması (İnsan Dilinde Paxos)
Raft mutabakatı 3 alt probleme böler:
+ *Lider Seçimi:* Lider kalp atışı göndermeyi keserse takipçiler seçim başlatır. Adayın lider olması için *Çoğunluk Oyunu (Quorum: \$N/2 + 1\$)* alması şarttır.
+ *Günlük Çoğaltma:* Lider isteği alır, günlüğüne yazar ve takipçilere çoğaltır. İşlem ancak çoğunluk onayladığında kalıcı (committed) sayılır.
+ *Güvenlik:* Bir sunucu belirli bir indekste işlemi onayladıysa, başka hiçbir sunucu o indekste farklı bir işlem onaylayamaz.

=== Google Spanner ve TrueTime
Google Spanner yavaş iki aşamalı kilitleme yapmadan küresel tutarlılığı, veri merkezlerindeki atomik saatler ve GPS alıcılarıyla zaman belirsizliğini 7 milisaniyenin altına indirerek (TrueTime API) çözer. CockroachDB ise bunu Hibrit Mantıksal Saatlerle (HLC) başarır.

== Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar
- *Bölünmüş Beyin (Split-Brain) Felaketi:* Mutabakat kümesini çift sayıda (2 veya 4 düğüm) kurmak; ağ koptuğunda iki tarafın da çoğunluk sağlayamaması veya iki tarafın da kendini lider sanıp çakışan veri yazması.
- *Kendi Mutabakatını Yazmak:* Kendi lider seçimi algoritmasını yazmaya kalkışmak ('Dünyada sadece iki mutabakat algoritması vardır: Paxos ve bozuk olanlar').
- *Geniş Alan Ağı (WAN) Gecikmesini Unutmak:* Kıtalararası dağıtık mutabakatın 10 milisaniyede dönmesini bekleyerek ışık hızına meydan okumak.

#architect-playbook(
  title: "MİMARIN EYLEM PLANI: BU HAFTAKİ SOMUT ADIMLAR",
  [
    - *1. Adım:* Mutabakat kümelerini daima TEK SAYIDA (3, 5 veya 7 düğüm) kur ki kesin çoğunluk garantilensin.
    - *2. Adım:* Dağıtık kilitler ve lider seçimi için etcd, Consul veya ZooKeeper gibi kanıtlanmış sistemleri kullan.
    - *3. Adım:* Çok bölgeli sistemlerde yazmaları kullanıcının kendi bölgesine yerelleştir; uzak bölgelere asenkron okuma kopyaları dağıt.
  ]
)

== Mimari Çıkarımlar ve Hile Tablosu
- Mutabakat algoritmaları kesin çoğunluk için daima tek sayıda düğüm gerektirir.
- Asla kendi dağıtık mutabakat algoritmanızı yazmayın; Raft ve etcd gibi devlere güvenin.
- Küresel tutarlılık daima ışık hızı gecikme vergisini tahsil eder.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM TARTIŞMA VE ÖDEV SORUSU",
  [
    *Ders Değerlendirmesi ve Ödev:* Ana bulut bölgenizde yarın tam bir bölgesel elektrik kesintisi yaşansa sisteminiz yeni bir lideri otomatik olarak seçebilir mi? Devir otomatik mi yoksa manuel DNS müdahalesi mi gerekiyor?
  ]
)