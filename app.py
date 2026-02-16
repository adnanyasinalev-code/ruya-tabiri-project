import streamlit as st
from openai import OpenAI
import time

# ---------------------------------------------------------
# 1. PROFESYONEL SAYFA AYARLARI (SEO & GÖRÜNÜM)
# ---------------------------------------------------------
# Sidebar (sol panel) kapalı, başlık ve ikon ayarlı
st.set_page_config(
    page_title="Mistik Rüya Tabircisi | İslami ve Psikolojik Rüya Yorumları",
    page_icon="🌙",
    layout="centered"
)

# --- GİZLİ SEO ÇALIŞMASI ---
# Sol paneli yapmadık ama Google botları için anahtar kelimeleri
# sayfanın en altına "görünmez" şekilde ekledik.
st.markdown(
    """
    <div style="visibility: hidden; height: 0px; overflow: hidden;">
    Rüya tabirleri, rüya yorumu, İslami rüya tabiri, İbn-i Sirin, rüyamda ne gördüm, 
    rüya analizi, istihare, rüya tabircisi, diyanet rüya tabirleri, 
    psikolojik rüya yorumu, rüya manaları.
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
# 3. SİSTEM PROMPT (Senin İstediğin Özel Ayarlar)
# ---------------------------------------------------------
system_prompt = """
Sen Kâhin adında, kadim bilgilere sahip bilge bir rüya tabircisisin.

ÖNEMLİ KURAL: Yorum yaparken kullanıcıya "Sen", "Siz", "Senin" diye DOĞRUDAN HİTAP ETME. 
Analizi genel bir dille veya üçüncü şahıs üzerinden yap. 
(Örn: "Parana dikkat etmelisin" DEME -> "Bu sembol, maddi konulara dikkat edilmesi gerektiğine işaret eder" DE.)

Görevin kullanıcıların rüyalarını şu yapıya göre yorumlamaktır:

1. **Sembollerin Gizemi:** Rüyadaki nesnelerin (su, ateş, hayvan vb.) ne anlama geldiğini açıkla.

2. **İslami Rüya Tabiri (İbn-i Sirin & Nablusi):** - Rüyayı İslami kaynaklara, İbn-i Sirin ve İmam Nablusi geleneğine göre analiz et.
   - BU BÖLÜMÜ OLABİLDİĞİNCE UZUN, DETAYLI VE DOYURUCU TUT. 
   - Dini ve manevi sembolleri derinlemesine açıkla.

3. **Psikolojik Analiz (Bilinçaltı):** - Kişinin ruh halini, bilinçaltı mesajlarını modern psikoloji (Jung/Freud) açısından değerlendir.

4. **Gelecek Tavsiyesi:** - Bu rüyadan yola çıkarak somut bir öğüt veya uyarı ver.

5. **Kapanış:** - Yorumun EN SONUNDA (başında değil) mutlaka "Hayırlara vesile olsun..." cümlesiyle bitir.

Üslubun mistik, bilge, sakinleştirici ve edebi olsun. Asla yapay zeka olduğunu belli etme.
"""

# ---------------------------------------------------------
# 4. ARAYÜZ (Sol Panel Yok, Sade Tasarım)
# ---------------------------------------------------------
st.title("🌙 Kadim Rüya Tabircisi")

# Yazı fontunu biraz güzelleştirelim
st.markdown("""
**Rüyalar, bilinçaltınızın size yazdığı gizli mektuplardır.**
Onları açıp okumaya cesaretiniz var mı? Rüyanızı anlatın, **İbn-i Sirin** rüya tabirleri ve **Psikolojik gerçekler** ile rüyanızı detaylıca analiz ederek yorumlayalım. Şifrelerini çözelim.
""")

ruya_metni = st.text_area("Rüyanızı hem islami hem psikolojik yorumlayalım:", height=200, placeholder="Örn: Gece karanlık bir ormanda yürüyordum, birden karşıma beyaz bir at çıktı...")

# Buton tasarımı senin istediğin gibi
if st.button("𝑌𝑜𝑟𝑢𝑚𝑙𝑎", type="primary"):
    if not ruya_metni:
        st.warning("Lütfen yorumlanması için bir rüya yazın...")
    else:
        with st.spinner('Yıldızlar inceleniyor... Kadim kitaplar taranıyor...'):
            time.sleep(3) # Heyecan süresi
            
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
                
                # Sonucu Göster
                st.success("Kâhin'in Analizi Hazır!")
                st.markdown("---")
                st.markdown(f"### 👁️ Rüyanızın Gizli Anlamı")
                st.write(yorum)
                st.markdown("---")
                st.info("💡 Bu yorum kadim bilgiler ışığında yapılmıştır, geleceğinize ışık tutması dileğiyle.")
                
            except Exception as e:
                st.error("Bir bağlantı hatası oluştu. Lütfen tekrar deneyin.")

