list1=[5,2];
list2=[13,14,30,81];
list3=[111,153,119,127,233,276];
list4=[1633,1731,1951,2768,2787,2931,2953,3441];
list5=[12421,16569,19602,22145,24297,25562,25921,26189,26762,32276];
list6=[6,1,2,9,1,2];
list7=[];

a=0
while a<6:
	blt_no=int(input("Biletinizdeki %d.Sayi = " % (a+1)))
	if blt_no>=0 and blt_no<10:
		list7.append(blt_no)
		a+=1
	else:
		print"aralik disi 0-9 arasinda giriniz!"

if list7[0]==list6[0] and list7[1]==list6[1] and list7[2]==list6[2] and list7[3]==list6[3] and list7[4]==list6[4]and list7[5]==list6[5]:
	print"Tebrikler Buyuk ikramiyeyi kazandiniz"
elif list7[0]!=list6[0] and list7[1]!=list6[1] and list7[2]!=list6[2] and list7[3]!=list6[3] and list7[4]!=list6[4]and list7[5]!=list6[5]:
  print"Kazanamadiniz"
else:
	for i1 in range(0,len(list1)):
		if list7[5]==list1[i1]:
			print"Tebrikler Amorti kazandiniz"
	
	son2=list7[4]*10+list7[5]
	for i in range(0,len(list2)):
		if list2[i]==son2:
			print"Son 2 Rakamina gore Tutturdunuz\nSon 2 Rakamina gore liste;",list2
		
	son3=list7[3]*100+list7[4]*10+list7[5]
	for i1 in range(0,len(list3)):
		if list3[i1]==son3:
			print"Son 3 Rakamina gore Tutturdunuz\nSon 3 Rakamina gore liste;",list3
		
	son4=list7[2]*1000+list7[3]*100+list7[4]*10+list7[5]
	for i2 in range(0,len(list4)):
		if list4[i2]==son4:
			print"Son 4 Rakamina gore Tutturdunuz\nSon 4 Rakamina gore liste;",list4
		
	son5=list7[1]*10000+list7[2]*1000+list7[3]*100+list7[4]*10+list7[5]
	for i3 in range(0,len(list5)):
		if list5[i3]==son5:
			print"Son 5 Rakamina gore Tutturdunuz\nSon 5 Rakamina gore liste;",list5