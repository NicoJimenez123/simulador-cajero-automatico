clave='JNXFEOBKYZRQMVDGALHUSIWCTP'
codigo=list(clave)
def desencriptar(f):
	f=f.upper()
	texto=''
	for i in f:
		if i.isdigit():
			texto+=codigo[int(i)]
		else:
			texto+=i
	return(texto)