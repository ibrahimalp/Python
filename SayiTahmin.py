sayi=100
tahmin=25
aralik=100
adm=0
print "Sayi","  aralik","  adim"
while True:
	if sayi>tahmin:
		adm+=1
		aralik/=2
		print sayi,"  ",aralik,"  ",adm
		sayi=sayi-aralik
	elif sayi<tahmin:
		adm+=1
		aralik/=2
		print sayi,"  ",aralik,"  ",adm
		sayi=sayi+aralik
	else:
		print adm,"Denemede Dogru Tahmini (",tahmin, ") buldu"
		break