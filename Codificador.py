import random
clave='JNXFEOBKYZRQMVDGALHUSIWCTP'
codigo=list(clave)
def encriptar(f):
	f=f.upper()
	salida=''
	for i in f:
		if i in clave:
			salida+=str(codigo.index(i))
		else:
			salida+=i
	return(salida)

w=encriptar('123123')
