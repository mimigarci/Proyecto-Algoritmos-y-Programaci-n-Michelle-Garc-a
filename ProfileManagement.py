
from MusicManagement import MusicManagement
from Artist import Artist
from Listener import Listener
from Song import Song
from Album import Album

import datetime

class ProfileManagement (MusicManagement):
    """Clase con las funciones pertenecientes al módulo de gestión de perfiles
    """
                
#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def register_profile (self):
        """Función para registrar una cuenta de Metrotify
        """    
        users = self.users

        print ("\n------------- Registro de Usuario ------------- \n")
        user_name = input("Introduzca su nombre: ")  
        user_email = input("Introduzca el email del usuario: ") 
        user_username = input("Introduzca un nombre de usuario: ") 
        user_id = ProfileManagement.generate_id
        
        while True:
            if ProfileManagement.id_avaiability(self, user_id, users) == True:
                if ProfileManagement.email_avaiability(self, user_email) == True:
                    if ProfileManagement.validate_email(self, user_email) == True:
                        if ProfileManagement.username_avaiability(self, user_name) == True:
                            user_type = input (""" 
        Tipo de cuenta:
        1. Musico
        2. Escucha
                                            
        ---> """)
                            if user_type == "1":
                                newArtist = Artist(user_id, user_name, user_email, user_username, user_type)
                                users.append(newArtist)
                                print ("\nEl usuario se ha registrado correctamente. Puede acceder a la plataforma.\n")
                                break

                            elif user_type == "2":
                                newUser = Listener(user_id, user_name, user_email, user_username, user_type)
                                users.append(newUser)
                                print ("\nEl usuario se ha registrado correctamente. Puede acceder a la plataforma.\n")
                                break
                                
                            else:
                                print ("\nEl tipo de cuenta introducido es inválido. Solo puede ser de tipo musico o escucha\n")
                                break
                        else:
                            print ("\nEl nombre de usuario que usted ha introducido ya se encuentra registrado.\n")
                            break
                    else:
                        print ("\nEl correo electrónico que usted ha introducido ya se encuentra registrado\n")
                        break
                else:
                    print ("El correo electrónico que usted ha introducido es inválido.")
                    break
            else:
                user_id = ProfileManagement.generate_id(self, users)

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
            if ProfileManagement.existent_username(self, user.username) == True:
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
                    
    def search_profile (self):
            matched_user = []
            #TODO: Validar que acepte mayusculas y minusculas por igual
            user_username = input ("Nombre de usuario del perfil: ")

            registered_users = len(self.users)
            if registered_users > 0:
                for i in self.users:
                    registered_users -= 1
                    if user_username in i.username:
                        matched_user.append(i)
                    else:
                        continue
            else:
                print ("No hay usuarios registrados bajo ese nombre")
            
            for m in matched_user:
                for j in range(1, len(matched_user)+1):
                    if matched_user.index(m) == j-1:
                        print (F"{j}. {m.username}")
                    else:
                        continue
            
            while True:
                try:  
                    user_associated_number = int (input ("Introduzca el número asociado al usuario de interés: "))   
                    if type(user_associated_number) == int:
                        if registered_users >= 0:
                            for i in matched_user:
                                registered_users -= 1
                                if matched_user.index(i)+1 == user_associated_number:
                                    if type(i) == Artist:
                                        print (f"""   {i.username}    """)
                                        Artist.read_attribute(i)
                                        break
                                    elif type (i) == Listener:
                                        print (f"""   {i.username}    """)
                                        Listener.read_attribute(i)
                                        break
                                    else:
                                        print ("No hay usuarios de ese tipo")
                                    break
                                else:
                                    continue
                        else:
                            print ("Lista vacía")
                            break
                    else:
                        print ("lol, el error esta en wanna play song")
                        break
                    
                    break
                    
                except ValueError:
                    print ("\nDebe introducir un número válido (entero)\n")
                
    
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

    def launch_album (self, artist_id: str):
        """_summary_

        Args:
            artist_id (str): _description_
        """     
        albums_list = self.albums
        registered_artist_list = []

        for i in self.users:
            if ProfileManagement.user_type(self, i) == Artist:
                registered_artist_list.append(i)
            else:
                continue

        for a in registered_artist_list:
            if a.id == artist_id:
                album_artist = artist_id
                album_published = datetime.date.today()
                album_id = ProfileManagement.generate_id(self, albums_list)
                album_name = input ("Nombre del álbum: ")
                album_description = input ("Descripción del álbum: ")
                album_cover = input ("Link de la portada del álbum: ")
                album_genre = input ("Género musical del álbum: ")
                album_tracklist = []
                
                #TODO: Realizar validaciones necesarias
                
                songs_list = self.songs
    
                while True:
                    added_songs_quantity = int(input("Número de canciones del album: "))

                    if type(added_songs_quantity) == int:
                        for j in range(1, added_songs_quantity):
                            print (f"\n{j+1}. Track")
                            song_artist_id = artist_id
                            song_id = ProfileManagement.generate_id(self, songs_list)
                            song_name = input ("Nombre de la canción: ")
                            song_duration = input ("Duración de la canción: ")
                            song_link = input ("Link de la canción (soundcloud): ")

                            newSong = Song(song_id, song_name, song_duration, song_link, song_artist_id)
                            album_tracklist.append(newSong)
                            self.songs.append(newSong)
                            
                        newAlbum = Album(album_id, album_name, album_description, album_cover, album_published, album_genre, album_artist, album_tracklist)
                        self.albums.append(newAlbum)

                        for ar in registered_artist_list:
                            if ar.id == artist_id:
                                ar.albums.append(newAlbum)
                            else:
                                continue
                        break
                            
                    elif ValueError:
                        print ("\nIntroduzca un número entero.\n")
                    else:
                        print ("Lol no se que paso")
                        break



#-------------------------------------------------------------------------------------------------------------------------------------------------
#TODO: Continuar función de crear playlist de un usuario
    def create_playlist (self, active_user_id):
        """Args:
            id (str): ID de la playlist
            name (str): Nombre de la playlist
            description (str): Descripción de la playlist
            creator (str): Usuario que creó la playlist
            tracks (list): Canciones de la playlist
        """     
        playlists_list = self.playlists
        playlist_id = ProfileManagement.generate_id(self, playlists_list)
        playlist_name = input ("Nombre de la playlist: ")
        playlist_description = input ("Descripción de la playlist: ")
        playlist_creator = active_user_id
        playlist_tracks =[]
        
        songs_list = self.songs

        while True:
            selected_song = ""
            song_to_add_quantity = int(input("Cantidad de canciones que desea añadir: "))
        
            try:
                if song_to_add_quantity > 0:
                    for k in range (1, song_to_add_quantity):
                        song_to_add_name = input("Nombre de la canción: ")
                        if ProfileManagement.check_name_registered(self, song_to_add_name, songs_list) == False:
                            print ("No hay canciones registradas bajo ese nombre")
                        
                        else:
                            matched_songs = ProfileManagement.check_name_registered(self, song_to_add_name, songs_list)
                            for i in matched_songs:
                                print (f"{matched_songs.index(i)+1}. {i.name}")
                            
                            selected_song = ProfileManagement.select_song(self, matched_songs)
                            
                            if type(selected_song) == Song:
                                playlist_tracks.append(selected_song)
                            else:
                                print ('LOOOOL algo falló en la parte seleccionar canciones')
                else:
                    print ("\nIntroduzca un número válido (Debe ser entero)\n")
            except ValueError:
                print ("\nIntroduzca un número válido (Debe ser entero)\n")

#-------------------------------------------------------------------------------------------------------------------------------------------------

    