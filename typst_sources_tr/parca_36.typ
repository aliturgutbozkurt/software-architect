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
  part-num: 36,
  section-title: "Bölüm 9: İnsan Mimarisi — Yetki Olmadan Liderlik Etmek",
  title: "Kıdemli Mühendisleri Geleceğin Mimarlarına Dönüştürmek",
  subtitle: "Sistem düşüncesini, ödünleşme analizini ve Staff+ mühendislik merdivenini öğreterek etkinizi çarpmak.",
  reading-time: "8 dk"
)

#war-story(
  title: "SAHADAN YAŞANMIŞ KRİZ HİKAYESİ",
  [Efsanevi bir Baş Mimar, 150 mühendislik dev bir organizasyonun tek hata noktasıydı. Her mimari karar, veritabanı şema değişikliği ve kütüphane seçimi onay için onun masasından geçmek zorundaydı. Haftada 70 saat çalışıyor, 35 toplantıya giriyor ve 40 tasarım belgesi inceliyordu. Düğünü için iki haftalık izne çıktığında tüm şirketin geliştirme hızı durdu: 12 ekibin pull request'leri onun imzasını beklediği için kilitlendi. Döndüğünde yorgunluktan bitmişti. Başkan Yardımcısı onu kenara çekti: 'Sen bu şirketin en zeki mühendis hissin ama aynı zamanda en büyük tıkanıklığısın. Senin görevin bütün mimari kararları tek başına almak değil; bu kararları sensiz alabilecek bir mühendis ordusu yetiştirmektir.']
)

== Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa
Bir mimarın büyüklüğü kendi aldığı kararların zekasıyla değil; etrafında mimar gibi düşünebilen kaç mühendis yetiştirdiğiyle ölçülür. Şirkette karmaşık sorunları çözebilen tek kişi sizseniz, dayanıklı bir mimari değil; sadece kendinize bağımlı bir mimari krallık kurmuşsunuz demektir. Gerçek liderlik karar yetkisini devretmek, zihinsel modelleri öğretmek ve Staff+ kariyer merdivenini inşa etmektir.

== Temel Mimari İlkeler ve Zihinsel Modeller
=== Staff+ Mühendisin Dört Rolü (Tanya Reilly)
- *Teknik Lider (Tech Lead):* Bir ekibin veya projenin teknik yürütmesini yönetir.
- *Mimar (Architect):* Çoklu ekipler arasında mimarinin bütünlüğünden ve yönünden sorumludur.
- *Çözücü (Solver):* Organizasyonun en derin, en kilit teknik krizlerine paraşütle inip çözen uzman.
- *Sağ Kol (Right Hand):* CTO veya VP ile ortak çalışarak kurumsal ve teknolojik stratejiyi şekillendiren danışman.

=== Sokratik Yöntemle Sistem Düşüncesi Öğretmek
Kıdemli bir mühendis size 'Redis mi PostgreSQL mi kullanalım?' diye sorduğunda ASLA doğrudan cevabı vermeyin! Sorularla yönlendirin: 'Veriye erişim sıklığımız ne? Veri kaybına tahammülümüz ne? Bu sunucu çökerse ne olur?' Kendi ödünleşme matrislerini kendilerinin çıkarmasını sağlayın.

== Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar
- *Kahraman Kapı Bekçisi:* Şirketteki her teknik tasarım belgesini bizzat onaylamakta diretmek.
- *Bilgi İstifçisi:* Bilgiyi iş güvencesi sayıp kimseyle paylaşmamak ve dokümantasyon yazmamak.
- *Kırıcı İncelemeci:* Tasarım incelemelerinde mühendisleri aşağılayıcı yorumlar bırakıp onları koçluk fırsatından mahrum etmek.

#architect-playbook(
  title: "MİMARIN EYLEM PLANI: BU HAFTAKİ SOMUT ADIMLAR",
  [
    - *1. Adım:* Mimari Çalışma Grubu kur: Kıdemli mühendisleri dönüşümlü olarak bu kurula dahil et ki çapraz kararları değerlendirmeyi öğrensinler.
    - *2. Adım:* Mentorluk yaparken Sokratik sorular sor: Cevabı vermek yerine ödünleşmeleri onların görmesini sağla.
    - *3. Adım:* Gelecek vadeden bir kıdemliyi bir sonraki büyük mimari belgenin eş-yazarı yap ve yönetim sunumunu ona yönettir.
  ]
)

== Mimari Çıkarımlar ve Hile Tablosu
- Bir mimar olarak en kalıcı mirasınız, arkanızda bıraktığınız insanların karar verme kalitesidir.
- Cevap vermeyi bırakın; gizli ödünleşmeleri aydınlatan doğru soruları sormaya başlayın.
- Tatile çıktığınızda mimariniz kilitleniyorsa, bir sistem kurmamışsınız demektir; sadece kendinize bağımlılık yaratmışsınızdır.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM TARTIŞMA VE ÖDEV SORUSU",
  [
    *Ders Değerlendirmesi ve Ödev:* Ekibinizdeki en yetenekli kıdemli mühendis kim? Bu ay kendi koçluğunuzla onun tek başına yönetebileceği bir mimari sorumluluk veya tasarım konusu ne olabilir?
  ]
)