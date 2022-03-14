"""
Proyecto Python y MySQL
- abrir asistente
- login y registro
- si elegimos "registro", creara un usuario en bbdd
- si elegimos "login", identificara al usuario y nos preguntara
- crear nota, mostrar nota, borrarlas
"""
print("""
Acciones disponibles:
    - registro
    - login
""")
accion = input("¿Que quieres hacer ?\n")
if accion == "registro":
    print("\nOK, Vamos a registrarte en el sistema...\n")
    nombre = input("Introduce tu nombre: ")
    apellido = input("Tus apellidos: ")
    email = input("Email: ")
    password = input("Contraseña: ")
elif accion == "login":
    print("Vale!! Identificate en el sistema....\n")
    email = input("Email: ")
    password = input("Contraseña: ")
