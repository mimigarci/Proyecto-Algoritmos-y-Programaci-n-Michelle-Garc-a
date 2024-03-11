from User import User
from Artist import Artist
from Listener import Listener
from Album import Album
from Playlist import Playlist
from Song import Song 
from Like import Like
import uuid
import requests
import os
 
class Functions:
    """Funciones pertenecientes al programa Metrotify
    """    
    
    # def correct_path (self, file):
    #     actual_rep = os.getcwd()
    #     actual_rep = dirname(__file__)
    #     corrected_dir = join(actual_rep, 'Database', file)

    #     return corrected_dir

    
    def download_database (self):

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

        #Condicional para verificar si se descargaron los datos correctamente
        
        # files_list = os.listdir()
        # downloaded_files = 0
        # for i in files_list:
        #     if i == "albums.text" or i == "playlist.text" or i == "users.text":
        #         downloaded_files += 1
        #         if downloaded_files == 3:
        #             print ("---- Base de datos cargada correctamente ----")
        #         else:
        #             print ("Hubo un error al cargar la base de datos. Compruebe su conexión a internet.")
                


        return print ("----- Base de datos descargada correctamente ----")
 

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
                    return False
                    
                else:
                    return True
            
    
    """------------------------ Función para generar un ID ------------------------"""
    
    def generate_id(self):
        generated_id = uuid.uuid4
        while Functions.id_avaiability(self, generated_id) == False:
            generated_id = uuid.uuid4
            if Functions.id_avaiability(self, generated_id) == True:
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
                if count_address == 1 and count_dots >= 1:
                    return True
                else:
                    return False
            else:
                continue
  

    """------------------------ Función para verificar si un nombre de usuario se encuentra registrado ------------------------"""

    def existent_user (self, user):
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

    

    #TODO: Revisar funcionalidad
    """------------------------ Función para registrar una cuenta de Metrotify ------------------------"""

    def register_profile (self):
        print ("\n------------- Registro de Usuario ------------- \n")
        user_name = input("Introduzca su nombre: ")  
        user_email = input("Introduzca el email del usuario: ") 
        user_username = input("Introduzca un nombre de usuario: ") 
        user_id = uuid.uuid4()
        
        while True:

            if Functions.id_avaiability(self, user_id) == True:
                if Functions.email_avaiability(self, user_email) and Functions.validate_email(self, user_email) == True:
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
                user_id = Functions.generate_id(self)


    """------------------------ Función para modificar la información personal de una cuenta ------------------------"""

    def modify_user (self, user_id):

        for i in self.users:
            if i.id == user_id:
                user = i
            else:
                continue
        
        while True:
            if Functions.existent_user(self, user.username) == True:
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
                    if Functions.email_avaiability(self, newEmail) == True:
                        if Functions.validate_email == True:
                            user.email = newEmail
                            print ("\n----- Cambio registrado -----\n")
                        else:
                            print ("El correo ingresado no es válido.")
                    else:
                        print ("El correo ingresado ya se encuentra registrado.")

                elif modify_attribute == "3":
                    newUsername = input ("Nombre nuevo: ")
                    if Functions.username_avaiability(self, newUsername) == True:
                        user.username = newUsername
                        print ("Cambio registrado.")
                    else:
                        print ("El nombre de usuario no se encuentra disponible.")

                # elif modify_attribute == "4":
                #     newType = input ("""Tipo de cuenta: 
                #     1. Escucha
                #     2. Musico 
                    
                #     ---> """)
                #     user.type = newType

                # #TODO: Revisar funcionalidad
                # elif modify_attribute == "5":
                #     newId = Functions.generate_id(self)
                #     if Functions.id_avaiability(self, newId) == True:
                #         user.id = newId
                #         print ("Un nuevo ID se ha registrado.")
                #     else:
                #         print ("Error 2")

                elif modify_attribute == "4":
                    break
                else:
                    print ("\nOpción inválida. Introduzca una opción válida por favor.\n")
            else:
                print ("El usuario no se encuentra registrado")
                break



    """------------------------ Función para eliminarla la información de una cuenta ------------------------"""

    def delete_account_data (self, account_id):

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

       


    def search_menu (self, active_user):
        while True:
            itemToSearch = input ("""-------- Buscador --------
                                
    1. Buscar canción
    2. Buscar album
    3. Buscar perfil                                                    
    4. Buscar playlist                                                                                                              
    5. Regresar                                                                                                              
                                
    ----> """)
            
            if itemToSearch == "1":
                Functions.search_songs(self, active_user)
                break

            if itemToSearch == "2":  
                Functions.search_songs(self, active_user)
                break

            elif itemToSearch == "3":
                Functions.search_users(self, active_user)
                break

            elif itemToSearch == "4":
                Functions.search_playlists(self, active_user)
                break

            elif itemToSearch == "5":
                break
            else:
                print ("\nOpción inválida\n")
        
    #TODO: Terminar función de búsqueda

    def search_songs (self, active_user):
        item_name = input ("\nIntroduzca el nombre de la canción: ")

        registered_songs = len(self.songs)
        matched_items = []
        if registered_songs >= 0:
            for i in self.songs:
                registered_songs -= 1
                if item_name in i.name:
                    matched_items.append(i)
                else:
                    continue
        else:
            print("No hay canciones registradas bajo ese nombre")

        registered_items = len(matched_items)
        if registered_items > 0:
            registered_items -= 1
            for i in matched_items:
                print (f"{matched_items.index(i)+1}. {i.name}")
        else:
            print ("No hay canciones registradas")

        choice = input ("Desea reproducir una canción? (Y/N)")
        if choice == "Y":
            Functions.choose(self, matched_items)
        elif choice == "N":
            print ("")
        else:
            print ("...Opción inválida")

    def choose (self, matched_items, active_user):
        chosen = int(input ("Número de la canción a reproducir:"))
        if chosen == int:
            for i in matched_items:
                if matched_items.index(i) == chosen-1:
                    Song.song_menu(i)
                else:
                    continue

        elif ValueError:
            print ("Introduzca un número dentro de la lista")

        
#TODO: Temrinar funcion de busqueda por albums
    def search_albums (self):
        item_name = input ("\nIntroduzca el nombre de la canción o del álbum: ")
        registered_albums = len(self.albums)
        if registered_albums >= 0:
            for i in self.albums:
                registered_albums -= 1
                for p in range(1, len(i.tracklist)):

                    if item_name in i.name:
                        print (f"""Nombre del álbum: {i.name}
    Tracklist:
                               
    {p} {i.read_tracklist}
""")
                    else:
                        continue
        else:
            print("No hay albumes registrados bajo ese nombre.")

#TODO: Terminar función de búsqueda de artistas
            
    def search_users (self):
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

#TODO: Terminar función de búsqueda de playlists
    def search_playlists (self, active_userId):
        pass


#TODO: Terminar función de definir top 5 de cada lista
    def top_5 (self, listToCheck):
        
        top_5_list = []
        for i in range(0, listToCheck+1):
            for j in listToCheck:
                if j.streams > [i].streams:
                    top_5_list.append()
        return top_5_list

#TODO: Terminar función de crear playlist de un usuario
    def create_playlist (self, creator_id):
        for i in self.users:
            if i.d == creator_id:
                pass

#TODO: Terminar función de lanzar album de un artista
    def launch_album (self, artist_id):
        for i in self.artists:
            if i.id == artist_id:
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
    
    def choose_song(self):
        pass
