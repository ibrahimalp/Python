def fonk1():
	print("1")
def fonk2(y):
	print("2")
	return y
def fonk3(z):
	print("3")
	return z()
print(fonk1())
print(5+fonk2(2))
print(fonk3(fonk1))
	