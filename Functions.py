import uuid
import re


class Functions:
    """Clase con las funciones pertenecientes al módulo de gestión de perfiles
    """
#-------------------------------------------------------------------------------------------------------------------------------------------------
   
    def username_avaiability (self, username):
        """Función para verificar si un nombre de usuario se encuentra disponible. Si este se encuentra disponible, retornará True.
        En caso contrario, retornará False.

        Args:
            username (): Nombre de usuario de un usuario.
        Returns:
            Bool
        """  

        for i in self.users:
            if username == i.username:
                return False
            else:
                return True

#-------------------------------------------------------------------------------------------------------------------------------------------------
            
    def email_avaiability (self, email):
        """Función para verificar si un email se encuentra disponible. Si este se encuentra disponible, retornará True.
        En caso contrario, retornará False.

        Args:
            email (): Dirección de correo de un usuario.

        Returns:
            Bool
        """            
        for i in self.users:
            if email == i.email:
                return False
            else:
                return True      

#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def id_avaiability (self, id, self_list):
        """Función para verificar si un id se encuentra disponible. Si este se encuentra disponible, retornará True.
        En caso contrario, retornará False.

        Args:
            id (): ID de un usuario.

        Returns:
            Bool
        """            
        for i in self_list:
            if id == i.id:
                return False
            else:
                return True
            
#-------------------------------------------------------------------------------------------------------------------------------------------------
             
    def validate_email(self, email):
        """Función para verificar si un email introducido es válido. Si este se encuentra disponible, retornará True.
        En caso contrario, retornará False.

        Args:
            email (_type_): Dirección de correo de un usuario.

        Returns:
            Bool
        """        
        
        valid_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]*\.*[com|org|edu]{3}$)'

        if re.match(valid_pattern, email) == True:
            return True
        else:
            return False
  
#-------------------------------------------------------------------------------------------------------------------------------------------------
            
    def existent_username (self, username):
        """Función para verificar si un nombre de usuario se encuentra registrado. Si este se encuentra registrado, retornará True.
        En caso contrario, retornará False.

        Args:
            user (): Nombre de usuario

        Returns:
            Bool
        """      
        search_length = len(self.users)
        if search_length >= 0:
            for i in self.users:
                search_length -= 1
                if i.username == username:
                    return True
                else:
                    continue
        else:
            return False

#-------------------------------------------------------------------------------------------------------------------------------------------------
        
    def generate_id(self, self_list):
        """Función para generar un ID
        """        
        generated_id = uuid.uuid4
        while Functions.id_avaiability(self, generated_id, self_list) == False:
            generated_id = uuid.uuid4
            if Functions.id_avaiability(self, generated_id, self_list) == True:
                break
            else:
                continue

#-------------------------------------------------------------------------------------------------------------------------------------------------
        