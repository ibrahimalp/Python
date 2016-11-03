a=1
adim=1
while True:
	if a**3<29:
		a+=0.0025
		print adim,".adim",a
		adim+=1
	else:
		print"kupkok (29)",a,"degerine yakindir"
		break