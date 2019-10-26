import os
def transacciones(money,user,destino):
	#veo si el usuario tiene el dinero suf. para hacer la transaccion | DineroUsuario y DineroDestino
	if user == destino:
		return "No puedes Transefirte Dinero a Ti mismo"
	else:
		lector=open("Dinero/dinero_"+user+".txt","r")
		du=float(lector.read())
		lector.close()
		lector2=open("Dinero/dinero_"+destino+".txt","r")
		dd=float(lector2.read())
		lector2.close()
		if du < money:
			return "Dinero para realizar Transaccion Insuficiente"
		if du >= money:
			lector=open("Dinero/dinero_"+user+".txt","w")
			lector.write(str(du-money))
			lector2=open("Dinero/dinero_"+destino+".txt","w")
			lector2.write(str(dd+money))
			lector2.close()
			lector.close()
			return "Transaccion Completada"
		