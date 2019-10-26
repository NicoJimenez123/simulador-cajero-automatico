import os
import time
import Login
from Transacciones import transacciones
informe = []
dinero = 0
def cargarUsuarios(user):
	file=open("Informes/informe_"+user+".txt", "r")
	informe=file.readlines()
	file.close()
	dinero=cargarDinero(user)
def retirar(user,dinero):
	ret=dinero
	if ret>dinero or ret<0:
		return "Error"
	else:	
		dinero-=ret
		informe.append("Dinero Retirado:$"+str(ret)+" a las "+time.strftime("%H:%M:%S"))
		file=open("Informes/informe_"+user+".txt", "a")
		file.write("Dinero Retirado:$"+str(ret)+" a las "+time.strftime("%H:%M:%S"))
		file.write(os.linesep)
		file.close()
		money=open("Dinero/dinero_"+user+".txt", "w")
		money.write(str(dinero))
		money.close()
		return "Operación Exitosa"
def depositar(dinero):
	band=0
	while band==0:
		dep=float(input("Cantidad a Depositar:$"))
		if dep<0:
			print("Error")
		else:	
			dinero+=dep
			informe.append("Dinero Depositado:$"+str(dep)+" a las "+time.strftime("%H:%M:%S"))
			file=open("Informes/informe_"+user+".txt", "a")
			file.write("Dinero Depositado:$"+str(dep)+" a las "+time.strftime("%H:%M:%S"))
			file.write(os.linesep)
			file.close()
			money=open("Dinero/dinero_"+user+".txt", "w")
			money.write(str(dinero))
			money.close()
			band=1
			return dinero
def transferir(dinero):
	destino=input("Ingrese la cuenta destinataria: ")
	while Login.Ver_User(destino)==False:
		print("Cuenta Destinataria no Existente")
		destino=input("Ingrese la cuenta destinataria: ")
	money=int(input("Ingrese el dinero a transferir:$"))
	transacciones(money,user,destino)
	return cargarDinero()
def infomov():
	if len(informe)==0:
		return "No hay registro"
	else:
		return informe
def salir(user):
	file = open("Informes/informe_"+user+".txt","w")
	for i in range(len(informe)):
		file.write(informe[i])
	file.write(os.linesep)
	file.close()
	money=open("Dinero/dinero_"+user+".txt", "w")
	money.write(str(dinero))
	money.close()
def cargarDinero(user):
	money=open("Dinero/dinero_"+user+".txt", "r")
	dinero=float(money.read())
	money.close()
	return dinero