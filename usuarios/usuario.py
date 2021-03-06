import usuarios.conexion as conexion
import datetime, hashlib

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()
        #cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        password_cifrado = cifrado.hexdigest()

        sql = "INSERT INTO usuarios VALUES (null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, password_cifrado, fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        return result
        
    def identificar(self):
        #comprobar si el usuario existe
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        # cifrar contraseña
        if len(self.password) <= 4:
            usuario = (self.email, self.password)
        else:
            cifrado = hashlib.sha256()
            cifrado.update(self.password.encode('utf8'))
            password_cifrado = cifrado.hexdigest()
            #datos para la consulta
            usuario = (self.email, password_cifrado)
            #consulta
        cursor.execute(sql, usuario)
        result = cursor.fetchone()
        return result