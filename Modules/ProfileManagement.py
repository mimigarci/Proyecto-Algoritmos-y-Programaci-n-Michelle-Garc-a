
from Modules.MusicManagement import MusicManagement
from Clases.Playlist import Playlist
from Clases.Artist import Artist
from Clases.Listener import Listener
from Clases.Song import Song
from Clases.Album import Album
from rich import print
import datetime

class ProfileManagement (MusicManagement):
    """Clase con las funciones pertenecientes al módulo de gestión de perfiles
    """
                
#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def register_profile (self):
        """Función para registrar una cuenta de Metrotify
        """  
        print ("\n[italic magenta]------------- Registro de Usuario ------------- \n")  
        users = self.users
        user_name = input("Introduzca su nombre: ")  
        user_email = input("Introduzca el email del usuario: ") 
        user_username = input("Introduzca un nombre de usuario: ") 
        user_id = ProfileManagement.generate_id(self, users)
        
        if ProfileManagement.validate_lenght(self, user_name) == True:
            if ProfileManagement.id_avaiability(self, user_id, users) == False:
                user_id = ProfileManagement.generate_id(self, users)                
            else: 
                if ProfileManagement.validate_email(self, user_email) == True:
                    if ProfileManagement.email_avaiability(self, user_email)  == True:
                        if ProfileManagement.username_avaiability(self, user_name) == True:
                            while True:
                                user_type = input (""" 
            Tipo de cuenta:
            1. Musico
            2. Escucha
                                                
            ---> """)
                                if user_type == "1":
                                    newArtist = Artist(user_id, user_name, user_email, user_username, user_type)
                                    users.append(newArtist)
                                    print ("\n[italic green]El usuario se ha registrado correctamente. Puede acceder a la plataforma.\n")
                                    break

                                elif user_type == "2":
                                    newUser = Listener(user_id, user_name, user_email, user_username, user_type)
                                    users.append(newUser)
                                    print ("\n[italic green]El usuario se ha registrado correctamente. Puede acceder a la plataforma.\n")
                                    break
                                    
                                else:
                                    print ("\n[italic red]El tipo de cuenta introducido es inválido. Solo puede ser de tipo musico o escucha\n")
                                    break
                        
                        else:
                            print ("\n[italic yellow]El correo electrónico introducido ya se encuentra registrado\n")
                            
                            
                    else:
                        print ("\n[italic red]El nombre de usuario introducido ya se encuentra registrado.\n")
                        
                        
                else:
                    print ("\n[italic red]El correo electrónico introducido es inválido.")
        else:
            print ("\n[italic red]Nombre de usuario inválido. Recuerde que el nombre de usuario tiene un máximo de 30 caracteres.")
            
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
                print ("\n[bold magenta]----- Configuración de la cuenta -----")
                modify_attribute = input("""                                                
    1. Cambiar nombre personal de la cuenta
    2. Actualizar email
    3. Cambiar nombre de usuario
    4. Regresar
                                    
    ---> """)
            
                if modify_attribute == "1":
                    newName = input ("Nombre nuevo: ")
                    if ProfileManagement.validate_lenght(self, newName) == True:
                        if ProfileManagement.validate_alphabetic(self, newName) == True:
                            user.name = newName
                            print ("\n[italic green]----- Cambio registrado -----\n")                                
                        else:
                            print ("\n[italic red]El nombre solo puede contener carácteres alfabéticos.\n")
                    else:
                        print ("\n[italic yellow]Nombre inválido. Solo se aceptan nombres con un máximo de 30 caracteres.\n")

                elif modify_attribute == "2":
                    newEmail = input ("Email nuevo: ")
                    if ProfileManagement.email_avaiability(self, newEmail) == True:
                        if ProfileManagement.validate_email == True:
                            user.email = newEmail
                            print ("\n[italic green]----- Cambio registrado -----\n")
                        else:
                            print ("\n[italic red]El correo ingresado no es válido.\n")
                    else:
                        print ("\n[italic red]El correo ingresado ya se encuentra registrado.\n")

                elif modify_attribute == "3":
                    newUsername = input ("Nombre nuevo: ")
                    if ProfileManagement.username_avaiability(self, newUsername) == True:
                        user.username = newUsername
                        print ("\n[italic green]----- Cambio registrado -----")
                    else:
                        print ("\n[italic red]El nombre de usuario no se encuentra disponible.\n")

                elif modify_attribute == "4":
                    break
                else:
                    print ("\n[italic red]Opción inválida. Introduzca una opción válida por favor.\n")
            else:
                print ("[italic red]...El usuario no se encuentra registrado")
                break
#-------------------------------------------------------------------------------------------------------------------------------------------------
                    
    def search_profile (self):
            matched_user = []
            user_name = input ("\nNombre del usuario: ").lower()
            users = self.users
            registered_users = len(users)
            if registered_users > 0:
                for i in users:
                    registered_users -= 1
                    if user_name in (i.name).lower() or user_name == i.name:
                        matched_user.append(i)
                    else:
                        continue

                matched_user_len = len(matched_user)
                if matched_user_len > 0:
                    for i in matched_user:
                        print (f"{matched_user.index(i)+1}. {i.name} // {i.username}")
                    while True:
                        user_associated_number = input ("\nIntroduzca el número asociado al usuario de interés: ")   
                        try:
                            user_associated_number = int(user_associated_number)  
                            if type(user_associated_number) == int:
                                if user_associated_number in range(1, matched_user_len) or user_associated_number == matched_user_len:
                                    if matched_user_len >= 0:
                                        for i in matched_user:
                                            matched_user_len -= 1
                                            if matched_user.index(i)+1 == user_associated_number:
                                                if type(i) == Artist:
                                                    print (f"""\n[italic magenta]   {i.username}    """)
                                                    Artist.read_attribute(i)
                                                    break
                                                elif type (i) == Listener:
                                                    print (f"""\n[italic magenta]   {i.username}    """)
                                                    Listener.read_attribute(i)
                                                    break
                                                else:
                                                    print ("\n[italic red]No hay registrados bajo esas credenciales.\n")
                                                break
                                            else:
                                                continue
                                    else:
                                        print ("\n[italic red]No hay registrados bajo esas credenciales.\n")
                                        break
                                else:
                                    print ("\n[italic red]Debe introducir un número que se encuentre dentro de la lista.\n")
                            else:
                                print ("\n[italic red]Debe introducir un número que se encuentre dentro de la lista. (entero)\n")
                            break
                        except ValueError:
                            print ("\n[italic red]Debe introducir caracter válido.\n")     
                else:
                    print ("\n[italic red]No hay registrados bajo esas credenciales.\n")
            
#-------------------------------------------------------------------------------------------------------------------------------------------------

    def delete_account_data (self, account_id):
        """Función para eliminarla la información de una cuenta.

        Args:
            account_id (): ID de la cuenta a eliminar.
        """        
        albums = self.albums
        users = self.users 
        playlists = self.playlists 
        songs = self.songs
        
        existent_users = len(users)
        if existent_users > 0:
            for u in users:
                existent_users -= 1
                if u.id == account_id:
                    if type(u) == Artist:
                        for a in albums:
                            album_artist = a.artist
                            if album_artist == account_id:
                                album_tracklist = a.tracklist
                                for s in album_tracklist:
                                    song_id = s.id
                                    for i in playlists:
                                        playlist_track = i.tracklist
                                        for g in playlist_track:
                                            if song_id == g.id:
                                                if g in playlist_track:                            
                                                    playlist_track.remove(s)
                                                if g in songs:
                                                    songs.remove(s)
                                                else:
                                                    continue
                                            else:
                                                continue
                                self.albums.remove(a)
                            else:
                                continue

                            if u in users:                             
                                self.users.remove(u)
                                print ("[italic green]...La cuenta se ha eliminado correctamente.")
                                break
                            else:
                                print ("[italic red]El usuario no existe dentro del programa")
                                break

                    elif type(u) == Listener:
                        for p in playlists:
                            if p.creator == account_id:
                                self.playlists.remove(p)
                            else:
                                continue
                        self.users.remove(u)  
                        print ("[italic red]La cuenta se ha eliminado correctamente.")     
                        break         
                    else:
                        continue
                else:
                    continue
        else:
            print ("[italic red]No hay usuarios registrados.")

#-------------------------------------------------------------------------------------------------------------------------------------------------

    def launch_album (self, artist_id: str):
        """Función para crear el álbum de un artista de Metrotify.

        Args:
            artist_id (str): ID del artista que creará el álbum.
        """     
        albums_list = self.albums
        registered_artist_list = []

        for i in self.users:
            if type(i) == Artist:
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
                   
                songs_list = self.songs
    
                while True:
                    added_songs_quantity = input("Número de canciones del album: ")

                    try:
                        added_songs_quantity = int(added_songs_quantity)
                        if type(added_songs_quantity) == int:
                            for j in range(0, added_songs_quantity):
                                print (f"\n{j+1}. Track")
                                song_artist_id = artist_id
                                song_id = ProfileManagement.generate_id(self, songs_list)
                                song_name = input ("Nombre de la canción: ")
                                song_duration = input ("Duración de la canción: ")
                                song_link = input ("Link de la canción (soundcloud): ")
                            
                                if ProfileManagement.validate_link(self, song_link) == True:
                                    newSong = Song(song_id, song_name, song_duration, song_link, song_artist_id)
                                    album_tracklist.append(newSong)
                                    self.songs.append(newSong)
                                else:
                                    print (print ("\n[italic red]No se pudo registrar la canción. El link es inválido.\n"))
                            
                            if ProfileManagement.validate_link(self, album_cover) == True:
                                if ProfileManagement.validate_lenght(self, song_name) == True:
                                    newAlbum = Album(album_id, album_name, album_description, album_cover, album_published, album_genre, album_artist, album_tracklist)
                                    self.albums.append(newAlbum)
                                    print ("\n[italic green]El álbum se ha registrado correctemente.\n")
                                else:
                                    print (print ("\n[italic red]...No se pudo registrar el album.\n"))
                            else:
                                print ("\n[italic red]No se pudo obtener la portada del álbum. El link introducido es inválido.\n")

                            for ar in registered_artist_list:
                                if ar.id == artist_id:
                                    ar.albums.append(newAlbum)
                                else:
                                    continue
                            break
                        else:
                            print ("\n[italic red]Debe introducir un número entero.\n")
                            
                    except ValueError:
                        print ("\n[italic red]Debe introducir un número entero.\n")
                    



#-------------------------------------------------------------------------------------------------------------------------------------------------

    def create_playlist (self, active_user_id):
        """Función para crear un objeto de tipo playlist.

        Args:
            active_user_id (str): ID del usuario activo.
        """          

        playlists_list = self.playlists
        playlist_id = ProfileManagement.generate_id(self, playlists_list)
        playlist_name = input ("\nNombre de la playlist: ")
        playlist_description = input ("Descripción de la playlist: ")
        playlist_creator = active_user_id
        playlist_tracks =[]
        
        songs_list = self.songs
        song_to_add_quantity = input("Cantidad de canciones que desea añadir: ")
        selected_song = ""

      
        try:
            song_to_add_quantity = int(song_to_add_quantity)
            if type(song_to_add_quantity) == int:
                while song_to_add_quantity > 0:
                    song_to_add_name = input("\nNombre de la canción: ")
                    if ProfileManagement.check_name_registered(self, song_to_add_name, songs_list) == False:
                        print ("\n[italic blue] No hay canciones registradas bajo esas credenciales.\n")

                    else:
                        matched_songs = ProfileManagement.check_name_registered(self, song_to_add_name, songs_list)
                        if len(matched_songs) > 0:
                            for i in matched_songs:
                                print (f"{matched_songs.index(i)+1}. {i.name}")
                        
                            selected_song = ProfileManagement.select_item(self, matched_songs)
                        
                            if selected_song == None:
                                print ("\n[italic red]Debe introducir un número asociado a una canción de la lista.\n")
                            else:
                                playlist_tracks.append(selected_song)
                                song_to_add_quantity -= 1
                        else:
                            print ("\n[italic blue] No hay canciones registradas bajo esas credenciales.\n")

                if len(playlist_tracks) > 0:
                    newPlaylist = Playlist(playlist_id, playlist_name, playlist_description, playlist_creator, playlist_tracks)
                    self.playlists.append(newPlaylist)

                    for u in self.users:
                        if u.id == playlist_creator:
                            u.playlists.append(newPlaylist)
                        else:
                            continue
                else:
                    print ("\n[italic red]No se añadió ninguna canción a la playlist\n")

                print ("[italic green]...La playlist se ha creado correctamente")
            else:
                print ("\n[italic red] Debe introducir un número válido entero\n")
        except ValueError:
            print ("\n[italic red] Debe introducir un número válido entero\n")

#-------------------------------------------------------------------------------------------------------------------------------------------------

    