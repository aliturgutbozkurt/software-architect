# Bölüm 5: Ölçeklenebilirlik ve Esneklik — İzdihamı Yönetmek (Parça 17 - 20)

SECTION_5_TR = {
    "section_num": 5,
    "section_title": "Ölçeklenebilirlik ve Esneklik — İzdihamı Yönetmek",
    "section_desc": "Patlayıcı kullanıcı artışlarına mimari hazırlık: durumsuz on iki faktörlü uygulamalar tasarlamak, Layer 4/7 yük dengeleyiciler ve API ağ geçitleri kurmak, küresel uçta (Edge) önbellekleme yapmak ve hız sınırlama ile sistemi korumak.",
    "parts": [
        {
            "part_num": 17,
            "title": "Yatay Ölçekleme: Durumsuzluk (Statelessness) ve 12-Faktör Uygulama",
            "subtitle": "Oturum durumunu sunucu belleğinde tutmanın otomatik ölçeklemeyi kullanıcılar için bir rulet oyununa çevirmesi.",
            "duration": "9 dk",
            "war_story": "Bir hızlı moda e-ticaret sitesi akşam 20:00'de ulusal televizyonda ana haberlere çıktı. Sitenin anlık ziyaretçisi 3 dakika içinde 500'den 60.000'e fırladı. Bulut otomatik ölçekleyicisi (auto-scaler) harika bir tepki vererek sunucu sayısını 2'den 30'a çıkardı. Ancak dakikalar içinde çağrı merkezine binlerce öfkeli telefon yağmaya başladı: Müşteriler sepete ürün ekliyor, 'Sonraki Sayfa'ya bastıklarında sepetleri bomboş görünüyordu! Ya da ödeme yaparken aniden sistemden atılıp bambaşka bir kullanıcının ekranını görüyorlardı! Neden mi? Geliştiriciler kullanıcının sepetini ve oturumunu Sunucu 1'in yerel RAM belleğinde tutmuştu. Yük dengeleyici bir sonraki isteği Sunucu 7'ye attığında, Sunucu 7 o kullanıcıyı daha önce hiç görmemişti.",
            "paradigm_shift": "Dikey ölçeklemenin (daha büyük makine almak) fiziksel ve mali bir tavanı vardır; yatay ölçekleme (daha fazla ucuz makine eklemek) ise neredeyse sonsuzdur—**ANCAK ve ANCAK** uygulama örnekleriniz tamamen durumsuz (stateless) ise. Yatay esnekliğin altın kuralı: *Herhangi bir sunucu herhangi bir saniyede tek bir kullanıcı bile fark etmeden öldürülebilmelidir.* Bir sunucu kendi içinde durum saklıyorsa o şefkatle bakılması gereken bir 'evcil hayvandır (pet)'; durumsuz ise otomatik ölçekleyicinin saniyeler içinde kesip yenisini koyabileceği bir 'büyükbaş hayvandır (cattle)'.",
            "core_concepts": [
                {
                    "heading": "12-Faktör Durumsuzluk İlkeleri",
                    "text": "- **Faktör VI (Süreçler):** Uygulamayı bir veya daha fazla durumsuz süreç olarak çalıştırın. Kalıcı olması gereken her veri mutlaka harici bir destek servisinde (Redis, PostgreSQL, S3) tutulmalıdır.\n- **Faktör III (Yapılandırma):** Konfigürasyonu kodda değil, ortam değişkenlerinde (ENV) saklayın.\n- **Faktör IX (Tek Kullanımlık):** Hızlı başlatma ve zarif kapatma (graceful shutdown) sağlayın. `SIGTERM` sinyali geldiğinde mevcuttaki istekleri 10 saniye içinde tamamlayıp temizce kapanın."
                },
                {
                    "heading": "Oturum Durumunu Dışsallaştırmak",
                    "text": "Oturumları asla yerel sunucu RAM'inde tutmayın: 1) Dağıtık Oturum Deposu (Redis kümesi), veya 2) Kriptografik olarak imzalanmış durumsuz token'lar (JWT) kullanın."
                }
            ],
            "anti_patterns": [
                "**Yapışkan Oturumlar (Sticky Sessions):** Kullanıcı A'yı hep Sunucu 1'e gitmeye zorlamak. Sunucu 1 çöktüğünde veya trafik azalıp kapandığında o sunucudaki tüm kullanıcıların oturumunun patlaması.",
                "**Yerel Diske Dosya Yükleme:** Kullanıcıların profil fotoğraflarını sunucunun yerel `/tmp` veya `/uploads` klasörüne kaydetmek; diğer 29 sunucunun o dosyadan habersiz olması.",
                "**Yavaş Başlayan Uygulama:** Başlarken veritabanından 4 GB veriyi RAM'e çekmeye çalışan ve açılması 8 dakika süren hantal uygulamalar (Trafik patlamasında otomatik ölçeklemeyi işlevsiz kılar)."
            ],
            "playbook": [
                "**1. Adım:** Kod tabanını tara: Statik yerel bellek içi haritaları (in-memory maps) ve yerel diske dosya yazan kodları kaldır.",
                "**2. Adım:** Bütün dosya yüklemelerini önceden imzalanmış URL'ler (pre-signed URLs) ile doğrudan nesne deposuna (S3, GCS) yönlendir.",
                "**3. Adım:** Uygulama açılış süresini 15 saniyenin altına indir ki bulut auto-scaling ani trafik dalgalarını karşılayabilsin."
            ],
            "takeaways": [
                "Sunucularınıza evcil hayvan gibi değil, büyükbaş hayvan gibi davranın.",
                "Uygulamanız herhangi bir sunucunun aniden `kill -9` ile kapatılmasını kaldıramıyorsa, yatay ölçeklenmeye hazır değilsiniz demektir.",
                "Tüm durumu harici veritabanlarına veya Redis'e çıkarın; işlem gücünü tamamen durumsuz tutun."
            ],
            "udemy_prompt": "Canlıdaki sunucularınızdan biri tam şu saniyede fişten çekilse, o sunucuya bağlı kullanıcıların başına ne gelir? Oturumları düşer mi, sepetleri kaybolur mu?"
        },
        {
            "part_num": 18,
            "title": "Yük Dengeleme, Ağ Geçitleri ve Tersine Vekil Sunucular (Reverse Proxies)",
            "subtitle": "Trafik orkestrasyonu: Layer 4 vs. Layer 7 yönlendirme, Envoy, Kong ve API Gateway mimarisi.",
            "duration": "9 dk",
            "war_story": "Bir video işleme girişiminin iki API ucu vardı: 5 milisaniyede biten `/api/v1/kullanici/profil` ve 4 dakika boyunca %100 CPU harcayarak MP4 dönüştüren `/api/v1/video/donustur`. Altyapı mühendisi tüm sunucuları basit bir Round-Robin Layer 4 (TCP) yük dengeleyicinin arkasına koydu. Sabah 11:00'de 5 kullanıcı aynı anda ağır 4K videolar yükledi. Round-robin algoritması bu ağır video işlerini sırayla 1, 2, 3, 4 ve 5 numaralı sunuculara dağıttı. Sonraki 4 dakika boyunca sadece profil fotoğrafına bakmak isteyen binlerce normal mobil kullanıcı da bu 5 sunucuya yönlendirildi ve istekleri video kuyruğunda bekleyip zaman aşımına uğradı! Yük dengeleyici uygulama yollarından habersiz olduğu için tüm platform çöktü.",
            "paradigm_shift": "Bir yük dengeleyici sadece trafiği ikiye bölen bir T-boru değildir; sisteminizin trafik orkestratörü, güvenlik görevlisi ve yönlendirme aklıdır. Aptal Layer 4'ten (Taşıma katmanı: IP/Port) akıllı Layer 7'ye (Uygulama katmanı: HTTP yolları, başlıklar, çerezler) geçmek; trafiği işin aciliyetine göre yönlendirmenizi, ağır işleri izole etmenizi ve SSL feshini dış sınırda yapmanızı sağlar.",
            "core_concepts": [
                {
                    "heading": "Layer 4 vs. Layer 7 Yük Dengeleme",
                    "text": "- **Layer 4 (L4 - TCP/UDP, Örn: AWS NLB):** Ultra düşük gecikme, saniyede milyonlarca paket taşır. Yalnızca IP ve Port'a bakar; HTTP başlıklarını, URL'leri veya çerezleri okuyamaz.\n- **Layer 7 (L7 - HTTP/HTTPS, Örn: NGINX, Envoy, AWS ALB):** URL yolunu ve HTTP başlıklarını inceler. Yola göre yönlendirme (`/video/*` -> ağır işlem kümesi, `/api/*` -> hızlı küme), SSL sonlandırma ve akıllı oran sınırlama sağlar."
                },
                {
                    "heading": "API Gateway Kalıbı (Kong, Envoy, Traefik)",
                    "text": "Bütün istemciler için tek giriş kapısı. Ortak dertleri merkezileştirir:\n1. Kimlik doğrulama ve JWT kontrolü\n2. Global hız sınırlama (Rate Limiting)\n3. Metrikler ve OpenTelemetry enjeksiyonu\n4. Canary yönlendirme ve Circuit Breaking"
                }
            ],
            "anti_patterns": [
                "**Round-Robin Körlüğü:** İstek sürelerinin birbirinden çok farklı olduğu sistemlerde sırayla dağıtım yapıp sunucuları kitlemek (Bunun yerine 'Least Connections' veya 'Peak EWMA' kullanın).",
                "**API Gateway Tanrı Servisi:** Gateway eklentilerinin içine karmaşık iş mantığı, SQL sorguları ve özel hesaplamalar yazıp gateway'i kırılgan bir monolite çevirmek.",
                "**Korumasız Arka Uçlar:** Mikroservisleri genel internete doğrudan açık bırakıp gateway'i bypass edilebilir kılmak."
            ],
            "playbook": [
                "**1. Adım:** İş yüklerini ayır: Ağır arka plan işlerini ve hızlı API sorgularını Layer 7 yönlendirmeyle bağımsız ölçeklenen sunucu havuzlarına yönlendir.",
                "**2. Adım:** Yük dengeleme algoritması olarak kör round-robin yerine 'En Az Bağlantı (Least Connections)' algoritmasını varsayılan yap.",
                "**3. Adım:** SSL/TLS şifre çözme yükünü uygulama sunucularından alıp yük dengeleyici veya gateway sınırında sonlandır."
            ],
            "takeaways": [
                "Layer 4 saf hız ve paket hacmi içindir; Layer 7 akıllı yönlendirme ve güvenlik yönetimi içindir.",
                "Bir API Gateway altyapı dertlerini çözmelidir, iş mantığını değil.",
                "İş yükünün niteliğine göre yönlendirme yapın; ağır bir raporun hafif bir login isteğini rehin almasına izin vermeyin."
            ],
            "udemy_prompt": "Mevcut yük dengeleyiciniz hangi yönlendirme algoritmasını kullanıyor? Sunuculardan birinin belleği şişse ve yavaşlasa, yönlendiriciniz ona daha az trafik gönderecek kadar akıllı mı?"
        },
        {
            "part_num": 19,
            "title": "İçerik Dağıtım Ağları (CDN) ve Uç Nokta Bilişim (Edge Computing)",
            "subtitle": "Işık hızı gecikme cezasını alt etmek ve küresel kullanıcılara 50 milisaniyenin altında hizmet vermek.",
            "duration": "8 dk",
            "war_story": "Bir SaaS analitik platformunun tüm sunucuları Kuzey Virginia'daki tek bir AWS veri merkezindeydi. Şirket Sidney/Avustralya'da dev bir kurumsal müşteriye imza attı. Ancak Avustralyalı yöneticiler dashboard'un 4.2 saniyede açılmasından şikayetçi oldu. Mühendisler 3 hafta boyunca SQL sorgularını optimize etti, JSON'ları sıkıştırdı; ama açılış süresi ancak 100 milisaniye kısaldı! Neden mi? Sidney ile Virginia arasındaki fiber optik kablo mesafesi gidiş-dönüş 30.000 kilometredir. Cam kablodaki ışık hızı zorunlu olarak 180ms gecikme üretir. Sayfanın yüklenmesi için gereken 18 sıralı CSS, font ve JS isteği, $18 \times 180\text{ms} = 3.24\text{ saniyeyi}$ salt okyanus tabanında seyahat ederek harcıyordu! Araya Cloudflare CDN koyduklarında Sidney'deki açılış süresi 380 milisaniyeye düştü.",
            "paradigm_shift": "Kodu ne kadar optimize ederseniz edin, ışık hızını yenemezsiniz. Küresel bir kitleye hızlı dijital deneyim sunmanın tek yolu, veriyi ve hesaplamayı fiziksel olarak kullanıcının yaşadığı şehre yaklaştırmaktır. Modern bir İçerik Dağıtım Ağı (CDN) sadece resim saklanan bir yer değildir; dünyada 300'den fazla şehirde bulunan, TLS'i sonlandıran, sunucusuz (serverless) kod çalıştıran ve ana sunucularınızı internet trafiğinin %95'inden koruyan programlanabilir bir küresel kalkandır.",
            "core_concepts": [
                {
                    "heading": "Uç Nokta Hiyerarşisi: Kaynak (Origin) vs. Uç (Edge PoP)",
                    "text": "- **Uç Nokta (Edge Point of Presence - PoP):** Londra, Tokyo, Sidney, İstanbul gibi metropollerdeki sunucular. Kullanıcı 5ms mesafedeki uç noktaya bağlanır.\n- **Kaynak Sunucu (Origin):** Veritabanınızın ve ana işlem gücünüzün olduğu merkez.\n- **HTTP Önbellek Başlıkları:**\n  - `Cache-Control: public, max-age=31536000, immutable` (Hash'lenmiş statik dosyalar için)\n  - `Cache-Control: s-maxage=60, stale-while-revalidate=300` (Yarı dinamik API yanıtları için)"
                },
                {
                    "heading": "Uç Nokta Bilişim (Cloudflare Workers, Fastly Compute, Lambda@Edge)",
                    "text": "Uç noktalarda hafif JavaScript veya WebAssembly çalıştırmak: 1) Coğrafi yönlendirmeler, 2) A/B testi çerez yönetimi, 3) Token doğrulama ve 4) Bot engelleme için devasa hız avantajı sağlar."
                }
            ],
            "anti_patterns": [
                "**Hash'siz Statik Dosyalar:** Dosya adına hash eklemeden (`app.js`) yayınlamak ve güncelleme anında kullanıcıların tarayıcısında eski sürümün takılıp kalması.",
                "**CDN Bypass Etmek:** Statik API yanıtlarına önbellek başlığı koymayıp viral bir sosyal medya akınında tüm trafiğin doğrudan kaynak veritabanına çarpmasına izin vermek.",
                "**Uçta Ağır Hesaplama:** Uç sunucularda ağır veritabanı sorguları veya uzun CPU hesaplamaları yapmaya kalkışıp zaman aşımına takılmak."
            ],
            "playbook": [
                "**1. Adım:** Derleme sürecini (Webpack/Vite) tüm statik dosyaların adlarına içerik özeti (content-hash) ekleyecek şekilde ayarla.",
                "**2. Adım:** Bütün hash'li statik dosyalara 1 yıllık `immutable` önbellek başlığı ata.",
                "**3. Adım:** Yarı dinamik halka açık API uçlarında `stale-while-revalidate` kullanarak CDN'in kullanıcılara anında eski kopyayı dönüp arka planda yenisini getirmesini sağla."
            ],
            "takeaways": [
                "Işık hızını refactor edemezsiniz; içeriği coğrafi olarak kullanıcıya yaklaştırın.",
                "İyi ayarlanmış bir CDN, gelen trafiğin %85 ila %95'ini ana sunucularınıza hiç değmeden karşılamalıdır.",
                "Dosya adlarına hash eklemek, uç noktadaki önbellek geçersiz kılma derdini kökten çözer."
            ],
            "udemy_prompt": "Tarayıcınızın Geliştirici Araçları (Network sekmesi) üzerinden şirketinizin ana sayfasını açın. JS ve CSS dosyalarınızın `Cache-Control` başlıkları ne? Bir CDN üzerinden mi geliyorlar yoksa doğrudan ana sunucudan mı?"
        },
        {
            "part_num": 20,
            "title": "Hız Sınırlama (Rate Limiting) ve Trafik Şekillendirme: Kalenizi Korumak",
            "subtitle": "Veri kazıyıcılardan (scrapers), kontrolden çıkmış döngülerden ve hacimsel saldırılardan sağ çıkma mimarisi.",
            "duration": "9 dk",
            "war_story": "Bir hava durumu API'sinin cömert bir ücretsiz planı vardı. Güneşli bir Salı sabahı, akıllı bahçe sulama cihazları üreten bir firmanın junior geliştiricisi toprağın nem durumuna göre hava tahminini çeken bir Python betiği yazdı. Ancak API çağrısını içine hiçbir `sleep` beklemesi koymadan sonsuz bir `while True:` döngüsüne yerleştirdi! Bu güncelleme 500 akıllı sulama cihazına yüklendi ve hava durumu şirketine saniyede 45.000 istek yağmaya başladı. Hava durumu API'sinde hız sınırlama yoktu. 60 saniye içinde veritabanı çöktü, gerçek mobil kullanıcılar 504 Gateway Timeout almaya başladı ve şirketin iki saatlik AWS internet çıkış (egress) faturası 4.500 doları aştı. Tüm şirket tek bir junior yazılımcının hatası yüzünden rehin alınmıştı.",
            "paradigm_shift": "Dağıtık dünyada sınırsız erişim sunmak varoluşsal bir intihardır. Dost müşteriler bile hatalı yeniden deneme döngüleriyle veya agresif botlarla sizi istemeden çökertebilir. Hız sınırlama (Rate Limiting) sadece parayla API paketi satanların kullandığı ticari bir sayaç değildir; mimarinin temel bağışıklık sistemidir. Usta bir mimar trafiği dış sınırda şekillendirir ve iç kaynakları ne pahasına olursa olsun korur.",
            "core_concepts": [
                {
                    "heading": "Klasik Hız Sınırlama Algoritmaları",
                    "text": "- **Token Bucket (Jeton Kovası):** Kovaya sabit hızla jeton damlar. Her istek bir jeton harcar. Ani trafik patlamalarına (burst) kova kapasitesi kadar izin verirken ortalama hızı korur. (API standartı).\n- **Leaky Bucket (Sızıntılı Kova):** İstekler kovaya dolar ve tabandaki delikten sabit hızla akar. Düzensiz trafiği sabit hızda pürüzsüz bir akışa dönüştürür.\n- **Kayan Pencere Sayacı (Sliding Window Counter):** İstek sayısını geçmiş ve şimdiki zaman diliminin ağırlıklı toplamıyla hesaplar. Düşük bellek tüketimi ve %99.9 doğruluk sunar."
                },
                {
                    "heading": "Ölçeklenebilir Hız Sınırlama Mimarisi",
                    "text": "Dağıtık hız sınırlamayı ASLA ilişkisel veritabanına sorgu atarak yapmayın! Atomik Lua betikleriyle çalışan bellek içi bir Redis kümesi veya NGINX/Cloudflare/Kong gibi dış ağ geçitleri kullanın."
                }
            ],
            "anti_patterns": [
                "**Yalnızca IP'ye Göre Kısıtlama:** Tek bir NAT ağ geçidinin arkasındaki 5.000 kişilik bir üniversiteyi veya şirketi tek bir kullanıcının hatası yüzünden toptan bloklamak.",
                "**Retry-After Başlığını Unutmak:** `HTTP 429 Too Many Requests` dönerken istemciye ne kadar beklemesi gerektiğini söyleyen `Retry-After: 30` başlığını vermemek; çaresiz istemcilerin daha da hızlı istek atmasına yol açmak.",
                "**Veritabanı Tabanlı Sayaç:** Her istekte SQL'e `INSERT INTO istek_loglari` yazmak; yani gelen bir DDoS atağında hız sınırlayıcının çalışabilmek için veritabanını bizzat kendisinin çökertmesi."
            ],
            "playbook": [
                "**1. Adım:** Katmanlı hız sınırlama kur: Anonim kullanıcılara IP bazlı, giriş yapmış kullanıcılara API anahtarı veya Kullanıcı ID'si bazlı limit koy.",
                "**2. Adım:** Standart RFC 6585 başlıklarını uygula: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`.",
                "**3. Adım:** Hız sınırlamayı en dış sınırda (CDN / Tersine Vekil) konumlandır ki engellenen istekler arka uç sunucularının CPU'suna asla dokunmasın."
            ],
            "takeaways": [
                "API'nizde hız sınırlama yoksa, sisteminizin ayakta kalması en dikkatsiz istemcinizin insafına kalmıştır.",
                "Token Bucket, esneklik ve patlama toleransı için endüstri standardı algoritmadır.",
                "Zararlı trafiği kalenin en dış kapısında durdurun; iç odalara girmesine izin vermeyin."
            ],
            "udemy_prompt": "Birisi şu an API'nize 10 saniyede 10.000 istek gönderse ne olur? Sisteminiz onu engeller mi, yoksa 10.000 sorgunun hepsini veritabanına çalıştırmayı dener mi?"
        }
    ]
}
