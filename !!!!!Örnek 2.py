x=25
epsilon=0.01
adim=0.1
tahmin=0.0
while tahmin<=x:
	if abs(tahmin**2-x)>=epsilon:
		tahmin+=adim
if abs(tahmin**2-x)>=epsilon:
	print "Hata"
else:
	print "Basarili :",tahmin