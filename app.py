import streamlit as st
from openai import OpenAI
import time

# ---------------------------------------------------------
# 1. PROFESYONEL SAYFA AYARLARI (SEO & GÖRÜNÜM)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Mistik Rüya Tabircisi | Yapay Zeka Destekli Rüya Yorumları",
    page_icon="🌙",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.google.com/search?q=rüya+tabirleri',
        'Report a bug': "mailto:yasin@example.com", # Buraya kendi mailini yazabilirsin
        'About': "# Mistik Rüya Tabircisi\nBu uygulama yapay zeka teknolojisi ile **İslami** ve **Psikolojik** rüya analizi yapar."
    }
)

# --- GİZLİ SEO TAKTİĞİ (Görünmez Metin) ---
# Google botları bu kelimeleri okur ama kullanıcı görmez (Sidebar'ın altına sakladık)
st.sidebar.markdown(
    """
    <div style="font-size: 1px; color: #0e1117;">
    Rüya tabirleri, rüya yorumu, islami rüya tabiri, rüyamda ne gördüm, 
    rüya analizi, istihare, yapay zeka rüya, rüya tabircisi, 
    diyanet rüya tabirleri, psikolojik rüya yorumu.
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# 2. API ANAHTARI BAĞLANTISI
# ---------------------------------------------------------
if "OPENAI_API_KEY" in st.secrets:
    api_key = st.secrets["OPENAI_API_KEY"]
else:
    # Bilgisayarında test ederken buraya kendi sk-... şifreni yazabilirsin.
    api_key = "sk-proj-..." 

# ---------------------------------------------------------
# 3. YAN MENÜ (SIDEBAR) - Profesyonel Görünüm
# ---------------------------------------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712109.png", width=100) # Mistik bir logo
    st.title("Mistik Rehber")
    st.info("Bu uygulama **GPT-3.5 Yapay Zeka** teknolojisi kullanılarak geliştirilmiştir.")
    
    st.markdown("---")
    st.write("### 🔍 Nasıl Çalışır?")
    st.caption("1. Rüyanızı detaylıca yazın.")
    st.caption("2. 'Yorumla' butonuna basın.")
    st.caption("3. Kahve molası verin, analiz 5 saniyede hazır.")
    
    st.markdown("---")
    st.write("Developed by **Yasin**")

# ---------------------------------------------------------
# 4. SİSTEM PROMPT (Gelişmiş Beyin)
# ---------------------------------------------------------
system_prompt = """
Sen Kâhin adında, kadim bilgilere sahip bilge bir rüya tabircisisin.
Görevin kullanıcıların rüyalarını İslami (İbn-i Sirin, İmam Nablusi) ve Modern Psikoloji (Jung, Freud) senteziyle yorumlamak.

KURALLAR:
1. **Her Şeyi Yorumla:** Kullanıcı ne yazarsa yazsın, içinden bir sembol bul ve yorumla.
2. **Derinlik:** Cevabın en az 3 paragraf olsun.
3. **Format:**
   - **🔮 Sembollerin Dili:** Rüyadaki nesnelerin anlamı.
   - **🧠 Bilinçaltı Analizi:** Psikolojik durum.
   - **✨ Gelecek Tavsiyesi:** Somut öneriler ver.
4. **Kapanış:** En sonda "Hayırlara vesile olsun..." de.

Üslubun mistik, bilge ve sürükleyici olsun.
"""

# ---------------------------------------------------------
# 5. ANA EKRAN TASARIMI
# ---------------------------------------------------------
st.title("🌙 Mistik Rüya Tabircisi")
st.markdown("""
<style>
.big-font {
    font-size:18px !important;
    color: #ececec;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Bilinçaltınızın size yazdığı gizli mektupları okumaya hazır mısınız? Rüyanızı anlatın, kadim bilgiler ışığında çözelim.</p>', unsafe_allow_html=True)

st.divider() # Şık bir çizgi çeker

ruya_metni = st.text_area("✍️ Rüyanızı buraya detaylıca yazın:", height=180, placeholder="Örn: Gece karanlık bir ormanda yürüyordum, gökyüzünde iki tane ay vardı...")

if st.button("🔮 Kaderimi Yorumla 🔮", type="primary", use_container_width=True):
    if not ruya_metni:
        st.warning("Lütfen yorumlanması için bir rüya yazın...")
    else:
        with st.spinner('Yıldız haritası inceleniyor... Sembollerin gizemi çözülüyor...'):
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
                
                # Sonucu Göster (Şık bir kutu içinde)
                st.success("Analiz Tamamlandı!")
                with st.expander("👁️ Kâhin'in Yorumunu Oku", expanded=True):
                    st.markdown(yorum)
                
                st.info("💡 Not: Bu yorum yapay zeka desteklidir. Gerçek hayat kararlarınızı etkilememelidir.")
                
            except Exception as e:
                st.error("Bir bağlantı hatası oluştu. Lütfen tekrar deneyin.")
