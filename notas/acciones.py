import notas.nota as modelo

class Acciones:

    def crear(self, user):
        print(f"\nOK, {user[1]} vamos a crear una nueva nota...")

        titulo = input("Introduce el titulo de tu nota: ")
        descripcion =input("Mete el contenido de tu nota: ")

        nota = modelo.Nota(user[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto, has guardado la nota {nota.titulo}")
        else:
            print(f"\n{user[1]}, tu nota no se ha guardado")

    def mostrar(self, user):
        print(f"\nVale {user[1]} aqui tienes tus notas:")

        nota = modelo.Nota(user[0])
        notas = nota.listar()
        
        for nota in notas:
            print("\n******************************************")
            print(nota[2])
            print(nota[3])
            print("\n******************************************")

    def borrar(self, user):
        print(f"\nVale {user[1]} vamos a borrar una nota.")
        titulo = input("Introduce el titulo de la nota a borrar: ")
        nota = modelo.Nota(user[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >=1:
            print(f"Hemos borrado la nota {nota.titulo}")
        else:
            print("No se ha borrado la nota. Intenta luego...")