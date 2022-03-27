import usuarios.usuario as model

class Acciones:

    def registro(self):

        print("\nOK, Vamos a registrarte en el sistema...\n")
        nombre = input("Introduce tu nombre: ")
        apellidos = input("Tus apellidos: ")
        email = input("Email: ")
        password = input("Contraseña: ")

        user = model.Usuario(nombre, apellidos, email, password)
        registro = user.registrar()
        
        if registro[0] >= 1:
            print ("perfecto")
        else:

            print("No se ha registrado !!")

    def login(self):
        print("Vale!! Identificate en el sistema....\n")
        try:

            email = input("Email: ")
            password = input("Contraseña: ")

            user = model.Usuario('', '', email, password)
            registro = user.identificar()

            if email == registro[3]:
                print(f"\nBienvenido {registro[1]}, te has identificado correctamente.")
                self.proximasAcciones(registro)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("Email o password incorrectos. Intentalo mas tarde.")
    def proximasAcciones(self, user):
        print("""
        Acciones disponibles:
            - crear notas (crear)
            - mostrar notas (mostrar)
            - eliminar notas (eliminar)
            - salir (salir)
        """)
        accion = input("Que quieres hacer?: ")
        if accion == "crear":
            print("Vamos a crear")
            self.proximasAcciones(user)
        elif accion == "mostrar":
            print("Vamos a mostrar.")
            self.proximasAcciones(user)
        elif accion == "eliminar":
            print("Vamos a eliminar")
            self.proximasAcciones(user)
        elif accion == "salir":
            print(f"Ok {user[1]}, hasta pronto !!")
            exit()
        
