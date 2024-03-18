
 
class User:
    """Usuario de Metrotify

    Returns:
        Objeto de la clase User
    """    

    
    def __init__(self, id: str, name: str, email: str, username: str, type: str):
        """Constructor de la clase User

        Args:
            id (str): ID del usuario
            name (str): Nombre del usuario
            email (str): Correo electrónico del usuario
            username (str): Nombre de la cuenta del usuario
            type (str): Tipo de cuenta del usuario
        """        
        self.id = id
        self.name = name
        self.email = email
        self.username = username
        self.type = type


    def read(self):
        """Función para leer los datos del usuario

        Returns:
            str: información del usuario
        """        
        return f"""
Nombre: {self.name}
Nombre de Usuario: {self.username}
ID: {self.id}

"""
        




