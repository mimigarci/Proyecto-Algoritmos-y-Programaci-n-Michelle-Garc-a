from User import User
from Artist import Artist
from Listener import Listener
from Album import Album
from Playlist import Playlist
from Song import Song 
from Like import Like
import uuid
import requests
 
class Functions:

    """------------------------ Función para descargar la información de Metrotify ------------------------"""

    def download (self):

        """Usuarios de Metrotify"""

        url_users = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json"
        request_users = requests.get(url_users)

        with open ("users.text", "w") as users_data:
            users_data.write(request_users.text)
       

        """Albumes de Metrotify"""

        url_albums = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json"
        request_albums = requests.get(url_albums)

        with open ("albums.text", "w") as albums_data:
            albums_data.write(request_albums.text)


        """Playlists de Metrotify"""
        url_playlist = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/playlists.json"
        request_playlists = requests.get(url_playlist)

        with open ("playlist.text", "w") as playlists_data:
            playlists_data.write(request_playlists.text)
 

    """------------------------ Función para verificar si un nombre de usuario se encuentra disponible ------------------------"""

    def username_avaiability (self, username):
            for i in self.users:
                if username == i.username:
                    avaiable = False
                else:
                    avaiable = True
            return avaiable
    
    """------------------------ Función para verificar si un email se encuentra disponible ------------------------"""

    def email_avaiability (self, email):
            for i in self.users:
                if email == i.email:
                    avaiable = False
                else:
                    avaiable = True      
            return avaiable 
    
    """------------------------ Función para verificar si un id se encuentra disponible ------------------------"""

    def id_avaiability (self, id):
            for i in self.users:
                if id == i.id:
                    avaiable = False
                    break
                else:
                    avaiable = True
            return avaiable
    
    """------------------------ Función para generar un ID ------------------------"""
    
    def generate_id(self, users_list):
        while True:
            generated_id = uuid.uuid4
            if Functions.id_avaiability(self, generated_id, users_list) == True:
                break
            else:
                continue
        return generated_id
    
    """------------------------ Función para verificar si un email introducido es válido ------------------------"""

    def validate_email(self, email):
        count_address = 0
        count_dots = 0
        
        for i in email:
            if i == "@" or i == ".":
                count_address += 1
                count_dots += 1
                if count_address <= 1 and count_dots >= 1:
                    valid = True
                else:
                    valid = False
            else:
                continue

        return valid
                

    """------------------------ Función para verificar si un nombre de usuario se encuentra registrado ------------------------"""

    def existent_user (self, user):
        search_length = len(self.users)
        if search_length >= 0:
            for i in self.users:
                search_length -= 1
                if i.username == user:
                    msg = True
                else:
                    continue

        else:
            msg = False
        
        return msg
    

    #TODO: Revisar funcionalidad
    """------------------------ Función para registrar una cuenta de Metrotify ------------------------"""

    def register_profile (self):
        
        print ("\n------------- Registro de Usuario ------------- \n")
        user_name = input("Introduzca su nombre: ")  
        user_email = input("Introduzca el email del usuario: ") 
        user_username = input("Introduzca un nombre de usuario: ") 
        user_id = uuid.uuid4()

        if Functions.id_avaiability(self, user_id) == True:
            if Functions.email_avaiability(self, user_email) == True:
                if Functions.username_avaiability(self, user_name) == True:
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
                    

                    elif user_type == "2":
                        newUser = Listener(user_id, user_name, user_email, user_username, user_type)
                        self.users.append(newUser)
                        self.listeners.append(newUser)
                        print ("\nEl usuario se ha registrado correctamente. Puede acceder a la plataforma.\n")
                
                        
                    else:
                        print ("\nEl tipo de cuenta introducido es inválido. Solo puede ser de tipo musico o escucha\n")
                else:
                    print ("\nEl nombre de usuario que usted ha introducido ya se encuentra registrado. Por favor introduzca otro.\n")
            else:
                print ("\nEl correo electrónico que usted ha introducido ya se encuentra registrado. Por favor introduzca otro.\n")
        else:
            user_id = Functions.generate_id(self)


    """------------------------ Función para modificar la información personal de una cuenta ------------------------"""

    def modify_user (self, user_id):

        for i in self.users:
            if i.id == user_id:
                user = i
            else:
                continue

        if Functions.existent_user(self, user) == True:
            modify_attribute = input("""Atributo de la cuenta a modificar 
                                 
1. Nombre personal de la cuenta
2. Email
3. Nombre usuario
                                 
---> """)
        
            if modify_attribute == "1":
                newName = input ("Nombre nuevo: ")
                if newName.isalpha:
                    user_id.name = newName
                    print ("Cambio registrado.")
                else:
                    print ("El nombre solo puede contener carácteres alfabéticos.")

            elif modify_attribute == "2":
                newEmail = input ("Email nuevo: ")
                if Functions.email_avaiability(self, newEmail) == True:
                    if Functions.validate_email == True:
                        user_id.email = newEmail
                        print ("Cambio registrado.")
                    else:
                        print ("El correo ingresado no es válido.")
                else:
                    print ("El correo ingresado ya se encuentra registrado.")

            elif modify_attribute == "3":
                newUsername = input ("Nombre nuevo: ")
                if Functions.username_avaiability(self, newUsername) == True:
                    user_id.username = newUsername
                    print ("Cambio registrado.")
                else:
                    print ("El nombre de usuario no se encuentra disponible.")

            elif modify_attribute == "4":
                newType = input ("Tipo de cuenta: ")
                user_id.type = newType

            #TODO: Revisar funcionalidad
            elif modify_attribute == "5":
                newId = Functions.generate_id(self)
                if Functions.id_avaiability(self, newId) == True:
                    user_id.id = newId
                    print ("Un nuevo ID se ha registrado.")
                else:
                    print ("Error 2")

            else:
                print ("Opción inválida. Regresando al menu principal...")
        else:
            print ("El usuario no se encuentra registrado")



    """------------------------ Función para eliminarla la información de una cuenta ------------------------"""

    def delete_AccountData (self, account_id):

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

       
    
    """------------------------ Menu de una cuenta de escucha de Metrotify ------------------------"""

#TODO: Revisar funcionalidad
    def listener_menu(self):
        
        active_listener = input ("Nombre de usuario del usuario activo: ")

        registered_listeners = len(self.listeners)
        if registered_listeners > 0:
            for i in self.listeners:
                registered_listeners -= 1
                if i.name == active_listener:
                    listener_id = i.id

                    listener_option = input ("""Seleccione una acción
                                    
1. Acceder al buscador
2. Crear una playlist
3. Cambiar la información personal la cuenta
4. Eliminar cuenta
                                    
    ---> """)
            
                    if listener_option == "1":
                        Functions.search_menu(self, listener_id)
                    elif listener_option == "2":
                        Functions.create_playlist(self)
                    elif listener_option == "3":
                        Functions.modify_user(self, listener_id)
                    elif listener_option == "4":
                        Functions.delete_AccountData(self, listener_id)
                    else:
                        print("Acción no registrada.")
                else:
                    continue
        else:
            print ("Nombre de usuario no registrado")



    """------------------------ Menu de una cuenta de artista de Metrotify ------------------------"""

    def artist_menu(self):

        artist_option = input ("""Seleccione una acción
                               
1. Lanzar un album
2. Cambiar la información personal la cuenta
3. Eliminar cuenta
                               
---> """)
        if artist_option == "1":
            Functions.launch_album(self)
        elif artist_option == "2":
            Functions.launch_album(self)
        elif artist_option == "3":
            Functions.launch_album(self)
        else:
            print("Acción no registrada...Volviendo al Menu principal")


    def search_menu (self, active_user):

        itemToSearch = input ("""-------- Buscador --------
                              
1. Buscar canción
2. Buscar perfil                                                    
3. Buscar playlist                                                                                                              
                            
----> """)
        
        if itemToSearch == "1":
            Functions.searchBySongsOrAlbum(self, active_user)
        if itemToSearch == "2":
            Functions.searchByUser(self, active_user)
        if itemToSearch == "3":
            Functions.searchPlaylists(self, active_user)
        else:
            print ("Acción no registrada... Volviendo al menu principal")
        
    
    def searchBySongsOrAlbum (self, active_userId):
        item_name = input ("\nIntroduzca el nombre de la canción o del álbum: ")

        registered_songs = len(self.songs)
        if registered_songs >= 0:
            for i in self.songs:
                registered_songs -= 1
                if item_name == i.name:
                    print (i.read)
                    Functions.interactionsMenu(self, i.id, active_userId)
                else:
                    continue
        else:
            print("No hay canciones registradas bajo ese nombre.")

        registered_albums = len(self.albums)
        if registered_albums >= 0:
            for i in self.albums:
                registered_albums -= 1
                if item_name == i.name:
                    print (f"Nombre del álbum: {i.read}")
                    print (f"""Tracklist
{i.read_tracklist}""")
                    Functions.interactionsMenu(self, i.id, active_userId)
                else:
                    continue
        else:
            print("No hay albumes registrados bajo ese nombre.")

#TODO: Terminar función de búsqueda de artistas
            
    def searchByUser (self, active_userId):
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
                                Functions.interactionsMenu(self)
                            else:
                                pass
                            
                    elif choose_view == "2":
                        for a in i.albums:
                            print (a.read)
                else:
                    continue
                

        else:
            print("No hay canciones registradas")

#TODO: Terminar función de búsqueda de playlists
    def searchPlaylists (self, active_userId):
        pass


#TODO: Terminar función de definir top 5 de cada lista
    def top_5 (self, listToCheck):
        
        top_5_list = []
        for i in range(0, listToCheck+1):
            for j in listToCheck:
                if j.streams > [i].streams:
                    i.append
        return top_5_list

#TODO: Terminar función de crear playlist de un usuario
    def create_playlist (self, playlist_creator):
        pass

#TODO: Terminar función de lanzar album de un artista
    def launch_album (self, artist_alias, artist_id):
        pass


    def give_like (self, item_id, user_id):
    
        for i in self.liked:
            if i.item == item_id and i.user == user_id:
                print ("Ese objeto ya tiene un like")
            else:
                newLike = Like(item_id, user_id)
                self.liked.append(newLike)

                for k in self.albums:
                    if k.item == item_id:
                        k.liked.append(newLike)
                    else:
                        continue

                for j in self.songs:
                    if j.item == item_id:
                        j.liked.append(newLike)
                    else:
                        continue

                for m in self.playlists:
                    if m.item == item_id:
                        m.liked.append(newLike)
                    else:
                        continue

                for p in self.artists:
                    if p.item == item_id:
                        p.liked.append(newLike)
                    else:
                        continue



    def remove_like (self, item, user):
        
        for i in self.liked:
            if i.item == item and i.user == user:
                self.liked.remove(i)
            else:
                continue

    def interactionsMenu (self, item_id, user_id):

        action = input ("""
1. Agregar a me gusta
2. Quitar de me gusta
                        """)
            
        if action == "1":
            Functions.give_like(self, item_id, user_id)
        elif action == "2":
            Functions.remove_like(self, item_id, user_id)
        else:
            print ("Opción inválida... Regresando al menu principal")

    def choose_songArtistProfile (self):
        pass
        
