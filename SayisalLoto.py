a=0
list1=[];
while a<6:
	kzn_no=int(input("Kazanan Numaralar %d.Sayi = " % (a+1)))
	if kzn_no>0 and kzn_no<50:
		if kzn_no in list1:
			print("Bu sayiyi daha once girdiniz!")
		else:
			list1.append(kzn_no)
			a+=1
	else:
		print("aralik disi 1-49 arasinda giriniz!")
b=0
list2=[];
while b<6:
	blt_no=int(input("Biletinizde ki Numaralar %d.Sayi = " % (b+1)))
	if blt_no>0 and blt_no<50:
		if blt_no in list2:
			print("Bu sayiyi daha once girdiniz!")
		else:
			list2.append(blt_no)
			b+=1
	else:
		print("aralik disi 1-49 arasinda giriniz!")
c=0
list3=[];
for i1 in range(0,6):
	for i2 in range(0,6):
		if list1[i1]==list2[i2]:
			list3.append(list1[i1])
		else:
			c+=1
dogru_sys=len(list3)
print ("Dogru bilinen numaralar =",list3,"%d Bildin" % dogru_sys)