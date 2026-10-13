# Parça 32: Kriz Yönetimi ve Suçlamasız Olay İncelemesi (Blameless Post-Mortem)
**Bölüm 8: Gözlemlenebilirlik ve Operasyonel Mükemmellik — Karanlıkta Görmek**  
*Tahmini Süre / Sesli Özet: 9 dk*  
*Yüksek performanslı mühendislik kültürleri felaketleri nasıl sistemik dayanıklılığa dönüştürür?*

---

## 🎙️ Mimarın Sahasından Yaşanmış Kriz Hikayesi

> Gergin bir Perşembe öğleden sonrasında acemi bir DevOps mühendisi test ortamı sandığı bir ekranda temizlik betiği çalıştırdı. Canlı veritabanıydı. Üç saniye içinde müşteri tablosu tamamen silindi. Şirkette panik koptu. CTO hemen genel Slack kanalına yazdı: 'Bu betiği kim çalıştırdı? Bu kabul edilemez bir sorumsuzluk!' Mühendis Cuma sabahı kovuldu. Üç ay sonra başka bir kıdemli mühendis gece yarısı stres altında bir hotfix geçerken aynı hatayı yaptı ve canlı stok tablosunu sildi! Neden mi? Çünkü canlı ve test ortamlarının sunucu isimleri neredeyse aynıydı ve betikte hiçbir onay sorusu yoktu. İlk mühendisi kovmak hiçbir mimari zafiyeti çözmemişti; sadece bir sonraki mühendisin hatasını korkuyla gizlemesine yol açmıştı.

## 🧠 Zihniyet Dönüşümü: Kod Yazarlığından Mimarlığa

İnsan hatası asla bir olayın kök nedeni değildir; insan hatası sistemik bir mimari veya yöntemsel açığın *belirtisidir*. Tek bir kişi tek bir tuşa basarak canlı veritabanını silebiliyorsa, o sistem mimari olarak kusurludur. Etsy ve John Allspaw'un öncülük ettiği **Suçlamasız Olay İncelemesi (Blameless Post-Mortem)** felsefesi şunu kabul eder: Mühendisler ellerindeki bilgi ve bağlamla ellerinden gelenin en iyisini yapmaya çalışan yetkin profesyonellerdir. Amaç insanı cezalandırmak değil; sistemik zaafları bulup otomatik bariyerler inşa etmektir.

## 📐 Temel Mimari İlkeler ve Zihinsel Modeller

### Suçlamasız Post-Mortem Şablonu
1. **Özet:** Ne oldu, müşteri etkisi neydi, kesinti kaç dakika sürdü?
2. **Zaman Çizelgesi:** Olay anından tespite, müdahaleye ve çözüme kadar dakika dakika kronoloji.
3. **Katkıda Bulunan Faktörler (5 Neden Analizi):** 'Ahmet yanlış komut yazdı'dan öteye geç: 'Neden terminal prodüksiyona doğrudan açıktı? Neden onay istemedi? Neden alarm 40 dakika sonra çaldı?'
4. **Neler İyi Gitti vs. Nerede Şanslıydık:** Ekip çalışmasını takdir et; tesadüfen kurtulan yerleri tespit et.
5. **Önleyici Eylemler:** Belirli kişilere atanmış tarihli somut mühendislik görevleri.

### Kriz Komutanı (Incident Commander) Rolü
Kritik bir Sev-1 krizinde demokrasi biter. Kriz Komutanı görev dağıtımını yapar, yöneticileri oyalayarak mühendislerin kafasını rahatlatır ve hata ayıklama kanalını sakin ve odaklı tutar.

## ⚠️ Kaçınılması Gereken Anti-Pattern'ler ve Tuzaklar

- **Günah Keçisi Kültürü:** Hata yapanı suçlamak, utandırmak veya kovmak; bu durum ekiplerin arızaları saklamasına ve risk almaktan kaçınmasına yol açar.
- **Aksiyon Mezarlığı:** Harika bir inceleme belgesi hazırlayıp oradaki 10 önleyici bileti hiçbir zaman sprint planına almayıp unutmak.
- **Tek Bir Kök Neden Yanılgısı:** Karmaşık sistemlerin neredeyse hiçbir zaman tek bir sebepten çökmediğini unutup 'tek suçlu' aramak.

## 🎯 Mimarın Eylem Planı: Bu Haftaki Somut Adımlar

- **1. Adım:** Açık kriz seviyeleri belirle (Sev-1: Gelir akışı durdu, Sev-2: Kısmi kesinti) ve net müdahale süreleri koy.
- **2. Adım:** Her Sev-1 veya Sev-2 olayından sonra 48 saat içinde mutlaka Suçlamasız Post-Mortem toplantısı yap.
- **3. Adım:** Çıkan önleyici aksiyon maddelerinin en az %50'sini hemen bir sonraki sprintin içerisine zorunlu olarak koy.

## 📌 Mimari Çıkarımlar ve Hile Tablosu

- İnsanları kovarak güvenilirlik elde edemezsiniz; güvenilirliği mühendislikle inşa edersiniz.
- Suçlamasız kültür yumuşak davranmak değil; sistemik gerçekleri acımasızca ortaya çıkarma disiplinidir.
- Post-mortem'i yapılmayan her kesinti, evrene boşuna ödenmiş bir okul harcıdır.

## 💡 Udemy Kursu & NotebookLM Tartışma ve Ödev Sorusu

**Ödev / Yansıtma Sorusu:** Şirketinizdeki son büyük kesintiyi hatırlayın: Odak noktası hatayı yapan kişiyi bulmak mıydı, yoksa o hataya izin veren sistem koşullarını onarmak mı?
