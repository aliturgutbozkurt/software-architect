# Bölüm 3: Veri Mimarisi — Durumun Yaşadığı, Öldüğü ve Yalan Söylediği Yer (Parça 09 - 12)

SECTION_3_TR = {
    "section_num": 3,
    "section_title": "Veri Mimarisi — Durumun Yaşadığı, Öldüğü ve Yalan Söylediği Yer",
    "section_desc": "İş dünyasının durum temelini tasarlamak: doğru depolama motorlarını seçmek, indeksleme ve kopyalarla darboğazları kırmak, tutarlılık modellerini yönetmek ve önbellek canavarını evcilleştirmek.",
    "parts": [
        {
            "part_num": 9,
            "title": "Çoklu Veri Kalıcılığı (Polyglot Persistence): Veriniz İçin Doğru Silahı Seçmek",
            "subtitle": "Tüm uygulama verisini tek bir SQL tablosuna veya Mongo koleksiyonuna tıkmanın mimari gafleti.",
            "duration": "9 dk",
            "war_story": "Bir sosyal ağ uygulamasında her şey tek bir PostgreSQL veritabanında tutuluyordu. 'Arkadaşlarımın Arkadaşları' öneri özelliği eklendiğinde, 12 milyon satırlık ilişki tablosu üzerinde 6 seviyeli özyinelemeli (recursive) bir SQL join sorgusu çalıştırıldı. Yoğun saatlerde her kullanıcı akışını yenilediğinde veritabanı CPU'su %100'e vuruyor ve tablo 15 saniye kilitleniyordu. Ekip, 'NoSQL çok hızlı' diyerek tüm şirketi MongoDB'ye taşımaya karar verdi. Üç ay sonra gördüler ki, ACID işlemleri olmadan bakiye kontrolü yapmak kullanıcı bakiyelerinin binlerce lira kaymasına ve çift harcamalara yol açtı! İlişkisel sorgu darboğazını çözmek isterken veri bütünlüğü kabusuna saplanmışlardı.",
            "paradigm_shift": "Kod gelip geçicidir; veri ise kalıcıdır. Martin Fowler'ın kavramsallaştırdığı **Polyglot Persistence**, tek bir mimaride farklı veri ihtiyaçları için farklı depolama teknolojilerini kullanma disiplinidir. Çekiçle vida sıkamazsınız. İlişkisel veritabanları (RDBMS) finansal işlemler ve karmaşık birleştirmelerde; Doküman depoları esnek ürün kataloglarında; Anahtar-Değer (Key-Value) depoları mikro saniyelik önbelleklerde; Çizge (Graph) veritabanları ise karmaşık ağ ilişkilerinde rakipsizdir.",
            "core_concepts": [
                {
                    "heading": "Modern Veri Silahları Cephaneliği",
                    "text": "- **İlişkisel (PostgreSQL, MySQL):** Şema güvenliği, ACID işlemleri, güçlü SQL birleştirmeleri. İş dünyasının %90'ı için varsayılan tercih.\n- **Anahtar-Değer (Redis, DynamoDB):** O(1) erişim hızı, oturum yönetimi, oran sınırlama (rate limiting).\n- **Doküman (MongoDB):** Hiyerarşik JSON yapıları, değişken ürün katalogları ve içerik yönetim sistemleri.\n- **Zaman Serisi / Geniş Sütun (TimescaleDB, Cassandra):** Yüksek yazma hacmi, IoT sensör logları ve finansal işlem akışları.\n- **Çizge (Neo4j):** Dolandırıcılık tespiti, sosyal ağlar ve izin hiyerarşileri."
                },
                {
                    "heading": "Temel Kural: Suçu Kanıtlanana Kadar PostgreSQL",
                    "text": "PostgreSQL'in (JSONB, tam metin arama ve indeksleriyle) yetersiz kaldığını telemetriyle kanıtlamadan egzotik veritabanlarına atlamayın. Her yeni veritabanı ekibi operasyonel olarak böler."
                }
            ],
            "anti_patterns": [
                "**Altın Çekiç Sendromu:** En sevdiği veritabanını (ister SQL ister Mongo) dünyadaki her sorunun çözümü sanmak.",
                "**Veritabanı Hayvanat Bahçesi:** 6 kişilik yazılım ekibinin prodüksiyonda 7 farklı veritabanı teknolojisini koşturmaya çalışması.",
                "**Eşzamanlı Çift Yazma:** Uygulama katmanında aynı anda hem PostgreSQL'e hem Elasticsearch'e yazmaya çalışıp ağ hatasında arama sonuçlarının veritabanıyla kalıcı olarak çelişmesine sebep olmak."
            ],
            "playbook": [
                "**1. Adım:** Veritabanı seçmeden önce veri erişim modellerini analiz et: Okuma ağırlıklı mı, yazma ağırlıklı mı, ilişki ağırlıklı mı?",
                "**2. Adım:** SQL join gecikmeleri 500ms'yi aşıyorsa, özel bir veri deposuna geçmeden önce 'okuma odaklı projeksiyon tablosu' oluşturmayı dene.",
                "**3. Adım:** İkincil arama motorlarını (Elasticsearch) ana veritabanından beslerken Change Data Capture (Debezium) mimarisi kur."
            ],
            "takeaways": [
                "Veri modelleri sistem mimarisini programlama dillerinden çok daha fazla dikte eder.",
                "PostgreSQL ile başlayın; yalnızca net bir sorgu darboğazı kanıtlandığında özelleşmiş depolara ayrılın.",
                "İki farklı veritabanına aynı anda senkron yazıyorsanız, elinizde saatli bir bomba tutuyorsunuz demektir."
            ],
            "udemy_prompt": "Şirketinizdeki veri modellerini inceleyin: İlişkisel tablolar içinde derin JSON aramaları mı yapıyorsunuz, yoksa NoSQL içinde karmaşık join simülasyonları mı? Bu durum performansı nasıl etkiliyor?"
        },
        {
            "part_num": 10,
            "title": "Veritabanı Darboğazı: İndeksleme, Parçalama (Sharding) ve Okuma Kopyaları",
            "subtitle": "Trafik 100 katına çıktığında ve sorgular sürünmeye başladığında veritabanınızı nasıl ölçeklersiniz?",
            "duration": "9 dk",
            "war_story": "Efsane Cuma gecesi 00:01'de bir e-ticaret sitesinin trafiği 2.000'den 80.000 eşzamanlı kullanıcıya fırladı. 90 saniye içinde veritabanı bağlantı havuzu tükendi. Bütün API sunucuları tek bir sorguya kilitlenmişti: `SELECT * FROM urunler WHERE kategori = 'elektronik' AND durum = 'aktif' ORDER BY ekleme_tarihi DESC`. Tabloda 40 milyon satır vardı ve ilgili kolonlarda birleşik (composite) indeks yoktu! Her arama diskten 14 GB veri okuyup tablo taraması (full table scan) yapıyordu. Sunucu çöktü. İki katı büyüklükte RAM ve CPU'ya sahip bir sunucuya geçtiler, o da 4 dakika sonra çöktü. Kesinti 6 saat sürdü ve şirket 1.8 milyon dolar ciro kaybetti.",
            "paradigm_shift": "Veritabanına daha fazla CPU ve RAM basmak (Dikey Ölçekleme) en kolay yoldur ancak sert bir fiziksel ve mali sınıra çarpar. Veritabanı yavaşladığında acemi geliştirici mikroservis diye bağırır; usta mimar ise sorgu planlayıcısını inceler, eksik bileşik indeksleri ekler, okuma trafiğini kopyalara (read replicas) dağıtır ve sadece kaçınılmaz olduğunda yatay parçalamaya (sharding) gider.",
            "core_concepts": [
                {
                    "heading": "Veritabanı Ölçekleme Merdiveni",
                    "text": "1. **1. Basamak: Sorgu ve İndeks Optimizasyonu:** `EXPLAIN ANALYZE` ile incele. B-Tree indeksleri ve kolon sırasının kritik olduğu bileşik indeksleri (önce eşitlik, sonra aralık sorgulanan kolonlar) doğru kur.\n2. **2. Basamak: Okuma Kopyaları ve Bağlantı Havuzlama:** Yazma trafiği Ana (Primary) sunucuya gider; okuma trafiği 3-4 Kopya (Replica) sunucuya dağıtılır. PgBouncer ile bağlantı havuzu yönetilir.\n3. **3. Basamak: Yatay Parçalama (Sharding):** Veriyi bir parçalama anahtarıyla (`kullanici_id % parca_sayisi`) bağımsız veritabanı sunucularına paylaştırmak."
                },
                {
                    "heading": "Kopya Gecikmesi (Replication Lag) Tuzağı",
                    "text": "Okuma kopyaları asenkrondur. Kullanıcı profilini güncelleyip hemen sayfayı yenilediğinde, okuma sorgusu henüz güncellenmemiş bir kopyaya düşerse eski halini görür! Çözüm: Yazma yapıldıktan sonraki 2 saniye boyunca okumaları da Ana sunucudan yapmak (Read-Your-Own-Writes)."
                }
            ],
            "anti_patterns": [
                "**Kör ORM Güveni:** Arka planda nasıl devasa sorgular ürettiğini bilmeden ORM'lerin oluşturduğu n+1 sorgularına göz yummak.",
                "**Aşırı İndeksleme:** 'İleride lazım olur' diye tablodaki her kolona indeks koyup yazma hızını %400 yavaşlatmak (çünkü her insert'te 15 ayrı B-Tree güncellenir).",
                "**Yanlış Parçalama Anahtarı:** Zamana göre sharding yapıp gelen tüm yeni yazma trafiğinin sadece en son sunucuya yüklenmesine yol açmak."
            ],
            "playbook": [
                "**1. Adım:** `pg_stat_statements` veya yavaş sorgu loglarını açıp veritabanı CPU'sunun %80'ini tüketen ilk 5 sorguyu tespit et.",
                "**2. Adım:** En yavaş sorguda `EXPLAIN (ANALYZE, BUFFERS)` çalıştırıp Seq Scan yerine Index Scan yapıldığından emin ol.",
                "**3. Adım:** Ağır analitik ve rapor sorgularını canlı veritabanından ayırıp özel bir salt-okunur kopyaya yönlendir."
            ],
            "takeaways": [
                "Tek bir eksik bileşik indeks, 2 milisaniyelik sorguyu 15 saniyelik bir sistem katiline dönüştürebilir.",
                "Veritabanını sharding ile bölmeye 100 bin dolar harcamadan önce, indekslemeye 1 saat ayırın.",
                "Asenkron okuma kopyaları kullanıyorsanız, kullanıcının kendi yazdığını anında görebilme garantisini tasarlayın."
            ],
            "udemy_prompt": "Projenizdeki en kritik arama sorgusunda `EXPLAIN ANALYZE` çalıştırın. Tablo taraması mı yapıyor, indeks taraması mı? Kaç satır filtreleniyor?"
        },
        {
            "part_num": 11,
            "title": "ACID vs. BASE Karşılaşması: Gerçek Dünyada Tutarlılık Modelleri",
            "subtitle": "CAP Teoremini yönetmek: Mükemmelliği mi yoksa ayakta kalmayı mı seçiyorsunuz?",
            "duration": "9 dk",
            "war_story": "Bir dijital cüzdan girişimi, yüksek işlem hacmini kaldırabilmek için BASE semantiğine sahip (Eventually Consistent) bir NoSQL veritabanı seçti. Bir Cuma akşamı bir üniversite öğrencisi, ATM'den 200 TL çekerken aynı saniyede mobil uygulamadan arkadaşına 200 TL transfer ettiğinde her iki işlemin de başarılı olduğunu keşfetti; çünkü dağıtık düğümler henüz bakiyeyi eşitlememişti! Hile TikTok'ta yayıldı. 48 saat içinde 10.000 kullanıcı sistemden 3.2 milyon TL çekti. Şirket API'yi kapatmak ve acil sermaye artırımına gitmek zorunda kaldı.",
            "paradigm_shift": "CAP teoremi (Tutarlılık, Erişilebilirlik, Bölünme Toleransı) akademik bir felsefe değil; dağıtık sistemlerin yerçekimi kanunudur. Ağda bir kopma veya gecikme olduğunda Sistem Tutarlılığı (yanlış veri vermemek için isteği reddetmek) ile Sistem Erişilebilirliği (veri bayat bile olsa isteğe yanıt vermek) arasında bir seçim yapmak ZORUNDASINIZ. Para işlemleri mutlak ACID ister; sosyal medyadaki beğeni sayıları ise BASE ile harika yaşar.",
            "core_concepts": [
                {
                    "heading": "ACID ve BASE Felsefesi",
                    "text": "- **ACID (Geleneksel RDBMS):**\n  - *Atomicity:* Ya hep ya hiç.\n  - *Consistency:* Veritabanı kuralları daima korunur.\n  - *Isolation:* Eşzamanlı işlemler birbirini bozmaz.\n  - *Durability:* Onaylanan işlem elektrik kesilse de kaybolmaz.\n- **BASE (Dağıtık NoSQL):**\n  - *Basically Available:* Sistem her zaman yanıt vermeye çalışır.\n  - *Soft State:* Veri arka planda senkronize olurken durum değişebilir.\n  - *Eventual Consistency:* Yeni güncelleme gelmezse tüm kopyalar eninde sonunda eşitlenir."
                },
                {
                    "heading": "PACELC Teoremi (CAP'in Ötesi)",
                    "text": "Bölünme (**P**artition) anında **A**vailability mi yoksa **C**onsistency mi seçiyorsun? Normal zamanda (**E**lse) ise **L**atency mi yoksa **C**onsistency mi seçiyorsun? Kıtalararası sistemlerde ışık hızını aşamazsınız; güçlü tutarlılık mutlaka gecikme vergisi ödetir."
                }
            ],
            "anti_patterns": [
                "**Milisaniyelik Masalı:** 'Eventual' kelimesini '2 milisaniyede eşitlenir' sanıp ağ koptuğunda kopyaların 10 dakika geriden gelmesine hazırlıksız yakalanmak.",
                "**Kıtalararası 2PC Fantezisi:** Kıtalar arasında 2-Phase Commit ile dağıtık ACID sağlamaya çalışıp işlem sürelerini 800ms'ye fırlatmak.",
                "**İzolasyon Seviyesi Körlüğü:** Birçok veritabanında varsayılan seviyenin `Read Committed` olduğunu ve fantom okumalara izin verdiğini bilmeden 'nasılsa ACID' rahatlığına kapılmak."
            ],
            "playbook": [
                "**1. Adım:** Verilerini ikiye ayır: 'Asla yanılmaması gerekenler' (Finans, Stok) vs. 'Geçici olarak bayat kalabilecekler' (İzlenme sayısı, Beğeniler).",
                "**2. Adım:** Finansal çekirdeği güçlü ACID ilişkisel veritabanında tut.",
                "**3. Adım:** Dağıtık servisler arasında ACID kilitleri yerine telafi edici işlemler (Saga) tasarla."
            ],
            "takeaways": [
                "Fiziği yenemezsiniz: Dağıtık düğümlerde yüksek erişilebilirlik anlık tutarlılıktan ödün vermeyi gerektirir.",
                "Bakiye ve bilet mutlak tutarlılık ister; sosyal akış ve öneriler eventual consistency ile yaşar.",
                "Eventual consistency seçtiyseniz, çakışma anında iş biriminin ne yapacağını önceden planlamalısınız."
            ],
            "udemy_prompt": "Ürününüzde güçlü tutarlılık kullanan bir özellik seçin. Bu veri 2 saniye gecikmeli gelseydi iş birimi gerçekten zarar görür müydü? Ne kazanırdınız?"
        },
        {
            "part_num": 12,
            "title": "Önbellekleme Stratejileri: Bilgisayar Biliminin İki Zor Şeyinden Biri",
            "subtitle": "Sistemi bayat veya hayalet verilerle zehirlemeden performansı 10 katına çıkarmanın yolları.",
            "duration": "9 dk",
            "war_story": "Bir spor yayın platformu veritabanını rahatlatmak için kullanıcı abonelik yetkilerini Redis'te 24 saat önbelleğe aldı. Bir kullanıcı derbi maçını izlemek için 'Standart' paketten 'Süper Lig VIP' paketine yükseltme yaptı. Kartından anında 499 TL çekildi. Ancak maçı açmak istediğinde ekranda 'Bu yayını izlemek için paketinizi yükseltin' uyarısı çıktı. Tekrar satın aldı, kartından bir 499 TL daha çekildi! Maç boyunca 40.000 kişi aynı hatayı yaşayıp şirketi sosyal medyada linç etti. Neden mi? Satın alma servisi veritabanını güncellemişti ancak önbellek anahtarını temizleyen hiçbir kod yoktu; sistem 24 saatlik sürenin (TTL) dolmasını bekliyordu!",
            "paradigm_shift": "Phil Karlton'ın efsanevi sözü mimarları yıllardır uyarır: 'Bilgisayar biliminde sadece iki zor problem vardır: Önbellek geçersiz kılma (cache invalidation) ve isimlendirme.' Önbellek sihirli bir hız butonu değildir; aynı gerçeğin iki kopyasını tutma yönünde açık bir karardır. Önbellek eklediğiniz anda tutarsızlık, bayat veri ve izdiham (stampede) risklerini kabul etmiş olursunuz.",
            "core_concepts": [
                {
                    "heading": "Temel Önbellekleme Modelleri",
                    "text": "- **Cache-Aside (Tembel Yükleme):** Uygulama önce önbelleğe bakar. Yoksa veritabanından okur, önbelleğe yazar ve döner. En yaygın ve güvenli model.\n- **Write-Through:** Uygulama önbelleğe yazar, önbellek katmanı anında veritabanına yazar. Her zaman tazedir, ancak yazma gecikmesi artar.\n- **Write-Behind (Gecikmeli Yazma):** Uygulama önbelleğe yazar, önbellek arka planda asenkron olarak DB'ye aktarır. Çok hızlıdır ama Redis çökerse veri kaybı riski taşır."
                },
                {
                    "heading": "Önbellek İzdihamı (Cache Stampede / Thundering Herd)",
                    "text": "Saniyede 10.000 istek alan popüler bir anahtarın süresi tam 12:00:00'da dolduğunda, aynı milisaniyede 10.000 isteğin hepsi önbelleği boş bulup veritabanına hücum eder ve veritabanını anında çökertir. Çözüm: Dağıtık kilitler (SingleFlight) ve rastgele TTL esnetmesi (Jitter)."
                }
            ],
            "anti_patterns": [
                "**Geçersiz Kılma Kancası Eksikliği:** Veritabanında satırı güncelleyip Redis'teki eski anahtarı silmeyi unutmak.",
                "**Sonsuz Önbellek:** TTL belirlemeden Redis'e veri basıp belleğin dolmasıyla sunucuyu OOM (Out of Memory) ile patlatmak.",
                "**İş Mantığını Önbelleğe Almak:** 10 farklı değişkene bağlı karmaşık hesaplama sonuçlarını önbelleğe alıp bir değişken değiştiğinde geçersiz kılmayı imkansız hale getirmek."
            ],
            "playbook": [
                "**1. Adım:** İstisnasız her önbellek anahtarına bir TTL (Yaşam Süresi) tanımla.",
                "**2. Adım:** Yazma anında önbellekteki veriyi değiştirmek yerine doğrudan sil (`DEL key`). Bırakın bir sonraki okuma veritabanından tazesini getirsin.",
                "**3. Adım:** Bütün TTL'lere rastgele sapma (jitter) ekle: `TTL = 300sn + rand(0, 60sn)`. Böylece tüm anahtarlar aynı saniyede düşmez."
            ],
            "takeaways": [
                "Önbellek bir performans hızlandırıcıdır, birincil veritabanı değildir. Önbellek silindiğinde sisteminiz çöküyorsa mimarisi bozuktur.",
                "Yazma anında önbelleği güncellemektense anahtarı silmek her zaman daha güvenlidir.",
                "İzdihamı önlemek için TTL sürelerine mutlaka rastgele varyasyon (jitter) ekleyin."
            ],
            "udemy_prompt": "Redis veya Memcached kümenizi inceleyin: TTL tanımlanmamış anahtarlar var mı? Redis sunucunuz şu an aniden yeniden başlasa ana veritabanınız ayakta kalabilir mi?"
        }
    ]
}
