"""
Proyecto Python y MySQL
- abrir asistente
- login y registro
- si elegimos "registro", creara un usuario en bbdd
- si elegimos "login", identificara al usuario y nos preguntara
- crear nota, mostrar nota, borrarlas
"""
from usuarios import acciones
print("""
Acciones disponibles:
    - registro
    - login
""")
crear = acciones.Acciones()
accion = input("¿Que quieres hacer ?\n")
if accion == "registro":
    crear.registro()
    
elif accion == "login":
    crear.login()
    
