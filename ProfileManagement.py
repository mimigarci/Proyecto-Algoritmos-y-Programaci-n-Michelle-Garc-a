
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
                if ProfileManagement.email_avaiability(self, user_email) and ProfileManagement.validate_email(self, user_email) == True:
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
                        print ("\nEl nombre de usuario que usted ha introducido ya se encuentra registrado. Por favor introduzca otro.\n")
                        break
                else:
                    print ("\nEl correo electrónico que usted ha introducido ya se encuentra registrado. Por favor introduzca otro.\n")
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
                    
    def search_profile (self, active_user_id):
            matched_user = []
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
                    print (F"{j}. {m.name}")

            return (matched_user, active_user_id)
    
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

        for i in registered_artist_list:
            if i.id == artist_id:
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
                added_songs_number = int(input("Número de canciones del album: "))

                while True:
                    if type(added_songs_number) == int:
                        for i in range(0, added_songs_number):
                            print (f"\n{i+1}. Track")
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


                        for i in registered_artist_list:
                            if i.id == artist_id:
                                i.albums.append(newAlbum)
                            else:
                                continue

                        break
                            
                    elif ValueError:
                        print ("Introduzca un número entero.")
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
        
        
        #Como podría añadir los elementos a la playlist??
        # if len(playlist_tracks) == 0:
        #     choose = input ("Des")

        #     song_name = input ("\nIntroduzca el nombre de la canción a agregar a la playlist: ")
        #     song_self_list = self.songs

        #     if MusicManagement.check_name_registered(self, song_name, song_self_list) == False:
        #         print ("No hay canciones registradas bajo ese nombre")
        #     else:
        #         matched_songs = MusicManagement.check_name_registered(self, song_name, song_self_list) 

        #     for i in matched_songs:
        #         print (f"{matched_songs.index(i)+1}. {i.name}")

        #     song_to_add = MusicManagement.select_song(self, matched_songs)

        #     if song_to_add == object:
        #         playlist_tracks.append(song_to_add)

        

