import os as o

# Kişisel müzik yolları kaldırıldı, genel liste isimleri eklendi
müsikler = {
    "liste1": [],  # Kullanıcı kendi yollarını ekleyecek
    "liste2": [],
    "liste3": []
}

print("""
__________.____       _____ _____.___.
\______   \    |     /  _  \\__  |   |
 |     ___/    |    /  /_\  \/   |   |
 |    |   |    |___/    |    \____   |
 |____|   |_______ \____|__  / ______|
                  \/       \/\/       
   _____   ____ _________________  __.
  /     \ |    |   \____    /    |/ _|
 /  \ /  \|    |   / /     /|      <  
/    Y    \    |  / /     /_|    |  \ 
\____|__  /______/ /_______ \____|__ \
        \/                 \/       \/
""")

while True:
    print("\nListeler:")
    for liste in müsikler:
        print("-", liste)

    mesaj = input("Liste adı gir: ").strip().lower()

    if mesaj in müsikler:
        liste = müsikler[mesaj]
        index = 0
        while index < len(liste):
            komut = input(">> (boşlukla çal, q ile çık): ")
            if "q" in komut:
                print("çıkılıyor...")
                break
            elif komut.strip() == "":
                print("Açılacak dosya:", liste[index])
                try:
                    o.startfile(liste[index])
                    index += 1
                except Exception as e:
                    print("Açılamadı:", e)
            else:
                print("Durdu. Boşluk veya 'q' kullan.")
    else:
        print("Geçersiz liste adı!")