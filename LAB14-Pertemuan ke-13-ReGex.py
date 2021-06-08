# 71200619_Untung Mangkunegara
# Referensi soal --> SOAL UG Tipe B no 3

# Seseorang adalah orang yang suka meme. Ia kesulitan menyebutkan huruf ‘a’, ‘u’, ‘e’, ‘o’ dan setiap kata yang
# mengandung huruf tersebut. Buatlah program yang mengganti keempat huruf tersebut menjadi i dalam
# sebuah string.

import re 

def Meme_I(kalimat):
    kalimat_kecil=kalimat.lower()
    kalimat_No_vokal=(re.sub("[aueo]","i",kalimat_kecil))
    pemisahan=re.split("\s",kalimat_No_vokal)
    print(kalimat_No_vokal)
    print("-->",pemisahan)

# Meme_I('Ular laRi lurussZZ')
Meme_I('JEJE SUKA BATAGORRRRRRR')
# Meme_I('rRiani aleRrrgi kacang')
# Meme_I('lLarRassS Saktii')
# Meme_I('SeLuruh kota meRupakan tempat beRrmain yang AsSyikK')