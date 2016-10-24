fak=int(input("Bir sayi giriniz = "))
adm_sayisi=fak
adm_sayisi=adm_sayisi-1
if fak==1:
	print(fak)
elif fak<1:
	print "girilen deger sifir veya negatif"
else:
	while True:
		fak=adm_sayisi*fak
		adm_sayisi=adm_sayisi-1
		if adm_sayisi<1:
			print fak	
			break