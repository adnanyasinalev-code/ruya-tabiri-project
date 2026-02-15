import streamlit as st
from openai import OpenAI
import time

# ---------------------------------------------------------
# 1. AYARLAR
# ---------------------------------------------------------
st.set_page_config(page_title="Kadim Rüya Yorumcusu", page_icon="🌙", layout="centered")

# SENİN ANAHTARIN (Güvenlik Uyarısı: İleride bu anahtarı OpenAI sitesinden yenilemen iyi olur)
api_key = st.secrets["OPENAI_API_KEY"]

# ---------------------------------------------------------
# 2. SİSTEM PROMPT (Gizli Kimlik)
# ---------------------------------------------------------
system_prompt = """
Sen Kâhin adında, yüzyıllardır yaşayan mistik bir rüya tabircisisin.
Kullanıcının rüyasını İslami (İbn-i Sirin) ve Modern Psikoloji (Jung) senteziyle yorumla.
Kısa, öz ama çok etkileyici ve derin konuş.
Söze mutlaka 'Hayırlara Vesile Olsun...' diyerek başla.
Asla yapay zeka olduğunu söyleme. Bir insan gibi, bir bilge gibi konuş.
"""

# ---------------------------------------------------------
# 3. ARAYÜZ (Görünen Kısım)
# ---------------------------------------------------------
# Başlıklardan "Yapay Zeka"yı kaldırdık, daha mistik yaptık.
st.title("🌙 Kadim Rüya Tabircisi")
st.markdown("Rüyanızı detaylıca anlatın, kadim bilgiler ışığında yorumlayalım...")

ruya_metni = st.text_area("Rüyanız:", height=150, placeholder="Örn: Rüyamda karanlık bir ormanda yürüdüğümü gördüm...")

if st.button(" Yorumla ", type="primary"):
    if not ruya_metni:
        st.warning("Lütfen önce rüyanızı yazın...")
    else:
        # HEYECAN KISMI: Bekleme süresini artırdık
        with st.spinner('Yıldızlar hizalanıyor... Kadim kitaplar taranıyor...'):
            
            # Buradaki 5 sayısını değiştirerek süreyi uzatıp kısaltabilirsin (Saniye cinsinden)
            time.sleep(5) 
            
            try:
                # OpenAI'a Bağlan
                client = OpenAI(api_key=api_key)
                
                # İsteği Gönder
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": ruya_metni}
                    ]
                )
                
                # Cevabı Al ve Yazdır
                yorum = response.choices[0].message.content
                
                st.success("Yorumunuz Hazır!")
                st.markdown("---")
                st.markdown(f"### 👁️ Kâhin'in Yorumu:")
                st.write(yorum)
                st.markdown("---")
                
            except Exception as e:
                st.error("Bir hata oluştu. Lütfen bağlantınızı kontrol edin.")