# Paketler
import base64
import binascii
import codecs

# Fonksiyonlar
def base64_sifrele(metin):
    return base64.b64encode(metin.encode('utf-8')).decode('utf-8')
def base64_desifrele(metin):
    return base64.b64decode(metin.encode('utf-8')).decode('utf-8')
def hex_sifrele(metin):
    return binascii.hexlify(metin.encode('utf-8')).decode('utf-8')
def hex_desifrele(metin):
    h_metin = ""
    for sifre in metin:
        if " " not in sifre:
            h_metin += sifre
    return binascii.unhexlify(h_metin.encode('utf-8')).decode('utf-8')
def rot13_sifrele():
    return codecs.encode(metin,'rot13')
def rot13_desifrele():
    return codecs.encode(metin,'rot13')
    
print("Şifrelemeye Hoşgeldiniz.. \n\n-Alqens")

while 1 == 1:

    print("\nŞifrele - 0")
    print("Deşifrele - 1")
    print("\n99 - Çıkış")


    tab0 = int(input("\n"))

    if tab0 == 0:
        while 1 == 1:
            print("\n0 - Base64")
            print("1 - Hex")
            print("2 - Rot13")
            print("\n99 - Geri")
    
            tab_sifre = int(input("\n"))
            if tab_sifre == 0:
                metin = str(input("Lütfen Bir Metin Giriniz: "))
                print("Şifre: ",base64_sifrele(metin))
            elif tab_sifre == 1:
                metin = str(input("Lütfen Bir Metin Giriniz: "))
                print("Şifre: ",hex_sifrele(metin))
            elif tab_sifre == 2:
                metin = str(input("Lütfen Bir Metin Giriniz: "))
                print("Şifre: ",rot13_sifrele(metin))
            elif tab_sifre == 99:
                break
            else:
                print("Lütfen Belirli Bir Tab Seçin!")
                continue
    elif tab0 == 1:
        while 1 == 1:
            print("\n0 - Base64")
            print("1 - Hex")
            print("2 - Rot13")
            print("\n99 - Geri")

            tab_desifre = int(input("\n"))
            if tab_desifre == 0:
                metin = str(input("Lütfen Şifreli Metini Giriniz: "))
                print("Şifre: ",base64_desifrele(metin))
            elif tab_desifre == 1:
                metin = str(input("Lütfen Şifreli Metini Giriniz: "))
                print("Şifre: ",hex_desifrele(metin))
            elif tab_desifre == 2:
                metin = str(input("Lütfen Şifreli Metini Giriniz: "))
                print("Şifre: ",rot13_desifrele(metin))
            elif tab_desifre == 99:
                break
            else:
                print("Lütfen Belirli Bir Tab Seçin!")
                continue
    elif tab0 == 99:
        exit()
    else:
        print("Lütfen Belirli Bir Tab Seçin!")