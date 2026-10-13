# Parça 04: Mimarın Not Defteri: Kararları ADR ile Belgelemek (Herkes Unutmadan Önce)
**Bölüm 1: Büyük Uyanış — Mimar Olarak İlk Gün**  
*Tahmini Süre / Sesli Özet: 8 dk*  
*Hafif siklet Mimari Karar Kayıtları (ADR) kurumsal hafıza kaybını ve bitmek bilmeyen toplantıları nasıl engeller?*

---

## 🎙️ Mimarın Sahasından Yaşanmış Kriz Hikayesi

> Bir sağlık teknolojisi şirketine yeni katılan kıdemli mimar, kod incelemesi yaparken her sorguyu yakalayıp veriyi hem Redis'te hem Memcached'de tutan tuhaf bir önbellek katmanı gördü. Ekip toplantısında güldü: 'Bunu hangi akılsız yazdı? Tam bir spagetti!' Odadaki herkes sustu. Başkan Yardımcısı gözlerini dikti: 'Üç yıl önce Sandy Kasırgası sırasında ana sağlayıcımız 4 gün kapandı. Eyalet yasalarına göre hasta kabulünü 1 dakika bile durdurursak lisansımız iptal ediliyordu. O çift katmanlı önbellek şirketi iflastan ve cezadan kurtardı.' Mimar yerin dibine geçti. Kimse o kararın neden alındığını yazmamıştı. İki ay sonra başka biri o kodu 'temizledi' ve ilk bölgesel internet kesintisinde şirket milyonlarca liralık ceza yedi.

## 🧠 Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa

Kaynak kod size sistemin *nasıl* çalıştığını söyler; ama *neden* öyle yapıldığını asla söylemez. Kod yazıldıktan 6 ay sonra o günkü piyasa baskıları, yasal zorunluluklar ve elenen alternatifler insan hafızasından silinir. Mimari Karar Kayıtları (ADR - Architecture Decision Records) olmadan ekipler 'Chesterton'ın Çiti' sendromuna yakalanır: Neden dikildiğini anlamadan çiti yıkarlar ve çitin engellediği boğalar tarafından ezilirler.

## 📐 Temel Mimari İlkeler ve Zihinsel Modeller

### Bir ADR Belgesinin Anatomisi (Michael Nygard Standardı)
Standart bir ADR, git deposunda saklanan basit bir Markdown dosyasıdır (`/docs/adr/0004-postgresql-secimi.md`):
1. **Başlık ve Durum:** ADR-0014: SQS ile Asenkron Sipariş İşleme (Önerildi / Kabul Edildi / İptal Edildi)
2. **Bağlam (Context):** Hangi iş ihtiyacı veya teknik kısıt bizi bu karara zorladı?
3. **Karar (Decision):** Net olarak ne yapmayı seçtik?
4. **Elenen Alternatifler:** Hangi seçenekleri neden eledik?
5. **Sonuçlar (Consequences):** Kabul edilen olumlu ve olumsuz bedeller.

### Bürokrasi Değil, Yaşayan Tarih
Bir ADR yazmak en fazla 15-20 dakika sürmelidir. Eğer bir vize başvurusu formuna dönerse mühendisler yazmayı bırakır. ADR'ları kodun hemen yanında tutun ki pull request'lerle birlikte yaşasın.

## ⚠️ Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar

- **Gizli Meclis Kararları:** Mimari kararları gizli Slack DM'lerinde alıp ekibe gerekçesiz ferman gibi duyurmak.
- **Confluence Mezarlığı:** Kararları kimsenin aramadığı ve güncellemediği tozlu wiki sayfalarına gömmek.
- **Sonsuz Taslak:** Bir ADR'ı 'Önerildi' statüsünde 6 ay bekleterek önemsiz ayrıntılar yüzünden felç olmak.

## 🎯 Mimarın Eylem Planı: Bu Haftaki Somut Adımlar

- **1. Adım:** Bugün ana git deponda bir `/docs/adr` klasörü aç ve içine örnek bir şablon koy.
- **2. Adım:** Bir PR veya toplantıda tartışma 30 dakikayı aştığında tartışmayı durdur: 'Bunu 1 sayfalık bir ADR taslağına dökelim ve artıları-eksileri yazalım.'
- **3. Adım:** Şirkete yeni başlayan her mühendisin ilk hafta okuması gereken ilk belgenin son 10 ADR olmasını sağla.

## 📌 Mimari Çıkarımlar ve Hile Tablosu

- Yazıya dökülmemiş bir mimari karar gerçekte var olmamıştır; sadece kulaktan kulağa yayılan bir dedikodudur.
- Elenen alternatifleri kaydetmek, aynı konunun seneye tekrar 4 saat tartışılmasını engeller.
- Neden orada olduğunu bilmediğin hiçbir mimari çiti yıkma.

## 💡 Udemy Kursu & NotebookLM Tartışma ve Ödev Sorusu

**Ödev / Yansıtma Sorusu:** Ekibinin son dönemde aldığı önemli bir teknik kararı seç (kütüphane, veritabanı veya bulut servisi). Bunun için 1 sayfalık bir ADR yaz; özellikle elenen alternatifleri belirt.
