# Parça 21: Her Şey Her An Çöker: Dayanıklı Mimarın Zihniyeti
**Bölüm 6: Güvenilirlik ve Hata Toleransı — Çöküş İçin Tasarlamak**  
*Tahmini Süre / Sesli Özet: 9 dk*  
*Amazon CTO'su Werner Vogels'ın demir yasasını benimsemek ve zarif bozulma (graceful degradation) tasarlamak.*

---

## 🎙️ Mimarın Sahasından Yaşanmış Kriz Hikayesi

> 28 Şubat 2017'de bir Amazon S3 mühendisi, Virginia bölgesindeki birkaç sunucuyu devre dışı bırakmak için bir komut girdi. Komuttaki küçük bir yazım hatası hedeflenenden çok daha fazla sunucuyu sildi ve ana S3 altyapısı çöktü. S3'e bağımlı binlerce büyük şirket anında karanlığa gömüldü. Ancak en trajikomik fiyaskoyu akıllı lamba üreten bir IoT şirketi yaşadı: Lambanın arka uç servisi bir log dosyasını S3'e yükleyemediği için tüm kimlik doğrulama akışı 500 hatası fırlattı! Amerika genelinde yüz binlerce insan, Virginia'daki bir depolama servisi çöktü diye evlerinin salonundaki fiziksel lambalarını açamadı ve saatlerce karanlıkta oturdu!

## 🧠 Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa

Amazon CTO'su Werner Vogels'ın ünlü sözü dağıtık mimarinin özetidir: *'Her şey her an çöker.'* Diskler bozulur, ağ switch'leri takılır, bulut bölgeleri su basar ve operatörler klavyede hata yapar. Acemi bir mimar hiçbir şeyin çökmeyeceği umuduyla sistem tasarlar; usta bir mimar ise her şeyin aynı anda çökeceğini varsayarak sistemin **Zarif Bozulma (Graceful Degradation)** ile ayakta kalmasını sağlar. Öneri motoru çöktüyse genel en popüler ürünleri gösterin; analitik çöktüyse logu sessizce yutun. Kozmetik bir özelliğin ana iş sürecini rehin almasına asla izin vermeyin.

## 📐 Temel Mimari İlkeler ve Zihinsel Modeller

### Zarif Bozulma ve Hasar Yarıçapı (Blast Radius)
- **Hasar Yarıçapı:** X Servisi çöktüğünde kullanıcıların ve özelliklerin yüzde kaçı etkileniyor? Mimarın görevi bu yarıçapı %100'den %5'e indirmektir.
- **Zarif Bozulma:** Bir bağımlılık kapalıyken 500 hatasıyla patlamak yerine yedek planı devreye sokmak:
  - Netflix: Kişiselleştirilmiş öneri AI'ı çökerse, herkese genel 'Top 10 Film' listesini gösterir.
  - E-Ticaret: Stok kontrol servisi çökerse siparişi alıp 'Stok onaylanıyor' durumuna çeker ve arka planda eşitler.

### Açık Başarısızlık vs. Kapalı Başarısızlık
- **Fail Closed (Güvenlik / Finans):** Dolandırıcılık tespiti servisi çöktüyse şüpheli ödemeyi reddet.
- **Fail Open (Kullanıcı Deneyimi):** Kullanıcı profil resmi servisi çöktüyse gri bir silüet çiz ve kullanıcının panele girmesine izin ver.

## ⚠️ Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar

- **Camdan Şato:** Sistemdeki her bir parçayı varoluşsal bağımlılık yapmak: Yorumlar veya anket servisi çöktüğünde ana sayfanın komple patlaması.
- **Kontrolsüz Kaskad Çöküş:** Yavaşlayan tek bir arka plan servisinin tüm platformdaki işlem thread'lerini tüketerek domino etkisiyle her şeyi devirmesi.
- **Sessiz Yutma:** Kritik veritabanı hatalarını `try { ... } catch (Exception e) {}` içine alıp hiçbir yere loglamadan felaketleri gizlemek.

## 🎯 Mimarın Eylem Planı: Bu Haftaki Somut Adımlar

- **1. Adım:** Bağımlılık Triage'ı yap: Servislerini Seviye 1 (Varoluşsal: Olmazsa iş durur) ve Seviye 2 (Yardımcı: Olmasa da olur) olarak etiketle.
- **2. Adım:** Bütün Seviye 2 bağımlılıklarına çöktüklerinde varsayılan değer dönen bir fallback mekanizması bağla.
- **3. Adım:** İstisnasız her ağ çağrısına 2 saniyeyi aşmayan katı bir zaman aşımı (timeout) koy.

## 📌 Mimari Çıkarımlar ve Hile Tablosu

- Kozmetik bir özelliğin şirketinizin ana gelir akışını rehin almasına izin vermeyin.
- Dayanıklılık donanımın ve ağların size ihanet edeceğini baştan kabul etmektir.
- Bir kriz anında %80 fonksiyonla hizmet vermeye devam eden bir sistem, %0'a çakılan bir sistemden fersah fersah üstündür.

## 💡 Udemy Kursu & NotebookLM Tartışma ve Ödev Sorusu

**Ödev / Yansıtma Sorusu:** Uygulamanızın ana sayfasına bakın: Veritabanınız şu an 5 saniyelik bir kesinti yaşasa sayfanın hangi kısımları yine de render edilebilir? Kullanıcıya bozulmuş ama çalışan bir arayüz sunabiliyor musunuz?
