import usuarios.usuario as model
import notas.acciones

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
            usuario = model.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has identificado correctamente en la fecha {login[5]}.")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("Email o password incorrectos. Intentalo mas tarde.")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
            - crear notas (crear)
            - mostrar notas (mostrar)
            - eliminar notas (eliminar)
            - salir (salir)
        """)
        accion = input("Que quieres hacer?: ")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            print("Vamos a crear")
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            print("Vamos a mostrar.")
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print(usuario)
            print(f"Ok {usuario[1]}, hasta pronto !!")
            exit()
        
