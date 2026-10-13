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
  part-num: 30,
  section-title: "Bölüm 8: Gözlemlenebilirlik ve Operasyonel Mükemmellik — Karanlıkta Görmek",
  title: "Hizmet Seviyesi Hedefleri: SLA, SLO ve Hata Bütçesi (Error Budget)",
  subtitle: "Google SRE ilkeleri Ürün ve Mühendislik arasındaki ezeli savaşı nasıl matematiksel bir uyuma dönüştürür?",
  reading-time: "9 dk"
)

#war-story(
  title: "SAHADAN YAŞANMIŞ KRİZ HİKAYESİ",
  [Bir SaaS şirketinde Ürün Yönetimi ile Mühendislik savaştaydı. Ürün Yöneticisi büyük bir müşteriyi bağlamak için bu ay 10 yeni özellik çıkarmak istiyordu. Mühendislik Direktörü ise 'Sistem çökmek üzere' diyerek tüm geliştirmeleri 3 ay durdurup veritabanını yeniden yazmak istiyordu. Sprint planlama toplantıları bağırış çağırışla geçiyordu. CEO toplantıda 'Sistemimiz yeterince kararlı mı?' diye sordu. Ürün 'Evet, süper!', Mühendislik ise 'Hayır, felaket!' dedi. İkisinin de elinde somut bir matematik olmadığı için şirket aylarca siyasi bir kilitlenme yaşadı.]
)

== Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa
'%100 kesintisizlik' istemek amatörce bir fantezidir. %100 güvenilirlik imkansızdır ve bunu kovalamak sonsuz bütçe gerektirirken özellik geliştirme hızını sıfıra indirir. Google Site Reliability Engineering (SRE) çerçevesi bu gerilimi matematikle çözer: *SLI (Göstergeler)*, *SLO (Hedefler)* ve *Hata Bütçesi (Error Budget)*. Hata bütçesi, kesintiyi inovasyon için harcanabilecek planlı bir kaynağa dönüştürür.

== Temel Mimari İlkeler ve Zihinsel Modeller
=== SRE Kutsal Üçlüsü
- *SLI (Service Level Indicator):* Ölçülen gerçek başarı oranı: `Başarılı İstekler / Toplam İstekler * 100%`.
- *SLO (Service Level Objective):* Ekip içi hedef: `30 günlük periyotta isteklerin %99.9'u SLI'ı karşılamalıdır`.
- *SLA (Service Level Agreement):* Müşteriye verilen ve cezai yaptırımı olan yasal sözleşme (Genellikle SLO'dan daha gevşektir, örn: %99.5).

=== Hata Bütçesi Denklemi
SLO'nuz %99.9 ise, aylık hata bütçeniz %0.1'dir (bu da ayda *tam 43.2 dakika kabul edilebilir kesinti veya bozulma* demektir). Eğer ay ortasında bütçeniz duruyorsa Ürün ekibi hızla riskli yenilikler deneyebilir! Ancak bütçe sıfırlandıysa tüm yeni özellik dağıtımları donar ve tüm kapasite stabiliteye ayrılır.

== Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar
- *Dört Dokuz Serabı:* Altyapınız ve bulut sağlayıcınız yalnızca %99.9 sunarken müşteriye sözleşmede %99.99 (ayda 4 dakika kesinti) taahhüt etmek.
- *Kibirli Göstergeler:* Kullanıcı deneyimi yerine sunucu CPU'sunu SLI olarak tanımlamak.
- *Dişsiz Hata Bütçesi:* Hata bütçesi %300 aşılmasına rağmen yönetimin kuralları çiğneyip riskli kodları zorla canlıya aldırması.

#architect-playbook(
  title: "MİMARIN EYLEM PLANI: BU HAFTAKİ SOMUT ADIMLAR",
  [
    - *1. Adım:* Temel kullanıcı akışınız için 1-2 kullanıcı odaklı SLI tanımla (Ödeme Başarı Oranı, Arama \< 300ms).
    - *2. Adım:* Ürün Yöneticisiyle oturup bir SLO belirle (%99.9 gibi) ve aylık izin verilen kesinti dakikanızı hesaplayın.
    - *3. Adım:* Net bir Hata Bütçesi Politikası yaz: Bütçe biterse güvenilirlik dışındaki tüm yeni özellik geliştirmeleri durur.
  ]
)

== Mimari Çıkarımlar ve Hile Tablosu
- %100 erişilebilirlik yanlış hedeftir; yeniliği durdurur ve sermayeyi yakar.
- SLO'lar Ürün ve Mühendislik arasındaki duygusal tartışmaları nesnel verilere dönüştürür.
- Hata Bütçesi mühendisliğe teknik borcu temizlemesi için meşru ve sorgulanamaz bir yetki verir.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM TARTIŞMA VE ÖDEV SORUSU",
  [
    *Ders Değerlendirmesi ve Ödev:* Ana servisinizin SLO hedefi nedir? Yoksa, 30 günlük bir sürede isteklerin yüzde kaçının başarısız olması müşterilerinizi gerçekten çıldırtır?
  ]
)