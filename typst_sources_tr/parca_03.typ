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
  part-num: 3,
  section-title: "Bölüm 1: Büyük Uyanış — Mimar Olarak İlk Gün",
  title: "Ödünleşme (Trade-off) Sanatı: Çözüm Yoktur, Yalnızca Tavizler Vardır",
  subtitle: "İki boyutlu siyah-beyaz dogmalardan çok boyutlu sonuç odaklı düşünmeye geçiş.",
  reading-time: "9 dk"
)

#war-story(
  title: "SAHADAN YAŞANMIŞ KRİZ HİKAYESİ",
  [Bir fintech şirketinde hisse senedi alım satımlarında iyimser (optimistic) mi yoksa kötümser (pessimistic) veritabanı kilitlemesi mi kullanılması gerektiği konusunda haftalarca süren kavgalar yaşandı. Bir taraf 'Asla çifte satışa izin veremeyiz!' diye bağırıyor, diğer taraf 'Yüksek yük altında kilitler sistemi felç eder!' diye diretiyordu. Toplantıya katılan Baş Mimar tahtaya yürüdü ve sadece iki sütun çizdi: 'Ne kazanıyoruz?' ve 'Bedeli ne?'. Verileri gösterdi: Şirketin saniyedeki işlem sayısı en yoğun anda bile 200'ü geçmiyordu; yani basit bir yeniden deneme (retry) döngüsüyle iyimser kilitleme %99.98 vakayı sıfır kilit maliyetiyle çözüyordu. Oda bir anda sessizleşti. Mesele doğru ya da yanlış değildi; kabul edilebilir ödünleşmenin ne olduğu meselesiydi.]
)

== Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa
Ekonomist Thomas Sowell'in dediği gibi: 'Çözüm diye bir şey yoktur; yalnızca ödünleşmeler (trade-offs) vardır.' Yazılım mimarisinde koşulsuz şartsız 'harika' olan tek bir tasarım deseni dahi yoktur. Her mimari karar bir ipotek sözleşmesidir: Size anında bir yetenek (hız, esneklik, bağımsızlık) kazandırır; karşılığında düzenli bir faiz (karmaşıklık, ağ gecikmesi, veri tutarlılığı zorluğu) tahsil eder. Mimarın süper gücü, sözleşme imzalanmadan önce ödenecek bedeli masaya yatırmaktır.

== Temel Mimari İlkeler ve Zihinsel Modeller
=== Mimari Ödünleşme Matrisi
İki mimari yönü kıyaslarken (Örn: Senkron REST vs. Asenkron Olaylar), şu 5 boyutta puanla:
+ *Karmaşıklık:* Ortalama bir geliştiricinin üzerindeki zihinsel yük.
+ *Performans ve Gecikme:* P99 yanıt süreleri ve ağ seyahatleri.
+ *Güvenilirlik ve Hata Modları:* Ara bir servis çöktüğünde ne oluyor?
+ *Operasyonel Maliyet:* Bulut faturası, loglama ve izleme giderleri.
+ *Geri Döndürülebilirlik:* Bu karar yanlış çıkarsa geriye dönmek ne kadar sürer?

=== Birinci Derece vs. İkinci Derece Düşünme
- *1. Derece Düşünme:* 'Monoliti 15 mikroservise bölersek her ekip bağımsız dağıtım yapabilir!' (Hızlı ve heyecanlı).
- *2. Derece Düşünme:* 'Artık dağıtık izleme, mTLS, Kafka şemaları, circuit breaker'lar ve çalışması 4 saat süren uçtan uca entegrasyon testlerine ihtiyacımız olacak.' (Olgun ve gerçekçi).

== Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar
- *Dini Taassup:* Mimari kalıpları (Clean Architecture, Mikroservisler, TDD vb.) sorgulanamaz kutsal metinler gibi savunmak.
- *Bedava Öğle Yemeği Yanılsaması:* 'Sıfır operasyonel karmaşıklıkla sonsuz ölçek' vaat eden bir bulut aracına veya kütüphaneye körü körüne inanmak.
- *Kör Optimizasyon:* Sisteme 200 saatlik dağıtık kilit karmaşıklığı ekleyerek dahili bir servisten sadece 3 milisaniye kazanmaya çalışmak.

#architect-playbook(
  title: "MİMARIN EYLEM PLANI: BU HAFTAKİ SOMUT ADIMLAR",
  [
    - *1. Adım:* Sözlüğünden 'En iyi pratik (Best Practice)' ifadesini çıkar; yerine 'Bu bağlam için en uygun pratik' de.
    - *2. Adım:* Bir sonraki teknik teklifinde, savunduğun tercihin en az 3 dezavantajını açıkça listele.
    - *3. Adım:* Biri sana 'Bu çözümün hiçbir dezavantajı yok' dediğinde, dezavantajlarını bulana kadar o çözümü onaylama.
  ]
)

== Mimari Çıkarımlar ve Hile Tablosu
- Mimarisinin hiçbir eksiği olmadığını söyleyen biri ya yalan söylüyordur ya da henüz o kodu canlıya almamıştır.
- İyi mimarlık her metriği maksimize etmek değil; hangi metriklerden feragat edeceğini akıllıca seçmektir.
- İkinci derece sonuçları görebilmek, acemi mimarla usta mimarı ayıran en temel farktır.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM TARTIŞMA VE ÖDEV SORUSU",
  [
    *Ders Değerlendirmesi ve Ödev:* Çok sevdiğin bir mimari deseni seç (Örn: Event Sourcing, GraphQL veya Mikroservisler). Bu deseni seçmenin bir şirket için tam bir felaket olacağı 3 somut senaryo yaz.
  ]
)