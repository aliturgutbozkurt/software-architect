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
  part-num: 10,
  section-title: "Bölüm 3: Veri Mimarisi — Durumun Yaşadığı, Öldüğü ve Yalan Söylediği Yer",
  title: "Veritabanı Darboğazı: İndeksleme, Parçalama (Sharding) ve Okuma Kopyaları",
  subtitle: "Trafik 100 katına çıktığında ve sorgular sürünmeye başladığında veritabanınızı nasıl ölçeklersiniz?",
  reading-time: "9 dk"
)

#war-story(
  title: "SAHADAN YAŞANMIŞ KRİZ HİKAYESİ",
  [Efsane Cuma gecesi 00:01'de bir e-ticaret sitesinin trafiği 2.000'den 80.000 eşzamanlı kullanıcıya fırladı. 90 saniye içinde veritabanı bağlantı havuzu tükendi. Bütün API sunucuları tek bir sorguya kilitlenmişti: `SELECT * FROM urunler WHERE kategori = 'elektronik' AND durum = 'aktif' ORDER BY ekleme_tarihi DESC`. Tabloda 40 milyon satır vardı ve ilgili kolonlarda birleşik (composite) indeks yoktu! Her arama diskten 14 GB veri okuyup tablo taraması (full table scan) yapıyordu. Sunucu çöktü. İki katı büyüklükte RAM ve CPU'ya sahip bir sunucuya geçtiler, o da 4 dakika sonra çöktü. Kesinti 6 saat sürdü ve şirket 1.8 milyon dolar ciro kaybetti.]
)

== Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa
Veritabanına daha fazla CPU ve RAM basmak (Dikey Ölçekleme) en kolay yoldur ancak sert bir fiziksel ve mali sınıra çarpar. Veritabanı yavaşladığında acemi geliştirici mikroservis diye bağırır; usta mimar ise sorgu planlayıcısını inceler, eksik bileşik indeksleri ekler, okuma trafiğini kopyalara (read replicas) dağıtır ve sadece kaçınılmaz olduğunda yatay parçalamaya (sharding) gider.

== Temel Mimari İlkeler ve Zihinsel Modeller
=== Veritabanı Ölçekleme Merdiveni
+ *1. Basamak: Sorgu ve İndeks Optimizasyonu:* `EXPLAIN ANALYZE` ile incele. B-Tree indeksleri ve kolon sırasının kritik olduğu bileşik indeksleri (önce eşitlik, sonra aralık sorgulanan kolonlar) doğru kur.
+ *2. Basamak: Okuma Kopyaları ve Bağlantı Havuzlama:* Yazma trafiği Ana (Primary) sunucuya gider; okuma trafiği 3-4 Kopya (Replica) sunucuya dağıtılır. PgBouncer ile bağlantı havuzu yönetilir.
+ *3. Basamak: Yatay Parçalama (Sharding):* Veriyi bir parçalama anahtarıyla (`kullanici_id % parca_sayisi`) bağımsız veritabanı sunucularına paylaştırmak.

=== Kopya Gecikmesi (Replication Lag) Tuzağı
Okuma kopyaları asenkrondur. Kullanıcı profilini güncelleyip hemen sayfayı yenilediğinde, okuma sorgusu henüz güncellenmemiş bir kopyaya düşerse eski halini görür! Çözüm: Yazma yapıldıktan sonraki 2 saniye boyunca okumaları da Ana sunucudan yapmak (Read-Your-Own-Writes).

== Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar
- *Kör ORM Güveni:* Arka planda nasıl devasa sorgular ürettiğini bilmeden ORM'lerin oluşturduğu n+1 sorgularına göz yummak.
- *Aşırı İndeksleme:* 'İleride lazım olur' diye tablodaki her kolona indeks koyup yazma hızını %400 yavaşlatmak (çünkü her insert'te 15 ayrı B-Tree güncellenir).
- *Yanlış Parçalama Anahtarı:* Zamana göre sharding yapıp gelen tüm yeni yazma trafiğinin sadece en son sunucuya yüklenmesine yol açmak.

#architect-playbook(
  title: "MİMARIN EYLEM PLANI: BU HAFTAKİ SOMUT ADIMLAR",
  [
    - *1. Adım:* `pg_stat_statements` veya yavaş sorgu loglarını açıp veritabanı CPU'sunun %80'ini tüketen ilk 5 sorguyu tespit et.
    - *2. Adım:* En yavaş sorguda `EXPLAIN (ANALYZE, BUFFERS)` çalıştırıp Seq Scan yerine Index Scan yapıldığından emin ol.
    - *3. Adım:* Ağır analitik ve rapor sorgularını canlı veritabanından ayırıp özel bir salt-okunur kopyaya yönlendir.
  ]
)

== Mimari Çıkarımlar ve Hile Tablosu
- Tek bir eksik bileşik indeks, 2 milisaniyelik sorguyu 15 saniyelik bir sistem katiline dönüştürebilir.
- Veritabanını sharding ile bölmeye 100 bin dolar harcamadan önce, indekslemeye 1 saat ayırın.
- Asenkron okuma kopyaları kullanıyorsanız, kullanıcının kendi yazdığını anında görebilme garantisini tasarlayın.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM TARTIŞMA VE ÖDEV SORUSU",
  [
    *Ders Değerlendirmesi ve Ödev:* Projenizdeki en kritik arama sorgusunda `EXPLAIN ANALYZE` çalıştırın. Tablo taraması mı yapıyor, indeks taraması mı? Kaç satır filtreleniyor?
  ]
)