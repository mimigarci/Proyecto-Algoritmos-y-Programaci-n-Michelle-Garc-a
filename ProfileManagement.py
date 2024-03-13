import uuid
from Artist import Artist
from Listener import Listener

class ProfileManagement:
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
    
    def id_avaiability (self, id):
        """Función para verificar si un id se encuentra disponible. Si este se encuentra disponible, retornará True.
        En caso contrario, retornará False.

        Args:
            id (): ID de un usuario.

        Returns:
            Bool
        """            
        for i in self.users:
            if id == i.id:
                return False
            else:
                return True
            
#-------------------------------------------------------------------------------------------------------------------------------------------------
             
    #TODO: Modificar funcionalidad
    def validate_email(self, email):
        """Función para verificar si un email introducido es válido. Si este se encuentra disponible, retornará True.
        En caso contrario, retornará False.

        Args:
            email (_type_): Dirección de correo de un usuario.

        Returns:
            Bool
        """        
        count_address = 0
        count_dots = 0
        
        for i in email:
            if i == "@" or i == ".":
                count_address += 1
                count_dots += 1
                if count_address == 1 and count_dots >= 1:
                    return True
                else:
                    return False
            else:
                continue
  
#-------------------------------------------------------------------------------------------------------------------------------------------------
            
    def existent_user (self, user):
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
                if i.username == user:
                    return True
                else:
                    continue
        else:
            return False

#-------------------------------------------------------------------------------------------------------------------------------------------------
        
    def generate_id(self):
        """Función para generar un ID
        """        
        generated_id = uuid.uuid4
        while ProfileManagement.id_avaiability(self, generated_id) == False:
            generated_id = uuid.uuid4
            if ProfileManagement.id_avaiability(self, generated_id) == True:
                break
            else:
                continue
                
#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def register_profile (self):
        """Función para registrar una cuenta de Metrotify
        """    

        print ("\n------------- Registro de Usuario ------------- \n")
        user_name = input("Introduzca su nombre: ")  
        user_email = input("Introduzca el email del usuario: ") 
        user_username = input("Introduzca un nombre de usuario: ") 
        user_id = uuid.uuid4()
        
        while True:
            if ProfileManagement.id_avaiability(self, user_id) == True:
                if ProfileManagement.email_avaiability(self, user_email) and ProfileManagement.validate_email(self, user_email) == True:
                    if ProfileManagement.username_avaiability(self, user_name) == True:
                        user_type = input (""" 
    Tipo de cuenta:
    1. Musico
    2. Escucha
                                        
    ---> """)
                        if user_type == "1":
                            newArtist = Artist(user_id, user_name, user_email, user_username, user_type)
                            self.users.append(newArtist)
                            self.artists.append(newArtist)
                            print ("\nEl usuario se ha registrado correctamente. Puede acceder a la plataforma.\n")
                            break

                        elif user_type == "2":
                            newUser = Listener(user_id, user_name, user_email, user_username, user_type)
                            self.users.append(newUser)
                            self.listeners.append(newUser)
                            print ("\nEl usuario se ha registrado correctamente. Puede acceder a la plataforma.\n")
                            break
                            
                        else:
                            print ("\nEl tipo de cuenta introducido es inválido. Solo puede ser de tipo musico o escucha\n")
                            break
                    else:
                        print ("\nEl nombre de usuario que usted ha introducido ya se encuentra registrado. Por favor introduzca otro.\n")
                        break
                else:
                    print ("\nEl correo electrónico que usted ha introducido ya se encuentra registrado. Por favor introduzca otro.\n")
                    break
            else:
                user_id = ProfileManagement.generate_id(self)

#-------------------------------------------------------------------------------------------------------------------------------------------------

    def modify_user (self, user_id):
        """Función para modificar la información personal de una cuenta

        Args:
            user_id (): ID del usuario cuya cuenta se va a modificar.
        """        

        for i in self.users:
            if i.id == user_id:
                user = i
            else:
                continue
        
        #Configuración del usuario
        while True:
            if ProfileManagement.existent_user(self, user.username) == True:
                modify_attribute = input("""----- Configuración de la cuenta ----- 
                                    
    1. Cambiar nombre personal de la cuenta
    2. Actualizar email
    3. Cambiar nombre de usuario
    4. Regresar
                                    
    ---> """)
            
                if modify_attribute == "1":
                    newName = input ("Nombre nuevo: ")
                    if newName.isalpha:
                        user.name = newName
                        print ("Cambio registrado.")
                    else:
                        print ("El nombre solo puede contener carácteres alfabéticos.")

                elif modify_attribute == "2":
                    newEmail = input ("Email nuevo: ")
                    if ProfileManagement.email_avaiability(self, newEmail) == True:
                        if ProfileManagement.validate_email == True:
                            user.email = newEmail
                            print ("\n----- Cambio registrado -----\n")
                        else:
                            print ("El correo ingresado no es válido.")
                    else:
                        print ("El correo ingresado ya se encuentra registrado.")

                elif modify_attribute == "3":
                    newUsername = input ("Nombre nuevo: ")
                    if ProfileManagement.username_avaiability(self, newUsername) == True:
                        user.username = newUsername
                        print ("Cambio registrado.")
                    else:
                        print ("El nombre de usuario no se encuentra disponible.")

                elif modify_attribute == "4":
                    break
                else:
                    print ("\nOpción inválida. Introduzca una opción válida por favor.\n")
            else:
                print ("El usuario no se encuentra registrado")
                break

#-------------------------------------------------------------------------------------------------------------------------------------------------

    def delete_account_data (self, account_id):
        """Función para eliminarla la información de una cuenta.

        Args:
            account_id (): ID de la cuenta a eliminar.
        """        

        existent_users = len(self.users)
        if existent_users > 0:
            for i in self.users:
                existent_users -= 1
                if i.id == account_id:
                    self.users.remove(i)
                    print ("La cuenta se ha eliminado correctamente.")
                else:
                    continue
        else:
            print ("No hay usuarios registrados.")

#-------------------------------------------------------------------------------------------------------------------------------------------------

    def search_user (self):
        artist_name = input ("Nombre del músico: ")

        registered_artist = len(self.artists)
        if registered_artist >= 0:
            for i in self.artists:
                registered_artist -= 1
                if artist_name == i.name:
                    print (i.read)

                    choose_view = input ("""
1. Ver canciones del músico
2. Ver albumes del músico
    
---> """)
                    if choose_view == "1":   
                        for s in i.albums:
                            print (s.read)
                            
                            select = input ("Desea escuchar una canción?")
                            
                            if select == "1":
                                pass
                            else:
                                pass
                            
                    elif choose_view == "2":
                        for a in i.albums:
                            print (a.read)
                else:
                    continue
                

        else:
            print("No hay canciones registradas")