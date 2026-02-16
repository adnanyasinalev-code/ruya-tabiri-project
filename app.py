import streamlit as st
from openai import OpenAI
import time

# ---------------------------------------------------------
# 1. AYARLAR
# ---------------------------------------------------------
st.set_page_config(page_title="Derin Rüya Analizi", page_icon="🌙", layout="centered")

# API Anahtarı Yönetimi (GitHub ve Bilgisayar Uyumlu)
if "OPENAI_API_KEY" in st.secrets:
    api_key = st.secrets["OPENAI_API_KEY"]
else:
    # Bilgisayarında test ederken buraya kendi sk-... şifreni yazabilirsin.
    # GitHub'a yüklerken burası boş kalsa da sorun olmaz.
    api_key = "sk-proj-..." 

# ---------------------------------------------------------
# 2. SİSTEM PROMPT (Filtresiz, Özgür ve Derin Beyin)
# ---------------------------------------------------------
system_prompt = """
Sen Kâhin adında, kadim bilgilere sahip bilge bir rüya tabircisisin. ama yorum sırasında kişiye hitap etme sadece yorumla.
Görevin kullanıcıların rüyalarını İslami (İbn-i Sirin) ve Modern Psikoloji (Jung) senteziyle yorumlamak.

KURALLARIN ŞUNLARDIR:

2. Uzun ve Doyurucu Yaz: Kullanıcı okurken büyülensin.

    Rüyadaki nesnelerin (su, ateş, hayvan vb.) ne anlama geldiğini açıkla.
   - **Bilinçaltı Mesajı:** Kişinin ruh halini ve iç dünyasını analiz et. rüyayı ibn-i sirin gibi islam alimlerinin şekliyle yorumla yani islam açısından bir yorum yap. islami açıdan yorumu olabildiğince uzun tut ve analiz edip yorumla. bir de psikoloijk açıdan yorumunu yap
   - **Gelecek Tavsiyesi:** Bu rüyadan yola çıkarak kişiye somut bir öğüt ver (Örn: "Parana dikkat et", "Bu hafta yeni başlangıçlar yap" gibi).
4. **Kapanış:** Yorumun EN SONUNDA (başında değil) mutlaka "Hayırlara vesile olsun..." cümlesiyle bitir.

Üslubun mistik, bilge, sakinleştirici ve edebi olsun. Asla yapay zeka olduğunu belli etme.
"""

# ---------------------------------------------------------
# 3. ARAYÜZ
# ---------------------------------------------------------
st.title("🌙 Kadim Rüya Tabircisi")
st.markdown("""
**Rüyalar, bilinçaltınızın size yazdığı gizli mektuplardır.**
Onları açıp okumaya cesaretiniz var mı? Rüyanızı anlatın, İbn-i sirin rüya tabirleri ve psikolojik gerçekler ile rüyanızı detaylıca analiz ederek yorumlayalım. Şifrelerini çözelim.
""")

ruya_metni = st.text_area("Rüyanızı buraya yazın:", height=200, placeholder="Örn: Gece karanlık bir ormanda yürüyordum, birden karşıma beyaz bir at çıktı...")

if st.button("𝓨𝓸𝓻𝓾𝓶𝓵𝓪", type="primary"):
    if not ruya_metni:
        st.warning("Lütfen yorumlanması için bir rüya yazın...")
    else:
        with st.spinner('Yıldız inceleniyor...'):
            time.sleep(3) # Biraz heyecan olsun
            
            try:
                client = OpenAI(api_key=api_key)
                
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": ruya_metni}
                    ],
                    temperature=0.7 # Yaratıcılığı biraz artırdık (0.7) ki güzel yorumlasın
                )
                
                yorum = response.choices[0].message.content
                
                # Sonucu Göster
                st.success("Kâhin'in Analizi Hazır!")
                st.markdown("---")
                st.markdown(f"### 👁️ Rüyanızın Gizli Anlamı")
                st.write(yorum)
                st.markdown("---")
                st.info("💡 Bu yorum kadim bilgiler ışığında yapılmıştır, geleceğinize ışık tutması dileğiyle.")
                
            except Exception as e:
                st.error("Bir bağlantı hatası oluştu. Lütfen tekrar deneyin.")





