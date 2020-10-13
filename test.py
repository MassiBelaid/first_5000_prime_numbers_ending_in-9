
def isPrime(num):
	i = 2
	while(i< num/2):
		if(num%i == 0):
			return False
		i +=1
	return True





i = 1
numero = 19
print("Le premier : {}".format(numero))
while(i < 5000):
	numero += 10
	if(isPrime(numero)):
		i += 1
		print("Le {} eme : {}".format(i,numero))









