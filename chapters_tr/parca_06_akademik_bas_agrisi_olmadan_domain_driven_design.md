# Parça 06: Akademik Baş Ağrısı Olmadan Domain-Driven Design: İnsan Dilinde Bounded Context
**Bölüm 2: Planlar ve Sınırlar — Karmaşıklığı Parçalara Ayırmak**  
*Tahmini Süre / Sesli Özet: 9 dk*  
*Mimarınızı veritabanı tabloları etrafında değil, iş dünyasının gerçekleri etrafında şekillendirin.*

---

## 🎙️ Mimarın Sahasından Yaşanmış Kriz Hikayesi

> Bir telekomünikasyon devi, `tbl_Kullanici` adında devasa bir tablo etrafında dönen kurumsal bir sistem kurdu. Satış departmanı için kullanıcı; sadece e-posta ve ilgi alanından ibaret anonim bir adaydı. Faturalama departmanı için kullanıcı; vergi numarası ve banka hesabı olan yasal bir tüzel kişilikti. Şebeke Güvenliği için ise kullanıcı; aktif bir SIM kart ve IMEI numarasıydı. Satış ekibi bayilerde hızlı kayıt için e-posta alanını opsiyonel yaptığında, Faturalama'nın toplu fatura kesim servisi NullPointerException ile patladı! Şirket 9 ay boyunca 'Evrensel Tekil Kullanıcı Nesnesi' üretmek için toplantılar yaptı. Tablo 142 kolona ulaştı ve kimseyi tatmin etmedi. Proje 4 milyon dolar zararla çöpe atıldı.

## 🧠 Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa

Karmaşık bir şirkette tüm gerçekliği kapsayan tek bir evrensel model diye bir şey yoktur. Eric Evans'ın Alan Odaklı Tasarım (DDD) felsefesinin en büyük aydınlanması şudur: Kelimeler yalnızca belirli bir **Sınırlı Bağlam (Bounded Context)** içinde kesin bir anlama sahiptir. Faturalama için müşteri bir fatura adresidir; Kargo için müşteri bir teslimat koordinatıdır; Destek için müşteri bir şikayet geçmişidir. Mimarın görevi bunları dev bir Frankenstein modelinde birleştirmek değil, açık sınırlar çizip aralarında tercüme yapmaktır.

## 📐 Temel Mimari İlkeler ve Zihinsel Modeller

### Gerçek Mühendisler İçin Pratik DDD Alet Çantası
- **Ortak Dil (Ubiquitous Language):** İş birimiyle mühendislerin anlaştığı ortak sözlük. Eğer iş birimi buna 'Poliçe İptali' diyorsa, kodda `is_deleted = true` yazamazsınız.
- **Sınırlı Bağlam (Bounded Context):** Bir modelin geçerli olduğu açık sınır. Bağlam A içinde 'Ürün' stok adedi demektir; Bağlam B içinde 'Ürün' pazarlama metni demektir.
- **Kök Varlık (Aggregate Root):** Veri tutarlılığını garanti eden bekçi nesne (Örn: Bir `Siparis`, altındaki `SiparisKalemleri`ni yönetir; dışarıdan bir kod kalemi doğrudan değiştiremez).

### Bozulma Önleyici Katman (Anti-Corruption Layer - ACL)
İki sınır bağlamı veya eski bir sistemle konuşurken, dış sistemin kirli ve spagetti veri yapılarının sizin temiz alanınıza sızmasına asla izin vermeyin. Araya bir tercüman adaptör (ACL) koyun.

## ⚠️ Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar

- **Tanrı Nesnesi (God Object):** Projenin her yerine bulaşan, 200 metodu ve 80 kolonu olan dev `User` veya `Order` sınıfları.
- **Kansız Alan Modeli (Anemic Domain Model):** Sadece getter/setter içeren aptal veri torbaları ve iş kurallarının 50 farklı servis sınıfına kontrolsüzce saçılması.
- **Akademik DDD Fetişizmi:** Basit bir SQL sorgusuyla çözülecek 3 satırlık iş için 10 katmanlı soyutlama ve repository yazıp sistemi boğmak.

## 🎯 Mimarın Eylem Planı: Bu Haftaki Somut Adımlar

- **1. Adım:** Bir 'Event Storming' atölyesi düzenle: İş birimi ve yazılımcıları dijital tahta başına toplayıp iş olaylarını kronolojik sırayla turuncu post-it'lerle dizin.
- **2. Adım:** Doğal olarak kümelenen olay gruplarının etrafına daire çizerek doğal Sınırlı Bağlamlarınızı (Bounded Context) keşfedin.
- **3. Adım:** Üçüncü parti kurumsal sağlayıcılarla entegre olurken ilk iş olarak bir Anti-Corruption Layer (ACL) tasarla.

## 📌 Mimari Çıkarımlar ve Hile Tablosu

- Modeller gerçek dünyanın fotokopisi değildir; belirli bir sınırdaki problemi çözmek için tasarlanmış haritalardır.
- Pazarlama ekibinin kullanıcı tanımının, muhasebenin defterini patlatmasına izin vermeyin.
- Kodunuzda iş biriminin dilini konuşun, yoksa tüm kariyeriniz biletleri Türkçeye çevirmekle geçer.

## 💡 Udemy Kursu & NotebookLM Tartışma ve Ödev Sorusu

**Ödev / Yansıtma Sorusu:** Mevcut kod tabanınızda 20'den fazla özelliği olan dev bir sınıf bulun. Bu sınıfı iki farklı sınırlı bağlama (bounded context) ait iki farklı modele bölebilir misiniz?
