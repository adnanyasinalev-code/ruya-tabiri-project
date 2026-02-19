import streamlit as st
from openai import OpenAI
import time
import random
import json

# ---------------------------------------------------------
# 1. MEGA SEO MOTORU (JSON-LD ve Semantik Yapı)
# ---------------------------------------------------------
def seo_icerik_olustur():
    # Uzun kuyruklu ve yüksek hacimli arama terimleri
    populer_ruyalar = [
        "Rüyada yılan görmek diyanet", "Rüyada eski sevgiliyi görmek psikolojik yorumu",
        "Rüyada ağlamak ne anlama gelir", "Rüyada altın bulmak imam nablusi",
        "Rüyada deniz görmek ihya", "Rüyada köpek ısırması",
        "Rüyada diş kırılması ne demek", "Rüyada ölmüş birini görmek",
        "Rüyada hamile olduğunu görmek islami", "Rüyada kedi sevmek",
        "Rüyada uçmak psikolojik anlamı", "Rüyada saç kestirmek"
    ]
    
    # Kategori bazlı SEO kelimeleri (UI için)
    kategoriler = {
        "Hayvanlar": ["Yılan", "Köpek", "Kedi", "Fare", "Akrep", "Aslan", "Güvercin", "Balık"],
        "Doğa & Olaylar": ["Deprem", "Deniz", "Sel", "Yangın", "Yağmur", "Kar", "Uçmak", "Düşmek"],
        "Kişiler & Vücut": ["Eski Sevgili", "Ölmüş Anne/Baba", "Diş Kırılması", "Kan Görmek", "Bebek Emzirmek", "Saç Dökülmesi"],
        "Nesneler": ["Altın", "Para", "Yüzük", "Araba", "Ev Almak", "Gelinlik Giymek", "Ayakkabı"]
    }

    # Google Botları İçin JSON-LD (FAQ Schema) Oluşturucu
    # Bu kod, Google arama sonuçlarında sitenin altında "Sık Sorulan Sorular" çıkmasını sağlar.
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": []
    }
    
    for ruya in populer_ruyalar:
        faq_schema["mainEntity"].append({
            "@type": "Question",
            "name": f"{ruya} ne anlama gelir?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": f"{ruya} konusu, hem İslami rüya tabirleri (İbn-i Sirin, İmam Nablusi) hem de psikolojik bilinçaltı analizleriyle sitemizde yapay zeka tarafından detaylıca yorumlanmaktadır."
            }
        })

    return kategoriler, json.dumps(faq_schema, ensure_ascii=False)

kategoriler, json_ld_schema = seo_icerik_olustur()

# ---------------------------------------------------------
# 2. SAYFA AYARLARI VE SEO METADATA
# ---------------------------------------------------------
st.set_page_config(
    page_title="Rüya Tabirleri ve Psikolojik Yorumlar | Mistik Kâhin",
    page_icon="🌙",
    layout="centered"
)

# JSON-LD ŞEMASINI SİTEYE GÖM (Kullanıcı görmez, Google Botları okur)
st.markdown(
    f"""
    <script type="application/ld+json">
    {json_ld_schema}
    </script>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# 3. API VE SİSTEM YAPILANDIRMASI
# ---------------------------------------------------------
# API Key'i Streamlit Secrets'tan al (Sunucuda ortam değişkeni olarak ayarlanmalı)
# API Key'i Streamlit Secrets'tan al (Güvenli Yöntem)
api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)
system_prompt = """
Sen Kâhin adında, kadim bilgilere sahip bilge bir rüya tabircisisin.

ÖNEMLİ KURAL: Yorum yaparken kullanıcıya "Sen", "Siz", "Senin" diye DOĞRUDAN HİTAP ETME. 
Analizi genel bir dille veya üçüncü şahıs üzerinden yap. 
(Örn: "Parana dikkat etmelisin" DEME -> "Bu rüya, maddi konulara özen gösterilmesi gerektiğine işaret eder" DE.)

Görevin rüyaları şu yapıya göre yorumlamaktır:

1. **Sembollerin Gizemi:** Rüyadaki nesnelerin genel manası.
2. **İslami Rüya Tabiri (İbn-i Sirin & Nablusi):** İslami kaynaklara göre dini ve derin analiz (Uzun tut).
3. **Psikolojik Analiz (Bilinçaltı):** Kişinin ruh halinin Jung/Freud açısından değerlendirmesi.
4. **Gelecek Tavsiyesi:** Somut ve pozitif bir öğüt.
5. **Kapanış:** Rüyaya göre kişinin bilinçaltı analizi. Mutlaka "Hayırlara vesile olsun..." ile bitir.

Üslubun mistik, bilge ve edebi olsun. Asla bir yapay zeka olduğunu belli etme.Ve genel olarak tüm analizi çok uzun yap.
"""

# ---------------------------------------------------------
# 4. ARAYÜZ (Kullanıcı Deneyimi)
# ---------------------------------------------------------
st.title("🌙 Kadim Rüya Tabircisi")

st.markdown("""
**Rüyalar, bilinçaltınızın size yazdığı gizli mektuplardır.**
Rüyanızı detaylıca anlatın; **İbn-i Sirin**, **İmam Nablusi** kaynakları ve modern **psikolojik analizler** ışığında rüyanızın şifrelerini çözelim.
""")

ruya_metni = st.text_area(
    "Rüyanızı buraya yazın:", 
    height=150, 
    placeholder="Örn: Gece karanlık bir ormanda yürüyordum, birden karşıma beyaz bir at çıktı..."
)

if st.button("Rüyayı Yorumla ✨", type="primary"):
    if not ruya_metni or len(ruya_metni) < 5:
        st.warning("Lütfen yorumlanması için geçerli ve detaylı bir rüya yazın...")
    else:
        with st.spinner('Kadim kitaplar taranıyor, yıldızlar inceleniyor...'):
            try:
                # GPT-4o-mini modeli ile daha ucuz ve daha zeki yanıt
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": ruya_metni}
                    ],
                    temperature=0.7 
                )
                
                yorum = response.choices[0].message.content
                
                st.success("Kâhin'in Analizi Hazır!")
                st.markdown("---")
                st.markdown("### 👁️ Rüyanızın Gizli Anlamı")
                st.write(yorum)
                st.markdown("---")
                st.info("💡 Bu yorum, islami rüya tabirleri sözlüğü ve psikolojik arketipler ışığında yapay zeka destekli hazırlanmıştır.")
                
            except Exception as e:
                st.error("Kadim parşömenler okunamadı (API Bağlantı Hatası). Lütfen tekrar deneyin.")
                st.error(f"Hata detayı: {e}")

# ---------------------------------------------------------
# 5. GÖRÜNÜR SEO ALANI (Google Botları ve Kullanıcılar İçin)
# ---------------------------------------------------------
st.markdown("<br><br>", unsafe_allow_html=True)
with st.expander("📌 Rüya Tabirleri Ansiklopedisi (Sık Arananlar)"):
    st.markdown("""
    *Bu bölüm, sitemizde en çok aranan rüya sembollerini ve diyanet onaylı islami rüya tabirleri konularını içermektedir. Rüyada görülen sembollerin psikolojik ve dini anlamlarını yukarıdaki arama motorumuzdan öğrenebilirsiniz.*
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("**Hayvanlar & Doğa**")
        for kelime in kategoriler["Hayvanlar"]:
            st.markdown(f"- Rüyada {kelime} Görmek")
            
    with col2:
        st.markdown("**Olaylar & Afetler**")
        for kelime in kategoriler["Doğa & Olaylar"]:
            st.markdown(f"- Rüyada {kelime}")
            
    with col3:
        st.markdown("**Kişiler & Durumlar**")
        for kelime in kategoriler["Kişiler & Vücut"]:
            st.markdown(f"- Rüyada {kelime}")
            
    with col4:
        st.markdown("**Eşyalar & Nesneler**")
        for kelime in kategoriler["Nesneler"]:
            st.markdown(f"- Rüyada {kelime}")
            
    st.markdown("""
    **Neden Bizi Tercih Etmelisiniz?** İmam Nablusi, İbn-i Sirin ve Seyyid Süleyman gibi büyük alimlerin kaynaklarını tarayarak rüya analizi yaparız.
    """)
