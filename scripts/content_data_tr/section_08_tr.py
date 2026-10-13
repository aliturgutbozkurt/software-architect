# Bölüm 8: Gözlemlenebilirlik ve Operasyonel Mükemmellik — Karanlıkta Görmek (Parça 29 - 32)

SECTION_8_TR = {
    "section_num": 8,
    "section_title": "Gözlemlenebilirlik ve Operasyonel Mükemmellik — Karanlıkta Görmek",
    "section_desc": "Kör sistemleri şeffaf cam kutulara dönüştürmek: OpenTelemetry metrikleri, logları ve dağıtık izleri; Google SRE hata bütçeleri; FinOps ile bulut israfını budamak ve suçlamasız post-mortem kültürü.",
    "parts": [
        {
            "part_num": 29,
            "title": "Gözlemlenebilirlik Üçlüsü: Metrikler, Loglar ve Dağıtık İzleme (Tracing)",
            "subtitle": "OpenTelemetry bağlam aktarımı ile 15 mikroservis arasındaki 200 milisaniyelik yavaşlığı 30 saniyede bulmak.",
            "duration": "9 dk",
            "war_story": "Bir online aracı kurumun 40 mikroservisi vardı. Borsa açılışında hisse senedi alım emri vermek 150 milisaniye yerine 8 saniye sürmeye başladı. Operasyon ekibi saniyede 50.000 satır yapılandırılmamış metin logu akan 40 ayrı terminal penceresine boş gözlerle bakıyordu. Her servis aynı şeyi yazıyordu: `Bağlantı zaman aşımı` veya `Alt servisten yanıt bekleniyor`. Ama suçlu kimdi? Ekipler 4 saat boyunca tartıştı: Emir ekibi hesap ekibini, hesap ekibi risk ekibini, risk ekibi veritabanı ekibini suçladı. Mimar nihayet sisteme tek bir `trace_id` ile OpenTelemetry dağıtık izleme kurduğunda gerçek 30 saniyede ortaya çıktı: Junior bir mühendisin yazdığı unutulmuş bir IP sorgu servisi, her hisse alımında aracı kurumun kendi IP adresini ters-DNS ile sorgulamaya çalışıyordu!",
            "paradigm_shift": "İzleme (Monitoring) sistem çöktüğünde size haber verir ('CPU %95'); Gözlemlenebilirlik (Observability) ise sistemin dış çıktılarına bakarak iç durumunu anlamanızı ve daha önce aklınıza gelmemiş soruları bile sorabilmenizi sağlar. Dağıtık bir mimaride `grep` ile hata arayamazsınız. İhtiyacınız olan **Gözlemlenebilirlik Üçlüsü**'dür: Metrikler yangın olduğunu haber verir, Loglar dumanın kokusunu tarif eder, Dağıtık İzleme (Tracing) ise yangını başlatan kibriti gösterir.",
            "core_concepts": [
                {
                    "heading": "Gözlemlenebilirlik Üçlüsünün Rolleri",
                    "text": "- **Metrikler (Prometheus, Datadog):** Zaman içindeki sayısal veriler (sayaçlar, göstergeler). Depolaması çok ucuzdur, alarmlar için harikadır ama tekil istek bağlamı içermez.\n- **Yapılandırılmış Loglar (JSON):** Detaylı olay kayıtları. Zaman damgası, seviye ve bağlam (`kullanici_id`, `islem_id`) içermelidir.\n- **Dağıtık İzleme (OpenTelemetry, Jaeger):** Bir isteği ağ sınırları boyunca adım adım takip eder. İsteğe benzersiz bir `trace_id` atanır ve her sekmede bir `span` oluşturulur. Gecikmeler şelale grafiğinde net şekilde görünür."
                },
                {
                    "heading": "Metriklerde Kardinalite Tuzağı",
                    "text": "Metrik etiketlerine asla `kullanici_id` veya `siparis_id` gibi yüksek kardinaliteli (milyonlarca farklı değer alabilen) alanlar eklemeyin! Prometheus'un belleğini patlatır ve SaaS faturanıza binlerce dolar yansıtır. Yüksek kardinalite log ve trace içindir."
                }
            ],
            "anti_patterns": [
                "**Düz Metin Loglama:** `console.log('Kullanıcı girdi: ' + id)` yazarak logları aranamaz hale getirmek (Bunun yerine JSON log kullanın).",
                "**Kopuk İzleme Zinciri:** Aşağı servise HTTP isteği atarken W3C `traceparent` başlığını iletmeyi unutup dağıtık izleme şelalesini parçalamak.",
                "**Alarm Yorgunluğu (Yalancı Çoban):** Önemsiz her uyarıya PagerDuty alarmı bağlayıp mühendisleri gece uyarıları sessize almaya alıştırmak."
            ],
            "playbook": [
                "**1. Adım:** Bütün servislerde üretici bağımsız standart olarak OpenTelemetry (OTel) SDK'sını kullan.",
                "**2. Adım:** API Gateway'de her gelen isteğe bir `trace_id` üret ve yanıt başlığına (`X-Trace-Id`) ekle.",
                "**3. Adım:** Bütün uygulama loglarını JSON formatına çevir ve o anki aktif `trace_id`yi her log satırına otomatik iliştir."
            ],
            "takeaways": [
                "Dağıtık izleme olmadan mikroservis debug etmek, 40 ayrı samanlıkta iğne aramaya benzer.",
                "Metrikler sorunu haber verir; izler (traces) yerini gösterir; loglar sebebini açıklar.",
                "Metrik etiketlerinde düşük kardinalite; log ve izlerde yüksek kardinalite kullanın."
            ],
            "udemy_prompt": "Canlıdaki tek bir kullanıcı isteğini alıp yaptığı tüm veritabanı sorgularını ve mikroservis seyahatlerini baştan sona tek bir ekranda görebiliyor musunuz? Eksik olan nedir?"
        },
        {
            "part_num": 30,
            "title": "Hizmet Seviyesi Hedefleri: SLA, SLO ve Hata Bütçesi (Error Budget)",
            "subtitle": "Google SRE ilkeleri Ürün ve Mühendislik arasındaki ezeli savaşı nasıl matematiksel bir uyuma dönüştürür?",
            "duration": "9 dk",
            "war_story": "Bir SaaS şirketinde Ürün Yönetimi ile Mühendislik savaştaydı. Ürün Yöneticisi büyük bir müşteriyi bağlamak için bu ay 10 yeni özellik çıkarmak istiyordu. Mühendislik Direktörü ise 'Sistem çökmek üzere' diyerek tüm geliştirmeleri 3 ay durdurup veritabanını yeniden yazmak istiyordu. Sprint planlama toplantıları bağırış çağırışla geçiyordu. CEO toplantıda 'Sistemimiz yeterince kararlı mı?' diye sordu. Ürün 'Evet, süper!', Mühendislik ise 'Hayır, felaket!' dedi. İkisinin de elinde somut bir matematik olmadığı için şirket aylarca siyasi bir kilitlenme yaşadı.",
            "paradigm_shift": "'%100 kesintisizlik' istemek amatörce bir fantezidir. %100 güvenilirlik imkansızdır ve bunu kovalamak sonsuz bütçe gerektirirken özellik geliştirme hızını sıfıra indirir. Google Site Reliability Engineering (SRE) çerçevesi bu gerilimi matematikle çözer: **SLI (Göstergeler)**, **SLO (Hedefler)** ve **Hata Bütçesi (Error Budget)**. Hata bütçesi, kesintiyi inovasyon için harcanabilecek planlı bir kaynağa dönüştürür.",
            "core_concepts": [
                {
                    "heading": "SRE Kutsal Üçlüsü",
                    "text": "- **SLI (Service Level Indicator):** Ölçülen gerçek başarı oranı: `Başarılı İstekler / Toplam İstekler * 100%`.\n- **SLO (Service Level Objective):** Ekip içi hedef: `30 günlük periyotta isteklerin %99.9'u SLI'ı karşılamalıdır`.\n- **SLA (Service Level Agreement):** Müşteriye verilen ve cezai yaptırımı olan yasal sözleşme (Genellikle SLO'dan daha gevşektir, örn: %99.5)."
                },
                {
                    "heading": "Hata Bütçesi Denklemi",
                    "text": "SLO'nuz %99.9 ise, aylık hata bütçeniz %0.1'dir (bu da ayda **tam 43.2 dakika kabul edilebilir kesinti veya bozulma** demektir). Eğer ay ortasında bütçeniz duruyorsa Ürün ekibi hızla riskli yenilikler deneyebilir! Ancak bütçe sıfırlandıysa tüm yeni özellik dağıtımları donar ve tüm kapasite stabiliteye ayrılır."
                }
            ],
            "anti_patterns": [
                "**Dört Dokuz Serabı:** Altyapınız ve bulut sağlayıcınız yalnızca %99.9 sunarken müşteriye sözleşmede %99.99 (ayda 4 dakika kesinti) taahhüt etmek.",
                "**Kibirli Göstergeler:** Kullanıcı deneyimi yerine sunucu CPU'sunu SLI olarak tanımlamak.",
                "**Dişsiz Hata Bütçesi:** Hata bütçesi %300 aşılmasına rağmen yönetimin kuralları çiğneyip riskli kodları zorla canlıya aldırması."
            ],
            "playbook": [
                "**1. Adım:** Temel kullanıcı akışınız için 1-2 kullanıcı odaklı SLI tanımla (Ödeme Başarı Oranı, Arama < 300ms).",
                "**2. Adım:** Ürün Yöneticisiyle oturup bir SLO belirle (%99.9 gibi) ve aylık izin verilen kesinti dakikanızı hesaplayın.",
                "**3. Adım:** Net bir Hata Bütçesi Politikası yaz: Bütçe biterse güvenilirlik dışındaki tüm yeni özellik geliştirmeleri durur."
            ],
            "takeaways": [
                "%100 erişilebilirlik yanlış hedeftir; yeniliği durdurur ve sermayeyi yakar.",
                "SLO'lar Ürün ve Mühendislik arasındaki duygusal tartışmaları nesnel verilere dönüştürür.",
                "Hata Bütçesi mühendisliğe teknik borcu temizlemesi için meşru ve sorgulanamaz bir yetki verir."
            ],
            "udemy_prompt": "Ana servisinizin SLO hedefi nedir? Yoksa, 30 günlük bir sürede isteklerin yüzde kaçının başarısız olması müşterilerinizi gerçekten çıldırtır?"
        },
        {
            "part_num": 31,
            "title": "FinOps ve Bulut Ekonomisi: Şirketi İflas Ettirmeyen Mimari",
            "subtitle": "Maliyet verimli mimariler tasarlamak ve binlerce dolarlık bulut vampirlerini yok etmek.",
            "duration": "9 dk",
            "war_story": "Yapay zeka tabanlı bir analitik girişimi 5 milyon dolar yatırım aldı. Altı ay sonra CEO dehşet içinde CTO'yu aradı: Aylık AWS faturası 4.000 dolardan 92.000 dolara fırlamıştı! İncelemede üç mimari rezalet ortaya çıktı: 1) Bir mühendis Kubernetes kümesinde CPU isteklerini aşırı şişirdiği için 80 sunucu ortalama %4 CPU ile bomboş çalışıyordu, 2) Kapatılmış test ortamlarından kalan boşta duran EBS diskleri ayda 12.000 dolar hayalet fatura üretiyordu, 3) Bir yedekleme betiği her 6 saatte bir 20 terabayt veriyi AWS bölgeleri arasında kopyalayarak ayda 30.000 dolar veri çıkış (egress) ücreti üretiyordu! Şirket ilk 100 müşterisini bile bulamadan yatırımının beşte birini bulut israfında yakmıştı.",
            "paradigm_shift": "Bulut bilişim sınırsız ve bedava bir açık büfe değildir; her mimari kararın anında dolar cinsinden bir karşılığı olan sayaçlı bir aboneliktir. Bulutta **mimarlık bir finans mühendisliğidir**. Usta bir mimar sadece 'Sistem 10 kat trafiği kaldırır mı?' diye sormaz; '10 kat trafikte işlem başına birim maliyetimiz ne olur?' diye sorar. Kullanıcı sayısı 2 katına çıkarken bulut faturası 4 katına çıkıyorsa o mimari iflas etmeye mahkumdur. **FinOps**, bulut maliyetini mimarinin temel bir kalite metriği haline getirme disiplinidir.",
            "core_concepts": [
                {
                    "heading": "Yazılım Mimarisinin Birim Ekonomisi",
                    "text": "- **Aktif Kullanıcı Başına Maliyet:** Kullanıcı başına geliriniz 0.05 dolarsa, kullanıcı başına altyapı maliyetiniz 0.01 doların altında olmak ZORUNDADIR.\n- **Ağ Çıkış Ücretleri (Egress):** Aynı veri merkezinde veri taşımak ücretsizdir; bölgeler (AZ) arası taşımak GB başına 0.01$; internete çıkarmak ise 0.09$'dır. Mimar sınırlar arası veri trafiğini minimize etmelidir."
                },
                {
                    "heading": "FinOps Optimizasyon Kolları",
                    "text": "1. **Doğru Boyutlandırma:** Konteyner CPU/RAM taleplerini gerçek P95 kullanımına göre küçültün.\n2. **Taahhüt İndirimleri (Savings Plans):** Öngörülebilir baz yükler için 1-3 yıllık taahhütle %40-60 tasarruf edin.\n3. **Spot Sunucular:** Durumsuz arka plan işlerinde ve testlerde %80 indirimli spot makineleri kullanın.\n4. **Depolama Kademelendirme:** Eski log ve yedekleri S3 Standard'dan otomatik yaşam döngüsüyle Glacier'a taşıyın."
                }
            ],
            "anti_patterns": [
                "**Aşırı Tahsis Refleksi:** 'Belki yoğun olur' diyerek her mikroservise 4 CPU ve 8 GB RAM verip sunucu kapasitesinin %95'ini boşta yatırmak.",
                "**Zombi Kaynak Mezarlığı:** Terk edilmiş yük dengeleyiciler, bağlanmamış diskler ve hafta sonları kimsenin bakmadığı çalışan test ortamları.",
                "**Bölgeler Arası Geveze Servisler:** Bölge 1'deki bir servisin Bölge 2'deki veritabanına saniyede 10.000 sorgu atıp şirkete binlerce dolar gizli ağ faturası çıkarması."
            ],
            "playbook": [
                "**1. Adım:** Zorunlu etiketleme (Tagging) getir: Her bulut kaynağında `Sahip`, `Ortam` ve `Servis` etiketi olsun.",
                "**2. Adım:** Bulut faturasının en büyük 3 harcama kalemini tespit et (genellikle EC2, RDS ve Veri Transferi).",
                "**3. Adım:** Geliştiriciler akşam evlerine gittiğinde tüm geliştirme ve test ortamlarını otomatik kapatan zamanlayıcı kur (%65 tasarruf)."
            ],
            "takeaways": [
                "İyi mimari, maliyet-etkin mimaridir; sınırsız bütçeyle herkes hızlı sistem kurabilir.",
                "Veri transfer ücretlerini şahin gibi izleyin; faturanın en sinsi kalemi ağ çıkışlarıdır.",
                "Test ortamlarını mesai bitiminde kapatmayı ve eski yedekleri arşivlemeyi otomatikleştirin."
            ],
            "udemy_prompt": "Şirketinizin aylık bulut faturasının ne kadar olduğunu biliyor musunuz? 1.000 API çağrısı veya aktif kullanıcı başına altyapı maliyetiniz kaç kuruş?"
        },
        {
            "part_num": 32,
            "title": "Kriz Yönetimi ve Suçlamasız Olay İncelemesi (Blameless Post-Mortem)",
            "subtitle": "Yüksek performanslı mühendislik kültürleri felaketleri nasıl sistemik dayanıklılığa dönüştürür?",
            "duration": "9 dk",
            "war_story": "Gergin bir Perşembe öğleden sonrasında acemi bir DevOps mühendisi test ortamı sandığı bir ekranda temizlik betiği çalıştırdı. Canlı veritabanıydı. Üç saniye içinde müşteri tablosu tamamen silindi. Şirkette panik koptu. CTO hemen genel Slack kanalına yazdı: 'Bu betiği kim çalıştırdı? Bu kabul edilemez bir sorumsuzluk!' Mühendis Cuma sabahı kovuldu. Üç ay sonra başka bir kıdemli mühendis gece yarısı stres altında bir hotfix geçerken aynı hatayı yaptı ve canlı stok tablosunu sildi! Neden mi? Çünkü canlı ve test ortamlarının sunucu isimleri neredeyse aynıydı ve betikte hiçbir onay sorusu yoktu. İlk mühendisi kovmak hiçbir mimari zafiyeti çözmemişti; sadece bir sonraki mühendisin hatasını korkuyla gizlemesine yol açmıştı.",
            "paradigm_shift": "İnsan hatası asla bir olayın kök nedeni değildir; insan hatası sistemik bir mimari veya yöntemsel açığın *belirtisidir*. Tek bir kişi tek bir tuşa basarak canlı veritabanını silebiliyorsa, o sistem mimari olarak kusurludur. Etsy ve John Allspaw'un öncülük ettiği **Suçlamasız Olay İncelemesi (Blameless Post-Mortem)** felsefesi şunu kabul eder: Mühendisler ellerindeki bilgi ve bağlamla ellerinden gelenin en iyisini yapmaya çalışan yetkin profesyonellerdir. Amaç insanı cezalandırmak değil; sistemik zaafları bulup otomatik bariyerler inşa etmektir.",
            "core_concepts": [
                {
                    "heading": "Suçlamasız Post-Mortem Şablonu",
                    "text": "1. **Özet:** Ne oldu, müşteri etkisi neydi, kesinti kaç dakika sürdü?\n2. **Zaman Çizelgesi:** Olay anından tespite, müdahaleye ve çözüme kadar dakika dakika kronoloji.\n3. **Katkıda Bulunan Faktörler (5 Neden Analizi):** 'Ahmet yanlış komut yazdı'dan öteye geç: 'Neden terminal prodüksiyona doğrudan açıktı? Neden onay istemedi? Neden alarm 40 dakika sonra çaldı?'\n4. **Neler İyi Gitti vs. Nerede Şanslıydık:** Ekip çalışmasını takdir et; tesadüfen kurtulan yerleri tespit et.\n5. **Önleyici Eylemler:** Belirli kişilere atanmış tarihli somut mühendislik görevleri."
                },
                {
                    "heading": "Kriz Komutanı (Incident Commander) Rolü",
                    "text": "Kritik bir Sev-1 krizinde demokrasi biter. Kriz Komutanı görev dağıtımını yapar, yöneticileri oyalayarak mühendislerin kafasını rahatlatır ve hata ayıklama kanalını sakin ve odaklı tutar."
                }
            ],
            "anti_patterns": [
                "**Günah Keçisi Kültürü:** Hata yapanı suçlamak, utandırmak veya kovmak; bu durum ekiplerin arızaları saklamasına ve risk almaktan kaçınmasına yol açar.",
                "**Aksiyon Mezarlığı:** Harika bir inceleme belgesi hazırlayıp oradaki 10 önleyici bileti hiçbir zaman sprint planına almayıp unutmak.",
                "**Tek Bir Kök Neden Yanılgısı:** Karmaşık sistemlerin neredeyse hiçbir zaman tek bir sebepten çökmediğini unutup 'tek suçlu' aramak."
            ],
            "playbook": [
                "**1. Adım:** Açık kriz seviyeleri belirle (Sev-1: Gelir akışı durdu, Sev-2: Kısmi kesinti) ve net müdahale süreleri koy.",
                "**2. Adım:** Her Sev-1 veya Sev-2 olayından sonra 48 saat içinde mutlaka Suçlamasız Post-Mortem toplantısı yap.",
                "**3. Adım:** Çıkan önleyici aksiyon maddelerinin en az %50'sini hemen bir sonraki sprintin içerisine zorunlu olarak koy."
            ],
            "takeaways": [
                "İnsanları kovarak güvenilirlik elde edemezsiniz; güvenilirliği mühendislikle inşa edersiniz.",
                "Suçlamasız kültür yumuşak davranmak değil; sistemik gerçekleri acımasızca ortaya çıkarma disiplinidir.",
                "Post-mortem'i yapılmayan her kesinti, evrene boşuna ödenmiş bir okul harcıdır."
            ],
            "udemy_prompt": "Şirketinizdeki son büyük kesintiyi hatırlayın: Odak noktası hatayı yapan kişiyi bulmak mıydı, yoksa o hataya izin veren sistem koşullarını onarmak mı?"
        }
    ]
}
