import streamlit as st
from openai import OpenAI
import time
import random

# ---------------------------------------------------------
# 1. MEGA SEO MOTORU (Spesifik ve Uzun Kuyruklu Kelimeler)
# ---------------------------------------------------------
def seo_keywords_olustur():
    # KATEGORİ 1: RENKLER VE SIFATLAR (Detaylı)
    sifatlar = [
        "kocaman", "küçücük", "yavru", "vahşi", "ölü", "canlı", "konuşan", "uçan", "yaralı", 
        "hamile", "ağlayan", "gülen", "çıplak", "eski", "yeni", "kirli", "temiz",
        "zifiri siyah", "bembeyaz", "kan kırmızısı", "altın sarısı", "bebek mavisi", 
        "turkuaz", "mor", "gümüş rengi", "bakır", "haki yeşil", "bulanık", "berrak"
    ]
    
    # KATEGORİ 2: EN ÇOK ARANAN NESNELER VE VARLIKLAR
    nesneler = [
        # Hayvanlar
        "yılan", "kara yılan", "sarı akrep", "kurt", "ayı", "bit", "pire", "hamam böceği", 
        "kuduz köpek", "siyah kedi", "beyaz güvercin", "yarasa", "örümcek", "timsah", "aslan", 
        "fare", "inek", "dana", "kurbanlık koyun", "at", "balık", "yunus",
        # Vücut ve Sağlık
        "diş", "azı dişi", "ön diş", "saç", "uzun saç", "kel kafa", "göz", "mavi göz", 
        "kan", "adet kanı", "tırnak", "ayak", "el", "bebek", "erkek bebek", "kız bebek",
        # Doğa ve Afetler
        "deniz", "dalgalı deniz", "tsunami", "deprem", "yangın", "sel", "kar", "fırtına", 
        "yağmur", "çamur", "toprak", "mezar", "gökyüzü", "yıldız", "dolunay",
        # Maddi Şeyler
        "altın", "çeyrek altın", "bilezik", "yüzük", "tektaş", "kağıt para", "dolar", 
        "bozuk para", "cüzdan", "ayakkabı", "topuklu ayakkabı", "gelinlik", "damatlık", 
        "yeni araba", "kırmızı araba", "eski ev", "büyük ev", "anahtar", "kapı",
        # Yiyecekler
        "ekmek", "et", "çiğ et", "süt", "yumurta", "bal", "zeytin", "incir", "üzüm", "elma"
    ]
    
    # KATEGORİ 3: EYLEMLER VE OLAYLAR (Dramatik ve Merak Edilenler)
    eylemler = [
        "görmek", "ısırması", "kovalaması", "saldırması", "öldürmek", "sevmek", "beslemek",
        "kaybetmek", "bulmak", "çalmak", "hediye almak", "vermek", "satın almak",
        "düşmek", "yüksekten düşmek", "uçmak", "yüzmek", "boğulmak", "yanmak",
        "kırılması", "dökülmesi", "kanaması", "ağrıması", "çekilmesi",
        "evlenmek", "nişanlanmak", "boşanmak", "aldatılmak", "terk edilmek",
        "ağlamak", "hıçkırarak ağlamak", "gülmek", "kavga etmek", "barışmak",
        "namaz kılmak", "dua etmek", "hacca gitmek", "camiye girmek", "ezan okumak"
    ]
    
    # KATEGORİ 4: KİŞİLER (Kim Görüldü?)
    kisiler = [
        "eski sevgili", "eski eş", "platonik aşk", "anne", "baba", "ölmüş baba", 
        "ölmüş anne", "kardeş", "abi", "abla", "düşman", "patron", "cumhurbaşkanı", 
        "ünlü biri", "tanımadık adam", "tanımadık kadın", "hırsız", "cin", "şeytan", "melek"
    ]
    
    # KATEGORİ 5: ARAMA BAĞLAMLARI (Google'a Ne Yazıyorlar?)
    baglamlar = [
        "diyanet rüya tabirleri", "islami rüya yorumu", "ne anlama gelir", 
        "rüya tabiri sözlüğü", "imam nablusi yorumu", "ibn-i sirin rüya tabiri", 
        "psikolojik yorumu", "dini anlamı", "rüya manaları", "ihya rüya tabirleri",
        "gerçek rüya yorumu", "rüya analizi yapay zeka"
    ]
    
    kelime_havuzu = []
    
    # KOMBİNASYON MOTORU (Binlerce cümle üretir)
    
    # 1. En popüler kombinasyon: Sifat + Nesne + Eylem + Bağlam
    # Örn: "Rüyada zifiri siyah yılan ısırması diyanet"
    for _ in range(300): # Rastgele 300 kombinasyon
        cumle = f"rüyada {random.choice(sifatlar)} {random.choice(nesneler)} {random.choice(eylemler)} {random.choice(baglamlar)}"
        kelime_havuzu.append(cumle)

    # 2. Kişi Odaklı Kombinasyon
    # Örn: "Rüyada eski sevgiliyi görmek ne anlama gelir"
    for kisi in kisiler:
        kelime_havuzu.append(f"rüyada {kisi} görmek {random.choice(baglamlar)}")
        kelime_havuzu.append(f"rüyada {kisi} ile konuşmak")
        kelime_havuzu.append(f"rüyada {kisi} ile kavga etmek")

    # 3. Nesne Odaklı (Basit Aramalar)
    for nesne in nesneler:
        kelime_havuzu.append(f"rüyada {nesne} görmek")
        kelime_havuzu.append(f"rüyada {nesne} ne demek")

    # Listeyi birleştir
    return ", ".join(kelime_havuzu)

# SEO Metnini Hazırla
generated_seo_text = seo_keywords_olustur()

# ---------------------------------------------------------
# 2. SAYFA AYARLARI
# ---------------------------------------------------------
st.set_page_config(
    page_title="Mistik Rüya Tabircisi | İslami ve Psikolojik Rüya Yorumları",
    page_icon="🌙",
    layout="centered"
)

# GİZLİ SEO ENJEKSİYONU (Kullanıcı Görmez, Google Görür)
st.markdown(
    f"""
    <div style="visibility: hidden; height: 1px; width: 1px; overflow: hidden; position: absolute; top: 0; left: 0;">
    {generated_seo_text}
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# 3. API ve SİSTEM
# ---------------------------------------------------------
if "OPENAI_API_KEY" in st.secrets:
    api_key = st.secrets["OPENAI_API_KEY"]
else:
    api_key = "sk-proj-..." 

system_prompt = """
Sen Kâhin adında, kadim bilgilere sahip bilge bir rüya tabircisisin.

ÖNEMLİ KURAL: Yorum yaparken kullanıcıya "Sen", "Siz", "Senin" diye DOĞRUDAN HİTAP ETME. 
Analizi genel bir dille veya üçüncü şahıs üzerinden yap. 
(Örn: "Parana dikkat etmelisin" DEME -> "Bu rüya, maddi konulara özen gösterilmesi gerektiğine işaret eder" DE.)

Görevin kullanıcıların rüyalarını şu yapıya göre yorumlamaktır:

1. **Sembollerin Gizemi:** Rüyadaki nesnelerin ne anlama geldiğini uzunca açıkla.

2. **İslami Rüya Tabiri (İbn-i Sirin & Nablusi):** - Rüyayı İslami kaynaklara, İbn-i Sirin ve İmam Nablusi geleneğine göre detaylıca analiz et.
   - BU BÖLÜMÜ OLABİLDİĞİNCE UZUN, DETAYLI VE DOYURUCU TUT. 
   - Dini sembolleri derinlemesine açıkla.

3. **Psikolojik Analiz (Bilinçaltı):** Kişinin ruh halini Jung/Freud açısından değerlendir.

4. **Gelecek Tavsiyesi:** Somut bir öğüt ver.

5. **Kapanış:**  en son rüyaya göre kişinin bilinç altı analizini yap. detaylı olsun.Yorumun EN SONUNDA mutlaka "Hayırlara vesile olsun..." cümlesiyle bitir.

Üslubun mistik, bilge, sakinleştirici ve edebi olsun. Asla yapay zeka olduğunu belli etme.
"""

# ---------------------------------------------------------
# 4. ARAYÜZ (Sade)
# ---------------------------------------------------------
st.title("🌙 Kadim Rüya Tabircisi")

st.markdown("""
**Rüyalar, bilinçaltınızın size yazdığı gizli mektuplardır.**
Onları açıp okumaya cesaretiniz var mı? Rüyanızı anlatın, **İbn-i Sirin** rüya tabirleri ve **Psikolojik gerçekler** ile rüyanızı detaylıca analiz ederek yorumlayalım. Şifrelerini çözelim.
""")

ruya_metni = st.text_area("Rüyanızı buraya yazın:", height=200, placeholder="Örn: Gece karanlık bir ormanda yürüyordum, birden karşıma beyaz bir at çıktı...")

if st.button("𝑌𝑜𝑟𝑢𝑚𝑙𝑎", type="primary"):
    if not ruya_metni:
        st.warning("Lütfen yorumlanması için bir rüya yazın...")
    else:
        with st.spinner('Yıldızlar inceleniyor... Kadim kitaplar taranıyor...'):
            time.sleep(3) 
            
            try:
                client = OpenAI(api_key=api_key)
                
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": ruya_metni}
                    ],
                    temperature=0.7 
                )
                
                yorum = response.choices[0].message.content
                
                st.success("Kâhin'in Analizi Hazır!")
                st.markdown("---")
                st.markdown(f"### 👁️ Rüyanızın Gizli Anlamı")
                st.write(yorum)
                st.markdown("---")
                st.info("💡 Bu yorum kadim bilgiler ışığında yapılmıştır, geleceğinize ışık tutması dileğiyle.")
                
            except Exception as e:
                st.error("Bir bağlantı hatası oluştu. Lütfen tekrar deneyin.")
