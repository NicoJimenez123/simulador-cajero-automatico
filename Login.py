import csv
from Codificador import encriptar

with open('Usuarios/Users.csv') as File:
	usuarios = dict(filter(None, csv.reader(File)))
File.close()


def login(usuario, contra):
	user = encriptar(usuario)
	password = encriptar(contra)
	if not Ver_User(user):
		return "Usuario no Registrado"
	if usuarios.get(user) == password:
		return "Sesion Iniciada"
	else:
		return "Usuario o Contraseña Incorrecto/s"

def register(user,password):
	if not Verifico(user):
		return "El Nombre debe contener al menos\n 6 Caracteres\n y no debe tener Numeros."
	user = encriptar(user)
	if user not in usuarios:
		password = encriptar(password)
		usuarios[user] = password
		variable = csv.writer(open('Usuarios/Users.csv','a',newline=''))
		variable.writerow([user, password])
		file = open("Dinero/dinero_"+user+".txt","w")
		file.write("1000")
		file.close()
		file = open("Informes/informe_"+user+".txt","w")
		file.close()
		return "Usuario Registrado con Exito"
	else:
		return "Usuario ya Existente"

def menu():
	print("1_Iniciar Sesion")
	print("2_Registrarse")
	print("3_Salir")
	return int(input("Escoja una Opcion: "))

def Verifico(user):
	for i in user:
		if i.isdigit():
			return False
	if len(user)<6:
		return False
	else:
		return True

def Ver_User(user):
	global usuarios
	with open('Usuarios/Users.csv') as file:
		usuarios = dict(filter(None, csv.reader(file)))
	file.close()
	if user not in usuarios:
		return False
	else:
		return True

while True:
	opc = menu()
	if opc == 1:
		usuario = input("Ingrese el Nombre de Usuario: ")
		contrasena = input("Ingrese la Contraseña ")
		login(usuario, contrasena)
	if opc == 2:
		usuario = input("Ingrese el Nombre de Usuario: ")
		contrasena = input("Ingrese la Contraseña ")
		register(usuario, contrasena)
	if opc == 3:
		break
