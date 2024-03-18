from Clases.Artist import Artist
from Modules.InteractionManagement import InteractionManagement
from Clases.Song import Song
from Clases.Playlist import Playlist
from Clases.Album import Album
from rich import print
import os
class MusicManagement (InteractionManagement):
    """Clase con las funciones pertenecientes al módulo de gestión de perfiles
    """    
 
#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def song_search_menu (self, active_user_id):
        """Buscador de canciones.

        Args:
            active_user_id (str): ID del usuario activo.
        """  

        while True:
            itemToSearch = input ("""\n-------- Buscador de canciones --------
                                
    1. Buscar por nombre de canción
    2. Buscar por album
    3. Buscar por perfil del artista                                                    
    4. Buscar playlist                                                                                                              
    5. Regresar                                                                                                              
                                
    ----> """)
            
            if itemToSearch == "1":
                MusicManagement.search_songs(self, active_user_id)
                break

            if itemToSearch == "2":  
                MusicManagement.search_albums(self, active_user_id)
                break

            elif itemToSearch == "3":
                MusicManagement.search_by_artist(self, active_user_id)
                break

            elif itemToSearch == "4":
                MusicManagement.search_playlists(self, active_user_id)
                break

            elif itemToSearch == "5":
                break
            else:
                print ("\n[italic red]...Opción inválida. Introduzca un número perteneciente al menu.\n")
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
                
    def search_songs (self, active_user_id):
        """Buscador de canciones por nombre.

        Args:
            active_user_id (str): ID del usuario activo.
        """       

        song_name = input ("\nIntroduzca el nombre de la canción: ")
        song_self_list = self.songs

        if MusicManagement.check_name_registered(self, song_name, song_self_list) == False:
            print ("\nNo hay canciones registradas bajo ese nombre\n")
        else:
            matched_songs = MusicManagement.check_name_registered(self, song_name, song_self_list) 
            if len(matched_songs) > 0:
                for i in matched_songs:
                    print (f"{matched_songs.index(i)+1}. {i.name}")
                
                found = MusicManagement.select_item(self, matched_songs)
                if found == None:
                    print ("\n[italic red]Debe introducir un número asociado a la lista.\n")
                else:
                    MusicManagement.song_menu(self, active_user_id, found)
            else:
                print ("\n[italic blue]No hay canciones registradas bajo esas credenciales\n")

#-------------------------------------------------------------------------------------------------------------------------------------------------

    def search_albums(self, active_user_id):
        """Buscador de canciones por album.

        Args:
            active_user_id (str): ID del usuario activo.
        """  
        album_name = input("\nIntroduzca el nombre del album: ").lower()
        album_self_list = self.albums

        if MusicManagement.check_name_registered(self, album_name, album_self_list) == False:
            print ("\n[italic red]No hay albumes registrados bajo esas credenciales.")
        else:
            matched_albums = MusicManagement.check_name_registered(self, album_name, album_self_list) 
            if len(matched_albums) > 0:
                for i in matched_albums:
                    print (f"{matched_albums.index(i)+1}. {i.name}")
            
                MusicManagement.album_and_playlist_menu(self, matched_albums, active_user_id)
            else:
                print ("\n[italic red]No hay albumes registrados bajo esas credenciales.")
            

#-------------------------------------------------------------------------------------------------------------------------------------------------

    def album_and_playlist_menu(self, item_list, active_user_id):
        """Función para acceder al menu de un álbum o una playlist
        
        Args:
            item_list (list): lista de álbumes o playlists. 
            active_user_id (list): ID del usuario que inició sesión/se encuentra activo.
        """    

        item_index = input("\nIntroduzca el número asociado: ")
        item_tracklist = ''
        item = ''
        try: 
            item_index = int(item_index)
            if type(item_index) == int:
                if item_index in range(0, len(item_list)) or item_index == len(item_index):
                    while True:
                        for i in item_list:
                            if item_list.index(i)+1 == item_index:
                                item = i
                                item.read

                                if type(item) == Playlist or type(item) == Album:
                                    item_tracklist = item.tracklist
                                else:
                                    print ("Objeto de tipo no registrado")
                            else:
                                continue
                        
                        choice = input("""
        1. Gestionar me gusta
        2. Reproducir una canción
        3. Regresar

            ---> """)
                    
                        if choice == "1":
                            MusicManagement.interactions_menu(self, item, active_user_id)

                        elif choice == "2":
                            for j in item_tracklist:
                                print (f"{item_tracklist.index(j)+1}. {j.name}")
                            
                            found = MusicManagement.select_item(self, item_tracklist)
                            if found == None:
                                print ("\n[italic red]Debe introducir un número asociado a la lista.\n")
                            else:
                                MusicManagement.song_menu(self, active_user_id, found)
                            
                        elif choice == "3":
                            break
                        else:
                            print ("\n[italic red]Opción inválida")
                else:
                    print ("\n[italic red]Debe introducir un número asociado a la lista.")
        except ValueError:
            print ("\n[italic red]Debe introducir un número asociado a la lista (entero).")
            

#-------------------------------------------------------------------------------------------------------------------------------------------------
            
    def search_by_artist (self, active_user_id):
        """Buscador de canciones por artista.

        Args:
            active_user_id (str): ID del usuario activo.
        """  
        artist_username = input("\n Nombre de usuario del artista: ").lower()
        matched_artists = []
        artist_songs = []
        registered_artists_list = []
        registered_albums = []

        for i in self.users:
            if type(i) == Artist:
                registered_artists_list.append(i)
            else:
                continue

        registered_artists_len = len(registered_artists_list)
        if registered_artists_len >= 0:
            for i in registered_artists_list:
                registered_artists_len -= 1
                if artist_username in (i.username).lower():
                    matched_artists.append(i)
                else:
                    continue

            if len(matched_artists) > 0:
                artist = MusicManagement.select_user_from_list(self, matched_artists)
                print (f"\n[italic magenta]   {artist.username}    ")

                if type(artist) == False:
                    print ("[italic blue]\nNo se encuentra en la lista.\n")
                else:
                    while True:
                        choose_view = input ("""
        1. Ver canciones del músico
        2. Ver albumes del músico
        3. Gestionar me gusta
        4. Regresar
                    
                ---> """)
                        if choose_view == "1":   
            
                            for a in artist.albums:
                                for s in a.tracklist:
                                    artist_songs.append(s)
                            
                            if len(artist_songs) > 0:
                                for k in artist_songs:
                                    print (f"{artist_songs.index(k)+1}. {k.name}")
                                
                                    found = MusicManagement.select_item(self, artist_songs)
                                    if found == None:
                                        print ("\n[italic red]Debe introducir un número asociado a la lista.\n")
                                    else:
                                        MusicManagement.song_menu(self,active_user_id, found)

                            else:
                                print ("Este músico no tiene ningún lanzamiento")
                                    
                        elif choose_view == "2":
                            registered_albums = artist.albums

                            if len(registered_albums) > 0:
                                for a in registered_albums:
                                    print ("")
                                    print (f"{registered_albums.index(a)+1}. {a.name}")
                                
                                MusicManagement.album_and_playlist_menu(self, registered_albums, active_user_id)
                            else:
                                print ("Este músico no tiene lanzamientos")

                        elif choose_view == "3":
                            artist_id = artist.id
                            liked_items = self.liked
                            MusicManagement.add_like(self, artist_id, active_user_id, liked_items) 

                        elif choose_view == "4":
                            break

                        else:
                            print ("\n[italic red]Opcion invalida\n")
            else:
                 print ("\n[italic red]No hay musicos registrados bajo esas credenciales.\n")
        else:
            print ("\n[italic red]No hay usuarios registrados\n")    

#-------------------------------------------------------------------------------------------------------------------------------------------------

    def select_user_from_list (self, user_list):
        """Función para seleccionar un usuario de una lista donde se encuentre registrado.

        Args:
            user_list (list): Lista de usuarios.
        """  
        for j in user_list:
            print (f"{user_list.index(j)+1}. {j.username}")

        user_number = int(input ("\nIntroduzca el número correspondiente al artista deseado: "))

        registered_artists_len = len(user_list)
        if registered_artists_len > 0:
            for i in user_list:
                registered_artists_len -= 1
                if user_list.index(i)+1 == user_number:
                    artist = i
                    return artist
                else:
                    continue
        else:
            return False
    

#-------------------------------------------------------------------------------------------------------------------------------------------------

    def search_playlists (self, active_user_id):
        """Buscador de canciones por playlist.

        Args:
            active_user_id (str): ID del usuario activo.
        """ 
        
        playlist_name = input ("\nIntroduzca el nombre de la playlist: ")
        matching_playlists = []

        registered_playlists = len(self.playlists)
        if registered_playlists >= 0:
            for j in self.playlists:
                registered_playlists -= 1
                if playlist_name in j.name:
                    matching_playlists.append(j)
                else:
                    continue
        else:
            print ("\n[italic blue]No hay playlists registradas bajo esas credenciales\n")

        if len(matching_playlists) > 0:
            print ("\n[bold white]------------- Playlists encontradas -------------\n")
            for k in matching_playlists:
                print (f"{matching_playlists.index(k)+1}. {k.name}")
            
            MusicManagement.album_and_playlist_menu(self, matching_playlists, active_user_id)

        else:
            print ("\n[italic red] No hay playlists registradas bajo esas credenciales\n")

#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def song_menu(self, active_user_id, chosen_song):
        """Menu de una canción. Permite reproducirla, ver sus datos o gestionar sus me gusta. 

        Args:
            active_user_id (str): ID del usuario activo.
            chosen_song(object): Objeto de tipo canción. Es la canción que se va a gestionar.
        """ 

        while True:
            select = input ("""
        Desea escuchar la canción?
                                                
        1. Si
        2. Solo ver datos
        3. Gestionar me gusta
        4. Regresar
                                                
        ---> """)
                                
            if select == "1":
                users = self.users
                albums = self.albums
                songs = self.songs
                Song.play_song(chosen_song, active_user_id, users, albums, songs)

            elif select == "2":
                print(Song.read(chosen_song))
                break
            elif select == "3":
                MusicManagement.interactions_menu(self, chosen_song, active_user_id)
                break
            elif select == "4":
                print ("\nRegresando...")
                break
            else:
                print ("\n[italic red]Opción inválida.\n")


#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def select_item(self, matched_items_list):
        """Función para seleccionar un elemento dentro de un menu a través de un número asociado.

        Args:
            matched_items_list (list): Lista de las canciones dentro del menu

        Returns:
            object : Canción correspondiente al número
            None: 
        """   
        object = ''

        while True:
            song_number = input ("\nIntroduzca el número del objeto deseado en la lista: ")  
            registered_items = len(matched_items_list)

            try:
                song_number = int(song_number)
                if type(song_number) == int:
                    if song_number in range(0, registered_items) or song_number == registered_items:
                        if registered_items >= 0:
                            for i in matched_items_list:
                                registered_items -= 1
                                if matched_items_list.index(i)+1 == song_number:
                                    object = i
                                    return object
                                else:
                                    continue
                        else:
                            print ("\n[italic blue]No hay usuarios registrados\n")
                    else:
                        return None    
                else:
                    return None
                
            except ValueError:
                return None

    
