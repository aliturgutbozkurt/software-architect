# Bölüm 1: Büyük Uyanış — Mimar Olarak İlk Gün (Parça 01 - 04)

SECTION_1_TR = {
    "section_num": 1,
    "section_title": "Büyük Uyanış — Mimar Olarak İlk Gün",
    "section_desc": "Akıllı algoritmalar yazmaktan; insanlara, ölçeğe ve zamana meydan okuyan dayanıklı sistemler tasarlamaya uzanan zihinsel ve teknik sıçrama.",
    "parts": [
        {
            "part_num": 1,
            "title": "Kod Yazmanın Yetmediği Gün: Bir Yazılım Mimarı Aslında Ne Yapar?",
            "subtitle": "Pazartesi sabahı sprint panosunda sana atanmış tek bir Jira görevi bile olmadığını fark ettiğin an.",
            "duration": "8 dk",
            "war_story": "Mert, şirketin efsanevi 10x kıdemli yazılımcısıydı. Öğle yemeğine çıkmadan önce 4.000 satırlık spagetti TypeScript kodunu tek başına refactor edebilir, uykusunda veritabanı sorgularını optimize edebilirdi. Cuma günü akşamüzeri Mühendislikten Sorumlu Başkan Yardımcısı sırtını sıvazladı: 'Mert, artık yeni Yazılım Mimarımız sensin!' Pazartesi sabahı 09:00'da Mert heyecanla masasına oturdu, IDE'sini açtı ve sprint panosuna baktı. Kendisine atanmış tek bir bilet bile yoktu. Takım liderine gidip 'Bana ne iş var?' diye sordu. Aldığı yanıt donup kalmasına yetti: 'Biz ne inşa edeceğimizi sana soracaktık.' Mert, kendini faydalı hissetmek için öğleye kadar açık kaynaklı bir kütüphanenin girintilerini düzeltti. Saat 14:00 olduğunda acı gerçeği anladı: Artık kimse ona bir yol haritası vermeyecekti. Yol haritasını çizen kişi artık bizzat kendisiydi.",
            "paradigm_shift": "Bir geliştiriciyken değerin somut çıktılarla ölçülürdü: birleştirilen pull request'ler, çözülen bug'lar, yazılan satırlar. Bir mimar olarak ise para birimin karar kalitesi, sistem sınırları ve organizasyonel uyumdur. Ralph Johnson'ın meşhur tanımıyla mimarlık: 'Gelecekte değiştirilmesi zor olan tüm kararlardır.' Eğer üretkenliğini IDE'de yazdığın kod satırıyla ölçmeye devam edersen, mimarlık rolünde kendini sürekli işsiz ve yetersiz hissedersin. Senin işin artık roket motorunu tek başına inşa etmek değil; bir bisiklete roket motoru takmaya kalkışmadığımızdan emin olmaktır.",
            "core_concepts": [
                {
                    "heading": "Yazılım Mimarisinin Üç Temel Direği",
                    "text": "1. **Yapı ve Ayrıştırma (Decomposition):** Karmaşık ve anlaşılmaz devasa bir iş probleminin, net sınırlarla yönetilebilir küçük modüllere bölünmesi.\n2. **Sistem Nitelikleri (The '-ilities'):** Ölçeklenebilirlik, erişilebilirlik, bakım kolaylığı, güvenlik ve test edilebilirlik. Bir sistem işlevsel olarak kusursuz çalışsa bile yük altında 14 saniyede yanıt veriyorsa mimari açıdan ölüdür.\n3. **Ödünleşme Yönetimi (Trade-offs):** Her mimari seçimin içinde hem avantajları hem de gizli bakım vergilerini barındıran bir paket anlaşma olduğunu kabul etmek."
                },
                {
                    "heading": "Mimarın Zaman Ufku",
                    "text": "Geliştiriciler mevcut sprint içinde yaşar (1-2 hafta). Takım liderleri çeyreklik hedeflere bakar (3 ay). Yazılım mimarı ise 1 ila 3 yıllık ufukta yaşamak zorundadır. Şirket başarılı olduğunda trafiğin, veri hacminin ve ekip büyüklüğünün nereye varacağını bugünden öngörmeli, ancak bugünden gereksiz spekülatif aşırı-mühendislik tuzağına düşmemelidir."
                }
            ],
            "anti_patterns": [
                "**Fildişi Kule Astronotu:** Kod tabanından tamamen kopup kimsenin okumadığı ve gerçekte uygulanamayacak 80 sayfalık Visio diyagramları çizen mimar.",
                "**Gizli Kod Korsanı:** Toplantılardan bunalıp gece 23:00'te sisteme gizlice girerek junior geliştiricilerin kodlarını 'anlatmakla vakit kaybetmeyeyim' diyerek yeniden yazan mimar.",
                "**Hacker News Turisti:** Hacker News'te gördüğü her yeni ve deneysel teknolojiyi prodüksiyona sokup şirketi alfa sürüm kobayına çeviren mimar."
            ],
            "playbook": [
                "**1. Adım:** Sistemin mevcut 'Değiştirilmesi En Zor' kararlarının envanterini çıkar: Veritabanı, ana mesajlaşma protokolü ve monolit sınırları.",
                "**2. Adım:** Ekipten en çok şikayet eden 3 kıdemli yazılımcıyla 30'ar dakikalık birebir görüş: 'Mevcut mimari her gün hangi noktada canınızı sıkıyor?'",
                "**3. Adım:** Temel başarım metriğini belirle: Mimari akış hızı (Yeni bir geliştirici, sistemi çökertme korkusu yaşamadan ne kadar hızla güvenli kod canlıya alabiliyor?)."
            ],
            "takeaways": [
                "Mimarlık kutu çizmek değil; gelecekte hangi dertlerden muzdarip olmak istediğini bugünden seçmektir.",
                "Kod, yazılımcı için bir varlık (asset); mimar için ise bir yükümlülüktür (liability). Yazılan her satır kod güncellenmek, yamalanmak ve bakımı yapılmak zorundadır.",
                "En iyi mimarlar kodu başkalarına iş bırakmamak için değil, problemi derinlemesine hissetmek için yazar."
            ],
            "udemy_prompt": "Şu an çalıştığın projeyi düşün: 2 yıl önce alınan ve bugün tüm ekibin şikayet ettiği tek bir mimari karar söyle. O gün o kararın mantıklı görünmesini sağlayan şartlar neydi?"
        },
        {
            "part_num": 2,
            "title": "CV Odaklı Geliştirmeden (RDD) Kaçış: Sıkıcılık vs. İş Gerçekleri",
            "subtitle": "45 kullanıcılı şirket içi bir admin panelinin neden Rust, Kafka ve CockroachDB kümesine ihtiyacı yoktur?",
            "duration": "8 dk",
            "war_story": "Hızla büyüyen bir e-ticaret girişiminde, müşteri temsilcilerinin iade işlemlerini onayladığı 45 kişilik dahili bir portal vardı. Ekibin yeni lideri, Big Tech mülakatlarında havalı görünmek adına bu basit CRUD panelini Apache Kafka, Rust mikro-servisleri ve CockroachDB dağıtık veritabanı kullanarak 'olaya dayalı (event-driven)' mimariye geçirmeye ikna etti. Altı ay sonra bir ağ gecikmesi sırasında Kafka consumer offset'leri kilitlendi. Basit bir 100 TL'lik iade işlemi 48 dakika sürmeye başladı. Üstelik Rust bellek yönetimini anlayan tek geliştirici istifa edip bir kripto şirketine geçmişti! Sistem çöktü ve tüm panel iki haftasonunda basit bir Django uygulamasıyla sıfırdan yeniden yazılmak zorunda kaldı.",
            "paradigm_shift": "CV Odaklı Geliştirme (Resume-Driven Development - RDD), teknoloji şirketlerinin gizli katilidir. Deneyimsiz yazılımcılar zekalarını ve yetkinliklerini kanıtlamak için en karmaşık araçları seçer; bilge mimarlar ise bilgeliklerini kanıtlamak için en sade ve sıkıcı araçları seçer. Dan McKinley'in altın kuralı: 'Sıkıcı Teknolojiyi Seçin (Choose Boring Technology).' Bir şirketin harcayabileceği yalnızca 3 'İnovasyon Jetonu' vardır. O jetonları şirketinizi rakiplerinizden ayıran temel iş mantığına harcayın; oturum çerezlerini nasıl sakladığınıza değil.",
            "core_concepts": [
                {
                    "heading": "İnovasyon Jetonu Bütçesi (Dan McKinley)",
                    "text": "Her şirketin sınırlı bir operasyonel risk bütçesi vardır. Alışılmadık bir veritabanı seçtiğinde bir jeton harcarsın. Yeni ve popüler bir dil seçtiğinde bir jeton daha gider. Tüm jetonlarını altyapı borularına harcarsan, şirkete para kazandıracak yenilikçi özellikleri üretmeye sıfır jetonun kalır."
                },
                {
                    "heading": "Toplam Sahip Olma Maliyeti (TCO)",
                    "text": "Teknolojinin maliyeti asla lisans bedeli değildir. Asıl maliyet; gecenin 3'ünde çalan çağrı cihazları, o dilde mühendis bulma zorluğu ve yıllarca süren versiyon yükseltme sancılarıdır. Dünyada 50.000 mühendisin uzman olduğu sıkıcı bir PostgreSQL, GitHub'da üç akademisyenin geliştirdiği egzotik bir dağıtık graf veritabanından fersah fersah daha ucuzdur."
                }
            ],
            "anti_patterns": [
                "**LinkedIn İstifçisi:** Kararları salt Netflix veya Google'ın iş ilanlarında çok geçiyor diye alan mühendis.",
                "**Erken Gezegensel Ölçekleyici:** Henüz 300 aktif kullanıcısı varken sistemi 500 milyon eşzamanlı kullanıcı kaldıracak şekilde tasarlayan mimar.",
                "**Burada Üretilmedi (NIH) Sendromu:** Redis'in 'fazla hantal' olduğunu iddia edip şirket içinde kendi bellek içi önbellek motorunu yazmaya kalkanlar."
            ],
            "playbook": [
                "**1. Adım:** Canlı ortamındaki farklı programlama dillerini ve veritabanı türlerini listele. Sayı 4'ü aşıyorsa tehlike çanları çalıyor demektir.",
                "**2. Adım:** Önerilen her yeni havalı teknolojiye 'Sıkıcı Teknoloji Testi' uygula: 'Bunu standart PostgreSQL ve basit kuyruklarla çözseydik ne kaybederdik?'",
                "**3. Adım:** İşe alım hızını hesapla: Bu teknolojiyi yazan kıdemli yarın ayrılsa, yerine birini bulup adapte etmek kaç ay sürer?"
            ],
            "takeaways": [
                "Usta bir mimarın alameti farikası, karmaşık problemleri basitleştirmesidir; basit problemleri karmaşıklaştırması değil.",
                "Sıkıcı teknoloji geceleri huzurla uyumanı sağlar; havalı teknoloji seni geceleri ücretsiz test kullanıcısına çevirir.",
                "Müşterinin tek ihtiyacı sağlam ahşap bir bank iken, üzerine dağıtık uzay istasyonu kurma."
            ],
            "udemy_prompt": "Şirketinizin mevcut teknoloji yığınına bakın. Sırf heyecan veya trend olduğu için seçilmiş ama operasyonel yük getiren bir araç var mı? Bugün olsa neyi seçerdiniz?"
        },
        {
            "part_num": 3,
            "title": "Ödünleşme (Trade-off) Sanatı: Çözüm Yoktur, Yalnızca Tavizler Vardır",
            "subtitle": "İki boyutlu siyah-beyaz dogmalardan çok boyutlu sonuç odaklı düşünmeye geçiş.",
            "duration": "9 dk",
            "war_story": "Bir fintech şirketinde hisse senedi alım satımlarında iyimser (optimistic) mi yoksa kötümser (pessimistic) veritabanı kilitlemesi mi kullanılması gerektiği konusunda haftalarca süren kavgalar yaşandı. Bir taraf 'Asla çifte satışa izin veremeyiz!' diye bağırıyor, diğer taraf 'Yüksek yük altında kilitler sistemi felç eder!' diye diretiyordu. Toplantıya katılan Baş Mimar tahtaya yürüdü ve sadece iki sütun çizdi: 'Ne kazanıyoruz?' ve 'Bedeli ne?'. Verileri gösterdi: Şirketin saniyedeki işlem sayısı en yoğun anda bile 200'ü geçmiyordu; yani basit bir yeniden deneme (retry) döngüsüyle iyimser kilitleme %99.98 vakayı sıfır kilit maliyetiyle çözüyordu. Oda bir anda sessizleşti. Mesele doğru ya da yanlış değildi; kabul edilebilir ödünleşmenin ne olduğu meselesiydi.",
            "paradigm_shift": "Ekonomist Thomas Sowell'in dediği gibi: 'Çözüm diye bir şey yoktur; yalnızca ödünleşmeler (trade-offs) vardır.' Yazılım mimarisinde koşulsuz şartsız 'harika' olan tek bir tasarım deseni dahi yoktur. Her mimari karar bir ipotek sözleşmesidir: Size anında bir yetenek (hız, esneklik, bağımsızlık) kazandırır; karşılığında düzenli bir faiz (karmaşıklık, ağ gecikmesi, veri tutarlılığı zorluğu) tahsil eder. Mimarın süper gücü, sözleşme imzalanmadan önce ödenecek bedeli masaya yatırmaktır.",
            "core_concepts": [
                {
                    "heading": "Mimari Ödünleşme Matrisi",
                    "text": "İki mimari yönü kıyaslarken (Örn: Senkron REST vs. Asenkron Olaylar), şu 5 boyutta puanla:\n1. **Karmaşıklık:** Ortalama bir geliştiricinin üzerindeki zihinsel yük.\n2. **Performans ve Gecikme:** P99 yanıt süreleri ve ağ seyahatleri.\n3. **Güvenilirlik ve Hata Modları:** Ara bir servis çöktüğünde ne oluyor?\n4. **Operasyonel Maliyet:** Bulut faturası, loglama ve izleme giderleri.\n5. **Geri Döndürülebilirlik:** Bu karar yanlış çıkarsa geriye dönmek ne kadar sürer?"
                },
                {
                    "heading": "Birinci Derece vs. İkinci Derece Düşünme",
                    "text": "- **1. Derece Düşünme:** 'Monoliti 15 mikroservise bölersek her ekip bağımsız dağıtım yapabilir!' (Hızlı ve heyecanlı).\n- **2. Derece Düşünme:** 'Artık dağıtık izleme, mTLS, Kafka şemaları, circuit breaker'lar ve çalışması 4 saat süren uçtan uca entegrasyon testlerine ihtiyacımız olacak.' (Olgun ve gerçekçi)."
                }
            ],
            "anti_patterns": [
                "**Dini Taassup:** Mimari kalıpları (Clean Architecture, Mikroservisler, TDD vb.) sorgulanamaz kutsal metinler gibi savunmak.",
                "**Bedava Öğle Yemeği Yanılsaması:** 'Sıfır operasyonel karmaşıklıkla sonsuz ölçek' vaat eden bir bulut aracına veya kütüphaneye körü körüne inanmak.",
                "**Kör Optimizasyon:** Sisteme 200 saatlik dağıtık kilit karmaşıklığı ekleyerek dahili bir servisten sadece 3 milisaniye kazanmaya çalışmak."
            ],
            "playbook": [
                "**1. Adım:** Sözlüğünden 'En iyi pratik (Best Practice)' ifadesini çıkar; yerine 'Bu bağlam için en uygun pratik' de.",
                "**2. Adım:** Bir sonraki teknik teklifinde, savunduğun tercihin en az 3 dezavantajını açıkça listele.",
                "**3. Adım:** Biri sana 'Bu çözümün hiçbir dezavantajı yok' dediğinde, dezavantajlarını bulana kadar o çözümü onaylama."
            ],
            "takeaways": [
                "Mimarisinin hiçbir eksiği olmadığını söyleyen biri ya yalan söylüyordur ya da henüz o kodu canlıya almamıştır.",
                "İyi mimarlık her metriği maksimize etmek değil; hangi metriklerden feragat edeceğini akıllıca seçmektir.",
                "İkinci derece sonuçları görebilmek, acemi mimarla usta mimarı ayıran en temel farktır."
            ],
            "udemy_prompt": "Çok sevdiğin bir mimari deseni seç (Örn: Event Sourcing, GraphQL veya Mikroservisler). Bu deseni seçmenin bir şirket için tam bir felaket olacağı 3 somut senaryo yaz."
        },
        {
            "part_num": 4,
            "title": "Mimarın Not Defteri: Kararları ADR ile Belgelemek (Herkes Unutmadan Önce)",
            "subtitle": "Hafif siklet Mimari Karar Kayıtları (ADR) kurumsal hafıza kaybını ve bitmek bilmeyen toplantıları nasıl engeller?",
            "duration": "8 dk",
            "war_story": "Bir sağlık teknolojisi şirketine yeni katılan kıdemli mimar, kod incelemesi yaparken her sorguyu yakalayıp veriyi hem Redis'te hem Memcached'de tutan tuhaf bir önbellek katmanı gördü. Ekip toplantısında güldü: 'Bunu hangi akılsız yazdı? Tam bir spagetti!' Odadaki herkes sustu. Başkan Yardımcısı gözlerini dikti: 'Üç yıl önce Sandy Kasırgası sırasında ana sağlayıcımız 4 gün kapandı. Eyalet yasalarına göre hasta kabulünü 1 dakika bile durdurursak lisansımız iptal ediliyordu. O çift katmanlı önbellek şirketi iflastan ve cezadan kurtardı.' Mimar yerin dibine geçti. Kimse o kararın neden alındığını yazmamıştı. İki ay sonra başka biri o kodu 'temizledi' ve ilk bölgesel internet kesintisinde şirket milyonlarca liralık ceza yedi.",
            "paradigm_shift": "Kaynak kod size sistemin *nasıl* çalıştığını söyler; ama *neden* öyle yapıldığını asla söylemez. Kod yazıldıktan 6 ay sonra o günkü piyasa baskıları, yasal zorunluluklar ve elenen alternatifler insan hafızasından silinir. Mimari Karar Kayıtları (ADR - Architecture Decision Records) olmadan ekipler 'Chesterton'ın Çiti' sendromuna yakalanır: Neden dikildiğini anlamadan çiti yıkarlar ve çitin engellediği boğalar tarafından ezilirler.",
            "core_concepts": [
                {
                    "heading": "Bir ADR Belgesinin Anatomisi (Michael Nygard Standardı)",
                    "text": "Standart bir ADR, git deposunda saklanan basit bir Markdown dosyasıdır (`/docs/adr/0004-postgresql-secimi.md`):\n1. **Başlık ve Durum:** ADR-0014: SQS ile Asenkron Sipariş İşleme (Önerildi / Kabul Edildi / İptal Edildi)\n2. **Bağlam (Context):** Hangi iş ihtiyacı veya teknik kısıt bizi bu karara zorladı?\n3. **Karar (Decision):** Net olarak ne yapmayı seçtik?\n4. **Elenen Alternatifler:** Hangi seçenekleri neden eledik?\n5. **Sonuçlar (Consequences):** Kabul edilen olumlu ve olumsuz bedeller."
                },
                {
                    "heading": "Bürokrasi Değil, Yaşayan Tarih",
                    "text": "Bir ADR yazmak en fazla 15-20 dakika sürmelidir. Eğer bir vize başvurusu formuna dönerse mühendisler yazmayı bırakır. ADR'ları kodun hemen yanında tutun ki pull request'lerle birlikte yaşasın."
                }
            ],
            "anti_patterns": [
                "**Gizli Meclis Kararları:** Mimari kararları gizli Slack DM'lerinde alıp ekibe gerekçesiz ferman gibi duyurmak.",
                "**Confluence Mezarlığı:** Kararları kimsenin aramadığı ve güncellemediği tozlu wiki sayfalarına gömmek.",
                "**Sonsuz Taslak:** Bir ADR'ı 'Önerildi' statüsünde 6 ay bekleterek önemsiz ayrıntılar yüzünden felç olmak."
            ],
            "playbook": [
                "**1. Adım:** Bugün ana git deponda bir `/docs/adr` klasörü aç ve içine örnek bir şablon koy.",
                "**2. Adım:** Bir PR veya toplantıda tartışma 30 dakikayı aştığında tartışmayı durdur: 'Bunu 1 sayfalık bir ADR taslağına dökelim ve artıları-eksileri yazalım.'",
                "**3. Adım:** Şirkete yeni başlayan her mühendisin ilk hafta okuması gereken ilk belgenin son 10 ADR olmasını sağla."
            ],
            "takeaways": [
                "Yazıya dökülmemiş bir mimari karar gerçekte var olmamıştır; sadece kulaktan kulağa yayılan bir dedikodudur.",
                "Elenen alternatifleri kaydetmek, aynı konunun seneye tekrar 4 saat tartışılmasını engeller.",
                "Neden orada olduğunu bilmediğin hiçbir mimari çiti yıkma."
            ],
            "udemy_prompt": "Ekibinin son dönemde aldığı önemli bir teknik kararı seç (kütüphane, veritabanı veya bulut servisi). Bunun için 1 sayfalık bir ADR yaz; özellikle elenen alternatifleri belirt."
        }
    ]
}
