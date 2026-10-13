# Parça 17: Yatay Ölçekleme: Durumsuzluk (Statelessness) ve 12-Faktör Uygulama
**Bölüm 5: Ölçeklenebilirlik ve Esneklik — İzdihamı Yönetmek**  
*Tahmini Süre / Sesli Özet: 9 dk*  
*Oturum durumunu sunucu belleğinde tutmanın otomatik ölçeklemeyi kullanıcılar için bir rulet oyununa çevirmesi.*

---

## 🎙️ Mimarın Sahasından Yaşanmış Kriz Hikayesi

> Bir hızlı moda e-ticaret sitesi akşam 20:00'de ulusal televizyonda ana haberlere çıktı. Sitenin anlık ziyaretçisi 3 dakika içinde 500'den 60.000'e fırladı. Bulut otomatik ölçekleyicisi (auto-scaler) harika bir tepki vererek sunucu sayısını 2'den 30'a çıkardı. Ancak dakikalar içinde çağrı merkezine binlerce öfkeli telefon yağmaya başladı: Müşteriler sepete ürün ekliyor, 'Sonraki Sayfa'ya bastıklarında sepetleri bomboş görünüyordu! Ya da ödeme yaparken aniden sistemden atılıp bambaşka bir kullanıcının ekranını görüyorlardı! Neden mi? Geliştiriciler kullanıcının sepetini ve oturumunu Sunucu 1'in yerel RAM belleğinde tutmuştu. Yük dengeleyici bir sonraki isteği Sunucu 7'ye attığında, Sunucu 7 o kullanıcıyı daha önce hiç görmemişti.

## 🧠 Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa

Dikey ölçeklemenin (daha büyük makine almak) fiziksel ve mali bir tavanı vardır; yatay ölçekleme (daha fazla ucuz makine eklemek) ise neredeyse sonsuzdur—**ANCAK ve ANCAK** uygulama örnekleriniz tamamen durumsuz (stateless) ise. Yatay esnekliğin altın kuralı: *Herhangi bir sunucu herhangi bir saniyede tek bir kullanıcı bile fark etmeden öldürülebilmelidir.* Bir sunucu kendi içinde durum saklıyorsa o şefkatle bakılması gereken bir 'evcil hayvandır (pet)'; durumsuz ise otomatik ölçekleyicinin saniyeler içinde kesip yenisini koyabileceği bir 'büyükbaş hayvandır (cattle)'.

## 📐 Temel Mimari İlkeler ve Zihinsel Modeller

### 12-Faktör Durumsuzluk İlkeleri
- **Faktör VI (Süreçler):** Uygulamayı bir veya daha fazla durumsuz süreç olarak çalıştırın. Kalıcı olması gereken her veri mutlaka harici bir destek servisinde (Redis, PostgreSQL, S3) tutulmalıdır.
- **Faktör III (Yapılandırma):** Konfigürasyonu kodda değil, ortam değişkenlerinde (ENV) saklayın.
- **Faktör IX (Tek Kullanımlık):** Hızlı başlatma ve zarif kapatma (graceful shutdown) sağlayın. `SIGTERM` sinyali geldiğinde mevcuttaki istekleri 10 saniye içinde tamamlayıp temizce kapanın.

### Oturum Durumunu Dışsallaştırmak
Oturumları asla yerel sunucu RAM'inde tutmayın: 1) Dağıtık Oturum Deposu (Redis kümesi), veya 2) Kriptografik olarak imzalanmış durumsuz token'lar (JWT) kullanın.

## ⚠️ Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar

- **Yapışkan Oturumlar (Sticky Sessions):** Kullanıcı A'yı hep Sunucu 1'e gitmeye zorlamak. Sunucu 1 çöktüğünde veya trafik azalıp kapandığında o sunucudaki tüm kullanıcıların oturumunun patlaması.
- **Yerel Diske Dosya Yükleme:** Kullanıcıların profil fotoğraflarını sunucunun yerel `/tmp` veya `/uploads` klasörüne kaydetmek; diğer 29 sunucunun o dosyadan habersiz olması.
- **Yavaş Başlayan Uygulama:** Başlarken veritabanından 4 GB veriyi RAM'e çekmeye çalışan ve açılması 8 dakika süren hantal uygulamalar (Trafik patlamasında otomatik ölçeklemeyi işlevsiz kılar).

## 🎯 Mimarın Eylem Planı: Bu Haftaki Somut Adımlar

- **1. Adım:** Kod tabanını tara: Statik yerel bellek içi haritaları (in-memory maps) ve yerel diske dosya yazan kodları kaldır.
- **2. Adım:** Bütün dosya yüklemelerini önceden imzalanmış URL'ler (pre-signed URLs) ile doğrudan nesne deposuna (S3, GCS) yönlendir.
- **3. Adım:** Uygulama açılış süresini 15 saniyenin altına indir ki bulut auto-scaling ani trafik dalgalarını karşılayabilsin.

## 📌 Mimari Çıkarımlar ve Hile Tablosu

- Sunucularınıza evcil hayvan gibi değil, büyükbaş hayvan gibi davranın.
- Uygulamanız herhangi bir sunucunun aniden `kill -9` ile kapatılmasını kaldıramıyorsa, yatay ölçeklenmeye hazır değilsiniz demektir.
- Tüm durumu harici veritabanlarına veya Redis'e çıkarın; işlem gücünü tamamen durumsuz tutun.

## 💡 Udemy Kursu & NotebookLM Tartışma ve Ödev Sorusu

**Ödev / Yansıtma Sorusu:** Canlıdaki sunucularınızdan biri tam şu saniyede fişten çekilse, o sunucuya bağlı kullanıcıların başına ne gelir? Oturumları düşer mi, sepetleri kaybolur mu?
