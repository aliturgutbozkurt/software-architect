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
  part-num: 31,
  section-title: "Bölüm 8: Gözlemlenebilirlik ve Operasyonel Mükemmellik — Karanlıkta Görmek",
  title: "FinOps ve Bulut Ekonomisi: Şirketi İflas Ettirmeyen Mimari",
  subtitle: "Maliyet verimli mimariler tasarlamak ve binlerce dolarlık bulut vampirlerini yok etmek.",
  reading-time: "9 dk"
)

#war-story(
  title: "SAHADAN YAŞANMIŞ KRİZ HİKAYESİ",
  [Yapay zeka tabanlı bir analitik girişimi 5 milyon dolar yatırım aldı. Altı ay sonra CEO dehşet içinde CTO'yu aradı: Aylık AWS faturası 4.000 dolardan 92.000 dolara fırlamıştı! İncelemede üç mimari rezalet ortaya çıktı: 1) Bir mühendis Kubernetes kümesinde CPU isteklerini aşırı şişirdiği için 80 sunucu ortalama %4 CPU ile bomboş çalışıyordu, 2) Kapatılmış test ortamlarından kalan boşta duran EBS diskleri ayda 12.000 dolar hayalet fatura üretiyordu, 3) Bir yedekleme betiği her 6 saatte bir 20 terabayt veriyi AWS bölgeleri arasında kopyalayarak ayda 30.000 dolar veri çıkış (egress) ücreti üretiyordu! Şirket ilk 100 müşterisini bile bulamadan yatırımının beşte birini bulut israfında yakmıştı.]
)

== Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa
Bulut bilişim sınırsız ve bedava bir açık büfe değildir; her mimari kararın anında dolar cinsinden bir karşılığı olan sayaçlı bir aboneliktir. Bulutta *mimarlık bir finans mühendisliğidir*. Usta bir mimar sadece 'Sistem 10 kat trafiği kaldırır mı?' diye sormaz; '10 kat trafikte işlem başına birim maliyetimiz ne olur?' diye sorar. Kullanıcı sayısı 2 katına çıkarken bulut faturası 4 katına çıkıyorsa o mimari iflas etmeye mahkumdur. *FinOps*, bulut maliyetini mimarinin temel bir kalite metriği haline getirme disiplinidir.

== Temel Mimari İlkeler ve Zihinsel Modeller
=== Yazılım Mimarisinin Birim Ekonomisi
- *Aktif Kullanıcı Başına Maliyet:* Kullanıcı başına geliriniz 0.05 dolarsa, kullanıcı başına altyapı maliyetiniz 0.01 doların altında olmak ZORUNDADIR.
- *Ağ Çıkış Ücretleri (Egress):* Aynı veri merkezinde veri taşımak ücretsizdir; bölgeler (AZ) arası taşımak GB başına 0.01\$; internete çıkarmak ise 0.09\$'dır. Mimar sınırlar arası veri trafiğini minimize etmelidir.

=== FinOps Optimizasyon Kolları
+ *Doğru Boyutlandırma:* Konteyner CPU/RAM taleplerini gerçek P95 kullanımına göre küçültün.
+ *Taahhüt İndirimleri (Savings Plans):* Öngörülebilir baz yükler için 1-3 yıllık taahhütle %40-60 tasarruf edin.
+ *Spot Sunucular:* Durumsuz arka plan işlerinde ve testlerde %80 indirimli spot makineleri kullanın.
+ *Depolama Kademelendirme:* Eski log ve yedekleri S3 Standard'dan otomatik yaşam döngüsüyle Glacier'a taşıyın.

== Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar
- *Aşırı Tahsis Refleksi:* 'Belki yoğun olur' diyerek her mikroservise 4 CPU ve 8 GB RAM verip sunucu kapasitesinin %95'ini boşta yatırmak.
- *Zombi Kaynak Mezarlığı:* Terk edilmiş yük dengeleyiciler, bağlanmamış diskler ve hafta sonları kimsenin bakmadığı çalışan test ortamları.
- *Bölgeler Arası Geveze Servisler:* Bölge 1'deki bir servisin Bölge 2'deki veritabanına saniyede 10.000 sorgu atıp şirkete binlerce dolar gizli ağ faturası çıkarması.

#architect-playbook(
  title: "MİMARIN EYLEM PLANI: BU HAFTAKİ SOMUT ADIMLAR",
  [
    - *1. Adım:* Zorunlu etiketleme (Tagging) getir: Her bulut kaynağında `Sahip`, `Ortam` ve `Servis` etiketi olsun.
    - *2. Adım:* Bulut faturasının en büyük 3 harcama kalemini tespit et (genellikle EC2, RDS ve Veri Transferi).
    - *3. Adım:* Geliştiriciler akşam evlerine gittiğinde tüm geliştirme ve test ortamlarını otomatik kapatan zamanlayıcı kur (%65 tasarruf).
  ]
)

== Mimari Çıkarımlar ve Hile Tablosu
- İyi mimari, maliyet-etkin mimaridir; sınırsız bütçeyle herkes hızlı sistem kurabilir.
- Veri transfer ücretlerini şahin gibi izleyin; faturanın en sinsi kalemi ağ çıkışlarıdır.
- Test ortamlarını mesai bitiminde kapatmayı ve eski yedekleri arşivlemeyi otomatikleştirin.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM TARTIŞMA VE ÖDEV SORUSU",
  [
    *Ders Değerlendirmesi ve Ödev:* Şirketinizin aylık bulut faturasının ne kadar olduğunu biliyor musunuz? 1.000 API çağrısı veya aktif kullanıcı başına altyapı maliyetiniz kaç kuruş?
  ]
)