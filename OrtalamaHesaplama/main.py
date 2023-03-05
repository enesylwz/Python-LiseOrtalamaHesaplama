print("Ortalama Hesaplama")

matematik = int(input("matematik notunuzu giriniz: "))
edebiyat = int(input("edebiyat notunuzu giriniz: "))
ingilizce = int(input("yabanci dil notunuzu giriniz: "))
tarih = int(input("tarih notunuzu giriniz: "))
din = int(input("din notunuzu giriniz: "))
coğrafya = int(input("coğrafya notunuzu giriniz: "))
fizik = int(input("fizik notunuzu giriniz: "))
kimya = int(input("kimya notunuzu giriniz: "))
almanca = int(input("ikinci yabanci dil notunuzu giriniz: "))
resim = int(input("görsel sanatlar notunuzu giriniz: "))
beden = int(input("beden eğitimi notunuzu giriniz: "))
secmeliders = int(input("seçmeli ders notunuzu giriniz: "))

ortalama = (matematik*6+edebiyat*5+ingilizce*4+tarih*2+din*2+coğrafya*2+fizik*2+kimya*2+almanca*2+resim*2+beden*2+secmeliders*2)/31

if (ortalama >= 85):
    print(ortalama," takdir almiştir.")

elif (ortalama >= 70):
    print(ortalama," teşekkür almiştir.")
else:
    print(ortalama," düz geçmiştir.")

if (ortalama < 50):
    print(ortalama," sinifta kalmiştir.")