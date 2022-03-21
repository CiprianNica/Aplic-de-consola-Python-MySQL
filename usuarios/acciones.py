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
        email = input("Email: ")
        password = input("Contraseña: ")

        user = model.Usuario('', '', email, password)
        registro = user.identificar()
        # if email == registro[3]:
        #     print('Corecto !!')
        # else:
        #     print('Email o password malos.')
