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
  part-num: 18,
  section-title: "Bölüm 5: Ölçeklenebilirlik ve Esneklik — İzdihamı Yönetmek",
  title: "Yük Dengeleme, Ağ Geçitleri ve Tersine Vekil Sunucular (Reverse Proxies)",
  subtitle: "Trafik orkestrasyonu: Layer 4 vs. Layer 7 yönlendirme, Envoy, Kong ve API Gateway mimarisi.",
  reading-time: "9 dk"
)

#war-story(
  title: "SAHADAN YAŞANMIŞ KRİZ HİKAYESİ",
  [Bir video işleme girişiminin iki API ucu vardı: 5 milisaniyede biten `/api/v1/kullanici/profil` ve 4 dakika boyunca %100 CPU harcayarak MP4 dönüştüren `/api/v1/video/donustur`. Altyapı mühendisi tüm sunucuları basit bir Round-Robin Layer 4 (TCP) yük dengeleyicinin arkasına koydu. Sabah 11:00'de 5 kullanıcı aynı anda ağır 4K videolar yükledi. Round-robin algoritması bu ağır video işlerini sırayla 1, 2, 3, 4 ve 5 numaralı sunuculara dağıttı. Sonraki 4 dakika boyunca sadece profil fotoğrafına bakmak isteyen binlerce normal mobil kullanıcı da bu 5 sunucuya yönlendirildi ve istekleri video kuyruğunda bekleyip zaman aşımına uğradı! Yük dengeleyici uygulama yollarından habersiz olduğu için tüm platform çöktü.]
)

== Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa
Bir yük dengeleyici sadece trafiği ikiye bölen bir T-boru değildir; sisteminizin trafik orkestratörü, güvenlik görevlisi ve yönlendirme aklıdır. Aptal Layer 4'ten (Taşıma katmanı: IP/Port) akıllı Layer 7'ye (Uygulama katmanı: HTTP yolları, başlıklar, çerezler) geçmek; trafiği işin aciliyetine göre yönlendirmenizi, ağır işleri izole etmenizi ve SSL feshini dış sınırda yapmanızı sağlar.

== Temel Mimari İlkeler ve Zihinsel Modeller
=== Layer 4 vs. Layer 7 Yük Dengeleme
- *Layer 4 (L4 - TCP/UDP, Örn: AWS NLB):* Ultra düşük gecikme, saniyede milyonlarca paket taşır. Yalnızca IP ve Port'a bakar; HTTP başlıklarını, URL'leri veya çerezleri okuyamaz.
- *Layer 7 (L7 - HTTP/HTTPS, Örn: NGINX, Envoy, AWS ALB):* URL yolunu ve HTTP başlıklarını inceler. Yola göre yönlendirme (`/video/*` -\> ağır işlem kümesi, `/api/*` -\> hızlı küme), SSL sonlandırma ve akıllı oran sınırlama sağlar.

=== API Gateway Kalıbı (Kong, Envoy, Traefik)
Bütün istemciler için tek giriş kapısı. Ortak dertleri merkezileştirir:
+ Kimlik doğrulama ve JWT kontrolü
+ Global hız sınırlama (Rate Limiting)
+ Metrikler ve OpenTelemetry enjeksiyonu
+ Canary yönlendirme ve Circuit Breaking

== Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar
- *Round-Robin Körlüğü:* İstek sürelerinin birbirinden çok farklı olduğu sistemlerde sırayla dağıtım yapıp sunucuları kitlemek (Bunun yerine 'Least Connections' veya 'Peak EWMA' kullanın).
- *API Gateway Tanrı Servisi:* Gateway eklentilerinin içine karmaşık iş mantığı, SQL sorguları ve özel hesaplamalar yazıp gateway'i kırılgan bir monolite çevirmek.
- *Korumasız Arka Uçlar:* Mikroservisleri genel internete doğrudan açık bırakıp gateway'i bypass edilebilir kılmak.

#architect-playbook(
  title: "MİMARIN EYLEM PLANI: BU HAFTAKİ SOMUT ADIMLAR",
  [
    - *1. Adım:* İş yüklerini ayır: Ağır arka plan işlerini ve hızlı API sorgularını Layer 7 yönlendirmeyle bağımsız ölçeklenen sunucu havuzlarına yönlendir.
    - *2. Adım:* Yük dengeleme algoritması olarak kör round-robin yerine 'En Az Bağlantı (Least Connections)' algoritmasını varsayılan yap.
    - *3. Adım:* SSL/TLS şifre çözme yükünü uygulama sunucularından alıp yük dengeleyici veya gateway sınırında sonlandır.
  ]
)

== Mimari Çıkarımlar ve Hile Tablosu
- Layer 4 saf hız ve paket hacmi içindir; Layer 7 akıllı yönlendirme ve güvenlik yönetimi içindir.
- Bir API Gateway altyapı dertlerini çözmelidir, iş mantığını değil.
- İş yükünün niteliğine göre yönlendirme yapın; ağır bir raporun hafif bir login isteğini rehin almasına izin vermeyin.

#udemy-corner(
  title: "UDEMY & NOTEBOOKLM TARTIŞMA VE ÖDEV SORUSU",
  [
    *Ders Değerlendirmesi ve Ödev:* Mevcut yük dengeleyiciniz hangi yönlendirme algoritmasını kullanıyor? Sunuculardan birinin belleği şişse ve yavaşlasa, yönlendiriciniz ona daha az trafik gönderecek kadar akıllı mı?
  ]
)