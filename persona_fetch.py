import argparse
import datetime

LANG_STRINGS = {
    "tr": {
        "isim": "İsim",
        "meslek": "Meslek",
        "şirket": "Şirket",
        "durum": "Durum",
        "diller": "Diller",
        "lokasyon": "Lokasyon",
        "ilgi_alani": "İlgi Alanı",
        "websitesi": "Web Sitesi",
        "mail": "E-posta",
        "sosyal": "Sosyal",
        "bio": "Hakkında",
        "yaş": "Yaş"
    },
    "en": {
        "isim": "Name",
        "meslek": "Job",
        "şirket": "Company",
        "durum": "Status",
        "diller": "Languages",
        "lokasyon": "Location",
        "ilgi_alani": "Interests",
        "websitesi": "Website",
        "mail": "Email",
        "sosyal": "Social",
        "bio": "Bio",
        "yaş": "Age"
    }
}

def renkli_yaz(metin, renk_kodu, aktif=True):
    return f"\033[{renk_kodu}m{metin}\033[0m" if aktif else metin

def hesapla_yas(dogum_str):
    try:
        dogum = datetime.datetime.strptime(dogum_str, "%Y-%m-%d")
        bugun = datetime.datetime.today()
        return bugun.year - dogum.year - ((bugun.month, bugun.day) < (dogum.month, dogum.day))
    except:
        return "?"

def logo_yukle(sistem_adi):
    ascii_dizin = "logos"
    yol = f"{ascii_dizin}/{sistem_adi.lower()}.txt"
    try:
        with open(yol, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return f"""
      .----.
     /      \\
    |        |   [ {sistem_adi} ]
     \\      /
      `----`
    """

def sor_ve_al(etiket, aktif=True):
    cevap = input(f"{etiket}: ").strip()
    return cevap

def dosyaya_kaydet(dosya_adi, logo_satirlar, bilgi_satirlari):
    with open(dosya_adi, "w", encoding="utf-8") as f:
        max_len = max(len(logo_satirlar), len(bilgi_satirlari))
        for i in range(max_len):
            sol = logo_satirlar[i] if i < len(logo_satirlar) else ""
            sag = bilgi_satirlari[i] if i < len(bilgi_satirlari) else ""
            f.write(f"{sol:<40}  {sag}\n")
    print(f"\nBilgiler '{dosya_adi}' dosyasına kaydedildi.")

def main():
    parser = argparse.ArgumentParser(description="PersonaFetch - NeoFetch but for humans (interactive).")
    parser.add_argument("--lang", choices=["tr", "en"], default="en", help="Language selection (default: en)")
    parser.add_argument("--no-color", action="store_true", help="Disable colored output")
    args = parser.parse_args()

    lang = args.lang
    renkli = not args.no_color
    etiketler = LANG_STRINGS[lang]

    print("=== PersonaFetch - NeoFetch but for humans ===\n")
    print("Please enter your information. Leave blank to skip any field.\n")

    bilgi = {}
    bilgi["isim"] = sor_ve_al(etiketler["isim"], renkli)
    bilgi["meslek"] = sor_ve_al(etiketler["meslek"], renkli)
    bilgi["şirket"] = sor_ve_al(etiketler["şirket"], renkli)
    bilgi["durum"] = sor_ve_al(etiketler["durum"], renkli)
    bilgi["diller"] = sor_ve_al(etiketler["diller"], renkli)
    bilgi["lokasyon"] = sor_ve_al(etiketler["lokasyon"], renkli)
    bilgi["ilgi_alani"] = sor_ve_al(etiketler["ilgi_alani"], renkli)
    bilgi["websitesi"] = sor_ve_al(etiketler["websitesi"], renkli)
    bilgi["mail"] = sor_ve_al(etiketler["mail"], renkli)
    bilgi["sosyal"] = sor_ve_al(etiketler["sosyal"], renkli)
    bilgi["bio"] = sor_ve_al(etiketler["bio"], renkli)
    bilgi["doğum_tarihi"] = sor_ve_al(f"{etiketler['yaş']} (YYYY-MM-DD format)", renkli)
    sistem = sor_ve_al("System/Distro name (e.g. debian, ubuntu, windows, mac)", renkli)

    logo = logo_yukle(sistem if sistem else "unknown")

    bilgi_satirlari = []
    def ekle(anahtar, veri):
        if veri:
            etiket = renkli_yaz(f"{etiketler.get(anahtar, anahtar)}:", '33', renkli)
            bilgi_satirlari.append(f"{etiket} {veri}")

    ekle("isim", bilgi.get("isim"))
    ekle("meslek", bilgi.get("meslek"))
    ekle("şirket", bilgi.get("şirket"))
    ekle("durum", bilgi.get("durum"))
    ekle("diller", bilgi.get("diller"))
    ekle("lokasyon", bilgi.get("lokasyon"))
    ekle("ilgi_alani", bilgi.get("ilgi_alani"))
    ekle("websitesi", bilgi.get("websitesi"))
    ekle("mail", bilgi.get("mail"))
    ekle("sosyal", bilgi.get("sosyal"))
    ekle("bio", bilgi.get("bio"))

    if bilgi.get("doğum_tarihi"):
        yas = hesapla_yas(bilgi.get("doğum_tarihi"))
        ekle("yaş", yas)

    logo_satirlar = logo.splitlines()
    max_len = max(len(logo_satirlar), len(bilgi_satirlari))
    print()
    for i in range(max_len):
        sol = logo_satirlar[i] if i < len(logo_satirlar) else ""
        sag = bilgi_satirlari[i] if i < len(bilgi_satirlari) else ""
        print(f"{sol:<40}  {sag}")

    # Çift dilli dosya kaydetme sorusu
    print("\nBilgileri bir dosyaya kaydetmek ister misin? / Do you want to save the info to a file?")
    dosya_adi = input("Dosya adı / Filename (örnek/example: persona.txt), boş bırak = kaydetme / leave empty = don't save: ").strip()
    if dosya_adi:
        dosyaya_kaydet(dosya_adi, logo_satirlar, bilgi_satirlari)

if __name__ == "__main__":
    main()
