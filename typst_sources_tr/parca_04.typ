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
  part-num: 4,
  section-title: "Bölüm 1: Büyük Uyanış — Mimar Olarak İlk Gün",
  title: "Mimarın Not Defteri: Kararları ADR ile Belgelemek (Herkes Unutmadan Önce)",
  subtitle: "Hafif siklet Mimari Karar Kayıtları (ADR) kurumsal hafıza kaybını ve bitmek bilmeyen toplantıları nasıl engeller?",
  reading-time: "8 dk"
)

#war-story(
  title: "SAHADAN YAŞANMIŞ KRİZ HİKAYESİ",
  [Bir sağlık teknolojisi şirketine yeni katılan kıdemli mimar, kod incelemesi yaparken her sorguyu yakalayıp veriyi hem Redis'te hem Memcached'de tutan tuhaf bir önbellek katmanı gördü. Ekip toplantısında güldü: 'Bunu hangi akılsız yazdı? Tam bir spagetti!' Odadaki herkes sustu. Başkan Yardımcısı gözlerini dikti: 'Üç yıl önce Sandy Kasırgası sırasında ana sağlayıcımız 4 gün kapandı. Eyalet yasalarına göre hasta kabulünü 1 dakika bile durdurursak lisansımız iptal ediliyordu. O çift katmanlı önbellek şirketi iflastan ve cezadan kurtardı.' Mimar yerin dibine geçti. Kimse o kararın neden alındığını yazmamıştı. İki ay sonra başka biri o kodu 'temizledi' ve ilk bölgesel internet kesintisinde şirket milyonlarca liralık ceza yedi.]
)

== Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa
Kaynak kod size sistemin *nasıl* çalıştığını söyler; ama *neden* öyle yapıldığını asla söylemez. Kod yazıldıktan 6 ay sonra o günkü piyasa baskıları, yasal zorunluluklar ve elenen alternatifler insan hafızasından silinir. Mimari Karar Kayıtları (ADR - Architecture Decision Records) olmadan ekipler 'Chesterton'ın Çiti' sendromuna yakalanır: Neden dikildiğini anlamadan çiti yıkarlar ve çitin engellediği boğalar tarafından ezilirler.

== Temel Mimari İlkeler ve Zihinsel Modeller
=== Bir ADR Belgesinin Anatomisi (Michael Nygard Standardı)
Standart bir ADR, git deposunda saklanan basit bir Markdown dosyasıdır (`/docs/adr/0004-postgresql-secimi.md`):
+ *Başlık ve Durum:* ADR-0014: SQS ile Asenkron Sipariş İşleme (Önerildi / Kabul Edildi / İptal Edildi)
+ *Bağlam (Context):* Hangi iş ihtiyacı veya teknik kısıt bizi bu karara zorladı?
+ *Karar (Decision):* Net olarak ne yapmayı seçtik?
+ *Elenen Alternatifler:* Hangi seçenekleri neden eledik?
+ *Sonuçlar (Consequences):* Kabul edilen olumlu ve olumsuz bedeller.

=== Bürokrasi Değil, Yaşayan Tarih
Bir ADR yazmak en fazla 15-20 dakika sürmelidir. Eğer bir vize başvurusu formuna dönerse mühendisler yazmayı bırakır. ADR'ları kodun hemen yanında tutun ki pull request'lerle birlikte yaşasın.

== Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar
- *Gizli Meclis Kararları:* Mimari kararları gizli Slack DM'lerinde alıp ekibe gerekçesiz ferman gibi duyurmak.
- *Confluence Mezarlığı:* Kararları kimsenin aramadığı ve güncellemediği tozlu wiki sayfalarına gömmek.
- *Sonsuz Taslak:* Bir ADR'ı 'Önerildi' statüsünde 6 ay bekleterek önemsiz ayrıntılar yüzünden felç olmak.

#architect-playbook(
  title: "MİMARIN EYLEM PLANI: BU HAFTAKİ SOMUT ADIMLAR",
  [
    - *1. Adım:* Bugün ana git deponda bir `/docs/adr` klasörü aç ve içine örnek bir şablon koy.
    - *2. Adım:* Bir PR veya toplantıda tartışma 30 dakikayı aştığında tartışmayı durdur: 'Bunu 1 sayfalık bir ADR taslağına dökelim ve artıları-eksileri yazalım.'
    - *3. Adım:* Şirkete yeni başlayan her mühendisin ilk hafta okuması gereken ilk belgenin son 10 ADR olmasını sağla.
  ]
)

== Mimari Çıkarımlar ve Hile Tablosu
- Yazıya dökülmemiş bir mimari karar gerçekte var olmamıştır; sadece kulaktan kulağa yayılan bir dedikodudur.
- Elenen alternatifleri kaydetmek, aynı konunun seneye tekrar 4 saat tartışılmasını engeller.
- Neden orada olduğunu bilmediğin hiçbir mimari çiti yıkma.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM TARTIŞMA VE ÖDEV SORUSU",
  [
    *Ders Değerlendirmesi ve Ödev:* Ekibinin son dönemde aldığı önemli bir teknik kararı seç (kütüphane, veritabanı veya bulut servisi). Bunun için 1 sayfalık bir ADR yaz; özellikle elenen alternatifleri belirt.
  ]
)