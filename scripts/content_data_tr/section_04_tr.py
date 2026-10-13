# Bölüm 4: Asenkron Ufuklar — Olay Odaklı Mimari (Parça 13 - 16)

SECTION_4_TR = {
    "section_num": 4,
    "section_title": "Asenkron Ufuklar — Olay Odaklı Mimari",
    "section_desc": "Senkron HTTP zincirlerinin prangalarından kurtulmak: olay odaklı sistemler tasarlamak, Kafka mekaniğinde ustalaşmak, dağıtık Saga işlemlerini yönetmek ve Event Sourcing / CQRS dengesini kurmak.",
    "parts": [
        {
            "part_num": 13,
            "title": "Senkron Cehennemden Asenkron Huzura: Kuyruklar, Konular ve Akışlar",
            "subtitle": "Yavaş bir üçüncü parti SMS sağlayıcısının ödeme akışınızı felç etmesini engellemenin yolları.",
            "duration": "9 dk",
            "war_story": "Bir havayolu biletleme sisteminde 'Bileti Al' butonuna basıldığında tek bir senkron HTTP isteği tetikleniyordu. Backend bu tek istek içinde sırayla: 1) Banka Sanal Posu, 2) Koltuk Rezervasyonu, 3) Sadakat Puanı Kontrolü, 4) Dolandırıcılık ML Analizi, 5) SMS Gateway ve 6) PDF Bilet Oluşturma servislerini senkron olarak çağırıyordu. Yılbaşı gecesi SMS sağlayıcısı aşırı yoğunluktan çöktü ve her isteğe 30 saniye sonra zaman aşımı (timeout) dönmeye başladı. Bütün web sunucusu thread'leri SMS cevabını beklerken kilitlendi. 4 dakika içinde şirketin tüm sunucuları yanıt veremez hale geldi; kullanıcılar bilet almayı bırakın, ana sayfada uçuş araması bile yapamadı.",
            "paradigm_shift": "Senkron istek-yanıt (request-response) mekanizması zamansal bir bağımlılık tuzağıdır: Sistem B o anda ayakta, hızlı ve erişilebilir değilse Sistem A işini tamamlayamaz. Asenkron olay odaklı mimaride ise üretici sadece olayı duyurur ('SiparisAlindi') ve kullanıcıya anında 202 Accepted döner. Üretici o olayı kimin dinlediğini bilmez. E-posta veya SMS servisi o an bakımda olsa bile mesajlar güvenli bir kuyrukta bekler ve servis açıldığında tek bir müşteri bile kaybetmeden işlenir.",
            "core_concepts": [
                {
                    "heading": "Mesajlaşma Yelpazesi: Kuyruk vs. Konu vs. Akış",
                    "text": "- **Noktadan Noktaya Kuyruk (RabbitMQ, SQS):** İş kuyruğu. Her mesajı çalışanlardan yalnızca BİRİ işler (Örn: Bir resmi boyutlandırmak).\n- **Yayınla-Abone Ol Konusu (SNS, Pub/Sub):** Fan-out modeli. Bir olay birden fazla aboneye kopyalanarak dağıtılır (Örn: Sipariş bildirimleri).\n- **Olay Akışı / Dağıtık Günlük (Kafka, Kinesis):** Diskte günlerce veya aylarca saklanan sıralı günlük (commit log). Tüketiciler kendi hızlarında okur, geçmişe dönüp tekrar oynatabilir."
                },
                {
                    "heading": "Komut (Command) vs. Olay (Event) Ayrımı",
                    "text": "- **Komut ('FaturaEpostasiGonder'):** Doğrudan niyet belirtir. Üretici ne yapılması gerektiğini ve kimin yapacağını bilir.\n- **Olay ('FaturaKesildi'):** Geçmişte gerçekleşmiş değiştirilemez bir olgudur. Üretici ne olduğunu söyler; kimin nasıl tepki vereceğine karışmaz."
                }
            ],
            "anti_patterns": [
                "**Ölümcül Senkron Zincir:** A servisi B'yi çağırır, B C'yi, C D'yi. Her servisin %99 erişilebilirliği varsa, 4 servislik zincirin toplam başarı şansı sadece %96'dır ($0.99^4$).",
                "**Akıllı Aracı, Aptal Tüketici:** İş mantığını Enterprise Service Bus (ESB) gibi kuyruk araçlarının içine gömmek yerine aracıyı aptal, uç noktaları akıllı tutmamak.",
                "**Sonsuz Yeniden Deneme (Poison Pill):** Bozuk bir mesajın fırlattığı hatayı yakalayıp Dead Letter Queue'ya (DLQ) atmadan 1 milyon kez tekrar denemek ve işleyicileri kilitlemek."
            ],
            "playbook": [
                "**1. Adım:** Kullanıcıya anında dönen HTTP uçlarını tara: Kullanıcının ekranda hemen görmesi gerekmeyen tüm işleri (e-posta, log, rapor) asenkron kuyruğa taşı.",
                "**2. Adım:** Sistemindeki her kuyruğa maksimum 3 denemeden sonra devreye giren bir Dead Letter Queue (DLQ) tanımla.",
                "**3. Adım:** Olay adlandırmalarında her zaman geçmiş zaman kullan: `UserRegistered`, `PaymentCaptured`."
            ],
            "takeaways": [
                "Zamansal ayrıştırma (temporal decoupling), sistem erişilebilirliğine verebileceğiniz en büyük hediyedir.",
                "Olaylarla geçmiş olguları duyurun; senkron zincirlerle başkalarına emir yağdırmayın.",
                "Dead Letter Queue'su olmayan her kuyruk, tek bir bozuk mesajla tüm çalışanlarınızı zehirleyebilir."
            ],
            "udemy_prompt": "Uygulamanızdaki ana kayıt veya satın alma akışına bakın: Kullanıcıya yanıt dönmeden önce arka planda senkron çağrılan kaç servis var? Hangileri asenkron kuyruğa taşınabilir?"
        },
        {
            "part_num": 14,
            "title": "Gözyaşı Dökmeden Kafka: Bölümler (Partitions), Offsetler ve Tüketici Grupları",
            "subtitle": "Geceleri kabus görmeden veri hatlarını ölçeklemek için dağıtık olay günlüklerinin gizemini çözmek.",
            "duration": "9 dk",
            "war_story": "Bir araç çağırma platformu sürücülerin GPS konumlarını takip etmek için Apache Kafka kurdu. Konu (topic) tek bir bölüm (partition) ile açıldı. Sürücü sayısı 500'den 50.000'e çıktığında tek sunucu tıkandı. Mühendis hemen 10 yeni tüketici (consumer) sunucusu başlattı. Ancak hayretle gördü ki bu 10 sunucudan sadece BİRİ çalışıyor, diğer 9'u %0 CPU ile boş oturuyordu! Panikleyen başka bir geliştirici partition anahtarını sürücü ID'si yerine rastgele UUID yaptı. Bir anda Sürücü 42'nin GPS sinyalleri 20 farklı bölüme saçıldı. Bir yolculuk sırasıyla: 1) Sürücü ulaştı, 2) Sürücü kabul etti, 3) Yolcu indi şeklinde ters sırayla işlendi! Yolcular hiç başlamamış yolculuklar için 400 TL faturalandırıldı.",
            "paradigm_shift": "Kafka geleneksel bir mesaj kuyruğu değildir; bölünmüş, çoğaltılmış, yalnızca sonuna ekleme yapılan (append-only) dağıtık bir işlem günlüğüdür. Kafka'da ölçeklenmenin temel birimi **Partition (Bölüm)**'dür ve Kafka'nın demir kuralı şudur: *Bir tüketici grubundaki aktif tüketici sayısı, konudaki partition sayısından fazla olamaz.* Paralel çalışan 10 işçi istiyorsanız en az 10 partition'ınız olmak zorundadır. Ve mesajların sırası önemliyse, aynı iş nesnesine ait olaylar mutlaka aynı partition anahtarıyla gönderilmelidir.",
            "core_concepts": [
                {
                    "heading": "Kafka'nın Temel Çarkları",
                    "text": "- **Partition ve Anahtarlar:** Kafka `hash(anahtar) % bolum_sayisi` formülünü kullanır. `siparis_123` için tüm olaylar aynı bölüme mutlak kronolojik sırayla düşer. Tüm konu genelinde global sıra yoktur; sıra YALNIZCA aynı partition içinde garantidir.\n- **Offset:** Bir partition içindeki her mesajın sıralı kimlik numarasıdır. Tüketiciler nereye kadar okuduklarını offset'lerini kaydederek (commit) takip eder.\n- **Tüketici Grupları (Consumer Groups):** Birlikte çalışan işçi grubu. Bir işçi çökerse Kafka 'Rebalance' yaparak o işçinin partition'ını gruptaki başka birine atar."
                },
                {
                    "heading": "Teslimat Garantileri: En Az Bir Kez (At-Least-Once)",
                    "text": "Dağıtık sistemlerde varsayılan garanti **En Az Bir Kez**'dir. Bir tüketici mesajı işleyip offset'i kaydedemeden çökerse, yerine gelen tüketici o mesajı TEKRAR okur! Bu yüzden tüketicileriniz mutlaka idempotent (mükerrer çalışmaya dayanıklı) olmalıdır."
                }
            ],
            "anti_patterns": [
                "**Rebalance Fırtınası:** Tüketici zaman aşımı sürelerini aşırı dar tutup uzun süren işlemlerde Kafka'nın işçiyi öldü sanarak sürekli partition dağıtımı yapması ve tüm sistemi kilitlemesi.",
                "**Rastgele Anahtar Tuzağı:** Sıralı işlenmesi gereken olaylarda partition anahtarını boş bırakıp olayların sırasını kaybetmek.",
                "**Devasa Mesaj Hatası:** Kafka üzerinden 20 MB'lık videolar veya dev PDF'ler taşımaya kalkışmak (Mesajda sadece S3 bağlantı adresini göndermelisiniz)."
            ],
            "playbook": [
                "**1. Adım:** Partition boyutlandırması: Hedeflenen veri hacmine göre partition sayısını belirle (her partition için saniyede 1-2 MB güvenli bir kuraldır).",
                "**2. Adım:** Sıralı olması gereken işlerde partition anahtarını mutlaka nesne ID'si (`musteri_id`) olarak belirle.",
                "**3. Adım:** Bütün olay işleyicilerini benzersiz olay ID'si (UUID) ve veritabanı benzersizlik kısıtlarıyla idempotent yap."
            ],
            "takeaways": [
                "Kafka sıralamayı yalnızca aynı partition içinde garanti eder, tüm konu genelinde değil.",
                "Partition sayısından fazla tüketici ayağa kaldırmak boşuna sunucu parası ödemektir.",
                "Mesajların sadece bir kez geleceğine asla güvenmeyin; her mesajın iki kez gelebileceğini varsayın."
            ],
            "udemy_prompt": "Tüketiciniz bir veritabanı kaydı attıktan hemen sonra ama Kafka'ya 'okudum' offset'ini bildirmeden önce çökerse ne olur? Kodunuz bu mükerrer okumayı güvenle atlatabilir mi?"
        },
        {
            "part_num": 15,
            "title": "Pratikte Eventual Consistency: Saga Kalıbı vs. İki Aşamalı İşleme (2PC)",
            "subtitle": "Kainatı kilitlemeden çok servisli karmaşık iş süreçlerini başarıyla yürütmek.",
            "duration": "9 dk",
            "war_story": "Bir seyahat portalı tek bir pakette Uçak, Otel ve Kiralık Araç rezervasyonunu birleştirmek istedi. Mimar, mikroservisler arasında dağıtık bir İki Aşamalı İşleme (2-Phase Commit - 2PC) mimarisi kurdu. Yoğun bir günde bir müşteri paket satın almak istedi. 2PC koordinatörü hava yolu veritabanındaki koltuğu ve otel veritabanındaki odayı satır kilidiyle kilitledi. Ardından kiralık araç API'sine istek attı. Araç firmasının API'si ağ sorunu yüzünden tam 42 saniye yanıt vermedi! Bu 42 saniye boyunca o uçak koltuğu ve otel odası kilitli kaldığı için 300 başka müşteri işlem yapamadı. Sonunda araç API'si zaman aşımına uğrayınca koordinatör üç veritabanında birden geri alma (rollback) yapmaya çalışırken kaskad bir kilitlenme yaşandı ve tüm biletleme sistemi dondu.",
            "paradigm_shift": "İki Aşamalı İşleme (2PC) modern bulut mimarilerinde ölçeklenemez. Ağ sınırları boyunca kaynakları kilitleyerek en yavaş ağ bağlantısını tüm şirketin darboğazına dönüştürür. Modern dağıtık mimarinin çözümü **Saga Kalıbı**'dır: Her servisin kendi yerel veritabanını güncelleyip bir sonraki adıma olay fırlattığı yerel işlemler dizisi. Bir adım patlarsa, sistem önceki adımların etkisini tersine çeviren **Telafi Edici İşlemleri (Compensating Transactions)** çalıştırır.",
            "core_concepts": [
                {
                    "heading": "Koreografi (Choreography) vs. Orkestrasyon (Orchestration)",
                    "text": "- **Koreografi (Olay Bazlı):** Her servis olayları dinler ve sıradakini tetikler: `SiparisServisi` -> `OdemeServisi` -> `StokServisi`. 2-3 adım için basittir ama adım sayısı arttıkça kimin neyi başlattığını takip etmek imkansızlaşır.\n- **Orkestrasyon (Merkezi Komuta):** Merkezi bir Saga Orkestratörü (Temporal.io, AWS Step Functions) servisleri sırayla yönetir: 'Ödemeyi al. Başarılıysa stoğu düş. Başarısızsa iade yap.' Görselleştirilebilir, izlenebilir ve yönetimi kolaydır."
                },
                {
                    "heading": "Telafi Edici İşlemler: Geri Alma (Rollback) Değil, Düzeltme",
                    "text": "Veritabanında rollback işlemi hiç yaşanmamış gibi siler. Bir Saga'da ise çalınan zili geri susturamazsınız: Müşteriye SMS gitti, karttan para çekildi. Telafi işlemi yeni bir telafi eylemi yaratır: İptal SMS'i göndermek, iade dekontu kesmek."
                }
            ],
            "anti_patterns": [
                "**Eksik Telafi Yolu:** Saga'nın başarı yolunu harika tasarlayıp 3. adım patladığında önceki adımları telafi edecek otomatik mekanizmayı hiç yazmamak.",
                "**İdempotent Olmayan Telafi:** İade servisini yeniden denerken idempotency anahtarı kullanmayıp müşteriye iki kat iade yapmak.",
                "**Dairesel Koreografi:** 8 servisin birbirine olay fırlattığı düzende Servis D'nin Servis B'yi tetiklemesiyle oluşan sonsuz döngüler."
            ],
            "playbook": [
                "**1. Adım:** İş süreci 3 adımı aşıyorsa veya finansal işlemler içeriyorsa doğrudan Orkestrasyon modelini seç.",
                "**2. Adım:** Kod yazmadan önce her adımın 'Başarı' ve 'Başarısızlık Telafisi' senaryosunu kağıda dök.",
                "**3. Adım:** Zaman aşımlarını ve yeniden denemeleri yönetmek için Temporal.io gibi hazır bir orkestrasyon motoru kullan."
            ],
            "takeaways": [
                "Mikroservisler arasında asla 2-Phase Commit kullanmayın; dağıtık kilitler sisteminizi felç eder.",
                "Saga kalıbı ACID atomikliğini iş seviyesinde eventual consistency ve esneklikle takas eder.",
                "Karmaşık süreçlerde merkezi bir orkestratör, olay koreografisini her zaman mağlup eder."
            ],
            "udemy_prompt": "Uygulamanızdaki çok adımlı bir süreci çizin (örn: sipariş, üyelik). 3. adım patladığında 1. ve 2. adımdaki işlemler otomatik olarak nasıl telafi ediliyor?"
        },
        {
            "part_num": 16,
            "title": "Event Sourcing ve CQRS: Geçmiş, Şimdiki Zamandan Daha Önemli Olduğunda",
            "subtitle": "Mimari karmaşıklıkta boğulmadan denetime açık ve geri sarılabilir sistemler kurmak.",
            "duration": "9 dk",
            "war_story": "Çok uluslu bir bankanın hesap yönetim sistemi bakiye bilgisini basit bir SQL satırı olarak tutuyordu: `UPDATE hesaplar SET bakiye = bakiye - 500 WHERE id = 12`. Bir sabah kurumsal bir müşteri panikle aradı: 'Dün bakiyemiz 1.2 milyon TL idi, bugün 450.000 TL görünüyor! Bu para nereye gitti?' Veritabanı yöneticisi logları aradı ama veritabanında yalnızca tek bir rakam vardı: 450.000 TL. O rakamın hangi işlemlerle, hangi otomatik kesintilerle oraya geldiğini kanıtlayan hiçbir iz yoktu! Banka denetimden geçemedi ve 250.000 TL ceza yedi. Şirket her para giriş çıkışını değiştirilemez bir olay olarak saklayan Event Sourcing mimarisine geçmek zorunda kaldı.",
            "paradigm_shift": "Geleneksel CRUD mimarileri tarihi yok eder: Bir satırı güncellediğinizde eski durum sonsuza dek silinir. **Event Sourcing** bunu tersine çevirir: Gerçeğin kaynağı mevcut durum değil, geçmişte yaşanan değiştirilemez olayların günlüğüdür (`HesapAcildi`, `ParaYatirildi`, `ParaCekildi`). Mevcut durum bu olayların baştan sona oynatılmasıyla hesaplanan bir sonuçtur. Bunu **CQRS (Command Query Responsibility Segregation)** ile birleştirdiğinizde; yazma işlemleri (Komutlar) olay günlüğüne giderken, okuma işlemleri (Sorgular) optimize edilmiş hazır tablolardan sunulur.",
            "core_concepts": [
                {
                    "heading": "CQRS ve Event Sourcing Bileşenleri",
                    "text": "- **Komut Tarafı:** İş kurallarını doğrular ve olay günlüğüne (Event Store) yeni olayı ekler.\n- **Olay Deposu (Event Store):** Yalnızca ekleme yapılan (append-only) veritabanı. Olaylar asla silinmez veya güncellenmez.\n- **Okuma Modeli (Projeksiyonlar):** Olayları dinleyip okuma için optimize edilmiş tablolara yazan işleyiciler (Örn: Arama için Elasticsearch, bakiye sorgusu için Redis).\n- **Anlık Görüntü (Snapshotting):** Mevcut durumu bulmak için 100.000 olayı baştan sona oynatmamak için her 100 olayda bir ara durum kaydı almak."
                },
                {
                    "heading": "Ne Zaman Kullanılmamalı? (Pratik Uyarı)",
                    "text": "Event Sourcing çok yüksek zihinsel yük getirir: 5 yıl önceki olay şemalarının güncellenmesi zordur, eventual consistency ekipleri zorlar ve KVKK 'Unutulma Hakkı' için kriptografik silme taklaları gerektirir. Sadece finans, sigorta ve denetim gerektiren çekirdek alanlarda kullanın; basit bir blogda asla kullanmayın."
                }
            ],
            "anti_patterns": [
                "**Her Yere Event Sourcing:** Basit bir profil ayarları veya blog yazısı için Event Sourcing kurup 10 kat daha fazla kod yazmak.",
                "**Değiştirilen Olay Hatası:** Projeksiyon hatası yüzünden olay deposuna yazılmış geçmiş bir olayı veritabanından güncellemeye kalkışmak.",
                "**Eksik Snapshot:** 5 milyon olayı her istekte sıfırdan oynatmaya çalışarak API gecikmelerini 30 saniyeye fırlatmak."
            ],
            "playbook": [
                "**1. Adım:** Event Sourcing'i sadece denetim geçmişinin ürünün kendisi olduğu alanlara (finans, kargo geçmişi) sakla.",
                "**2. Adım:** Olay şemalarını baştan savunmacı tasarla: Olay alanlarını versiyonla (`SiparisAlindiV1`, `SiparisAlindiV2`).",
                "**3. Adım:** Durum yeniden oluşturma sürelerini 10 milisaniyenin altında tutmak için ilk günden Snapshotting mekanizmasını kur."
            ],
            "takeaways": [
                "CRUD anlık durumu gösterir; Event Sourcing o duruma nasıl geldiğinizin hikayesini anlatır.",
                "CQRS yazma modeliyle okuma modelini birbirinden ayırarak ikisini de bağımsız optimize etmenizi sağlar.",
                "Event Sourcing bir Ferrari'dir: İnanılmaz güçlüdür ama bakımı ve yakıtı son derece pahalıdır."
            ],
            "udemy_prompt": "Şirketinizde geçmiş hareketlerin silinmez bir kütükte saklanmasından en çok fayda sağlayacak alan neresidir? CQRS'i mevcut sisteminize sokmanın en büyük riski ne olurdu?"
        }
    ]
}
