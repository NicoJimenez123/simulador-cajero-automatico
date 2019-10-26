import Cajero
from TaTeTi_V3 import jugar
import os
def menu():
	print("~~Menu Inicial~~")
	print("Opciones:\n1_Usar el Cajero\n2_Jugar al TaTeTi")
	return int(input("Opcion: "))
a=True
while a:
	opc=menu()
	if opc == 1:
		os.system("cls")
		Cajero.cajero()
	if opc == 2:
		jugar()
		os.system("pause")