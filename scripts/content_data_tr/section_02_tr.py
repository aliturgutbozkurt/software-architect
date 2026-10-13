# Bölüm 2: Planlar ve Sınırlar — Karmaşıklığı Parçalara Ayırmak (Parça 05 - 08)

SECTION_2_TR = {
    "section_num": 2,
    "section_title": "Planlar ve Sınırlar — Karmaşıklığı Parçalara Ayırmak",
    "section_desc": "Yazılım sistemlerinin temel geometrisinde ustalaşmak: sınırları çizmek, monolitleri modülerleştirmek, pratik alan odaklı tasarım (DDD) ve bozulmaz API sözleşmeleri üretmek.",
    "parts": [
        {
            "part_num": 5,
            "title": "Monolit Geri Dönüyor: Ne Zaman Birleşik Kalmalı, Ne Zaman Bölünmeli?",
            "subtitle": "Şirketiniz henüz kaldıramayacak durumdayken ağır 'dağıtık sistemler vergisini' ödemekten nasıl kaçınırsınız?",
            "duration": "9 dk",
            "war_story": "8 kişilik bir lojistik girişiminde günde 500 paket dağıtılıyordu. Konferans videolarını izleyen lider ekip, 'Gerçek teknoloji şirketleri mikroservis kullanır' diyerek derli toplu Ruby on Rails monolitlerini 24 farklı mikroservise böldü. Bir anda tek bir kargo siparişi oluşturmak 6 ayrı veritabanı arasında 9 ağ çağrısı koordine etmeyi gerektirdi. Bildirim servisi 200ms geciktiğinde müşterinin kredi kartından iki kez para çekiliyordu. Geliştiriciler yeni özellik geliştirmek yerine zamanlarının %60'ını JSON dönüştürme ve dağıtık yarış durumlarını (race conditions) debug etmekle harcadı. Yatırım paraları bittiğinde, aylık 80 dolarlık tek bir sunucuda rahatça çalışacak sistem için AWS Kubernetes'e ayda 18.000 dolar ödüyorlardı.",
            "paradigm_shift": "Dağıtık sistemler vergisi gerçektir, pahalıdır ve pazarlığa açık değildir. Bir monoliti mikroservislere böldüğünüzde; bellek içi fonksiyon çağrılarını ağ çağrılarıyla, derleme anı güvenliğini çalışma anı serileştirmesiyle ve atomik ACID veritabanı işlemlerini eventual consistency baş ağrısıyla takas edersiniz. Martin Fowler'ın 'Dağıtık Nesnelerin Birinci Yasası' hala geçerlidir: *Nesnelerinizi dağıtmayın.* İyi tasarlanmış bir Modüler Monolit, kontrolsüz bir mikroservis çorbasından neredeyse her zaman kat kat üstündür.",
            "core_concepts": [
                {
                    "heading": "Modüler Monolit vs. Mikroservis Sınırı",
                    "text": "- **Modüler Monolit:** Tek bir dağıtım paketi, ancak paket/modül görünürlüğü ile sıkı sınırlarla ayrılmış etki alanları. Hızlı derleme, paylaşılan bellek, kolay yerel hata ayıklama ve tekil veritabanı işlemleri.\n- **Mikroservisler:** Bağımsız dağıtım ve bağımsız ölçeklenebilirlik. Yalnızca 50+ mühendisin aynı kod tabanında birbirine çarptığı veya devasa ölçek farklarının tek bir ikiliyi tıkadığı durumlarda meşrudur."
                },
                {
                    "heading": "Dağıtık Sistemler Vergisi Kontrol Listesi",
                    "text": "Bölünmeden önce şu bedelleri ödemeye hazır mısınız?\n1. Dağıtık izleme (OpenTelemetry).\n2. Ağ gecikmesi (her sekmede 5-50ms).\n3. Devre kesiciler (circuit breakers) ve yeniden deneme fırtınaları.\n4. Çift yazma (dual-write) tutarsızlıkları."
                }
            ],
            "anti_patterns": [
                "**Dağıtık Monolit:** Mikroservislerin tüm operasyonel kabuslarına (ağ gecikmesi, kademeli çöküş) sahipken, aynı zamanda monolitlerin tüm hantallığına (servislerin canlıya alınırken aynı anda ve belirli sırada çıkma zorunluluğu) sahip olan ucube mimari.",
                "**Erken Mikroservis:** Etki alanı sınırları henüz oturmadan servisleri bölüp her hafta 5 farklı git reposunda çapraz refactoring yapmak zorunda kalmak.",
                "**Paylaşılan Veritabanı Mikroservisi:** 10 ayrı mikroservisin hepsinin aynı veritabanı tablolarına doğrudan sorgu atması, kapsüllemeyi tamamen yok etmesi."
            ],
            "playbook": [
                "**1. Adım:** Sisteminizi önce Modüler Monolit olarak inşa edin: Modül A'nın Modül B'nin dahili sınıflarını çağırmasını linter kurallarıyla engelleyin.",
                "**2. Adım:** Servisleri varlık bazında bölmeyin ('Kullanıcı Servisi', 'Tarih Servisi' gibi); bağımsız iş yetenekleri bazında bölün ('Ödeme Takas' vs. 'Katalog Arama').",
                "**3. Adım:** Ayrıştırma Testi: Bir modülü yalnızca tamamen farklı bir ölçeklenme profili gerektirdiğinde veya tamamen bağımsız bir ekibe devredildiğinde ayrı bir mikroservise dönüştürün."
            ],
            "takeaways": [
                "Düzgün bir monolit inşa edemiyorsanız, başarılı bir dağıtık sistem inşa edebileceğinizi nereden çıkarıyorsunuz?",
                "Mikroservisler kötü kodun teknik ilacı değil; devasa ekiplerin organizasyonel koordinasyon çözümüdür.",
                "Modern donanımlarda çalışan modüler bir monolit, milyonlarca kullanıcıyı sıfır operasyonel dertle kaldırabilir."
            ],
            "udemy_prompt": "Mevcut sisteminize bakın. Mikroservis kullanıyorsanız, canlıya çıkarken mutlaka birlikte dağıtılması gereken servisleriniz var mı? Monolitteyseniz, en çok dağıtım sürtüşmesi yaratan alan neresi?"
        },
        {
            "part_num": 6,
            "title": "Akademik Baş Ağrısı Olmadan Domain-Driven Design: İnsan Dilinde Bounded Context",
            "subtitle": "Mimarınızı veritabanı tabloları etrafında değil, iş dünyasının gerçekleri etrafında şekillendirin.",
            "duration": "9 dk",
            "war_story": "Bir telekomünikasyon devi, `tbl_Kullanici` adında devasa bir tablo etrafında dönen kurumsal bir sistem kurdu. Satış departmanı için kullanıcı; sadece e-posta ve ilgi alanından ibaret anonim bir adaydı. Faturalama departmanı için kullanıcı; vergi numarası ve banka hesabı olan yasal bir tüzel kişilikti. Şebeke Güvenliği için ise kullanıcı; aktif bir SIM kart ve IMEI numarasıydı. Satış ekibi bayilerde hızlı kayıt için e-posta alanını opsiyonel yaptığında, Faturalama'nın toplu fatura kesim servisi NullPointerException ile patladı! Şirket 9 ay boyunca 'Evrensel Tekil Kullanıcı Nesnesi' üretmek için toplantılar yaptı. Tablo 142 kolona ulaştı ve kimseyi tatmin etmedi. Proje 4 milyon dolar zararla çöpe atıldı.",
            "paradigm_shift": "Karmaşık bir şirkette tüm gerçekliği kapsayan tek bir evrensel model diye bir şey yoktur. Eric Evans'ın Alan Odaklı Tasarım (DDD) felsefesinin en büyük aydınlanması şudur: Kelimeler yalnızca belirli bir **Sınırlı Bağlam (Bounded Context)** içinde kesin bir anlama sahiptir. Faturalama için müşteri bir fatura adresidir; Kargo için müşteri bir teslimat koordinatıdır; Destek için müşteri bir şikayet geçmişidir. Mimarın görevi bunları dev bir Frankenstein modelinde birleştirmek değil, açık sınırlar çizip aralarında tercüme yapmaktır.",
            "core_concepts": [
                {
                    "heading": "Gerçek Mühendisler İçin Pratik DDD Alet Çantası",
                    "text": "- **Ortak Dil (Ubiquitous Language):** İş birimiyle mühendislerin anlaştığı ortak sözlük. Eğer iş birimi buna 'Poliçe İptali' diyorsa, kodda `is_deleted = true` yazamazsınız.\n- **Sınırlı Bağlam (Bounded Context):** Bir modelin geçerli olduğu açık sınır. Bağlam A içinde 'Ürün' stok adedi demektir; Bağlam B içinde 'Ürün' pazarlama metni demektir.\n- **Kök Varlık (Aggregate Root):** Veri tutarlılığını garanti eden bekçi nesne (Örn: Bir `Siparis`, altındaki `SiparisKalemleri`ni yönetir; dışarıdan bir kod kalemi doğrudan değiştiremez)."
                },
                {
                    "heading": "Bozulma Önleyici Katman (Anti-Corruption Layer - ACL)",
                    "text": "İki sınır bağlamı veya eski bir sistemle konuşurken, dış sistemin kirli ve spagetti veri yapılarının sizin temiz alanınıza sızmasına asla izin vermeyin. Araya bir tercüman adaptör (ACL) koyun."
                }
            ],
            "anti_patterns": [
                "**Tanrı Nesnesi (God Object):** Projenin her yerine bulaşan, 200 metodu ve 80 kolonu olan dev `User` veya `Order` sınıfları.",
                "**Kansız Alan Modeli (Anemic Domain Model):** Sadece getter/setter içeren aptal veri torbaları ve iş kurallarının 50 farklı servis sınıfına kontrolsüzce saçılması.",
                "**Akademik DDD Fetişizmi:** Basit bir SQL sorgusuyla çözülecek 3 satırlık iş için 10 katmanlı soyutlama ve repository yazıp sistemi boğmak."
            ],
            "playbook": [
                "**1. Adım:** Bir 'Event Storming' atölyesi düzenle: İş birimi ve yazılımcıları dijital tahta başına toplayıp iş olaylarını kronolojik sırayla turuncu post-it'lerle dizin.",
                "**2. Adım:** Doğal olarak kümelenen olay gruplarının etrafına daire çizerek doğal Sınırlı Bağlamlarınızı (Bounded Context) keşfedin.",
                "**3. Adım:** Üçüncü parti kurumsal sağlayıcılarla entegre olurken ilk iş olarak bir Anti-Corruption Layer (ACL) tasarla."
            ],
            "takeaways": [
                "Modeller gerçek dünyanın fotokopisi değildir; belirli bir sınırdaki problemi çözmek için tasarlanmış haritalardır.",
                "Pazarlama ekibinin kullanıcı tanımının, muhasebenin defterini patlatmasına izin vermeyin.",
                "Kodunuzda iş biriminin dilini konuşun, yoksa tüm kariyeriniz biletleri Türkçeye çevirmekle geçer."
            ],
            "udemy_prompt": "Mevcut kod tabanınızda 20'den fazla özelliği olan dev bir sınıf bulun. Bu sınıfı iki farklı sınırlı bağlama (bounded context) ait iki farklı modele bölebilir misiniz?"
        },
        {
            "part_num": 7,
            "title": "Bağlaşıklık ve Uyum (Coupling vs. Cohesion): Sistemleri Yaşatan veya Öldüren İkiz Güç",
            "subtitle": "Ön yüzde bir butonun rengini değiştirmenin fiziksel depodaki paketleme robotlarını durdurmaması için.",
            "duration": "8 dk",
            "war_story": "Büyük bir perakende uygulamasında kampanya döneminde bir kriz patlak verdi. Pazarlama ekibi açılış sayfasındaki tanıtım kutusunun metnini 'Ücretsiz Kargo' yerine 'Kargo Bedava' olarak güncelledi. Kod canlıya alındıktan on dakika sonra, fiziksel depodaki barkod okuyucu robotik vinçler durdu! Neden mi? Depodaki barkod sistemi, sepetin JSON çıktısını ayrıştırıyor ve kargo ağırlık kategorisini belirlemek için arayüzdeki banner metnini `*Kargo*` regex'iyle kontrol ediyordu! Metin değişince sistem tanımsız hata fırlattı ve tüm lojistik operasyonu kilitlendi. Bir pazarlama metni değişikliği koca fabrikayı durdurmuştu.",
            "paradigm_shift": "Bağlaşıklık (Coupling), modüller arasındaki bağımlılık derecesidir; Uyum (Cohesion) ise bir modülün içindeki fonksiyonların ne kadar tek bir amaca odaklandığıdır. Larry Constantine'in 1974'te formüle ettiği kural hala değişmemiştir: **Yüksek Uyum, Gevşek Bağlaşıklık (High Cohesion, Loose Coupling).** Birlikte değişmesi gereken şeyler aynı yerde yaşamıyorsa düşük uyum vardır. Modül A'daki tek bir satırı değiştirmek Modül B'yi bozuyor veya yeniden dağıtılmasını gerektiriyorsa sıkı bağlaşıklık vardır.",
            "core_concepts": [
                {
                    "heading": "Bağlaşıklık Türleri (Masumdan Zehirliye)",
                    "text": "- **Veri Bağlaşıklığı (Sağlıklı):** Modüller birbirine sadece işi yapacak temel parametreleri geçirir.\n- **Kontrol Bağlaşıklığı (Şüpheli):** Modül A, Modül B'ye dahili yürütme akışını dikte eden bayraklar (`ozelLoglamaYap=true`) gönderir.\n- **Ortak/Veritabanı Bağlaşıklığı (Tehlikeli):** Birden fazla modül aynı paylaşılan veritabanı tablolarını doğrudan okur ve yazar.\n- **İçerik Bağlaşıklığı (Ölümcül):** Modül A, Modül B'nin özel (private) değişkenlerine erişip içeriden müdahale eder."
                },
                {
                    "heading": "Demeter Yasası (En Az Bilgi İlkesi)",
                    "text": "Yabancılarla konuşmayın: `siparis.getMusteri().getAdres().getPostaKodu().vergiHesapla()` çağrısı çağıranı 4 seviye derinliğindeki iç yapıya sıkı sıkıya bağlar. Bunun yerine `siparis.vergiHesapla()` çağrılmalı ve iç gezintiyi nesne kendisi yönetmelidir."
                }
            ],
            "anti_patterns": [
                "**Saçma Sapan Ameliyat (Shotgun Surgery):** Tek bir iş kuralını değiştirmek için 5 farklı serviste 18 ayrı dosyayı düzenlemek zorunda kalmak.",
                "**Ortak Çöp Çekmecesi (Common/Utils):** Şirketteki her servisin import ettiği, içinde 40.000 satır ilgisiz kod barındıran kontrolsüz `CommonUtils` kütüphaneleri.",
                "**Gezgin Veri (Tramp Data):** Sırf en alttaki fonksiyon bir `kullanici_id`ye ihtiyaç duyuyor diye 12 katman boyunca 50 alanlık koca bir bağlam nesnesini elden ele gezdirmek."
            ],
            "playbook": [
                "**1. Adım:** Git geçmişinde değişiklik sıklığı (churn) analizi yap: Neredeyse her pull request'te düzenlenen ilk 5 dosyayı bul. Orası senin toksik bağlaşıklık merkezindir.",
                "**2. Adım:** En çok sürtüşme yaratan noktayı bir arayüz (interface) veya olay (event) arkasına alarak soyutla.",
                "**3. Adım:** Ortak `Common` paketini dağıt; o kodları gerçek sahiplerinin modüllerine taşı."
            ],
            "takeaways": [
                "Ekip büyüdükçe yazılım geliştirme hızının yavaşlamasının 1 numaralı sebebi sıkı bağlaşıklıktır.",
                "Uyum odaklanmakla ilgilidir: Bir sınıf veya servis tek bir işi yapmalı ve onu eksiksiz yapmalıdır.",
                "İki servisin her zaman birlikte canlıya alınması gerekiyorsa, onlar iki servis değil; arasına ağ kablosu çekilmiş tek bir servistir."
            ],
            "udemy_prompt": "Git reponuzun son 6 aylık geçmişini tarayın. En sık değiştirilen dosya hangisi? Neden bu kadar çok farklı özellik o dosyaya dokunmak zorunda kalıyor?"
        },
        {
            "part_num": 8,
            "title": "Kutsal Bir Sözleşme Olarak API Tasarımı: REST, gRPC ve GraphQL Karşılaştırması",
            "subtitle": "İstemci uygulamaların Cuma akşamı patlamadan güvenle tüketebileceği arayüzler tasarlamak.",
            "duration": "9 dk",
            "war_story": "2 milyon aktif mobil kullanıcısı olan bir mobil bankacılık uygulamasında backend geliştirici Cuma akşamı `/api/v1/hesaplar` ucundaki `hesap_no` alanını temiz kod aşkına `hesapNo` olarak güncelledi. Web ekibi hemen güncellemeyi alıp canlıya çıktı. Ancak App Store ve Google Play'den uygulamasını henüz güncellememiş 1.4 milyon kullanıcının hesap bakiyeleri Cumartesi sabahı birden 0.00 TL görünmeye başladı! Bankanın çağrı merkezi kilitlendi, hisseler değer kaybetti. Kullanıcıların telefonundaki eski uygulamayı zorla güncelleyemeyeceğiniz için sistem acil gece yarısı yamasıyla geri alınmak zorunda kaldı.",
            "paradigm_shift": "Dahili bir fonksiyon imzası size aittir; ancak yayınlanmış bir API tüketicilerinize aittir. Bir API mobil cihazlara, üçüncü parti ortaklara veya genel kullanıma açıldığı anda geri alınamaz bir sözleşmeye dönüşür. Kullanıcıların telefonlarını ne zaman güncelleyeceğini kontrol edemezsiniz. Usta bir mimar API'leri geriye dönük mutlak uyumluluk (backward compatibility) ve toleranslı okuma ilkeleriyle tasarlar.",
            "core_concepts": [
                {
                    "heading": "Protokol Karşılaştırması",
                    "text": "- **REST (HTTP/JSON):** Evrensel, tarayıcıda kolay debug edilir, genel geliştirici ekosistemleri ve standart CRUD işleri için ideal.\n- **gRPC (HTTP/2 üzerinde Protobuf):** İkili serileştirme ile ultra yüksek hız, sıkı şema sözleşmeleri, iki yönlü akış. Mikroservislerin iç haberleşmesinin tartışmasız kralı.\n- **GraphQL:** İstemcinin ihtiyacı olan veriyi kendisinin seçtiği yapı. Mobil uygulamalarda gereksiz veri indirmeyi (over-fetching) engeller, zengin dashboard'lar için harikadır."
                },
                {
                    "heading": "API Evriminin Altın Kuralları",
                    "text": "1. **Yalnızca Ekleme Yapılabilir (Additive Changes):** Yeni alanlar ekleyebilirsiniz; fakat mevcut bir alanı silemez veya yeniden adlandıramazsınız.\n2. **Toleranslı Okuyucu Kalıbı:** İstemciler JSON yanıtında tanımadıkları yeni alanları yoksaymalıdır.\n3. **Idempotency Anahtarları:** Veri değiştiren tüm uçlar (`POST /odemeler`) bir `Idempotency-Key` başlığı kabul ederek mükerrer çekimleri engellemelidir."
                }
            ],
            "anti_patterns": [
                "**Veritabanını Dışarı Sızdırmak:** `SELECT * FROM kullanicilar` sonucunu doğrudan JSON olarak dönüp kullanıcının şifre özetlerini ve iç tablo kolonlarını internete açmak.",
                "**GraphQL Vahşi Batısı:** Derinlik sınırı koymadan genel internete açılan GraphQL uçları yüzünden kötü niyetli kişilerin iç içe sorgularla sunucuları kilitlemesi.",
                "**Sessiz Kırıcı Değişiklik:** Versiyon numarasını değiştirmeden bir alanın biçimini (örn: ISO 8601 tarih yerine milisaniye dönmek) değiştirmek."
            ],
            "playbook": [
                "**1. Adım:** Kod yazmadan önce OpenAPI (Swagger) veya Protobuf sözleşmesini yazıp onaylatın (API-First Tasarım).",
                "**2. Adım:** CI/CD sürecine otomatik sözleşme testleri (Pact gibi) entegre ederek kırıcı değişikliklerin canlıya gitmesini engelleyin.",
                "**3. Adım:** Tüm kritik ödeme ve sipariş uçlarında `Idempotency-Key` başlığını zorunlu hale getirin."
            ],
            "takeaways": [
                "API'ler sonsuza dek yaşar: Biri o uca göre mobil uygulama derlediğinde, o şemayı yıllarca desteklemek zorunda kalırsınız.",
                "Dahili servis haberleşmesinde gRPC'nin hızını; dış dünyada REST veya GraphQL'in esnekliğini kullanın.",
                "Veritabanı kolonundaki bir isim değişikliğinin dış dünyadaki API kontratını kırmasına asla izin vermeyin."
            ],
            "udemy_prompt": "Şirketinizdeki ana API uçlarından birini inceleyin. Versiyonlama nasıl yapılıyor? 3 yıl önce yazılmış eski bir mobil istemci bugün o uca istek atsa çalışmaya devam eder mi?"
        }
    ]
}
