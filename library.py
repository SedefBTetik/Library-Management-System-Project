import os
import codecs

def list_book():
    os.system('cls')
    print("Kitap listele")
    dosya = codecs.open("books.txt", "r", "UTF-8")
    print(dosya.read())
    dosya.close()
    input("\nDevam etmek için enter...")

def add_book():
    os.system('cls')
    print("Kitap Ekle")
    kitap_adi=input("Kitabın adı : ")
    kitap_yazari=input("Kitabın yazarı : ")
    basim_yili=input("Basım yılı : ")
    sayfa_sayisi=input("Sayfa sayısı : ")
    kitap_bilgileri=kitap_adi + ", " + kitap_yazari + ", " + basim_yili + ", " + sayfa_sayisi +"\n"
    dosya = codecs.open("books.txt", "a", "UTF-8")
    dosya.write(kitap_bilgileri)
    dosya.close()
    input("\nDevam etmek için enter...")

def del_book():
    os.system('cls')
    print("Kitap Sil")
    
    silinecek_kitap_adi = input("Silmek istediğin kitap : ")
    okunan_kitap_sayisi = 0
    sayac = 0
    
    orijinal_dosya = codecs.open("books.txt", "r", "UTF-8")
    
    for okunan_satir in orijinal_dosya:
        yeni_dosya = codecs.open("books2.txt", "a", "UTF-8")
        okunan_kitap_sayisi += 1
        parcalar = okunan_satir.split(", ")
    
        if silinecek_kitap_adi != parcalar[0]:
            korunacak_kitap_bilgileri = parcalar[0] + ", " + parcalar[1] + ", " + parcalar[2] + ", " + parcalar[3]
            yeni_dosya.write(korunacak_kitap_bilgileri)
            yeni_dosya.close()
    
    orijinal_dosya.close()
    yeni_dosya.close()
    os.remove("books.txt")
    os.rename("books2.txt", "books.txt")
          
    input("\nDevam etmek için enter...")

while True:

    os.system('cls')
    
    print("""
          *** MENÜ***
          
          1) Kitapları Listele
          
          2) Kitap Ekle
          
          3) Kitabı Kaldır

          4) Çıkış
          """)

    secim = input("Seçiminiz: ")

    if secim == "1":
        list_book()
    elif secim == "2":
        add_book()
    elif secim == "3":
        del_book()
    elif secim == "4":
        break
      