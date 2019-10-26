import copy
import os
import random
def jugar():
	def mostrarTablero():
		print(' ' + tablero[7] + ' | ' + tablero[8] + ' | ' + tablero[9])
		print("-----------")
		print(' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6])	
		print('-----------')
		print(' ' + tablero[1] + ' | ' + tablero[2] + ' | ' + tablero[3])
	def jugada(pj):
		if pj==1:
			letra='O'
		if pj==2:
			letra='X'
		estado=False
		while estado==False:
			os.system("cls")
			mostrarTablero()
			print("Turno del jugador: ",pj)
			if pj == 1:
				eleccion=int(input("Elija una posicion: "))
			if pj == 2:
				eleccion=IA()
			if eleccion in range(1,10):
				estadoJugada=comprueboJugada(eleccion,pj,tablero)
				if estadoJugada==True:
					estado=True
					jugadas.remove(eleccion)
			elegido=comprueboGanador(tablero)
			if elegido == 1:
				return 1
			if elegido == 2:
				return 2
	def comprueboJugada(eleccion,pj,tablero):
		if tablero[eleccion]=='X' or tablero[eleccion]=='O':
			return False
		if tablero[eleccion]==' ' and pj==1:
			tablero[eleccion]='O'
			return True
		if tablero[eleccion]==' ' and pj==2:
			tablero[eleccion]='X'
			return True
	def comprueboGanador(tablero):
		if((tablero[1]==tablero[4] and tablero[7]==tablero[4]) or (tablero[1]==tablero[5] and tablero[9]==tablero[5])):
			if tablero[1]=='O':
				return 1
			if tablero[1]=='X':
				return 2
		if(tablero[2]==tablero[5] and tablero[8]==tablero[5]):
			if tablero[2]=='O':
				return 1
			if tablero[2]=='X':
				return 2
		if((tablero[3]==tablero[6] and tablero[9]==tablero[6]) or (tablero[1]==tablero[2] and tablero[3]==tablero[2])):
			if tablero[3]=='O':
				return 1
			if tablero[3]=='X':
				return 2
		if(tablero[4]==tablero[5] and tablero[5]==tablero[6]):
			if tablero[4]=='O':
				return 1
			if tablero[4]=='X':
				return 2
		if(tablero[7]==tablero[8] and tablero[9]==tablero[8]):
			if tablero[7]=='O':
				return 1
			if tablero[7]=='X':
				return 2
		if(tablero[7]==tablero[5] and tablero[7]==tablero[3]):
			if tablero[3]=='O':
				return 1
			if tablero[3]=='X':
				return 2
	def IA():
		copiaTablero=tablero.copy()
		for i in list(jugadas):
			copiaTablero[i]='X'
			if comprueboGanador(copiaTablero) == 2:
				return i	
			else:
				copiaTablero[i]=' '
		for i in list(jugadas):
			copiaTablero[i]='O'
			if comprueboGanador(copiaTablero) == 1:
				return i	
			else:
				copiaTablero[i]=' '
		for i in list([1,3,7,9]):
			if comprueboJugada(i,2,copiaTablero)==True:
				return i
		if comprueboJugada(5,2,copiaTablero)==True:
			return 5
		return random.choice(jugadas)
			
	elegido=None
	jugadas=[1,2,3,4,5,6,7,8,9]
	tablero=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
	for i in range(1,10):
		if i%2!=0:
			elegido=jugada(1)
		if i%2==0:
			elegido=jugada(2)
		if elegido == 1:
			os.system("cls")
			mostrarTablero()
			print("El ganador es el 1")
			break
		if elegido == 2:
			os.system("cls")
			mostrarTablero()
			print("El ganador es el 2")
			break
		if i == 9 and elegido == None:
			os.system("cls")
			mostrarTablero()
			print("Empate")
if __name__=="__main__":
	jugar()