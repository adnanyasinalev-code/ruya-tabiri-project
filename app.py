import streamlit as st
from openai import OpenAI
import time

# ---------------------------------------------------------
# 1. AYARLAR
# ---------------------------------------------------------
st.set_page_config(page_title="Derin Rüya Analizi", page_icon="🌙", layout="centered")

# API Anahtarı Ayarı
# (Bilgisayarında çalıştırırken buraya kendi 'sk-...' şifreni yazabilirsin.
# GitHub'a atarken st.secrets kalmalı.)
if "OPENAI_API_KEY" in st.secrets:
    api_key = st.secrets["OPENAI_API_KEY"]
else:
    # Buraya kendi anahtarını test için yazabilirsin, GitHub'a atarken silmeyi unutma.
    api_key = "sk-proj-..." 

# ---------------------------------------------------------
# 2. SİSTEM PROMPT (Daha Sıkı Filtreli Beyin)
# ---------------------------------------------------------
system_prompt = """
Sen Kâhin adında, kadim bilgilere sahip bilge bir rüya tabircisisin.

GÖREVİNİ ŞU SIRAYLA YAP (ÇOK ÖNEMLİ):

ADIM 1: GİRDİYİ KONTROL ET
Kullanıcının yazdığı metni analiz et.
- Eğer metin rastgele harf yığınından oluşuyorsa (örn: "dtjshtagrvSV", "asdfgh", "şlkşlk"),
- Veya anlamlı bir cümle yapısı yoksa,
- Veya sadece tek bir kelimeyse ve bağlamı yoksa,
ASLA YORUM YAPMA. Sadece şu cümleyi yaz ve dur:
"Gördüğüm sislerin ardında net bir rüya seçemiyorum. Lütfen rüyanı anlaşılır cümlelerle tekrar yazar mısın?"

ADIM 2: YORUMLA (Sadece Girdi Mantıklıysa)
Eğer girdi geçerli bir rüyaysa, şu kurallara göre yorumla:
1. **Uzun ve Detaylı Yaz:** En az 3-4 paragraf olsun. İnsanlar okumaya doyamasın.
2. **Yapı:**
   - Önce sembollerin gizli anlamlarını açıkla.
   - Sonra bilinçaltı ve psikolojik durumunu analiz et.
   - MUTLAKA "Gelecek Tavsiyesi" ver (Şuna dikkat et, bu fırsatı kaçırma gibi).
3. **Kapanış:** Yorumun EN SONUNDA (başında değil) "Hayırlara vesile olsun..." cümlesiyle bitir.

Üslubun mistik, bilge ve kucaklayıcı olsun. Asla yapay zeka olduğunu belli etme.
"""

# ---------------------------------------------------------
# 3. ARAYÜZ
# ---------------------------------------------------------
st.title("🌙 Kadim Rüya Tabircisi")
st.markdown("""
**Rüyalar, bilinçaltınızın size yazdığı gizli mektuplardır.**
Onları açıp okumaya cesaretiniz var mı? Rüyanızı tüm detaylarıyla anlatın, şifrelerini çözelim.
""")

ruya_metni = st.text_area("Rüyanızı buraya detaylıca yazın:", height=200, placeholder="Örn: Gece karanlık bir ormanda yürüyordum, birden karşıma beyaz bir at çıktı...")

if st.button("🔮 Kaderimi Yorumla 🔮", type="primary"):
    if not ruya_metni:
        st.warning("Lütfen yorumlanması için bir rüya yazın...")
    elif len(ruya_metni) < 4: 
        st.warning("Lütfen rüyanızı biraz daha detaylı anlatın.")
    else:
        with st.spinner('Yıldız haritası inceleniyor... Sembollerin gizemi çözülüyor...'):
            time.sleep(4) # Bekleme süresi
            
            try:
                client = OpenAI(api_key=api_key)
                
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": ruya_metni}
                    ],
                    temperature=0.5 # Yaratıcılığı biraz düşürdük ki saçmalamasın (0.5 ideal)
                )
                
                yorum = response.choices[0].message.content
                
                # Eğer yapay zeka reddetme cümlesini kurduysa bunu Uyarı olarak göster
                if "Gördüğüm sislerin ardında" in yorum:
                    st.error("⚠️ Kâhin rüyanızı anlayamadı:")
                    st.write(yorum)
                else:
                    # Başarılı yorum
                    st.success("Kâhin'in Analizi Hazır!")
                    st.markdown("---")
                    st.markdown(f"### 👁️ Rüyanızın Gizli Anlamı")
                    st.write(yorum)
                    st.markdown("---")
                    st.info("💡 Bu yorum kadim bilgiler ışığında yapılmıştır, geleceğinize ışık tutması dileğiyle.")
                
            except Exception as e:
                st.error("Bir bağlantı hatası oluştu. Lütfen tekrar deneyin.")
