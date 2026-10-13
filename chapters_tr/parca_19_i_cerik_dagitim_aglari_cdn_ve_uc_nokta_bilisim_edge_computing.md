# Parça 19: İçerik Dağıtım Ağları (CDN) ve Uç Nokta Bilişim (Edge Computing)
**Bölüm 5: Ölçeklenebilirlik ve Esneklik — İzdihamı Yönetmek**  
*Tahmini Süre / Sesli Özet: 8 dk*  
*Işık hızı gecikme cezasını alt etmek ve küresel kullanıcılara 50 milisaniyenin altında hizmet vermek.*

---

## 🎙️ Mimarın Sahasından Yaşanmış Kriz Hikayesi

> Bir SaaS analitik platformunun tüm sunucuları Kuzey Virginia'daki tek bir AWS veri merkezindeydi. Şirket Sidney/Avustralya'da dev bir kurumsal müşteriye imza attı. Ancak Avustralyalı yöneticiler dashboard'un 4.2 saniyede açılmasından şikayetçi oldu. Mühendisler 3 hafta boyunca SQL sorgularını optimize etti, JSON'ları sıkıştırdı; ama açılış süresi ancak 100 milisaniye kısaldı! Neden mi? Sidney ile Virginia arasındaki fiber optik kablo mesafesi gidiş-dönüş 30.000 kilometredir. Cam kablodaki ışık hızı zorunlu olarak 180ms gecikme üretir. Sayfanın yüklenmesi için gereken 18 sıralı CSS, font ve JS isteği, $18 	imes 180	ext{ms} = 3.24	ext{ saniyeyi}$ salt okyanus tabanında seyahat ederek harcıyordu! Araya Cloudflare CDN koyduklarında Sidney'deki açılış süresi 380 milisaniyeye düştü.

## 🧠 Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa

Kodu ne kadar optimize ederseniz edin, ışık hızını yenemezsiniz. Küresel bir kitleye hızlı dijital deneyim sunmanın tek yolu, veriyi ve hesaplamayı fiziksel olarak kullanıcının yaşadığı şehre yaklaştırmaktır. Modern bir İçerik Dağıtım Ağı (CDN) sadece resim saklanan bir yer değildir; dünyada 300'den fazla şehirde bulunan, TLS'i sonlandıran, sunucusuz (serverless) kod çalıştıran ve ana sunucularınızı internet trafiğinin %95'inden koruyan programlanabilir bir küresel kalkandır.

## 📐 Temel Mimari İlkeler ve Zihinsel Modeller

### Uç Nokta Hiyerarşisi: Kaynak (Origin) vs. Uç (Edge PoP)
- **Uç Nokta (Edge Point of Presence - PoP):** Londra, Tokyo, Sidney, İstanbul gibi metropollerdeki sunucular. Kullanıcı 5ms mesafedeki uç noktaya bağlanır.
- **Kaynak Sunucu (Origin):** Veritabanınızın ve ana işlem gücünüzün olduğu merkez.
- **HTTP Önbellek Başlıkları:**
  - `Cache-Control: public, max-age=31536000, immutable` (Hash'lenmiş statik dosyalar için)
  - `Cache-Control: s-maxage=60, stale-while-revalidate=300` (Yarı dinamik API yanıtları için)

### Uç Nokta Bilişim (Cloudflare Workers, Fastly Compute, Lambda@Edge)
Uç noktalarda hafif JavaScript veya WebAssembly çalıştırmak: 1) Coğrafi yönlendirmeler, 2) A/B testi çerez yönetimi, 3) Token doğrulama ve 4) Bot engelleme için devasa hız avantajı sağlar.

## ⚠️ Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar

- **Hash'siz Statik Dosyalar:** Dosya adına hash eklemeden (`app.js`) yayınlamak ve güncelleme anında kullanıcıların tarayıcısında eski sürümün takılıp kalması.
- **CDN Bypass Etmek:** Statik API yanıtlarına önbellek başlığı koymayıp viral bir sosyal medya akınında tüm trafiğin doğrudan kaynak veritabanına çarpmasına izin vermek.
- **Uçta Ağır Hesaplama:** Uç sunucularda ağır veritabanı sorguları veya uzun CPU hesaplamaları yapmaya kalkışıp zaman aşımına takılmak.

## 🎯 Mimarın Eylem Planı: Bu Haftaki Somut Adımlar

- **1. Adım:** Derleme sürecini (Webpack/Vite) tüm statik dosyaların adlarına içerik özeti (content-hash) ekleyecek şekilde ayarla.
- **2. Adım:** Bütün hash'li statik dosyalara 1 yıllık `immutable` önbellek başlığı ata.
- **3. Adım:** Yarı dinamik halka açık API uçlarında `stale-while-revalidate` kullanarak CDN'in kullanıcılara anında eski kopyayı dönüp arka planda yenisini getirmesini sağla.

## 📌 Mimari Çıkarımlar ve Hile Tablosu

- Işık hızını refactor edemezsiniz; içeriği coğrafi olarak kullanıcıya yaklaştırın.
- İyi ayarlanmış bir CDN, gelen trafiğin %85 ila %95'ini ana sunucularınıza hiç değmeden karşılamalıdır.
- Dosya adlarına hash eklemek, uç noktadaki önbellek geçersiz kılma derdini kökten çözer.

## 💡 Udemy Kursu & NotebookLM Tartışma ve Ödev Sorusu

**Ödev / Yansıtma Sorusu:** Tarayıcınızın Geliştirici Araçları (Network sekmesi) üzerinden şirketinizin ana sayfasını açın. JS ve CSS dosyalarınızın `Cache-Control` başlıkları ne? Bir CDN üzerinden mi geliyorlar yoksa doğrudan ana sunucudan mı?
