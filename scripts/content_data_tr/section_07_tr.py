# Bölüm 7: Güvenlik ve Sıfır Güven (Zero Trust) — Krallığı Savunmak (Parça 25 - 28)

SECTION_7_TR = {
    "section_num": 7,
    "section_title": "Güvenlik ve Sıfır Güven — Krallığı Savunmak",
    "section_desc": "Derinlemesine savunma mimarisi: Sıfır Güven (Zero Trust) ve mTLS ile kale yanılsamalarını yıkmak, RBAC ve ABAC ile dinamik yetkilendirme kurmak, anahtarları korumak ve tedarik zinciri tehditlerini modellemek.",
    "parts": [
        {
            "part_num": 25,
            "title": "Sıfır Güven Mimarisi (Zero Trust): Asla Güvenme, Daima Doğrula",
            "subtitle": "Kurumsal VPN çevrelerinin neden öldüğü ve mikroservislerin karşılıklı TLS (mTLS) ile nasıl güvenceye alınacağı.",
            "duration": "9 dk",
            "war_story": "2013 yılında perakende devi Target, tarihin en büyük veri ihlallerinden birini yaşadı. Saldırganlar ana ödeme sistemine doğrudan sızmadı; Target'ın soğutma sistemlerini uzaktan izleyen üçüncü parti bir havalandırma (HVAC) taşeronunun VPN giriş bilgilerini çaldılar. VPN'in içine girdiklerinde ağın devasa, dümdüz bir salon olduğunu gördüler: İçeride hiçbir iç güvenlik duvarı veya mikroservis kimlik kontrolü yoktu! Saldırganlar havalandırma sunucusundan doğrudan mağaza kasalarının pos cihazlarına atladılar ve 40 milyon kredi kartını kopyaladılar. Target 200 milyon dolardan fazla tazminat ödedi ve CEO istifa etmek zorunda kaldı.",
            "paradigm_shift": "Geleneksel 'Kale ve Hendek' modeli (güvenlik duvarının içindeki her şeye güven, dışındakilere güvenme) artık çökmüştür. Saldırgan bir oltalama e-postası veya bir taşeron şifresiyle iç ağa sızdığı anda tüm veritabanlarınız savunmasız kalır. **Sıfır Güven (Zero Trust) Mimarisi** şu üç ilkeyle çalışır: 1) Açıkça doğrula, 2) En az yetkiyi ver, 3) İhlal edildiğini varsay. İç ağdaki her bir servis, yanındaki diğer servise sanki açık internetteymiş gibi şüpheyle yaklaşmalıdır.",
            "core_concepts": [
                {
                    "heading": "Yazılım Mimarları İçin Sıfır Güven İlkeleri",
                    "text": "- **Çevre Değil, Kimlik:** IP adresleri güven sağlamaz. Her istek kriptografik olarak imzalanmış kimlik token'ları (SPIFFE ID, JWT, OAuth) taşımalıdır.\n- **Karşılıklı TLS (mTLS):** Standart TLS'de sadece istemci sunucunun sertifikasını doğrular. mTLS'de ise SUNUCU DA İSTEMCİYİ doğrular. İki taraf da kimliğini kanıtlar ve ağdaki tüm trafik şifrelenir. Servis mesh (Istio, Linkerd) veya Envoy yan araçlarıyla uygulama koduna dokunmadan kurulur."
                },
                {
                    "heading": "Mikro Segmentasyon ve En Az Yetki İlkesi",
                    "text": "Ön yüz web servisi doğrudan müşteri ödeme veritabanına ağ seviyesinde fiziksel olarak bağlanamamalıdır. Yalnızca kimliği doğrulanmış bir mTLS kanalı üzerinden Ödeme API'siyle konuşabilir."
                }
            ],
            "anti_patterns": [
                "**Düz İç Ağ Rehaveti:** 'Burası bizim güvenli AWS VPC'miz, kendi kodumuza da mı güvenmeyeceğiz?' diyerek servisler arasındaki kimlik doğrulamasını kapatmak.",
                "**Statik IP Beyaz Listesi:** Konteynerlerin sürekli yeniden başlayıp IP değiştirdiği bulut ortamlarında statik IP listeleriyle güvenlik sağlamaya çalışmak.",
                "**Aşırı Yetkili Servis Hesabı:** Basit bir e-posta bildirim servisine 'yapılandırması kolay olsun' diye AWS `AdministratorAccess` yetkisi vermek."
            ],
            "playbook": [
                "**1. Adım:** İç servis ağını denetle: Kümedeki rastgele bir konteyner doğrudan canlı veritabanına şifresiz TCP sorgusu atabiliyor mu?",
                "**2. Adım:** Mikroservisler arasına Envoy veya hafif bir servis mesh ile mTLS kur.",
                "**3. Adım:** Her servisin bulut IAM rollerini denetle; tüm joker (`*`) izinleri kaldırıp en az yetki kuralını uygula."
            ],
            "takeaways": [
                "Saldırganın zaten iç ağınızda olduğunu varsayın; savunmanızı buna göre tasarlayın.",
                "IP adresleri kimlik değildir; kriptografik sertifikalar ve token'lar kimliktir.",
                "Mikro segmentasyon ve mTLS ile hasar yarıçapını olabildiğince daraltın."
            ],
            "udemy_prompt": "Kötü niyetli biri şu an ön yüz sunucularınızdan birine shell erişimi sağlasa, şifresiz olarak başka hangi veritabanlarına veya iç servislere erişebilir?"
        },
        {
            "part_num": 26,
            "title": "Ölçekte Kimlik ve Yetkilendirme: OAuth2, OIDC ve RBAC vs. ABAC",
            "subtitle": "Başlık boyutlarını patlatmadan kimlik doğrulama ile ayrıntılı izinleri birbirinden ayırmak.",
            "duration": "9 dk",
            "war_story": "Bir sağlık teknolojisi platformunda mimarlık ekibi her istekte veritabanına gitmemek için doktorların tüm izinlerini doğrudan JSON Web Token (JWT) içine kodlamaya karar verdi. Büyük hastane zincirlerine bağlı uzman doktorlar için bu izinler; 400 klinik kodu, 80 hastane kanadı ve 50 özel prosedür yetkisi içeriyordu. Altıncı ayda JWT boyutu 28 kilobayta fırladı! Doktorlar acil hasta konsültasyonu açmaya çalıştığında NGINX tersine vekil sunucuları `HTTP 431 Request Header Fields Too Large` hatası vererek doktorları kilitledi. Daha da kötüsü, bir doktorun yetkisi suiistimal yüzünden iptal edildiğinde, stateless JWT 24 saat geçerli kaldığı için doktor sisteme girmeye devam etti!",
            "paradigm_shift": "Kimlik Doğrulama (AuthN: *Sen kimsin?*) ile Yetkilendirme (AuthZ: *Neleri yapmaya iznin var?*) iki farklı mimari problemdir. OAuth 2.0 ve OIDC kimlik tespitini çözmüştür; ancak ölçeklenebilir yetkilendirme, izinleri devasa JWT token'larına tıkmakla çözülemez. Modern mimariler hafif kimlik token'ları ile harici çalışan dinamik yetkilendirme motorlarını (**RBAC** veya **ABAC**) birbirinden ayırır.",
            "core_concepts": [
                {
                    "heading": "Kimlik Protokollerinin Özeti",
                    "text": "- **OpenID Connect (OIDC):** Kimliği doğrular ve kullanıcı profilini içeren bir `id_token` (JWT) üretir.\n- **OAuth 2.0:** Yetkilendirme çerçevesi. İstemcinin kullanıcı adına kaynaklara erişmesini sağlayan `access_token` üretir.\n- **RBAC (Rol Tabanlı Erişim):** İzinler rollere atanır (Yönetici, Editör). Basittir ama kurumsal kurallar arttıkça 'Rol Patlaması' yaşanır.\n- **ABAC / ReBAC (Özellik Tabanlı Erişim):** Kararlar kurallarla verilir: `Kullanıcı X Belge Y'yi düzenleyebilir Mİ EĞER Kullanıcı.Bölüm == Belge.Bölüm VE Saat < 18:00?` (Örn: Open Policy Agent - OPA, Oso)."
                },
                {
                    "heading": "Anında İptal (Revocation) Stratejisi",
                    "text": "JWT yaşam sürelerini kısa tutun (5 - 15 dakika). Anında oturum kapatma ve engelleme için Redis üzerinde hafif bir kara liste (blacklist) kontrolü yapın."
                }
            ],
            "anti_patterns": [
                "**50 KB'lık JWT Canavarı:** Kullanıcının adresini, tüm rollerini ve profil detaylarını HTTP başlığına tıkmak.",
                "**Kod İçi Sabit İzin Kontrolleri:** Servis kodlarının içine `if (user.rol == 'mudur' && user.ulke == 'TR')` yazıp iş kurallarını 50 yere saçmak.",
                "**Kendi Kriptografisini Yazmak:** Kendi şifre özetleme veya oturum algoritmasını icat etmeye kalkışmak (Bcrypt, Argon2 varken)."
            ],
            "playbook": [
                "**1. Adım:** OIDC/OAuth 2.0 için hazır bir kimlik sağlayıcı (Auth0, Keycloak veya AWS Cognito) entegre et.",
                "**2. Adım:** Yetkilendirme kurallarını Open Policy Agent (OPA) gibi harici bir kural motorunda topla.",
                "**3. Adım:** Access Token süresini 15 dakika yap ve dönen yenileme token'ları (refresh tokens) kullan."
            ],
            "takeaways": [
                "AuthN kapıyı çalanın kim olduğunu söyler; AuthZ hangi odalara girebileceğini belirler.",
                "Stateless token'ları hafif tutun; ayrıntılı izinleri dinamik yetki motorlarına bırakın.",
                "Asla kendi güvenlik ve şifreleme algoritmanızı yazmayın; denetlenmiş standartları kullanın."
            ],
            "udemy_prompt": "Sisteminiz anında yetki iptalini nasıl yönetiyor? Bir çalışanın işine şu an son verilse, açık oturumu hemen kapanır mı yoksa token süresi bitene kadar sisteme erişebilir mi?"
        },
        {
            "part_num": 27,
            "title": "Gizli Anahtar Yönetimi, Şifreleme ve Veri Gizliliği",
            "subtitle": "Haber bültenlerine manşet olmadan API anahtarlarını, şifreleri ve müşteri verilerini korumak.",
            "duration": "9 dk",
            "war_story": "Girişimde çalışan bir yazılımcı gece 02:30'da acil bir veritabanı hatasını çözerken kolaylık olsun diye canlı veritabanı şifresini ve AWS master anahtarlarını doğrudan `config.js` dosyasına yapıştırdı. Hatayı çözdü, commit attı ve GitHub'a push'ladı. Ancak şirketin deposu halka açıktı! GitHub commit'lerini tarayan otomatik botlar 8 dakika içinde AWS anahtarlarını yakaladı. Saat 03:15 olduğunda saldırganlar 12 farklı AWS bölgesinde Monero kripto parası kazan 400 adet devasa GPU sunucusu başlatmıştı bile. CTO sabah uyandığında şirket 42.000 dolarlık bir bulut faturasıyla ve çalınmış bir veritabanıyla baş başa kaldı.",
            "paradigm_shift": "Gizli anahtarları kaynak kodda tutmak veya git deposuna commit'lemek, evinizin anahtarını sokak kapısının üzerine bantlamaktan farksızdır. Git geçmişi kalıcıdır. Bir mimar; anahtarların çalışma anında güvenli bir kasadan dinamik olarak enjekte edildiği, otomatik olarak döndürüldüğü (rotation) ve verinin hem beklemede hem de taşınırken Zarf Şifreleme (Envelope Encryption) ile korunduğu sistemler tasarlar.",
            "core_concepts": [
                {
                    "heading": "Gizli Anahtar Yönetim Seviyeleri",
                    "text": "- **Seviye 0 (İntihar):** Kodun içinde veya git'e atılan `.env` dosyalarında tutmak.\n- **Seviye 1 (Temel):** CI/CD ortam değişkenleriyle dağıtım anında enjekte etmek.\n- **Seviye 2 (Modern Standart):** Özel Anahtar Kasaları (HashiCorp Vault, AWS Secrets Manager). Anahtarlar çalışma anında IAM rolüyle dinamik çekilir.\n- **Seviye 3 (Sıfır Güven):** Geçici Dinamik Anahtarlar. Kasa veritabanında sadece 60 dakika geçerli geçici bir kullanıcı açar ve süre bitince iptal eder."
                },
                {
                    "heading": "Zarf Şifreleme (Envelope Encryption) ve KMS",
                    "text": "10 GB'lık veriyi ağ üzerinden şifrelemek yavaştır. Zarf şifreleme iki katman kullanır:\n1. Yerel bir **Veri Şifreleme Anahtarı (DEK)** veriyi yerel olarak anında şifreler.\n2. Bulut KMS servisi sadece bu DEK anahtarını ana anahtarla (KEK) şifreler.\n3. Verinin yanında sadece şifrelenmiş DEK saklanır."
                }
            ],
            "anti_patterns": [
                "**Docker İmajına Şifre Gömmek:** Dockerfile katmanlarına `ENV DB_PASS=gizli123` yazıp imajı çekebilen herkese şifreyi hediye etmek.",
                "**Loglara Hassas Veri Basmak:** Kullanıcı şifrelerini veya kredi kartlarını log dosyalarına yazdırmak (`logger.info('Kullanıcı: ' + user)`), Datadog'u KVKK suç mahalline çevirmek.",
                "**Dönmeyen Anahtarlar:** Aynı veritabanı şifresini işten ayrılan 20 mühendise rağmen 5 yıl boyunca hiç değiştirmeden kullanmak."
            ],
            "playbook": [
                "**1. Adım:** Git geçmişinde sızmış şifreleri bulmak için hemen Trufflehog veya git-secrets çalıştır.",
                "**2. Adım:** Statik konfigürasyon şifrelerini merkezi bir kasaya (AWS Secrets Manager / Vault) taşı.",
                "**3. Adım:** Loglama katmanına otomatik maskeleme ekleyerek kredi kartı, şifre ve kimlik numaralarını loglardan temizle."
            ],
            "takeaways": [
                "Kaynak kod sadece mantık içindir, asla sır barındırmaz. Git'e girmiş bir anahtar taviz verilmiş sayılır.",
                "Otomatik anahtar döndürme (rotation) anahtar sızıntılarına karşı en büyük kalkanınızdır.",
                "Hassas müşteri verilerini log sınırında maskeleyin; log sisteminiz veri sızıntı kaynağı olmasın."
            ],
            "udemy_prompt": "Kod tabanınızda `password`, `secret` veya `apiKey` kelimelerini aratın. Sabit değerler var mı? Canlı veritabanı şifrenizi şu an değiştirmek isteseniz bu ne kadar sürer?"
        },
        {
            "part_num": 28,
            "title": "Tedarik Zinciri Güvenliği ve Tehdit Modellemesi (STRIDE)",
            "subtitle": "Kötü niyetli npm paketlerinden korunmak ve tasarım aşamasında STRIDE risklerini hesaplamak.",
            "duration": "9 dk",
            "war_story": "2018 yılında haftalık 2 milyon indirilen açık kaynaklı JavaScript kütüphanesi `event-stream`'in yorgun geliştiricisi, repoyu yardım teklif eden tanımadığı birine devretti. Yeni sahip kütüphaneye sessizce `flatmap-stream` adında minik bir bağımlılık ekledi. Bu bağımlılığın içinde açık kaynaklı Copay Bitcoin cüzdanındaki özel anahtarları çalmak üzere şifrelenmiş zararlı bir kod vardı! Aylarca yazılımcılar hiçbir şeyden habersiz `npm install` diyerek bu truva atını kendi ticari yazılımlarına çektiler. Şirketlerin kendi kodlarında tek satır değişiklik olmamasına rağmen sistemlerinde truva atı çalışıyordu.",
            "paradigm_shift": "Modern yazılımlar sıfırdan yazılmaz; binlerce açık kaynaklı bağımlılıktan monte edilir. Siz 1.000 satır özel kod yazdığınızda, internetteki yabancıların yazdığı 500.000 satırlık üçüncü parti kodu projenize dahil edersiniz. Güvenlik sınırınız `node_modules` içindeki en zayıf paket kadardır. Mimari güvenlik; otomatik Yazılım Malzeme Listesi (SBOM) takibi, zafiyet taramaları ve tasarım aşamasında **STRIDE Tehdit Modellemesi** gerektirir.",
            "core_concepts": [
                {
                    "heading": "STRIDE Tehdit Modelleme Çerçevesi (Microsoft Standardı)",
                    "text": "Sistemi inşa etmeden önce her bileşeni şu 6 tehdide karşı test et:\n- **S - Spoofing (Kimliğe Bürünme):** Saldırgan başka bir kullanıcının veya servisin yerine geçebilir mi?\n- **T - Tampering (Veri Tahrifatı):** Veri yolda veya veritabanında fark edilmeden değiştirilebilir mi?\n- **R - Repudiation (İnkar Edilebilirlik):** Kullanıcı yaptığı işlemi inkar edebilir mi (denetim logu eksikliği)?\n- **I - Information Disclosure (Bilgi İfşası):** Gizli veriler yetkisiz kişilere sızabilir mi?\n- **D - Denial of Service (Hizmet Engelleme):** Sistem aşırı yükle çökertilebilir mi?\n- **E - Elevation of Privilege (Yetki Yükseltme):** Normal kullanıcı yönetici haklarına sıçrayabilir mi?"
                },
                {
                    "heading": "Tedarik Zinciri Kalkanları (SBOM ve Kilit Dosyaları)",
                    "text": "1. **Kilit Dosyaları:** `package-lock.json` veya `poetry.lock` dosyalarını mutlaka git'e atın.\n2. **Otomatik Tarama:** CI/CD'de Dependabot veya Snyk çalıştırın.\n3. **Özel Paket Deposu:** Açık kaynaklı paketleri doğrudan internetten değil, taranmış şirket içi artifact reposundan (Nexus/Artifactory) çekin."
                }
            ],
            "anti_patterns": [
                "**Ucu Açık Versiyonlar:** Kilit dosyası kullanmadan `package.json` içine `*` veya `^` koyup gece derlemesinde güncellenen zararlı paketi canlıya çekmek.",
                "**Güvenlik Uyarılarını Görmezden Gelmek:** Dependabot'un bildirdiği 'Kritik' açık uyarılarını aylarca kapatmayıp spam muamelesi yapmak.",
                "**Kör Konteyner Güveni:** Docker Hub'dan kimin hazırladığı belli olmayan rastgele taban imajları (`FROM ahmet/python`) indirip kullanmak."
            ],
            "playbook": [
                "**1. Adım:** Bir sonraki büyük mimari tasarımında 1 saatlik STRIDE tehdit modelleme toplantısı yap.",
                "**2. Adım:** CI/CD sürecine Kritik güvenlik açığı tespit ettiğinde derlemeyi durduran otomatik bağımlılık tarayıcı ekle.",
                "**3. Adım:** Üretim paketleriniz için otomatik bir Yazılım Malzeme Listesi (SBOM) çıktısı üret."
            ],
            "takeaways": [
                "Projenize dahil ettiğiniz her üçüncü parti satır kodun güvenliğinden bizzat siz sorumlusunuz.",
                "STRIDE, açıkları olay yaşandıktan sonra değil, tasarım aşamasında bulmanızı sağlayan sistematik bir pusuladır.",
                "Bağımlılıklarınızı kilitleyin, paketlerinizi tarayın ve açık kaynak dünyasına tedbirli yaklaşın."
            ],
            "udemy_prompt": "Projenizde `npm audit` veya `pip audit` çalıştırın. Kaç güvenlik açığı listelendi? Kaç tanesi 'High' veya 'Critical' seviyesinde?"
        }
    ]
}
