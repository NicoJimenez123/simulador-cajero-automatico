import random
clave='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
codigo=list(clave)
random.shuffle(codigo)
for i in list(codigo):
	print(i,end='')