from ProfileManagement import ProfileManagement
from MusicManagement import MusicManagement
from InteractionManagement import InteractionManagement
from Indicators import Indicators
from Artist import Artist
from Listener import Listener
from Album import Album
from Playlist import Playlist
from Song import Song 
from rich import print
import requests
import json
import os

 
class Program(ProfileManagement, MusicManagement, InteractionManagement, Indicators):
    """_suEs la encargada de abrir y gestionar todas las operaciones que se tienen que llevar a cabo para gestionar la aplicaciónmmary_

    Args:
        ProfileManagement (class): Módulo de Gestión de Perfiles
        MusicManagement (class): Módulo de Gestión Musical
        InteractionManagement (class): Módulo de Gestión de Interacciones
        Indicators (class): Indicadores
    """     
    def __init__(self):
        """Constructor de la clase Programa:

            self.songs: Lista con todas las canciones registradas en Metrotify.
            self.users: Lista de todos los usuarios registrados en Metrotify.
            self.artists: Lista con todos los usuarios de tipo "músico".
            self.listeners: Lista con todos los usuarios de tipo "escucha".
            self.albums: Lista con todas los álbums registrados dentro de Metrotify.
            self.playlists: Lista con todas las listas de reproducción dentro de Metrotify.
        """   

        self.songs = []
        self.users =  []
        self.artists = []
        self.listeners = []
        self.albums = []
        self.playlists = []
        self.likes = []


#-------------------------------------------------------------------------------------------------------------------------------------------------            
                    
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

        #TODO: Condicional para verificar si se descargaron los datos correctamente
        
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
    
# -------------------------------------------------------------------------------------------------------------------------------

    def open_database (self): 
        """Función para leer toda la información dentro de las bases de datos

        Args:
            users (list): Lista de los usuarios registrados dentro de la base de datos.
            albums (list): Lista de los álbums registrados dentro de la base de datos.
            playlists (list): Lista de las playlists registradas dentro de la base de datos.

        """ 

        with open('users.text','r') as users_file:
            users = json.load(users_file)
            for i in users: 
                user_id = i["id"]
                user_name = i["name"]
                user_email = i["email"]
                user_username = i["username"]
                
                if i["type"] == "musician":
                    user_type = "musician"

                    newUser = Artist(user_id, user_name, user_email, user_username, user_type)
                    self.users.append(newUser)
                    self.artists.append(newUser)

                elif i["type"] == "listener":
                    user_type = "listener"

                    newUser = Listener(user_id, user_name, user_email, user_username, user_type)
                    self.users.append(newUser)
                    self.listeners.append(newUser)
                
                else:
                    print ("Tipo de cuenta no registrado.")

     
        with open('albums.text','r') as albums_file:
            albums = json.load(albums_file)
            for i in albums:
                album_id = i["id"]
                album_name = i["name"]
                album_description = i["description"]
                album_cover = i["cover"]
                album_published = i["published"]
                album_genre = i["genre"]
                album_artist = i["artist"]

                album_tracklist = i["tracklist"]
                tracklist = []
                for j in album_tracklist:
                    song_id = j["id"]
                    song_name = j["name"]
                    song_duration = j["duration"]
                    song_link = j["link"]

                    newSong = Song(song_id, song_name, song_duration, song_link, album_artist)
                    tracklist.append(newSong)
                    self.songs.append(newSong)
                    
                newAlbum = Album(album_id, album_name, album_description, album_cover, album_published, album_genre, album_artist, tracklist)
                self.albums.append(newAlbum)


        with open('playlist.text','r') as playlists_file:
            playlists = json.load(playlists_file)
            for i in playlists:

                playlist_id = i["id"]
                playlist_name = i["name"]
                playlist_description = i["description"]
                playlist_creator = i["creator"]
                playlist_tracks = i["tracks"]     
                tracks = []

                for id_song in playlist_tracks:
                    for song in self.songs:
                        if id_song == song.id:
                            tracks.append(song)
                        else:
                            continue

                newPlaylist = Playlist(playlist_id, playlist_name, playlist_description, playlist_creator, tracks)
                self.playlists.append(newPlaylist)

#-------------------------------------------------------------------------------------------------------------------------------------------------
#TODO: Crear y guardar base de datos 
    def save_database(self):
        pass

#------------------------------------------------------------------------------------------------------------------------------------------------- 

    def manage_music(self):
        """Funcion para manejar el Módulo de Gestión Musical
        """        
        while True:
            option = input ("""
    ¿Cómo desea acceder al programa?
                                
    1. Escucha
    2. Musico
    3. Regresar
                                                        
    ---> """)
            
            if option =="1":
                Program.listener_menu(self)
                break
            elif option =="2":
                Program.artist_menu(self)
                break
            elif option =="3":
                Program.menu(self)
                break
            else:
                print ("Opción inválida")

#-------------------------------------------------------------------------------------------------------------------------------------------------

    #TODO:  Hacer gráficos (matplotlib o bokeh)
    def indicators (self):
        registered_songs = self.songs
        registered_albums = self.albums
        registered_artists = self.artists
        registered_listener_streams = self.listeners

        while True:
        
            option = input ("""
    ¿Qué desea ver?
                                
    1. Top 5 canciones más escuchadas
    2. Top 5 álbumes más escuchados
    3. Top 5 músicos más escuchados
    4. Top 5 escuchas que más han utilizado la plataforma
    5. Ver gráficas
    6. Regresar
                                                        
    ---> """)
            

            if option =="1":
                top_5_songs = Program.set_top_5(self, registered_songs)
                Program.read_top_5(self, top_5_songs)
                break

            elif option =="2":
                top_5_albums =Program.read_top_5(self, registered_albums)
                Program.read_top_5(self, top_5_albums)
                break

            elif option =="3":
                top_5_artists = Program.read_top_5(self, registered_artists)
                Program.read_top_5(self, top_5_artists)
                break

            elif option =="4":
                top_5_listeners = Program.read_top_5(self, registered_listener_streams)
                Program.read_top_5(self, top_5_listeners)
                break

            elif option =="5":

                pass

            elif option =="6":
                break

            else:
                print ("Opción inválida")

#-------------------------------------------------------------------------------------------------------------------------------------------------

    def listener_menu(self):
        os.system('cls')

        active_listener = input ("Nombre de usuario del escucha activo (username): ")

        registered_listeners = len(self.listeners)
        if Program.existent_username(self, active_listener) == True:
            for i in self.users:
                registered_listeners -= 1
                if i.username == active_listener:
                    listener_id = i.id

                    while True:
                        listener_option = input ("""Seleccione una acción
                                        
    1. Acceder al buscador
    2. Crear una playlist
    3. Cambiar la información personal de la cuenta
    4. Eliminar cuenta
    5. Regresar
                                        
        ---> """)
                        if listener_option == "1":
                            Program.search_menu(self, listener_id)

                        elif listener_option == "2":
                            Program.create_playlist(self, listener_id)

                        elif listener_option == "3":
                            Program.modify_user(self, listener_id)

                        elif listener_option == "4":
                            Program.delete_account_data(self, listener_id)

                        elif listener_option == "5":
                            Program.menu(self)
                            break

                        else:
                            print("\nOpción inválida. Introduzca una opción válida por favor.\n")
                else:
                    continue
        else:
            print ("...El nombre de usuario no se encuentra registrado. Introduzca un nombre de usuario válido")
    

#-------------------------------------------------------------------------------------------------------------------------------------------------
            
    def artist_menu(self):
        os.system('cls')

        active_artist = input ("Nombre de usuario del musico activo (username): ")

        registered_artists = len(self.artists)
        if registered_artists >= 0:
            for i in self.users:
                registered_artists -= 1
                if i.username == active_artist:
                    artist_id = i.id
                    while True:
                        artist_option = input ("""Seleccione una acción
                                
    1. Lanzar un album
    2. Cambiar la información personal la cuenta
    3. Eliminar cuenta
    4. Regresar
                                
    ---> """)
            
                        if artist_option == "1":
                            Program.launch_album(self, artist_id)
                            break
                        elif artist_option == "2":
                            Program.modify_user(self, artist_id)
                            break
                        elif artist_option == "3":
                            Program.delete_account_data(self, artist_id)
                            break
                            
                        elif artist_option == "4":
                            break
                        else:
                            print("\nOpción inválida\n")
                else:
                    continue
            else:
                print ("...El nombre de usuario no se encuentra registrado. Introduzca un nombre de usuario válido")
        else:
            print ("...El nombre de usuario no se encuentra registrado. Introduzca un nombre de usuario válido")
            
#-------------------------------------------------------------------------------------------------------------------------------------------------   

    def menu(self):
        while True:
            choice = input("""
Seleccione una acción a realizar:                

0. Cargar base de datos                            
1. Iniciar sesión                                                                                                                              
2. Registrar un nuevo usuario                                                                                                                              
3. Ver Indicadores                                              
4. Salir                                           

---> """)
            
            if choice == "0":
                Program.download_database(self)
                Program.open_database(self)
                os.system('cls')

            elif choice == "1":
                Program.manage_music(self)
            
            elif choice == "2":
                Program.register_profile(self)
                
            elif choice == "3":
                Program.indicators(self)

            elif choice == "4":
                print ("\nCerrando programa...")
                break
            else:
                print ("\nOpción inválida\n")

#-------------------------------------------------------------------------------------------------------------------------------------------------
    def start_program(self):
            print ("\nInicializando programa...")
            print ("""
                    Bienvenido a Metrotify!""")
            Program.menu(self)