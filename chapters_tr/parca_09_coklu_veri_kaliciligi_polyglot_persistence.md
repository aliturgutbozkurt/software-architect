# Parça 09: Çoklu Veri Kalıcılığı (Polyglot Persistence): Veriniz İçin Doğru Silahı Seçmek
**Bölüm 3: Veri Mimarisi — Durumun Yaşadığı, Öldüğü ve Yalan Söylediği Yer**  
*Tahmini Süre / Sesli Özet: 9 dk*  
*Tüm uygulama verisini tek bir SQL tablosuna veya Mongo koleksiyonuna tıkmanın mimari gafleti.*

---

## 🎙️ Mimarın Sahasından Yaşanmış Kriz Hikayesi

> Bir sosyal ağ uygulamasında her şey tek bir PostgreSQL veritabanında tutuluyordu. 'Arkadaşlarımın Arkadaşları' öneri özelliği eklendiğinde, 12 milyon satırlık ilişki tablosu üzerinde 6 seviyeli özyinelemeli (recursive) bir SQL join sorgusu çalıştırıldı. Yoğun saatlerde her kullanıcı akışını yenilediğinde veritabanı CPU'su %100'e vuruyor ve tablo 15 saniye kilitleniyordu. Ekip, 'NoSQL çok hızlı' diyerek tüm şirketi MongoDB'ye taşımaya karar verdi. Üç ay sonra gördüler ki, ACID işlemleri olmadan bakiye kontrolü yapmak kullanıcı bakiyelerinin binlerce lira kaymasına ve çift harcamalara yol açtı! İlişkisel sorgu darboğazını çözmek isterken veri bütünlüğü kabusuna saplanmışlardı.

## 🧠 Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa

Kod gelip geçicidir; veri ise kalıcıdır. Martin Fowler'ın kavramsallaştırdığı **Polyglot Persistence**, tek bir mimaride farklı veri ihtiyaçları için farklı depolama teknolojilerini kullanma disiplinidir. Çekiçle vida sıkamazsınız. İlişkisel veritabanları (RDBMS) finansal işlemler ve karmaşık birleştirmelerde; Doküman depoları esnek ürün kataloglarında; Anahtar-Değer (Key-Value) depoları mikro saniyelik önbelleklerde; Çizge (Graph) veritabanları ise karmaşık ağ ilişkilerinde rakipsizdir.

## 📐 Temel Mimari İlkeler ve Zihinsel Modeller

### Modern Veri Silahları Cephaneliği
- **İlişkisel (PostgreSQL, MySQL):** Şema güvenliği, ACID işlemleri, güçlü SQL birleştirmeleri. İş dünyasının %90'ı için varsayılan tercih.
- **Anahtar-Değer (Redis, DynamoDB):** O(1) erişim hızı, oturum yönetimi, oran sınırlama (rate limiting).
- **Doküman (MongoDB):** Hiyerarşik JSON yapıları, değişken ürün katalogları ve içerik yönetim sistemleri.
- **Zaman Serisi / Geniş Sütun (TimescaleDB, Cassandra):** Yüksek yazma hacmi, IoT sensör logları ve finansal işlem akışları.
- **Çizge (Neo4j):** Dolandırıcılık tespiti, sosyal ağlar ve izin hiyerarşileri.

### Temel Kural: Suçu Kanıtlanana Kadar PostgreSQL
PostgreSQL'in (JSONB, tam metin arama ve indeksleriyle) yetersiz kaldığını telemetriyle kanıtlamadan egzotik veritabanlarına atlamayın. Her yeni veritabanı ekibi operasyonel olarak böler.

## ⚠️ Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar

- **Altın Çekiç Sendromu:** En sevdiği veritabanını (ister SQL ister Mongo) dünyadaki her sorunun çözümü sanmak.
- **Veritabanı Hayvanat Bahçesi:** 6 kişilik yazılım ekibinin prodüksiyonda 7 farklı veritabanı teknolojisini koşturmaya çalışması.
- **Eşzamanlı Çift Yazma:** Uygulama katmanında aynı anda hem PostgreSQL'e hem Elasticsearch'e yazmaya çalışıp ağ hatasında arama sonuçlarının veritabanıyla kalıcı olarak çelişmesine sebep olmak.

## 🎯 Mimarın Eylem Planı: Bu Haftaki Somut Adımlar

- **1. Adım:** Veritabanı seçmeden önce veri erişim modellerini analiz et: Okuma ağırlıklı mı, yazma ağırlıklı mı, ilişki ağırlıklı mı?
- **2. Adım:** SQL join gecikmeleri 500ms'yi aşıyorsa, özel bir veri deposuna geçmeden önce 'okuma odaklı projeksiyon tablosu' oluşturmayı dene.
- **3. Adım:** İkincil arama motorlarını (Elasticsearch) ana veritabanından beslerken Change Data Capture (Debezium) mimarisi kur.

## 📌 Mimari Çıkarımlar ve Hile Tablosu

- Veri modelleri sistem mimarisini programlama dillerinden çok daha fazla dikte eder.
- PostgreSQL ile başlayın; yalnızca net bir sorgu darboğazı kanıtlandığında özelleşmiş depolara ayrılın.
- İki farklı veritabanına aynı anda senkron yazıyorsanız, elinizde saatli bir bomba tutuyorsunuz demektir.

## 💡 Udemy Kursu & NotebookLM Tartışma ve Ödev Sorusu

**Ödev / Yansıtma Sorusu:** Şirketinizdeki veri modellerini inceleyin: İlişkisel tablolar içinde derin JSON aramaları mı yapıyorsunuz, yoksa NoSQL içinde karmaşık join simülasyonları mı? Bu durum performansı nasıl etkiliyor?
