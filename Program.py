from Modules.ProfileManagement import ProfileManagement
from Clases.Artist import Artist
from Clases.Listener import Listener
from Clases.Album import Album
from Clases.Playlist import Playlist
from Clases.Song import Song 
from rich import print
import requests
import json
import os
import pickle
import sys

 
class Program(ProfileManagement):
    """Es la encargada de abrir y gestionar todas las operaciones que se tienen que llevar a cabo para gestionar la aplicación.
    Hereda de las clases del Módulo de Gestión de Perfiles y de Tools.

    Args:
        ProfileManagement (class): Clase con las funciones pertinentse al módulo de Gestión de Perfiles.
    """    

    def __init__(self):
        """Constructor de la clase Programa. Contiene todas las listas donde se almacena la información.
        
        self.songs = Lista de objetos de tipo cancion.
        self.users = Lista de objetos de tipo usuario.
        self.albums = Lista de objetos de tipo album.
        self.playlists = Lista de objetos de tipo playlist.
        self.liked = Lista de likes registrados en la plataforma.
        
        """        
        self.songs = []
        self.users =  []
        self.albums = []
        self.playlists = []
        self.liked = []


#-------------------------------------------------------------------------------------------------------------------------------------------------            
                    
    def download_API (self):
        """Función para descargar la información de la API y guardarlas dentro de un archivo txt. Por cada link existe un archivo diferente.
        """        
        
        #Try and except para verificar la conexión a internet.
        try:
            #Descarga de usuarios de la API
            url_users = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json"
            request_users = requests.get(url_users)

            with open ("Api/users.text", "w") as users_data:
                users_data.write(request_users.text)
            

            #Descarga de albumes de la API
            url_albums = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json"
            request_albums = requests.get(url_albums)

            with open ("Api/albums.text", "w") as albums_data:
                albums_data.write(request_albums.text)


            #Descarga de playlists de la API
            url_playlist = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/playlists.json"
            request_playlists = requests.get(url_playlist)

            with open ("Api/playlist.text", "w") as playlists_data:
                playlists_data.write(request_playlists.text)

            print ("[italic magenta]----- Base de datos descargada correctamente ----")

        except:
            print("[italic magenta] No se pudo descargar la API. Compruebe su conexión a internet.")

    
# -------------------------------------------------------------------------------------------------------------------------------

    def open_API (self): 
        """Función para crear objetos a partir de la API.
        """ 

        #Crear usuarios a partir de la información de la API.
        with open('Api/users.text','r') as users_file:
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

                elif i["type"] == "listener":
                    user_type = "listener"
                    newUser = Listener(user_id, user_name, user_email, user_username, user_type)
                    self.users.append(newUser)
                
                else:
                    print ("[italic yellow]...Tipo de cuenta no registrado")

        #Crear albumes a partir de la información de la API.
        with open('Api/albums.text','r') as albums_file:
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

                    #Crear canciones a partir de los álbumes de la API.
                    newSong = Song(song_id, song_name, song_duration, song_link, album_artist)
                    tracklist.append(newSong)
                    self.songs.append(newSong)

                    for u in self.users:
                        if u.id == album_artist:
                            u.songs.append(newSong)
                    else:
                        continue 

                newAlbum = Album(album_id, album_name, album_description, album_cover, album_published, album_genre, album_artist, tracklist)
                self.albums.append(newAlbum)
            
                for u in self.users:
                    if u.id == album_artist:
                        u.albums.append(newAlbum)
                    else:
                        continue 

        #Crear playlists a partir de la información de la API.
        with open('Api/playlist.text','r') as playlists_file:
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

                for u in self.users:
                    if u.id == playlist_creator:
                        u.playlists.append(newPlaylist)
                    else:
                        continue 

#-------------------------------------------------------------------------------------------------------------------------------------------------

    def write_data(self):  
        """Función para guardar la información del programa.
        """    

        data_to_save = [self.users, self.songs, self.albums, self.playlists]
        file_pickle = 'Db/Data.pickle'

        with open(file_pickle, 'wb') as k:
            pickle.dump(data_to_save, k)

        print ("[italic green]=== Guardado finalizado ===")

#-------------------------------------------------------------------------------------------------------------------------------------------------
        
    def get_info_from_data (self):
        """Función para obtener la información actual del programa.
        """        
        file_name = 'Db/Data.pickle'
        try:
            with open(file_name, "rb") as m:
                
                info_from_data_txt = pickle.load(m)
                
                self.users= info_from_data_txt[0] 
                self.songs= info_from_data_txt[1] 
                self.albums= info_from_data_txt[2] 
                self.playlists= info_from_data_txt[3]

                print(f'\n [italic magenta]Datos cargados correctamente')   
        except:
            print ('[italic red] ERROR ---- No hay información para guardar')         

#------------------------------------------------------------------------------------------------------------------------------------------------- 

    def manage_music(self):
        """Funcion para llamar al módulo de gestión musical. Permite el inicio de sesión de los usuarios según su tipo de usuario.
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
                print ("[italic red]Opción inválida")

#-------------------------------------------------------------------------------------------------------------------------------------------------

    def indicators (self):
        """Menu para ver los indicadores del programa. Muestra los top 5 de cada objeto junto a sus gráficos.
        """        
        registered_songs = self.songs
        registered_albums = self.albums
        registered_artists = []
        registered_listeners = []


        registered_users = len(self.users)
        if registered_users >= 0:
            for i in self.users:
                registered_users -= 1
                if type(i) == Artist:
                    registered_artists.append(i)
                elif type(i) == Listener:
                    registered_listeners.append(i)
                else:
                    continue
        else:
            print ("[italic yellow] --- No hay usuarios registrados ---")


        while True:
        
            option = input ("""
    ¿Qué desea ver?
                                
    1. Top 5 canciones más escuchadas
    2. Top 5 álbumes más escuchados
    3. Top 5 músicos más escuchados
    4. Top 5 escuchas que más han utilizado la plataforma
    5. Regresar
                                                        
    ---> """)
            

            if option =="1":
                top_5_songs = Program.set_top(self, registered_songs, 5)
                Program.read_top(self, top_5_songs)
                Program.top_bar_plots(self, top_5_songs)

            elif option =="2":
                top_5_albums =Program.set_top(self, registered_albums, 5)
                Program.read_top(self, top_5_albums)
                Program.top_bar_plots(self, top_5_albums)

            elif option =="3":
                top_5_artists = Program.set_top(self, registered_artists, 5)
                Program.read_top(self, top_5_artists)
                Program.top_bar_plots(self, top_5_artists)

            elif option =="4":
                top_5_listeners = Program.set_top(self, registered_listeners, 5)
                Program.read_top(self, top_5_listeners)
                Program.top_bar_plots(self, top_5_listeners)

            elif option =="5":
                break

            else:
                print ("[italic red]...Opción inválida")

#-------------------------------------------------------------------------------------------------------------------------------------------------

    def listener_menu(self):
        """Menu de los escuhas de Metrotify. Se activa si el usuario activo es de tipo escucha. Muestra las opciones pertinentes a los
        escuchas.
        """        
        os.system('cls')

        active_listener = input ("Nombre de usuario del escucha activo (username): ")
        registered_listeners = []
        listener_id = ""

        for i in self.users:
            if type(i) == Listener:
                registered_listeners.append(i)
            else:
                continue

        if Program.existent_username(self, active_listener) == True:
            for i in registered_listeners:
                if i.username == active_listener:
                    listener_id = i.id

                    print (f"\n[italic green]--- Hola, {i.name} ...has iniciado sesión ---\n")
                    while True:
                        print ("\n[italic magenta]---------- Acciones ---------- ")
                        listener_option = input ("""                            
    1. Buscar una canción
    2. Buscar un perfil
    3. Crear una playlist
    4. Cambiar la información personal de la cuenta
    5. Eliminar cuenta
    6. Regresar
                                        
        ---> """)
                        if listener_option == "1":
                            Program.song_search_menu(self, listener_id)

                        elif listener_option == "2":
                            Program.search_profile(self)

                        elif listener_option == "3":
                            Program.create_playlist(self, listener_id)

                        elif listener_option == "4":
                            Program.modify_user(self, listener_id)

                        elif listener_option == "5":
                            Program.delete_account_data(self, listener_id)

                        elif listener_option == "6":
                            Program.menu(self)
                            break

                        else:
                            print("\n[italic red]Opción inválida. Introduzca una opción válida por favor.\n")
                else:
                    continue
        else:
            print ("\n[italic red]...El nombre de usuario no se encuentra registrado. Introduzca un nombre de usuario válido")

#-------------------------------------------------------------------------------------------------------------------------------------------------
            
    def artist_menu(self):
        """Menu de los músicos de Metrotify. Se activa si el usuario activo es de tipo músico. Muestra las opciones pertinentes a los
        músicos.
        """        
        os.system('cls')

        active_artist = input ("Nombre de usuario del musico activo (username): ")
        registered_artists = []

        for i in self.users:
            if type(i) == Artist:
                registered_artists.append(i)
            else:
                continue

        if Program.existent_username(self, active_artist) == True:
            for i in registered_artists:
                if i.username == active_artist:
                    artist_id = i.id
                    print ("\n[italic green]--- Sesión iniciada correctamente ---\n")
                    while True:
                        print ("\n[italic magenta]---------- Acciones ---------- ")
                        artist_option = input ("""                                                                 
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
                            print("\n[italic red]Opción inválida. Introduzca una opción válida por favor.\n")
                else:
                    continue
        else:
            print ("\n[italic red]...El nombre de usuario no se encuentra registrado. Introduzca un nombre de usuario válido")
            
#-------------------------------------------------------------------------------------------------------------------------------------------------   

    def menu(self):
        """Menu principal de Metrotify. Posee las acciones principales para gestionar el programa.
        """   

        while True:
            Program.banner(self)
            print ("\n[italic magenta]---------- Acciones ---------- ")
            choice = input("""              
0. Cargar API                          
1. Cargar data de la aplicación                          
2. Registrar un usuario nuevo                                                                                                                             
3. Iniciar sesión                                                                                                                               
4. Ver Indicadores                                              
5. Guardar y salir                                                                          

---> """)
            
            if choice == "0":
                Program.download_API(self)
                Program.open_API(self)
                os.system('cls')

            elif choice == "1":
                Program.get_info_from_data(self)
                
            elif choice == "2":
                print ("\n[italic magenta] ...Accediendo a interfaz\n")
                Program.register_profile(self)
    
            elif choice == "3":
                print ("\n[italic magenta] ...Accediendo a interfaz\n")
                Program.manage_music(self)
                
            elif choice == "4":
                print ("\n[italic magenta] ...Accediendo a interfaz\n")
                Program.indicators(self)

            elif choice == "5":
                Program.write_data(self)
                print ("\n[italic magenta]Cerrando programa...")
                sys.exit()
 
            else:
                print ("\n[italic red]Opción inválida\n")
                os.system('cls')

#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def start_program(self):
        """Función para darle inicio al programa
        """            
        print ("\n[italic magenta]Inicializando programa...")
        print ("""
[bold white]🎵 Bienvenido a 🎵""")
        Program.menu(self)


