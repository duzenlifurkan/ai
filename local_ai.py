import ollama

def yerel_asistan(soru, dokuman_metni):
    prompt = f"""
    Aşağıdaki metni dikkatlice oku ve SADECE bu metne dayanarak soruyu cevapla.
    Metinde cevabı bulunmayan sorular için "Bu bilgi belgelerimde yer almıyor." de.

    METİN:
    {dokuman_metni}

    SORU: {soru}
    """

    response = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': prompt}]
    )
    
    return response['message']['content']

ozel_bilgiler = "Proje kod adı Alpha1. Yayın tarihi 15 Ekim 2026. Bütçe 50.000 TL."
print(yerel_asistan("Projenin yayın tarihi nedir?", ozel_bilgiler))