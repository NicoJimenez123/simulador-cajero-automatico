# -*- coding: utf-8 -*- 
import tkinter as tk
import Login
import Cajero
def pantallaMenu(usuario):
	def volver():
		cajeroScreen.destroy()
		pantallaPrincipal()
	def salir():
		Cajero.salir(usuario)
		screen.destroy()
	def panelDinero(nombre):
		def volverMenu():
			dineroScreen.destroy()
			pantallaMenu()
		def funcionesCajero(nombre,dinero,destino=None):
			resultado = ""
			if nombre == "Retirar":
				resultado = Cajero.retirar(usuario,dinero)
			textoResultado.configure(text=resultado)
			textoResultado.pack()
		cajeroScreen.destroy()
		dineroScreen = tk.Canvas()
		textoDinero = tk.Label(dineroScreen,text="Panel de "+nombre)
		campoDinero = tk.Entry(dineroScreen,textvariable=dinero)
		textoResultado = tk.Label(dineroScreen,text="")
		botonAceptar = tk.Button(dineroScreen,text="Aceptar",command=lambda:funcionesCajero(nombre,int(dinero.get())))
		botonVolver = tk.Button(dineroScreen,text="Volver",command=volverMenu)
		dineroScreen.pack()
		textoDinero.pack()
		campoDinero.pack()
		botonAceptar.pack()
		botonVolver.pack()
		
	cajeroScreen = tk.Canvas()
	dinero = tk.StringVar()
	botonRetirar = tk.Button(cajeroScreen,text="Retirar",command=lambda:panelDinero("Retirar"))
	botonDepositar = tk.Button(cajeroScreen,text="Depositar",command=lambda:panelDinero("Despositar"))
	botonTransferir = tk.Button(cajeroScreen,text="Transferir",command=lambda:panelDinero("Transferir"))
	botonInforme = tk.Button(cajeroScreen,text="Informe de\nMovimientos",command=lambda:panelDinero("Informe"))
	botonCuenta = tk.Button(cajeroScreen,text="Estado de Cuenta",command=lambda:panelDinero("Cuenta"))
	botonLogout = tk.Button(cajeroScreen,text="Log Out",command=volver)
	botonSalir = tk.Button(cajeroScreen,text="Salir",command=salir)
	
	cajeroScreen.pack()
	botonRetirar.pack()
	botonDepositar.pack()
	botonTransferir.pack()
	botonInforme.pack()
	botonCuenta.pack()
	botonLogout.pack()
	botonSalir.pack()
def pantallaLog_Reg(opcion,tituloCanvas,botonCanvas):
	def verificar():
		user = usuario.get()
		password = contrasena.get()
		resultado = ""
		if user == "Usuario" and password == "Contrasena":
			resultado = "Ingrese otro Nombre de\n Usuario/Contrasena"
		elif user != "" and len(user) >= 6 and password != "":
			if opcion == "login":
				resultado = Login.login(user,password)
			if opcion == "register":
				resultado = Login.register(user,password)
		resultadoLogueo.configure(text=resultado)
		resultadoLogueo.pack()
		if resultado == "Sesion Iniciada":
			loginScreen.destroy()
			pantallaMenu(user)
	def volver():
		loginScreen.destroy()
		pantallaPrincipal()
	#Definir Lienzo
	loginScreen = tk.Canvas()
	#Widgets
	textoPrin = tk.Label(loginScreen,text=tituloCanvas)
	resultadoLogueo = tk.Label(loginScreen,text="",foreground="#ff0000")
	campoUser = tk.Entry(loginScreen,textvariable=usuario)
	campoContrasena = tk.Entry(loginScreen,textvariable=contrasena)
	botonLogin = tk.Button(loginScreen,text=botonCanvas,command=verificar)
	botonVolver = tk.Button(loginScreen,text="Volver",command=volver)
	#Anadir Lienzo a la Pantalla Principal
	loginScreen.pack()
	#Anadir Widgets al Lienzo
	textoPrin.pack()
	campoUser.pack()
	campoContrasena.pack()
	botonLogin.pack()
	botonVolver.pack()
	
def pantallaPrincipal():
	def llamarLogin():
		principalScreen.destroy()
		pantallaLog_Reg(opcion="login",tituloCanvas="Inicio de Sesión",botonCanvas="Iniciar Sesión")
	def llamarRegister():
		principalScreen.destroy()
		pantallaLog_Reg(opcion="register",tituloCanvas="Registro",botonCanvas="Registrarse")
	principalScreen = tk.Canvas()
	botonLogin = tk.Button(principalScreen,text="Login",command=llamarLogin)
	botonRegister = tk.Button(principalScreen,text="Register",command=llamarRegister)
	botonSalir = tk.Button(principalScreen,text="Salir",command=screen.destroy)
	
	principalScreen.pack()
	botonLogin.pack()
	botonRegister.pack()
	botonSalir.pack()

if __name__ == "__main__":
		screen = tk.Tk()
		screen.title("Ventana de Login")
		screen.geometry("200x200")
		#Variables para los Entry
		usuario = tk.StringVar()
		contrasena = tk.StringVar()
		usuario.set("Usuario")
		contrasena.set("Contrasena")
		pantallaPrincipal()
