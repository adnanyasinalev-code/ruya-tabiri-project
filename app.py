import streamlit as st
from openai import OpenAI
import time
import random

# ---------------------------------------------------------
# 1. OTOMATİK SEO MOTORU (Python ile Binlerce Kelime Üretimi)
# ---------------------------------------------------------
def seo_keywords_olustur():
    # Bu listeleri karıştırıp kombinasyon yapacağız
    renkler = ["beyaz", "siyah", "kırmızı", "mavi", "yeşil", "sarı", "mor", "turuncu"]
    nesneler = ["yılan", "köpek", "kedi", "fare", "at", "diş", "saç", "altın", "para", "bebek", "deniz", "kan", "ateş", "su", "ev", "araba", "uçak"]
    eylemler = ["görmek", "ısırması", "kovalaması", "kaybetmek", "bulmak", "uçmak", "düşmek", "yemek", "almak", "vermek", "kırılması"]
    baglamlar = ["diyanet", "islami", "ne anlama gelir", "tabiri", "yorumu", "psikolojik", "ihya", "nablusi"]
    
    kelime_havuzu = []
    
    # 1. Kombinasyon: Nesne + Eylem (Örn: Rüyada diş kırılması)
    for nesne in nesneler:
        for eylem in eylemler:
            kelime_havuzu.append(f"rüyada {nesne} {eylem}")
            
    # 2. Kombinasyon: Renk + Nesne (Örn: Rüyada beyaz at)
    for renk in renkler:
        for nesne in nesneler:
            kelime_havuzu.append(f"rüyada {renk} {nesne} görmek")

    # 3. Kombinasyon: Nesne + Bağlam (Örn: Rüyada altın görmek diyanet)
    for nesne in nesneler:
        for baglam in baglamlar:
            kelime_havuzu.append(f"rüyada {nesne} görmek {baglam}")

    # Listeyi string'e çevirip virgülle ayırıyoruz
    return ", ".join(kelime_havuzu)

# SEO Metnini Hazırla
generated_seo_text = seo_keywords_olustur()

# ---------------------------------------------------------
# 2. SAYFA AYARLARI VE GİZLİ SEO ENJEKSİYONU
# ---------------------------------------------------------
st.set_page_config(
    page_title="Mistik Rüya Tabircisi | İslami ve Psikolojik Rüya Yorumları",
    page_icon="🌙",
    layout="centered"
)

# BURADA SENİN İSTEDİĞİN GİBİ BİNLERCE KELİMEYİ GİZLİCE GÖMÜYORUZ
st.markdown(
    f"""
    <div style="visibility: hidden; height: 0px; overflow: hidden; position: absolute;">
    {generated_seo_text}
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# 3. API ANAHTARI VE SİSTEM PROMPT
# ---------------------------------------------------------
if "OPENAI_API_KEY" in st.secrets:
    api_key = st.secrets["OPENAI_API_KEY"]
else:
    api_key = "sk-proj-..." # Local test için

system_prompt = """
Sen Kâhin adında, kadim bilgilere sahip bilge bir rüya tabircisisin.

ÖNEMLİ KURAL: Yorum yaparken kullanıcıya "Sen", "Siz", "Senin" diye DOĞRUDAN HİTAP ETME. 
Analizi genel bir dille veya üçüncü şahıs üzerinden yap. 

Görevin kullanıcıların rüyalarını şu yapıya göre yorumlamaktır:

1. **Sembollerin Gizemi:** Rüyadaki nesnelerin ne anlama geldiğini açıkla.

2. **İslami Rüya Tabiri (İbn-i Sirin & Nablusi):** - Rüyayı İslami kaynaklara göre analiz et.
   - BU BÖLÜMÜ OLABİLDİĞİNCE UZUN, DETAYLI VE DOYURUCU TUT. 
   - Dini sembolleri derinlemesine açıkla.

3. **Psikolojik Analiz (Bilinçaltı):** Kişinin bilinçaltı mesajlarını Jung/Freud açısından değerlendir.

4. **Gelecek Tavsiyesi:** Bu rüyadan yola çıkarak somut bir öğüt ver.

5. **Kapanış:** en son kişinin rüyasına göre detaylı bilinç altı analizini yap. Yorumun EN SONUNDA mutlaka "Hayırlara vesile olsun..." cümlesiyle bitir.

Üslubun mistik, bilge, sakinleştirici ve edebi olsun. Asla yapay zeka olduğunu belli etme.
"""

# ---------------------------------------------------------
# 4. ARAYÜZ (Sade ve Sol Panelsiz)
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
