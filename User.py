""" Clase User: usuarios de Metrotify. """

class User:
    
    def __init__(self, id: str, name: str, email: str, username: str, type: str):

        self.id = id
        self.name = name
        self.email = email
        self.username = username
        self.type = type

        """Constructor de la clase User
        
            id: ID del usuario
            name: Nombre del usuario
            email: Correo electrónico del usuario
            username: Nombre de la cuenta del usuario
            type: Tipo de cuenta del usuario

        """

    def read(self):
        """Función para leer los datos del usuario

        Returns:
            string: información del usuario
        """        
        return f""" -------- Información del usuario {self.id} --------

ID del usuario: {self.id}
Nombre: {self.name}
Email: {self.email}
Username: {self.username}
Tipo: {self.id}

"""
        




