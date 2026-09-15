import os
from openai import OpenAI

client = OpenAI(api_key="SEZARR")

OGRETILEN_BILGILER = """
Bir yapay zeka aracı

"""

def kendi_yapay_zekana_sor(kullanici_sorusu):
    system_prompt = f"""
    Sen sadece sana verilen 'BİLGİ TABANI' içindeki bilgileri kullanarak cevap veren bir asistansın.
    
    KURALLAR:
    1. SADECE aşağıda verilen BİLGİ TABANI içindeki bilgileri kullan.
    2. Eğer soru verilen bilgi tabanında yer almıyorsa, KESİNLİKLE genel kültürünle veya dışarıdan bilgiyle cevap verme.
    3. Bilgi bulunmadığında tam olarak şu cevabı ver: "Bu konuda eğitilmedim, sadece tanımlı bilgilerim dahilinde yardımcı olabilirim."
    
    BİLGİ TABANI:
    {OGRETILEN_BILGILER}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": kullanici_sorusu}
        ],
        temperature=0.0
    )
    
    return response.choices[0].message.content

print(kendi_yapay_zekana_sor("Fiyatlara KDV dahil mi?"))
print(kendi_yapay_zekana_sor("Türkiye'nin başkenti neresidir?"))