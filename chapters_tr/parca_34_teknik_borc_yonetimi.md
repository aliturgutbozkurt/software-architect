# Parça 34: Teknik Borç Yönetimi: Ne Zaman Ödemeli, Ne Zaman Refactor Etmeli, Ne Zaman Sıfırdan Yazmalı?
**Bölüm 9: İnsan Mimarisi — Yetki Olmadan Liderlik Etmek**  
*Tahmini Süre / Sesli Özet: 9 dk*  
*Teknik borcu duygusal bir utanç vesilesi değil, finansal bir kaldıraç gibi yönetmek.*

---

## 🎙️ Mimarın Sahasından Yaşanmış Kriz Hikayesi

> Bir medikal SaaS şirketinin 10 yıllık eski bir monolitik Java backend'i vardı. Her yeni özellik iki katı sürede çıkıyordu. Yönetim kurulu kampında Baş Mimar coşkulu bir sunum yaptı: 'Teknik borcumuz artık sürdürülemez! Tüm ürün geliştirmelerini 6 ay tamamen dondurmalı ve platformu modern Go mikroservisleriyle sıfırdan yeniden yazmalıyız!' Yönetim korkup 3 milyon dolarlık bütçeyi onayladı. 18 ay geçtiğinde yeniden yazım projesi henüz %40 seviyesindeydi! Bu sırada özellik çıkarmaya devam eden rakipler şirketin pazar payının %35'ini çaldı. CEO projeyi durdurdu, mimarı kovdu ve şirket rakibine yok pahasına satıldı. Sıfırdan yazım şirketi batırmıştı.

## 🧠 Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa

Ward Cunningham 'Teknik Borç' terimini kötü kod için bir bahane olsun diye değil, finansal borçlanma analojisi olarak ortaya attı: Erken bir pazar fırsatını yakalamak için bilinçli olarak borçlanmak (hızlı ve mükemmel olmayan bir kod çıkarmak) meşru bir iş stratejisidir; yeter ki anaparayı ve faizini zamanında ödeyin. Ancak kontrolsüz teknik borç bileşik faiz gibi birikir ve sonunda tüm mühendislik hızını rehin alır. Bir mimar asla 'her şeyi durdurup sıfırdan yazalım' demez; borcu **Boğucu İncir Kalıbı (Strangler Fig Pattern)** ile adım adım öder.

## 📐 Temel Mimari İlkeler ve Zihinsel Modeller

### Teknik Borç Kadranı (Martin Fowler)
- **Bilinçli ve İhtiyatlı:** 'Yılbaşına yetişmek için bu özelliği böyle çıkarıyoruz; Q1'de vergi mantığını refactor edeceğiz.' (Akıllıca kaldıraç).
- **Bilinçli ve Pervasız:** 'Test yazacak vaktimiz yok, canlıya bas gitsin.' (Felaket).
- **Bilinçsiz ve İhtiyatlı:** 'Bir yıllık kullanıcı verisinden sonra anladık ki ilk şemamız ideal değilmiş.' (Doğal öğrenme süreci).
- **Bilinçsiz ve Pervasız:** Tasarım kalıplarından habersiz kişilerin yazdığı spagetti kod.

### Boğucu İncir (Strangler Fig) Modernizasyon Kalıbı
Uçan uçağın motorunu havada sıfırdan yapmaya kalkmayın! Eski sistemin önüne bir API Gateway koyun. Yeni özelliği veya eski bir modülü modern mimaride yazın. Trafiğin %10'unu oraya verin. Eski monoliti parça parça boğun; en sonunda içi boşalan dinozoru fişten çekip silin.

## ⚠️ Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar

- **İkinci Sistem Sendromu (Sıfırdan Yeniden Yazım):** Çalışan ve para kazandıran eski sistemi çöpe atıp 'kusursuz' bir yenisini yazmaya kalkışmak (Neredeyse her zaman iflasla sonuçlanır).
- **Ahlakçı Mühendis:** Her teknik borcu ahlaki bir günah sayıp kod estetik olarak kusursuz olana kadar canlıya çıkmayı reddetmek.
- **Teknik Borç İflası:** Borcu 4 yıl boyunca görmezden gelip yeni bir yazılımcının onboarding süresini 3 aya, bir bugfix süresini 6 haftaya çıkarmak.

## 🎯 Mimarın Eylem Planı: Bu Haftaki Somut Adımlar

- **1. Adım:** '%20 Yatırım Kuralı'nı kurumsal politika yap: Her sprint kapasitesinin %20'si teknik borç temizliğine ayrılsın.
- **2. Adım:** İş birimine 'kod temizliği' diye proje sunma; 'müşteri kaybını azaltmak' veya 'canlıya çıkış hızını 2 katına çıkarmak' olarak sun.
- **3. Adım:** Eski sistem modernizasyonunda asla özellikleri dondurma; Strangler Fig ile adım adım ilerle.

## 📌 Mimari Çıkarımlar ve Hile Tablosu

- Sıfırdan yeniden yazım mühendislik kariyerlerinin mezarlığıdır; eski sistemleri boğarak dönüştürün.
- Teknik borç finansal bir kaldıraçtır: Hız gerektiğinde bilinçli borçlanın, planlı şekilde geri ödeyin.
- Bir refactoring'i iş hızı veya risk azaltımıyla açıklayamıyorsanız, yapmayın.

## 💡 Udemy Kursu & NotebookLM Tartışma ve Ödev Sorusu

**Ödev / Yansıtma Sorusu:** Kod tabanınızdaki en büyük teknik borç nedir? Bunu CFO'nuza sunacak olsaydınız, şirkete sağlayacağı ticari faydayı hangi kelimelerle anlatırdınız?
