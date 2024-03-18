from Clases.Album import Album
from Clases.Song import Song
from rich import print
import matplotlib.pyplot as mpl
import uuid
import re
import validators


class Tools:
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
            if email != i.email:
                return True
            else:
                return False      

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

        validation = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if re.fullmatch(validation, email):
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
        """Función para generar un ID no registrado en la plataforma.
        """        
        generated_id = uuid.uuid4
        while Tools.id_avaiability(self, generated_id, self_list) == False:
            generated_id = uuid.uuid4

            return generated_id

#-------------------------------------------------------------------------------------------------------------------------------------------------
            
    def check_name_registered(self, item_name: str, item_self_list: list):
        """Función para obtener todos los objetos registrados bajo un nombre. Si se encuentra registrado bajo ese nombre, se agregará a una lista con los
        objetos coincidentes. En caso contrario, se retornará un booleano indicando que no existen objetos bajo ese nombre.

        Args:
            item_name (str): Nombre del objeto
            item_self_list (list): Lista donde se encuentra el objeto

        Returns:
            matched_items (list): lista con los objetos coincidentes o un booleano False
        """        
        list_items = len(item_self_list)
        matched_items = []
        if list_items >= 0:
            for i in item_self_list:
                list_items -= 1
                if item_name.lower() in (i.name).lower():
                    matched_items.append(i)
                else:
                    continue
            
            return matched_items
        else:
            return False
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
            
    def validate_lenght(self, user_input):
        """Función para validar la longitud de un string introducido por pantalla.

        Args:
            user_input (str): String introducido por pantalla.

        Returns:
            Bool: Si retorna true, el string tiene una longitud adecuada. Si retorna false, excede la longitud de carácteres permitidos.
        """        
        if len(user_input) <= 30:
            return True
        elif len(user_input) > 30:
            return False
        else:
            return None

#-------------------------------------------------------------------------------------------------------------------------------------------------        
    def set_top (self, list_to_check, amount):
        """Función para definir el top 5 de una lista.

        Args:
            listToCheck (list): lista cuyo top 5 se ha de definir.

        Returns:
            top_5_list: lista nueva con el top 5 de esa lista inicial.
        """
        
        top_list = []
        registered_items_in_list = len(list_to_check)
        if registered_items_in_list > 0: 
            for k in range(registered_items_in_list):
                min_idx = k
                for idx in range(k+1, registered_items_in_list):
                    if list_to_check[min_idx].streams < list_to_check[idx].streams:
                        min_idx = idx
                    else:
                        continue

                list_to_check[k], list_to_check[min_idx] = list_to_check[min_idx], list_to_check[k]

            item_amount = 0
            pos = 0
            for i in list_to_check:
                if item_amount < amount:
                    top_list.append(list_to_check[pos])
                    item_amount += 1
                    pos += 1
                elif item_amount == amount:
                    break
                else:
                    print ("---- DATABASE ERROR ----")
                    break
        
            return top_list
        else:
            return None
            
#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def read_top (self, top_list):
        """Función para imprimir por pantalla la información dentro del top 5 con más streams de un objeto. 

        Args:
            top_list (list): lista con el top 5 con más streams de un objeto.
        """        
        if top_list == None:
            print ("----- NO STREAMS REGISTERED -----")
        else:
            for i in top_list:
                if type(i) == Song or type(i) == Album:
                    print (f"{top_list.index(i)+1}. {i.name}" )
                else:
                    print (f"{top_list.index(i)+1}. {i.username}" )

#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def top_bar_plots (self, top_list):
        """Función para mostrar la gráfica de barras de una lista.

        Args:
            top_list (list): lista del top 5 de un objeto de Metrotify.
        """        
        if len(top_list) > 0:
            streams1 = top_list[0].streams
            streams2 = top_list[1].streams
            streams3 = top_list[2].streams
            streams4 = top_list[3].streams
            streams5 = top_list[4].streams

            x = [top_list[0].name, top_list[1].name, top_list[2].name, top_list[3].name, top_list[4].name]
            y = [streams1, streams2, streams3, streams4, streams5]

            mpl.bar(x, y)
            mpl.show()
        else:
            return None

#-------------------------------------------------------------------------------------------------------------------------------------------------
        
    def validate_link(self, link):
        """Función para validar si un link es válido.

        Args:
            link (str): link de un buscador.

        Returns:
            Bool: Retorna True si el link es válido. De lo contrario, retornará False.
        """        
        if validators.url(link) == True:
            return True
        elif validators.url(link) == False:
            return False
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
        
    def banner(self):
        """Banner de Metrotify
        """        
        print("""[bold green]
     __  __        _              _   _  __       
    |  \/  |  __ _| |_  _ __ ___ | |_(_)/ _|_   _ 
    | |\/| | / _ \  __| '__/ _ \| __ | | |_| | | |
    | |  | |   __/  |_| | | (_) | |_ | |  _| |_| |
    |_|  |_| \___| \__|_|  \___/ \_ _| |_|  \__, |
                                            |___/ 
              """)
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
            
    def validate_alphabetic (self, newName):
        """Función para validar si un nombre de usuario tiene carácteres alfabéticos.

        Args:
            newName (str): Nombre de usuario a validar.

        Returns:
            Bool: Retorna True si es alfabético. Retorna False si contiene caracteres que no son alfabéticos.
        """        

        count = 0

        for i in newName:
            if i.isalpha() or i == " ":
                count += 1
            else:
                count = count
   
        if count == len(newName):
            return True
        else:
            return False

                
        