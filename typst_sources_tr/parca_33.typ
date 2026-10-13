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
  part-num: 33,
  section-title: "Bölüm 9: İnsan Mimarisi — Yetki Olmadan Liderlik Etmek",
  title: "Conway Yasası ve Ekip Topolojileri (Team Topologies): Ekipleri Mimariyi Yansıtacak Şekilde Yapılandırmak",
  subtitle: "Sistem mimarinizin neden kaçınılmaz olarak şirketinizin iletişim şemasını kopyalayacağı gerçeği.",
  reading-time: "9 dk"
)

#war-story(
  title: "SAHADAN YAŞANMIŞ KRİZ HİKAYESİ",
  [Bir fintech şirketinin 60 mühendisi fonksiyonel kulelere bölünmüştü: Veritabanı Ekibi (DBA'ler), Backend Ekibi, Frontend Ekibi ve Altyapı Ekibi. Ürün ekibi 'Kripto Para Alım-Satımı' özelliğini duyurmak istedi. Özelliği çıkarmak için Frontend ekibinin Backend ekibine bilet açması gerekti. Backend ekibi, Veritabanı ekibi tabloları açana kadar koda başlayamadı. Veritabanı ekibi ise 6 hafta doluydu! Tablolar açıldıktan sonra Backend işi bitirdi, bu kez Altyapı ekibinin sunucu açacak vakti yoktu. Gerçekte 2 haftalık bir kodlama işi şirkette tam 9 ay sürdü! Şirket, 4 ayrı yönetim silosunu birebir yansıtan 4 katmanlı hantal bir mimari üretmişti.]
)

== Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa
1967 yılında Melvin Conway ölümsüz bir sosyo-teknik yasa keşfetti: *'Sistem tasarlayan organizasyonlar, kaçınılmaz olarak kendi iletişim yapılarının bir kopyası olan tasarımlar üretmeye mahkumdur.'* Dört derleyici ekibiniz varsa, 4 geçişli bir derleyiciniz olur. İzole bir güvenlik ekibiniz varsa, sisteminize sonradan yamanmış güvenlik kontrolleriniz olur. Ekip iletişim sınırlarını değiştirmeden yazılım mimarisini değiştiremezsiniz. Usta mimarlar *Ters Conway Manevrası (Inverse Conway Maneuver)* yapar: İstenen hedef mimariyi çizerler, ardından organizasyon şemasını o mimariyi yansıtacak şekilde yeniden dizerler.

== Temel Mimari İlkeler ve Zihinsel Modeller
=== Ekip Topolojileri Çerçevesi (Team Topologies)
- *Akışa Hizalanmış Ekipler (Stream-Aligned):* Uçtan uca bir iş değerine odaklanmış çapraz fonksiyonel ekipler (Ürün, Tasarım, Ön Yüz, Arka Yüz tek ekipte; Örn: 'Ödeme Ekibi', 'Arama Ekibi').
- *Platform Ekipleri:* Diğer ekipler bilet açmadan kendi kendine dağıtım yapabilsin diye dahili araçlar (CI/CD, Kubernetes) sunan altyapı ekibi.
- *Yetkinleştirici Ekipler (Enabling):* Yeni teknolojileri (AI, güvenlik) takımlara öğretip ayrılan gezici koçlar.
- *Karmaşık Alt Sistem Ekipleri:* Özel matematik, video codec veya 3D motor yazan nadir uzmanlar.

=== Zihinsel Yük (Cognitive Load) Bir Mimari Kısıttır
Her ekibin sınırlı bir zihinsel kapasitesi vardır. Tek bir takıma 3 bulut sağlayıcısında 14 mikroservis ve 4 farklı dil verirseniz, zihinsel tükenmişlik kaliteyi yerle bir eder. Mimari, ekipleri zihinsel iflastan korumalıdır.

== Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar
- *Fonksiyonel Silo Tuzağı:* Ekipleri teknoloji katmanına göre (Frontendciler, Backendciler, DBAlar) ayırıp her özellikte devasa el değiştirme gecikmeleri yaşamak.
- *Bilet Alan Platform Ekibi:* Yeni bir veritabanı açmak veya pod deploy etmek için Jira bileti doldurulmasını şart koşan bürokratik altyapı ekipleri.
- *Yetim Servisler:* İki yıl önce dağıtılmış bir ekibin yazdığı, prodüksiyonda çalışan ama kimsenin nasıl derlendiğini bilmediği sahipsiz servisler.

#architect-playbook(
  title: "MİMARIN EYLEM PLANI: BU HAFTAKİ SOMUT ADIMLAR",
  [
    - *1. Adım:* Mevcut organizasyon şemanı al ve mimari diyagramının yanına koy: İletişim sınırlarının mimari sınırlarla nerede kavga ettiğini gör.
    - *2. Adım:* Fonksiyonel kulelerden, kendi başına bağımsız canlıya çıkabilen çapraz fonksiyonel Akış Ekiplerine geçişi planla.
    - *3. Adım:* Platform ekibine hedef koy: Başarısı, diğer ekiplerin kendileriyle hiç konuşmadan ne kadar hızlı canlıya çıkabildiğiyle ölçülecektir.
  ]
)

== Mimari Çıkarımlar ve Hile Tablosu
- Conway Yasasından kaçamazsınız: Yazılım mimariniz her zaman şirketinizin organizasyon şemasını kopyalar.
- Ters Conway Manevrası uygulayın: Ekiplerinizi hedeflediğiniz yazılım mimarisine göre dizin.
- Platform ekibinin başarısı diğer ekiplere hizmet bileti kesmekle değil, self-servis araçlar sunmakla ölçülür.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM TARTIŞMA VE ÖDEV SORUSU",
  [
    *Ders Değerlendirmesi ve Ödev:* Şirketinizin organizasyon şemasını bir kağıda, sisteminizin mimarisini diğer kağıda çizin. Hangi ekip sınırları kodun canlıya çıkışında en büyük sürtüşmeyi ve gecikmeyi yaratıyor?
  ]
)