# Parça 05: Monolit Geri Dönüyor: Ne Zaman Birleşik Kalmalı, Ne Zaman Bölünmeli?
**Bölüm 2: Planlar ve Sınırlar — Karmaşıklığı Parçalara Ayırmak**  
*Tahmini Süre / Sesli Özet: 9 dk*  
*Şirketiniz henüz kaldıramayacak durumdayken ağır 'dağıtık sistemler vergisini' ödemekten nasıl kaçınırsınız?*

---

## 🎙️ Mimarın Sahasından Yaşanmış Kriz Hikayesi

> 8 kişilik bir lojistik girişiminde günde 500 paket dağıtılıyordu. Konferans videolarını izleyen lider ekip, 'Gerçek teknoloji şirketleri mikroservis kullanır' diyerek derli toplu Ruby on Rails monolitlerini 24 farklı mikroservise böldü. Bir anda tek bir kargo siparişi oluşturmak 6 ayrı veritabanı arasında 9 ağ çağrısı koordine etmeyi gerektirdi. Bildirim servisi 200ms geciktiğinde müşterinin kredi kartından iki kez para çekiliyordu. Geliştiriciler yeni özellik geliştirmek yerine zamanlarının %60'ını JSON dönüştürme ve dağıtık yarış durumlarını (race conditions) debug etmekle harcadı. Yatırım paraları bittiğinde, aylık 80 dolarlık tek bir sunucuda rahatça çalışacak sistem için AWS Kubernetes'e ayda 18.000 dolar ödüyorlardı.

## 🧠 Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa

Dağıtık sistemler vergisi gerçektir, pahalıdır ve pazarlığa açık değildir. Bir monoliti mikroservislere böldüğünüzde; bellek içi fonksiyon çağrılarını ağ çağrılarıyla, derleme anı güvenliğini çalışma anı serileştirmesiyle ve atomik ACID veritabanı işlemlerini eventual consistency baş ağrısıyla takas edersiniz. Martin Fowler'ın 'Dağıtık Nesnelerin Birinci Yasası' hala geçerlidir: *Nesnelerinizi dağıtmayın.* İyi tasarlanmış bir Modüler Monolit, kontrolsüz bir mikroservis çorbasından neredeyse her zaman kat kat üstündür.

## 📐 Temel Mimari İlkeler ve Zihinsel Modeller

### Modüler Monolit vs. Mikroservis Sınırı
- **Modüler Monolit:** Tek bir dağıtım paketi, ancak paket/modül görünürlüğü ile sıkı sınırlarla ayrılmış etki alanları. Hızlı derleme, paylaşılan bellek, kolay yerel hata ayıklama ve tekil veritabanı işlemleri.
- **Mikroservisler:** Bağımsız dağıtım ve bağımsız ölçeklenebilirlik. Yalnızca 50+ mühendisin aynı kod tabanında birbirine çarptığı veya devasa ölçek farklarının tek bir ikiliyi tıkadığı durumlarda meşrudur.

### Dağıtık Sistemler Vergisi Kontrol Listesi
Bölünmeden önce şu bedelleri ödemeye hazır mısınız?
1. Dağıtık izleme (OpenTelemetry).
2. Ağ gecikmesi (her sekmede 5-50ms).
3. Devre kesiciler (circuit breakers) ve yeniden deneme fırtınaları.
4. Çift yazma (dual-write) tutarsızlıkları.

## ⚠️ Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar

- **Dağıtık Monolit:** Mikroservislerin tüm operasyonel kabuslarına (ağ gecikmesi, kademeli çöküş) sahipken, aynı zamanda monolitlerin tüm hantallığına (servislerin canlıya alınırken aynı anda ve belirli sırada çıkma zorunluluğu) sahip olan ucube mimari.
- **Erken Mikroservis:** Etki alanı sınırları henüz oturmadan servisleri bölüp her hafta 5 farklı git reposunda çapraz refactoring yapmak zorunda kalmak.
- **Paylaşılan Veritabanı Mikroservisi:** 10 ayrı mikroservisin hepsinin aynı veritabanı tablolarına doğrudan sorgu atması, kapsüllemeyi tamamen yok etmesi.

## 🎯 Mimarın Eylem Planı: Bu Haftaki Somut Adımlar

- **1. Adım:** Sisteminizi önce Modüler Monolit olarak inşa edin: Modül A'nın Modül B'nin dahili sınıflarını çağırmasını linter kurallarıyla engelleyin.
- **2. Adım:** Servisleri varlık bazında bölmeyin ('Kullanıcı Servisi', 'Tarih Servisi' gibi); bağımsız iş yetenekleri bazında bölün ('Ödeme Takas' vs. 'Katalog Arama').
- **3. Adım:** Ayrıştırma Testi: Bir modülü yalnızca tamamen farklı bir ölçeklenme profili gerektirdiğinde veya tamamen bağımsız bir ekibe devredildiğinde ayrı bir mikroservise dönüştürün.

## 📌 Mimari Çıkarımlar ve Hile Tablosu

- Düzgün bir monolit inşa edemiyorsanız, başarılı bir dağıtık sistem inşa edebileceğinizi nereden çıkarıyorsunuz?
- Mikroservisler kötü kodun teknik ilacı değil; devasa ekiplerin organizasyonel koordinasyon çözümüdür.
- Modern donanımlarda çalışan modüler bir monolit, milyonlarca kullanıcıyı sıfır operasyonel dertle kaldırabilir.

## 💡 Udemy Kursu & NotebookLM Tartışma ve Ödev Sorusu

**Ödev / Yansıtma Sorusu:** Mevcut sisteminize bakın. Mikroservis kullanıyorsanız, canlıya çıkarken mutlaka birlikte dağıtılması gereken servisleriniz var mı? Monolitteyseniz, en çok dağıtım sürtüşmesi yaratan alan neresi?
