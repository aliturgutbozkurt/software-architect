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
  part-num: 40,
  section-title: "Bölüm 10: Modern Ufuklar — Yapay Zeka Çağında Mimarlık ve Kurumsal Ustalık",
  title: "Mimarın Kutup Yıldızı: Bilgelik, Alçakgönüllülük ve Zamansız Zanaat",
  subtitle: "Yazılım mimarisinin zen felsefesi: Eksilterek sadeleşmek, alçakgönüllü kalmak ve kalıcı bir miras bırakmak.",
  reading-time: "8 dk"
)

#war-story(
  title: "SAHADAN YAŞANMIŞ KRİZ HİKAYESİ",
  [Efsanevi bir kıdemli yazılım mimarı, 80 milyon dolar yatırım almış ancak batmak üzere olan bir girişimi ziyarete gitti. Girişimin genç liderleri gururla mimari tahtalarını gösterdiler: 65 mikroservis, 4 farklı mesaj kuyruğu, 3 farklı vektör veritabanı ve karmaşık Kubernetes servis mesh'leri içeren bir labirent! Ekip zamanının %80'ini altyapı bug'larını çözmekle, sadece %20'sini ürün geliştirmekle harcıyordu. Şirket iflasın eşiğindeydi. Yaşlı mimar iki saat boyunca sessizce dinledi, tahtaya yürüdü, silgiyi aldı ve silmeye başladı. 50 mikroservisi sildi, 3 mesaj kuyruğunu tek bir kuyrukta birleştirdi, egzotik dağıtık veritabanlarını basit bir PostgreSQL ile değiştirdi. Üç ay içinde şirketin canlıya çıkış hızı 5 kat arttı, hatalar %80 azaldı ve girişim kâra geçti. Genç mühendis sordu: 'Bu kadar karmaşık bir sistemi nasıl inşa edebildiniz?' Mimar gülümsedi: 'Herkes karmaşık bir şey yapabilir. Ustalık, neleri dışarıda bırakacağını bilmektir.']
)

== Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa
Bir mühendisin mesleki yolculuğu üç aşamalı bir yay çizer: Birinci aşamada (Junior), araçları bilmezsiniz ve basit özellikleri yazmakta zorlanırsınız. İkinci aşamada (Mid-Senior), tasarım kalıplarını, mikroservisleri ve egzotik araçları keşfedersiniz; zekanızı kanıtlamak için HEPSİNİ her yerde kullanmak istersiniz. Üçüncü aşamada (Usta Mimar), anlarsınız ki *mükemmellik eklenecek bir şey kalmadığında değil, çıkarılacak hiçbir şey kalmadığında elde edilir* (Antoine de Saint-Exupéry). Yazılım mimarlığı bir ego savaşı değildir; insan problemlerini mümkün olan en sade, en dayanıklı sistemlerle çözme zanaatıdır.

== Temel Mimari İlkeler ve Zihinsel Modeller
=== Yazılım Mimarisinin Beş Zamansız İlkesi
+ *Sadelik En Üst Düzey Gelişmişliktir:* Sıkıcı, kanıtlanmış teknolojiyi seçin. Karmaşıklık her gün ödediğiniz bir vergidir.
+ *Değişim İçin Tasarlayın:* Değişmeyecek tek şey gereksinimlerin ve trafiğin değişeceğidir. Kodu silmeyi ve değiştirmeyi kolaylaştıran sınırlar çizin.
+ *Teknoloji Değil, İnsan:* Conway Yasası kraldır. Morali yüksek, psikolojik güvenliği olan bir ekibin kurduğu vasat mimari; birbirine küsmüş bir ekibin kurduğu parlak mimariyi her zaman ezer.
+ *En İyi Pratik Yoktur, Bağlam Vardır:* Dogmaları sorgulayın. Google'ı kurtaran şey 10 kişilik bir girişimi batırabilir.
+ *Alçakgönüllülük En Büyük Gücünüzdür:* Meraklı kalın, yanıldığınızı kabul edin ve başarınızı yetiştirdiğiniz mühendislerle ölçün.

=== Mimarın Gerçek Mirası
Bir şirketten ayrıldığınızda kimse yazdığınız zekice bash betiklerini veya karmaşık tasarım kalıplarını hatırlamayacak. Hatırlayacakları tek şey: Sistem ayakta kaldı mı? Yeni başlayanlar ilk haftasında güvenle kod çıkarabildi mi? Ve insanlara şefkatle, sabırla mentorluk yaptınız mı?

== Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar
- *Entelektüel Kibir Tuzağı:* 'Mimar' unvanına sahip olmanın her gün kod yazan mühendislerden daha zeki olmak anlamına geldiğine inanmak.
- *Karmaşıklık Bağımlılığı:* Kendi değerini sağladığı iş değeriyle değil, mimarisinin karmaşıklığıyla ölçmek.
- *Teknoloji Kinisti:* Geçmişe o kadar saplanmak ki yapay zeka ve modern bulut araçları gibi yeni inovasyonları 'geçici heves' diye toptan reddetmek.

#architect-playbook(
  title: "MİMARIN EYLEM PLANI: BU HAFTAKİ SOMUT ADIMLAR",
  [
    - *1. Adım:* Sistemini 'Silgi Zihniyeti' ile tara: Sistemi daha sade kılmak için bu çeyrek hangi bileşeni, veritabanını veya servisi sistemden çıkarabilirsin?
    - *2. Adım:* Her hafta 2 saatini konfor alanının dışındaki bir konuyu (AI, FinOps, Dağıtık Konsensüs) öğrenmeye ayır.
    - *3. Adım:* Ekibini kutla: Testleri güncelleyen, bağımlılıkları yamayan ve prodüksiyonu sessizce ayakta tutan o görünmez kahramanlara teşekkür et.
  ]
)

== Mimari Çıkarımlar ve Hile Tablosu
- Problemi çözen en sade sistem, inşa edeceğiniz en büyük başyapıttır.
- Mimarlık, beş yıl sonra kodunuza bakım yapacak tanımadığınız o geliştiriciye duyduğunuz bir empati eylemidir.
- Gerçek ustalık görünmezdir: Mimarlık gerçekten harika olduğunda, insanlar orada olduğunu bile unutur.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM TARTIŞMA VE ÖDEV SORUSU",
  [
    *Ders Değerlendirmesi ve Ödev:* Bir Yazılım Mimarı Gibi Düşünmek eğitimini tamamladınız! Kendi 'Mimar Manifestonuzu' yazın: Kariyerinizin geri kalanında tasarlayacağınız her sisteme rehberlik edecek 3 vazgeçilmez ilkeniz nedir?
  ]
)