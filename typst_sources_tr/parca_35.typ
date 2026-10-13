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
  part-num: 35,
  section-title: "Bölüm 9: İnsan Mimarisi — Yetki Olmadan Liderlik Etmek",
  title: "İkna Sanatı: Mimari Vizyonu Mühendis Olmayan Yöneticilere Satmak",
  subtitle: "CEO, CFO ve Satış Direktörünü teknik yol haritanız için nasıl heyecanlandırırsınız?",
  reading-time: "9 dk"
)

#war-story(
  title: "SAHADAN YAŞANMIŞ KRİZ HİKAYESİ",
  [Hırslı bir kurumsal mimar, Kubernetes ve Kafka geçişi için 800.000 dolarlık bütçeyi onaylatmak üzere 70 slaytlık bir sunum hazırladı. Slaytlar UML diyagramları, Raft mutabakat algoritmaları ve Protobuf serileştirme grafiklerinden geçilmiyordu. Yönetim kuruluna sundu. CEO dört kez saatine baktı, CFO'nun gözleri daldı. Sunum bittiğinde CFO sordu: 'Bu 800.000 doları harcarsak müşteriler bize daha çok para ödeyecek mi?' Mimar kekeledi: 'Şey, hayır ama konteynerlerimiz elastik orkestre edilecek!' Teklif oybirliğiyle reddedildi. Bir ay sonra başka bir lider aynı projeyi 3 slaytla sundu: '1) Geçen yıl sepet kesintileri bize 1.4 milyon dolar satış kaybettirdi. 2) Bu altyapı tek hata noktalarını kaldırıyor. 3) Beklenen net tasarruf: Yılda 900.000 dolar.' Bütçe 10 dakikada onaylandı.]
)

== Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa
Teknik dehanız, onu iş dünyasının ana dilinde anlatamadığınız sürece değersizdir. C-Level yöneticilerin hiçbiri Kubernetes, Kafka veya Clean Architecture ile ilgilenmez. İlgilendikleri üç şey vardır: *Geliri Artırmak (+\$\$)*, *Maliyeti Düşürmek (-\$\$)* ve *İş Riskini Azaltmak (Kalkan)*. Bir mimar çift dilli olmalıdır: Mühendislerle konuşurken kod ve dağıtık sistemler; yöneticilerle konuşurken sermaye getirisi (ROI) ve risk dili.

== Temel Mimari İlkeler ve Zihinsel Modeller
=== Yönetimin Üç Para Birimi
- *Gelir (+\$\$):* Bu mimari yeni ürün yeteneklerinin önünü açıyor mu, kurumsal müşteri kazanımını hızlandırıyor mu?
- *Maliyet (-\$\$):* Bu mimari bulut israfını, lisans ücretlerini veya yazılımcı oryantasyon süresini düşürüyor mu?
- *Risk (Kalkan):* Bu mimari yasal cezaları (KVKK/GDPR), veri sızıntısı itibar kaybını veya kampanya günü çöküşlerini engelliyor mu?

=== 1 Sayfalık Mimari Teklif Çerçevesi
+ *Yönetici Özeti (1 paragraf):* Hangi iş problemini çözüyoruz, öneri ne ve maliyeti kaç para?
+ *Hareketsiz Kalmanın Maliyeti:* Önümüzdeki 12 ay hiçbir şey yapmazsak ne kadar para veya müşteri kaybedeceğiz?
+ *Önerilen Çözüm (Sade Dille):* Sıfır kısaltma ve jargonsuz temiz özet.
+ *Dönüm Noktaları:* Çeyreklik somut teslimatlar.
+ *ROI ve Başarı Metrikleri:* Yatırımın başarılı olduğunu hangi rakamla kanıtlayacağız?

== Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar
- *Jargon Kalesi:* Güvensizliğini gizlemek için yöneticilerin önünde eBPF, WASM, Raft gibi teknik terimlerin arkasına saklanmak.
- *Kıyamet Tellallığı:* Her refactoring isteğinde 'Her şey yanıyor, yarın batacağız!' diyerek inandırıcılığını yitirmek.
- *Diktatör Mimar:* Geliştiricileri dinlemeden yukarıdan fermanlar yağdırıp sahada dirençle karşılaşmak.

#architect-playbook(
  title: "MİMARIN EYLEM PLANI: BU HAFTAKİ SOMUT ADIMLAR",
  [
    - *1. Adım:* Teknik iş listendeki her maddeyi 3 para birimine göre etiketle: Gelir, Maliyet veya Risk.
    - *2. Adım:* Satış, Ürün ve Destek liderleriyle ayda bir 20 dakikalık kahve iç: 'Müşteri karşısında sizi en çok mahcup eden teknik sorun ne?'
    - *3. Adım:* Sunumunu mühendis olmayan bir arkadaşına anlat: 60 saniyede temel faydayı anlayamıyorsa sunumu baştan yaz.
  ]
)

== Mimari Çıkarımlar ve Hile Tablosu
- Mimarinizin değerini teknik olmayan birine anlatamıyorsanız, siz de onu yeterince anlamamışsınız demektir.
- Yönetim kurulu sermaye ve risk diliyle konuşur; onların lehçesini öğrenin.
- Mimarlar resmi makam gücüyle değil; etki, empati ve netlikle liderlik eder.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM TARTIŞMA VE ÖDEV SORUSU",
  [
    *Ders Değerlendirmesi ve Ödev:* Şu an tutkuyla istediğiniz bir mimari refactoring projesini seçin. CEO'nuza içinde tek bir teknik kısaltma bile olmayan 3 cümlelik bir asansör konuşması hazırlayın.
  ]
)