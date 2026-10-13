# Bölüm 6: Güvenilirlik ve Hata Toleransı — Çöküş İçin Tasarlamak (Parça 21 - 24)

SECTION_6_TR = {
    "section_num": 6,
    "section_title": "Güvenilirlik ve Hata Toleransı — Çöküş İçin Tasarlamak",
    "section_desc": "Kaosun içinde ayakta kalan sistemler inşa etmek: Werner Vogels'ın hata felsefesi, devre kesiciler ve bölmelerle hasar yarıçapını izole etmek, kaos mühendisliğini silahlandırmak ve kesintisiz dağıtım yapmak.",
    "parts": [
        {
            "part_num": 21,
            "title": "Her Şey Her An Çöker: Dayanıklı Mimarın Zihniyeti",
            "subtitle": "Amazon CTO'su Werner Vogels'ın demir yasasını benimsemek ve zarif bozulma (graceful degradation) tasarlamak.",
            "duration": "9 dk",
            "war_story": "28 Şubat 2017'de bir Amazon S3 mühendisi, Virginia bölgesindeki birkaç sunucuyu devre dışı bırakmak için bir komut girdi. Komuttaki küçük bir yazım hatası hedeflenenden çok daha fazla sunucuyu sildi ve ana S3 altyapısı çöktü. S3'e bağımlı binlerce büyük şirket anında karanlığa gömüldü. Ancak en trajikomik fiyaskoyu akıllı lamba üreten bir IoT şirketi yaşadı: Lambanın arka uç servisi bir log dosyasını S3'e yükleyemediği için tüm kimlik doğrulama akışı 500 hatası fırlattı! Amerika genelinde yüz binlerce insan, Virginia'daki bir depolama servisi çöktü diye evlerinin salonundaki fiziksel lambalarını açamadı ve saatlerce karanlıkta oturdu!",
            "paradigm_shift": "Amazon CTO'su Werner Vogels'ın ünlü sözü dağıtık mimarinin özetidir: *'Her şey her an çöker.'* Diskler bozulur, ağ switch'leri takılır, bulut bölgeleri su basar ve operatörler klavyede hata yapar. Acemi bir mimar hiçbir şeyin çökmeyeceği umuduyla sistem tasarlar; usta bir mimar ise her şeyin aynı anda çökeceğini varsayarak sistemin **Zarif Bozulma (Graceful Degradation)** ile ayakta kalmasını sağlar. Öneri motoru çöktüyse genel en popüler ürünleri gösterin; analitik çöktüyse logu sessizce yutun. Kozmetik bir özelliğin ana iş sürecini rehin almasına asla izin vermeyin.",
            "core_concepts": [
                {
                    "heading": "Zarif Bozulma ve Hasar Yarıçapı (Blast Radius)",
                    "text": "- **Hasar Yarıçapı:** X Servisi çöktüğünde kullanıcıların ve özelliklerin yüzde kaçı etkileniyor? Mimarın görevi bu yarıçapı %100'den %5'e indirmektir.\n- **Zarif Bozulma:** Bir bağımlılık kapalıyken 500 hatasıyla patlamak yerine yedek planı devreye sokmak:\n  - Netflix: Kişiselleştirilmiş öneri AI'ı çökerse, herkese genel 'Top 10 Film' listesini gösterir.\n  - E-Ticaret: Stok kontrol servisi çökerse siparişi alıp 'Stok onaylanıyor' durumuna çeker ve arka planda eşitler."
                },
                {
                    "heading": "Açık Başarısızlık vs. Kapalı Başarısızlık",
                    "text": "- **Fail Closed (Güvenlik / Finans):** Dolandırıcılık tespiti servisi çöktüyse şüpheli ödemeyi reddet.\n- **Fail Open (Kullanıcı Deneyimi):** Kullanıcı profil resmi servisi çöktüyse gri bir silüet çiz ve kullanıcının panele girmesine izin ver."
                }
            ],
            "anti_patterns": [
                "**Camdan Şato:** Sistemdeki her bir parçayı varoluşsal bağımlılık yapmak: Yorumlar veya anket servisi çöktüğünde ana sayfanın komple patlaması.",
                "**Kontrolsüz Kaskad Çöküş:** Yavaşlayan tek bir arka plan servisinin tüm platformdaki işlem thread'lerini tüketerek domino etkisiyle her şeyi devirmesi.",
                "**Sessiz Yutma:** Kritik veritabanı hatalarını `try { ... } catch (Exception e) {}` içine alıp hiçbir yere loglamadan felaketleri gizlemek."
            ],
            "playbook": [
                "**1. Adım:** Bağımlılık Triage'ı yap: Servislerini Seviye 1 (Varoluşsal: Olmazsa iş durur) ve Seviye 2 (Yardımcı: Olmasa da olur) olarak etiketle.",
                "**2. Adım:** Bütün Seviye 2 bağımlılıklarına çöktüklerinde varsayılan değer dönen bir fallback mekanizması bağla.",
                "**3. Adım:** İstisnasız her ağ çağrısına 2 saniyeyi aşmayan katı bir zaman aşımı (timeout) koy."
            ],
            "takeaways": [
                "Kozmetik bir özelliğin şirketinizin ana gelir akışını rehin almasına izin vermeyin.",
                "Dayanıklılık donanımın ve ağların size ihanet edeceğini baştan kabul etmektir.",
                "Bir kriz anında %80 fonksiyonla hizmet vermeye devam eden bir sistem, %0'a çakılan bir sistemden fersah fersah üstündür."
            ],
            "udemy_prompt": "Uygulamanızın ana sayfasına bakın: Veritabanınız şu an 5 saniyelik bir kesinti yaşasa sayfanın hangi kısımları yine de render edilebilir? Kullanıcıya bozulmuş ama çalışan bir arayüz sunabiliyor musunuz?"
        },
        {
            "part_num": 22,
            "title": "Devre Kesiciler (Circuit Breakers), Bölmeler (Bulkheads) ve Üstel Geri Çekilme (Exponential Backoff)",
            "subtitle": "Kendi kendinize DDoS saldırısı yapmayı engellemek ve bir savaş gemisi gibi hasarı izole etmek.",
            "duration": "9 dk",
            "war_story": "Bir ödeme kuruluşunda döviz çevrim servisinde 100ms'lik bir gecikme yaşandı. Ana ödeme servisi agresif bir yeniden deneme (retry) kuralına sahipti: Yanıt gelmezse hemen 5 kez tekrar dene! Gecikme arttıkça gelen 1.000 kullanıcı isteği anında 6.000 eşzamanlı isteğe dönüştü ve zaten zorlanan döviz servisini bombaladı. Döviz servisi CPU %100 ile çöktü. Artık anında 503 hatası dönüyordu ama ana servis 5 kez yeniden denemeye tam gaz devam etti! Döviz servisi yeniden başlatıldığında bile biriken milyonlarca deneme isteği ayağa kalkmasına fırsat vermeden onu tekrar yıktı. Mühendisler kendi elleriyle kendilerine bir DDoS silahı inşa etmişlerdi.",
            "paradigm_shift": "Zorlanan bir bağımlılığı hemen ve durmaksızın yeniden denemek, hasta bir atı daha hızlı koşsun diye kırbaçlamaya benzer; onu öldürürsünüz. Dayanıklı dağıtık sistemler; denemeleri zamana yaymak için **Jitter ile Üstel Geri Çekilme (Exponential Backoff)**, can çekişen servise giden musluğu kapatıp nefes almasını sağlamak için **Devre Kesici (Circuit Breaker)** ve yangının diğer odalara sıçramaması için **Bölmeler (Bulkheads)** kullanır.",
            "core_concepts": [
                {
                    "heading": "Devre Kesici (Circuit Breaker) Durum Makinesi",
                    "text": "- **Kapalı (Closed - Normal):** İstekler geçer. Hatalar sayılır.\n- **Açık (Open - Devre Attı):** Hata oranı eşiği (örn: son 10 saniyede %50 başarısızlık) aşıldığında devre AÇILIR. İstekler aşağıya hiç gönderilmeden anında başarısız sayılır veya fallback döner. Arka uç nefes alır.\n- **Yarı Açık (Half-Open - Test):** 30 saniye sonra küçük bir test trafiği gönderilir. Başarılıysa Kapalı'ya döner; başarısızsa tekrar Açık duruma geçer."
                },
                {
                    "heading": "Bölme (Bulkhead) Deseni (Gemi Gövdesi İzolasyonu)",
                    "text": "Bir savaş gemisi torpido yediğinde su geçirmez bölmeleri kapatarak tek bir odanın batmasını sağlar, tüm gemi batmaz. Yazılımda da iş parçacığı (thread) ve bağlantı havuzlarını ayırın: Arka plan raporlama thread'leri asla müşteri ödeme thread'leriyle aynı havuzu paylaşmamalıdır."
                },
                {
                    "heading": "Jitter ile Üstel Geri Çekilme",
                    "text": "Yeniden deneme formülü: $\\text{bekleme} = 2^{\\text{deneme}} + \\text{rastgele\\_sapma}$. Jitter istemcilerin aynı milisaniyede hep birlikte hücum etmesini engeller."
                }
            ],
            "anti_patterns": [
                "**Kör Yeniden Deneme:** `while (error) { retry(); }` — Sistemi kurtulamaz bir ölüm döngüsüne sokmanın garantili yolu.",
                "**Zaman Aşımı Olmayan İstekler:** Bir socket bağlantısını açık bırakıp thread'i sonsuza dek askıda tutmak.",
                "**Ortak Thread Havuzu Tuzağı:** Hem kritik API isteklerini hem de 10 dakikalık PDF üretimlerini aynı thread havuzundan beslemek."
            ],
            "playbook": [
                "**1. Adım:** Dış dünya ile konuşan tüm istemcilerde Circuit Breaker (Resilience4j, Polly veya Envoy) kur.",
                "**2. Adım:** Tüm yeniden deneme kodlarına rastgele sapmalı (jitter) üstel geri çekilme ekle.",
                "**3. Adım:** Ödeme ve sepet bağlantı havuzlarını diğer tali servislerden bölmelerle (bulkhead) ayır."
            ],
            "takeaways": [
                "Karşı taraf boğulurken hızla başarısız olun (fail fast); kullanıcıyı ekranda 60 saniye bekletmeyin.",
                "Jitter içermeyen bir yeniden deneme politikası, palto giymiş bir DDoS saldırısından farksızdır.",
                "Bölmeler ana gelir kanallarınızı tali özelliklerin kurbanı olmaktan korur."
            ],
            "udemy_prompt": "Kodunuzdaki HTTP istemcilerini açın: Her istekte açıkça tanımlanmış bir zaman aşımı var mı? Hata durumunda yeniden deneme stratejiniz nasıl çalışıyor?"
        },
        {
            "part_num": 23,
            "title": "Kaos Mühendisliği (Chaos Engineering): Sistem Sizi Çökertmeden Önce Onu Bilerek Bozmak",
            "subtitle": "Netflix'in Chaos Monkey aracı sektöre yıkılmaz mimariler kurmayı nasıl öğretti?",
            "duration": "9 dk",
            "war_story": "2011 yılında Netflix, geleneksel IT yöneticilerini dehşete düşüren bir açıklama yaptı: 'Chaos Monkey' adında bir yazılım yazmışlardı ve bu yazılım mesai saatleri içinde prodüksiyonda rastgele sunucuları çatır çatır öldürüyordu! Geleneksel yöneticiler buna 'çılgınlık' dedi. Ancak Netflix mimarlarının muhteşem bir vizyonu vardı: Mühendisler masalarında kahvelerini yudumlarken sunucuların sürekli öldüğü bir ortamda, hiç kimse tek bir sunucuya bağımlı kırılgan bir sistem yazamazdı! 2012 yılında tüm bir AWS veri merkezi çöktüğünde, rakipler günlerce kapalı kalırken Netflix tek bir kullanıcının bile filmini durdurmadan yayına devam etti.",
            "paradigm_shift": "Kaos Mühendisliği rastgele ortalığı kırıp dökmek değildir; bir sistemin prodüksiyondaki çalkantılı koşullara dayanma kabiliyetine güven inşa etmek için yapılan bilimsel bir deney disiplinidir. Bir hipotez kurarsınız ('Eğer Redis ana sunucusu çökerse, uygulama 200ms gecikmeyle kopyalardan okumaya devam eder'), kontrollü bir hasar yarıçapında arızayı enjekte edersiniz, telemetriyi izlersiniz ve zayıflığı gece saat 03:00'te bir kriz patlamadan önce mesai saatinde tespit edip düzeltirsiniz.",
            "core_concepts": [
                {
                    "heading": "Kaos Mühendisliğinin Bilimsel Metodu",
                    "text": "1. **Durağan Durumu Tanımla (Steady State):** Normal durumdaki temel metrikleri ölç (Örn: Dakikadaki sipariş, P99 gecikme < 300ms, hata oranı < %0.1).\n2. **Hipotez Kur:** Arıza anında durağan durumun korunacağını öngör.\n3. **Kontrollü Hata Enjekte Et:** Gerçek dünya felaketini simüle et (bir veritabanı düğümünü kapat, ağa 500ms gecikme ekle).\n4. **Durağan Durumu Doğrula:** Kullanıcı etkilendi mi? Hipotez çöktüyse açığı buldun demektir.\n5. **Otomatize Et ve Düzelt:** Mimariyi güçlendir ve testin düzenli çalışmasını sağla."
                },
                {
                    "heading": "RTO vs. RPO: Felaket Kurtarma Metrikleri",
                    "text": "- **RTO (Recovery Time Objective):** Sistem ne kadar süre kapalı kalabilir? (Hedef: < 5 dakika).\n- **RPO (Recovery Point Objective):** Şirket ne kadar veri kaybına dayanabilir? (Hedef: 0 işlem)."
                }
            ],
            "anti_patterns": [
                "**Gözleme Dayalı Olmayan Kaos:** İzleme panoları ve uyarıları tam olmayan bir sisteme hata basıp deneyi körü körüne bir felakete çevirmek.",
                "**İlk Günden Büyük Patlama:** Test ortamında hiç denemeden ilk günden ana canlı veritabanını kapatmaya kalkışmak.",
                "**Kağıt Üstünde Felaket Planı:** Beş yıldır hiç tatbikatı yapılmamış, dolapta duran 200 sayfalık tozlu 'Felaket Kurtarma Kitapçığı'."
            ],
            "playbook": [
                "**1. Adım:** Test ortamında bir 'Kaos Günü' düzenle: Üçüncü parti ödeme servisinin bağlantısını kesip arayüzün nasıl davrandığını izle.",
                "**2. Adım:** Test ortamında rastgele konteyner öldürmeyi otomatikleştir (Chaos Mesh ile).",
                "**3. Adım:** Veritabanı devretme (failover) tatbikatı yap: Otomatik yedek sunucuya geçişin gerçekten çalıştığını doğrula."
            ],
            "takeaways": [
                "Kaosun olup olmayacağını siz seçemezsiniz; kaos sizi seçer. Kaos mühendisliği ne zaman ve nasıl olacağını seçmenizi sağlar.",
                "Test edilmemiş bir yedek veya otomatik geçiş mekanizması sadece tatlı bir hayaldir.",
                "Kontrollü küçük deneylerle sisteme olan güveninizi adım adım inşa edin."
            ],
            "udemy_prompt": "Ekibiniz en son ne zaman ana veritabanı çöktüğünde ne olacağını test etti? Otomatik geçiş çalıştı mı yoksa manuel müdahale mi gerekti?"
        },
        {
            "part_num": 24,
            "title": "Sıfır Kesintili Dağıtımlar: Mavi-Yeşil (Blue-Green), Kanarya (Canary) ve Özellik Bayrakları (Feature Flags)",
            "subtitle": "Kullanıcılarınızı ve nöbetçi ekibinizi dehşete düşürmeden günde 50 kez canlıya kod çıkmak.",
            "duration": "9 dk",
            "war_story": "Bir bordro SaaS şirketinin her Cumartesi gece 02:00'de planlı bakım penceresi vardı. Geliştiriciler bu saatten nefret ederdi. Bir hafta sonu 80 milyon satırlık bir tabloya `NOT NULL` kolon ekleyen bir veritabanı migrasyonu çalıştırıldı. Tablo kilitlendi. Sunucular zaman aşımına düştü. Sabah 05:00'te ekip panikle sürümü geri almaya (rollback) çalıştı ama ara şema değişiklikleri yüzünden geri alma komutları da patladı! Sistem Pazartesi 11:00'e kadar kapalı kaldı. Binlerce şirket çalışanlarının maaşlarını yatıramadı ve şirket 600.000 dolarlık kurumsal sözleşme iptalleriyle sarsıldı.",
            "paradigm_shift": "'Bakım penceresi' kavramı 1990'ların antika bir alışkanlığıdır. Modern yazılım mimarisi sıfır kesintili sürekli dağıtımı zorunlu kılar. Kod dağıtmak (sunuculara dosya kopyalamak) ile özellik yayınlamak (kullanıcıların erişimine açmak) birbirinden tamamen koparılmalıdır. **Mavi-Yeşil Dağıtım**, **Kanarya Sürümleri** ve **Özellik Bayrakları (Feature Flags)** ile riski neredeyse sıfıra indirerek gün ortasında canlıya çıkabilirsiniz.",
            "core_concepts": [
                {
                    "heading": "Sıfır Kesintili Dağıtım Stratejileri",
                    "text": "- **Mavi-Yeşil (Blue-Green):** Biri canlı (Mavi), diğeri boşta (Yeşil) iki özdeş ortam. Yeni sürüm Yeşile kurulur, duman testleri yapılır. Yönlendirici bir saniyede trafiği Mavi'den Yeşil'e çevirir. Sorun çıkarsa 1 saniyede geri dönülür.\n- **Kanarya (Canary):** Trafiğin %2'si yeni sürüme yönlendirilir. Metrikler 15 dakika izlenir. Sorun yoksa kademeli olarak %10, %50 ve %100'e çıkarılır.\n- **Özellik Bayrakları (Feature Flags):** Kod canlıya kapalı olarak atılır. Ürün yöneticisi panodan özelliği belirli kullanıcılara tek tıkla açar."
                },
                {
                    "heading": "Genişlet ve Daralt Kalıbı (Expand & Contract)",
                    "text": "Veritabanı kolonunu asla tek seferde yeniden adlandırmayın! 3 aşama izleyin:\n1. **Genişlet:** Yeni kolonu ekle. Uygulama hem eskiye hem yeniye yazsın.\n2. **Göç:** Arka planda eski verileri yeniye kopyala.\n3. **Daralt:** Okumaları yeniye al ve bir sonraki sprintte eski kolonu güvenle sil."
                }
            ],
            "anti_patterns": [
                "**Büyük Patlama (Big Bang) Sürümü:** 45 özelliği ve 6 veritabanı migrasyonunu iki ayda bir gecenin köründe tek seferde canlıya almaya kalkışmak.",
                "**Yıkıcı Veritabanı Değişikliği:** Canlı trafik akarken kolon silmek veya isim değiştirmek; çalışan eski sunucuların anında çökmesi.",
                "**Özellik Bayrağı Borcu:** Kullanılmış bayrakları koddan temizlemeyip kod tabanını iç içe geçmiş if-else çöplüğüne çevirmek."
            ],
            "playbook": [
                "**1. Adım:** API Gateway veya Ingress seviyesinde Kanarya yönlendirmeyi kur (trafiğin %5'ini yeni pod'lara ver).",
                "**2. Adım:** Bütün veritabanı değişikliklerinde 'Genişlet ve Daralt' kuralını zorunlu kıl.",
                "**3. Adım:** Kritik her yeni iş özelliğini bir Feature Flag arkasına alarak canlıya al."
            ],
            "takeaways": [
                "Kod canlıya almak heyecanlı bir kriz değil; sıkıcı, rutin bir iş olmalıdır.",
                "Teknik dağıtım ile işlevsel yayını özellik bayraklarıyla birbirinden ayırın.",
                "Veritabanı şema değişikliklerini her zaman çalışan eski kodla geriye dönük uyumlu tutun."
            ],
            "udemy_prompt": "Ekibiniz veritabanı migrasyonlarını nasıl yapıyor? Bir migrasyon yarıda patlasa, sistemi kapatmadan veya veri kaybetmeden geri dönebiliyor musunuz?"
        }
    ]
}
