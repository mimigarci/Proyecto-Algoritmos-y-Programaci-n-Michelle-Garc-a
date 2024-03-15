from Functions import Functions
from Artist import Artist
import os
class MusicManagement (Functions):
    """Clase con las funciones pertenecientes al módulo de gestión de perfiles
    """    

#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def search_menu (self, active_user):
        while True:
            itemToSearch = input ("""-------- Buscador de canciones --------
                                
    1. Buscar por nombre de canción
    2. Buscar por album
    3. Buscar por perfil del artista                                                    
    4. Buscar playlist                                                                                                              
    5. Regresar                                                                                                              
                                
    ----> """)
            
            if itemToSearch == "1":
                MusicManagement.search_songs(self, active_user)
                break

            if itemToSearch == "2":  
                MusicManagement.search_albums(self, active_user)
                break

            elif itemToSearch == "3":
                MusicManagement.search_by_artist(self, active_user)
                break

            elif itemToSearch == "4":
                MusicManagement.search_playlists(self, active_user)
                break

            elif itemToSearch == "5":
                #TODO: Función para buscar perfil de un escucha
                break

            elif itemToSearch == "5":
                print("Regresando...")
                os.system('cls')
                break
            else:
                print ("\nOpción inválida\n")
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
                
    def search_songs (self, active_user):
        song_name = input ("\nIntroduzca el nombre de la canción: ")
        song_self_list = self.songs

        if MusicManagement.check_name_registered(self, song_name, song_self_list) == False:
            print ("No hay canciones registradas bajo ese nombre")
        else:
            matched_songs = MusicManagement.check_name_registered(self, song_name, song_self_list) 
            for i in matched_songs:
                print (f"{matched_songs.index(i)+1}. {i.name}")
        
            MusicManagement.wanna_play_song(self, matched_songs, active_user)

#-------------------------------------------------------------------------------------------------------------------------------------------------

    def search_albums(self, active_user_id):
        album_name = input("\nIntroduzca el nombre del album: ")
        album_self_list = self.albums

        if MusicManagement.check_name_registered(self, album_name, album_self_list) == False:
            print ("No hay albumes registradas bajo ese nombre")
        else:
            matched_albums = MusicManagement.check_name_registered(self, album_name, album_self_list) 
            for i in matched_albums:
                print (f"{matched_albums.index(i)+1}. {i.name}")
        
            MusicManagement.read_to_play_tracklist(self, matched_albums, active_user_id)


#-------------------------------------------------------------------------------------------------------------------------------------------------
            
    def read_to_play_tracklist(self, item_list, active_user_id):
        item_index = int(input("Introduzca el número del álbum que desea reproducir: "))

        if item_index == int:
            for i in item_list:
                if item_list.index(i) == item_index:
                    item_tracklist = i.tracklist
                else:
                    continue

            for j in item_tracklist:
                print (f"{item_tracklist.index(j)+1}. {j.name}")
            
            MusicManagement.wanna_play_song(self, active_user_id)

        elif ValueError:
            print ("Introduzca el número correspondiente a la canción que desea reproducir (entero).")
        else:
            print ('Lol, no se que paso aqui')


#-------------------------------------------------------------------------------------------------------------------------------------------------

            
    def search_by_artist (self, active_user_id):
        artist_username = input("Nombre de usuario del artista: ")
        matched_artists = []
        artist_songs = []
        registered_artists_list = []

        for i in self.users:
            if MusicManagement.user_type(self, i) == Artist:
                registered_artists_list.append(i)
            else:
                continue

        registered_artists_len = len(registered_artists_list)
        if registered_artists_list >= 0:
            for i in registered_artists_list:
                registered_artists_len -= 1
                if artist_username in i.username:
                    matched_artists.append(i)
                else:
                    continue

            if len(matched_artists) > 0:
                for j in matched_artists:
                    print (f"{matched_artists.index(j)+1}. {j.username}")

                artist = MusicManagement.select_artist_from_list(self, matched_artists)
                print (Artist.read(artist))

                if type(artist) == False:
                    print ("No se encuentra en la lista lol")
                else:
                    while True:
                        choose_view = input ("""
                1. Ver canciones del músico
                2. Ver albumes del músico
                3. Regresar
                    
                ---> """)
                        if choose_view == "1":   
                            for a in artist.albums:
                                for s in a:
                                    artist_songs.append(s)
                            
                            for k in artist_songs:
                                print (f"{artist_songs.index(k)}. {k.name}")
                            
                            if len(artist_songs) > 0:
                                MusicManagement.wanna_play_song(self, active_user_id, artist_songs)
                            else:
                                print ("Este músico no tiene ningún lanzamiento")
                                    
                        elif choose_view == "2":
                            if len(artist.albums) > 0:

                                for a in artist.albums:
                                    print (f"{artist.albums.index(a)+1}. {a.name}")
                                
                                MusicManagement.read_to_play_tracklist(self, artist.albums, active_user_id)
                            else:
                                print ("Este músico no tiene lanzamientos")

                        elif choose_view == "3":
                            break

                        else:
                            print ("\nOpcion invalida\n")
            
        else:
            print ("No hay usuarios registrados")

        

#-------------------------------------------------------------------------------------------------------------------------------------------------

    def select_artist_from_list (self, artist_list):
        artist_number = int(input ("\nIntroduzca el número correspondiente al artista deseado: "))

        registered_artists_len = len(artist_list)
        if registered_artists_len > 0:
            for i in artist_list:
                registered_artists_len -= 1
                if artist_list.index(i)+1 == artist_number:
                    artist = i
                    return artist
                else:
                    continue
        else:
            return False
    

#-------------------------------------------------------------------------------------------------------------------------------------------------

    def search_playlists (self, active_user_id):
        
        playlist_name = input ("Introduzca el nombre de la playlist")
        playlist_creator = input ("Introduzca el nombre de usuario del creador de la playlist: ")
        matching_playlists = []

        for u in self.users:
            if u.username == playlist_creator:
                p_creator_id = u.id
            else:
                continue
        
        registered_playlists = len(self.playlists)
        if registered_playlists >= 0:
            for j in self.playlists:
                registered_playlists -= 1
                if playlist_name in j.name and p_creator_id == j.creator:
                    matching_playlists.append(j)
                else:
                    continue
        else:
            print ("No hay playlists registradas bajo esas credenciales")

        if len(matching_playlists) > 0:
            print ("------------- Playlists encontradas -------------")
            for k in matching_playlists:
                print (f"{matching_playlists.index(k)+1}. {k.name}")
        else:
            print ("No hay playlists registradas bajo esas credenciales")

        MusicManagement.read_to_play_tracklist(self, matching_playlists, active_user_id)

#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def wanna_play_song(self, active_userId, matched_songs):

        while True:
            MusicManagement.select_song(self, matched_songs)

            select = input ("""
        Desea escuchar una canción de la lista?
                                                
        1. Si
        2. No
        3. Regresar
                                                
        --->""")
                                
            if select == "1":
                chosen_song = MusicManagement.select_song(self, matched_songs)
                chosen_song.play_song(self, active_userId)

            elif select == "2":
                
                print (chosen_song.read)
                break
            elif select == "3":
                print ("\nRegresando...")
                break
            else:
                print ("\nOpción inválida.\n")


#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def select_song(self, matched_items_list):
        """Función para seleccionar una canción dentro de un menu a través de un número asociado.

        Args:
            matched_items_list (list): Lista de las canciones dentro del menu

        Returns:
            object : Canción correspondiente al número
        """   
        while True:
            song_number = int (input ("Introduzca el número de la canción: "))    
            registered_items = len(matched_items_list)
            object
            if song_number == int:
                if registered_items >= 0:
                    for i in matched_items_list:
                        registered_items -= 1
                        if matched_items_list.index(i)+1 == song_number:
                            object = i
                            print (object.read)
                            break
                        else:
                            continue
                else:
                    print ("Lista vacía")
            elif ValueError:
                print ("Debe introducir un número válido (entero)")

            else:
                print ("lol, el error esta en wanna play song")
                break
            
            return object
    
