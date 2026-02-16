import streamlit as st
from openai import OpenAI
import time

# ---------------------------------------------------------
# 1. AYARLAR
# ---------------------------------------------------------
st.set_page_config(page_title="Derin Rüya Analizi", page_icon="🌙", layout="centered")

# DİKKAT: Buraya kendi 'sk-' ile başlayan şifreni tekrar yapıştırman gerekebilir 
# (Eğer st.secrets kullanıyorsan bu satırı silip st.secrets satırını açabilirsin)
# Şimdilik senin kolayca yapıştırman için değişkeni buraya koyuyorum:
api_key = st.secrets["OPENAI_API_KEY"] 
# Eğer bilgisayarında hata alırsan yukarıdaki satırı silip tırnak içinde şifreni yaz: api_key = "sk-..."

# ---------------------------------------------------------
# 2. SİSTEM PROMPT (Yapay Zekanın Yeni Beyni)
# ---------------------------------------------------------
system_prompt = """
Sen Kâhin adında, kadim bilgilere sahip bilge bir rüya tabircisisin.
Görevin kullanıcıların rüyalarını İslami (İbn-i Sirin) ve Modern Psikoloji (Jung) senteziyle yorumlamak.

KURALLARIN ŞUNLARDIR:
1. **Uzun ve Detaylı Yaz:** Kullanıcı tatmin olmalı. Cevap en az 3-4 dolgun paragraf olsun.
2. **Yapılandırılmış Cevap Ver:**
   - Önce rüyadaki sembollerin derin anlamlarını açıkla.
   - Sonra kişinin şu anki ruh halini ve bilinçaltını analiz et.
   - EN ÖNEMLİSİ: Rüyadan yola çıkarak kişiye "Gelecek Tavsiyeleri" ver (Şundan sakın, şu fırsatı değerlendir gibi).
3. **Üslup:** Mistik, edebi, kucaklayıcı ve bilge bir dil kullan.
4. **Kapanış:** Yorumun EN SONUNDA mutlaka "Hayırlara vesile olsun..." cümlesini kullan. Başta kullanma.

GÜVENLİK FİLTRESİ (ÇOK ÖNEMLİ):
Eğer kullanıcı klavyeye rastgele basmışsa (Örn: "asdfg", "şlkgşlskfg") veya rüya ile alakasız anlamsız bir şey yazmışsa, analiz yapma. 
Sadece şu cevabı ver: "Gördüğüm sislerin ardında net bir rüya seçemiyorum. Lütfen rüyanı daha anlaşılır cümlelerle, detaylandırarak tekrar yazar mısın?"
Ancak ufak yazım hatalarını (Örn: "rüyada kpek gördm") görmezden gel ve yorumla.
"""

# ---------------------------------------------------------
# 3. ARAYÜZ
# ---------------------------------------------------------
st.title("🌙 Gizemli Rüya Tabircisi")
st.markdown("""
**Rüyalar, bilinçaltınızın size yazdığı gizli mektuplardır.**
Onları açıp okumaya cesaretiniz var mı? Rüyanızı tüm detaylarıyla anlatın, şifrelerini çözelim.
""")

# Metin kutusunu biraz daha büyüttük (height=200) ki kullanıcı uzun yazmaya teşvik edilsin
ruya_metni = st.text_area("Rüyanızı buraya detaylıca yazın:", height=200, placeholder="Örn: Gece karanlık bir ormanda yürüyordum, birden karşıma beyaz bir at çıktı. Atın gözleri parlıyordu ve bana doğru koşmaya başladı...")

if st.button("🔮 Kaderimi Yorumla 🔮", type="primary"):
    if not ruya_metni:
        st.warning("Lütfen yorumlanması için bir rüya yazın...")
    elif len(ruya_metni) < 5: # Çok kısa (örn: "a") girişleri engellemek için basit bir filtre
        st.warning("Lütfen rüyanızı biraz daha detaylı anlatın.")
    else:
        # Heyecan ve Bekleme Süresi
        with st.spinner('Yıldız haritası inceleniyor... Sembollerin gizemi çözülüyor...'):
            time.sleep(5) # 5 Saniye bekletme (İsteğe bağlı artırılabilir)
            
            try:
                # OpenAI'a Bağlan
                client = OpenAI(api_key=api_key)
                
                # İsteği Gönder
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": ruya_metni}
                    ],
                    temperature=0.7 # Yaratıcılık ayarı (0.7 iyidir)
                )
                
                # Cevabı Al
                yorum = response.choices[0].message.content
                
                # Eğer "Gördüğüm sislerin ardında..." cevabı geldiyse bunu uyarı olarak göster
                if "Gördüğüm sislerin" in yorum:
                    st.error(yorum)
                else:
                    # Başarılı yorumu göster
                    st.success("Kâhin'in Analizi Hazır!")
                    st.markdown("---")
                    st.markdown(f"### 👁️ Rüyanızın Gizli Anlamı")
                    st.write(yorum)
                    st.markdown("---")
                    st.info("💡 İpucu: Rüyalarınızı ne kadar detaylı anlatırsanız, yorum o kadar isabetli olur.")
                
            except Exception as e:
                st.error("Bir bağlantı hatası oluştu. Lütfen tekrar deneyin.")
                # Hata detayını sadece geliştirici görsün diye commentledim
                # st.write(e)
