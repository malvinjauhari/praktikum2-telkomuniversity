umur = 17
kartu_pelajar = "ada"

print("Umur anda =", umur, "Tahun")

if umur >= 17:
    print("Umur memenuhi syarat")
    if kartu_pelajar == "ada" or kartu_pelajar == "ono":
        print("Anda mendapatkan diskon pelajar")
    else:
        print("Anda tidak mendapatkan diskon pelajar")
else:
    print("Umur tidak memenuhi syarat")
    


