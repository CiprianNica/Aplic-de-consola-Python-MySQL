import notas.nota

class Acciones:

    def crear(self, user):
        print(f"\nOK, {user[1]} vamos a crear una nueva nota...")

        titulo = input("Introduce el titulo de tu nota: ")
        descripcion =input("Mete el contenido de tu nota: ")

        nota = notas.nota.Nota(user[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto, has guardado la nota {nota.titulo}")
        else:
            print(f"\n{user[1]}, tu nota no se ha guardado")    
