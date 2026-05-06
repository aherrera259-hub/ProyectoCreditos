import json
import os

class Estudiante:
    def __init__(self, codigo, nombre, password, carrera, creditos):
        self.codigo = codigo
        self.nombre = nombre
        self.password = password
        self.carrera = carrera
        self.creditos = creditos

def cargar_datos():
    if not os.path.exists("usuarios.json"):
        with open("usuarios.json", "w") as f:
            json.dump({"data": []}, f)
    with open("usuarios.json", "r") as f:
        return json.load(f)


def guardar_datos(data):
    with open("usuarios.json", "w") as f:
        json.dump(data, f, indent=4)

class Sistema:
    def __init__(self):
        self.usuario_actual = None

    def registrar(self):
        data = cargar_datos()

        codigo = input("Código: ")

        for u in data["data"]:
            if u["codigo"] == codigo:
                print("El usuario ya existe")
                return

        nombre = input("Nombre: ")
        password = input("Password: ")
        carrera = input("Carrera: ")
        creditos = int(input("Créditos aprobados: "))

        est = Estudiante(codigo, nombre, password, carrera, creditos)

        data["data"].append(est.__dict__)
        guardar_datos(data)

        print("Usuario registrado")

    def login(self):
        data = cargar_datos()

        codigo = input("Código: ")
        password = input("Password: ")

        for u in data["data"]:
            if u["codigo"] == codigo and u["password"] == password:
                self.usuario_actual = u
                print("Bienvenido", u["nombre"])
                return

        print("Datos incorrectos")

    def ver_datos(self):
        if not self.usuario_actual:
            print("Debe iniciar sesión")
            return

        print("\n--- DATOS DEL ESTUDIANTE ---")
        print("Nombre:", self.usuario_actual["nombre"])
        print("Código:", self.usuario_actual["codigo"])
        print("Carrera:", self.usuario_actual["carrera"])
        print("Créditos:", self.usuario_actual["creditos"])


def menu():
    print("\n--- SISTEMA CGU ---")
    print("1. Registrar")
    print("2. Login")
    print("3. Ver datos")
    print("4. Salir")

sistema = Sistema()

while True:
    menu()
    op = input("Seleccione: ")

    if op == "1":
        sistema.registrar()

    elif op == "2":
        sistema.login()

    elif op == "3":
        sistema.ver_datos()

    elif op == "4":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")
