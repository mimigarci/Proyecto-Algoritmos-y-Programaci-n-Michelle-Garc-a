from User import User
from Artist import Artist
from Listener import Listener
from Album import Album
from Playlist import Playlist
from Song import Song 
from Functions import Functions
from rich import print
import json
import os

 


class Program(Functions):
    """Es la encargada de abrir y gestionar todas las operaciones que se tienen que llevar a cabo para gestionar Metrotify

    Args:
        Functions (_type_): Clase con todas las funciones a utilizar del programa
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
        

     

    def open_database (self): 
        """Función para leer toda la información dentro de las bases de datos

        Args:
            users (list): Lista de los usuarios registrados dentro de la base de datos.
            albums (list): Lista de los álbums registrados dentro de la base de datos.
            playlists (list): Lista de las playlists registradas dentro de la base de datos.

        """ 

# -------------------------------------------------------------------------------------------------------------------------------
# Esta parte de la función trabaja con la lista de usuarios de la base de datos. Es la encargada de separar toda la información 
# relevante para crear los objetos de tipo "User" (Usuarios de Metrotify). Además, los clasifica de acuerdo a su tipo. Si el tipo
# del usuario es músico, se agregará a la lista de artistas, si es escucha se agregará a la lista de escuchas. De no ser ninguno 
# de los dos, se enviará un mensaje de error dentro del sistema.
# -------------------------------------------------------------------------------------------------------------------------------
              

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


# -------------------------------------------------------------------------------------------------------------------------------
# Esta parte de la función trabaja con la lista de albums de la base de datos. Separa toda la información relevante para crear 
# los objetos de tipo "Album" (Álbumes de Metrotify). Además, creará los objetos de tipo "Song" correspondientes antes de añadirlos 
# a la lista del álbum. Los mismos serán añadidos a la lista de canciones de Metrotify. Igualmente, se buscará al artista 
# correspondiente al álbum dentro de la base de datos y este se registrará como su intérprete.
# -------------------------------------------------------------------------------------------------------------------------------
     
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

# -------------------------------------------------------------------------------------------------------------------------------
# Esta parte de la función trabaja con la lista de playlists de la base de datos. Separa toda la información relevante para crear 
# los objetos de tipo "Playlist" (Playlists de Metrotify).
# -------------------------------------------------------------------------------------------------------------------------------
  
        with open('playlist.text','r') as playlists_file:
            playlists = json.load(playlists_file)
            for i in playlists:

                playlist_id = i["id"]
                playlist_name = i["name"]
                playlist_description = i["description"]
                playlist_creator = i["creator"]
                playlist_tracks = i["tracks"]

# -------------------------------------------------------------------------------------------------------------------------------                
# En la lista playlist_tracks se registra el ID de las canciones correspondientes a la lista de reproducción. Para registrar 
# las canciones correspondientes, se verificará si el id de la canción coincide con alguno que se encuentre registrado dentro 
# de la lista de canciones de Metrotify. En caso de coincidir, se agregará a la lista de canciones de la playlist, si no coincide 
# no se agregará nada a la lista de canciones.  
# -------------------------------------------------------------------------------------------------------------------------------
                         
                tracks = []
                for id_song in playlist_tracks:
                    for song in self.songs:
                        if id_song == song.id:
                            tracks.append(song)
                        else:
                            continue

                newPlaylist = Playlist(playlist_id, playlist_name, playlist_description, playlist_creator, tracks)
                self.playlists.append(newPlaylist)


#TODO: Crear y guardar base de datos 
    def save_database(self):
        pass
        

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



    def indicators (self):
        #TODO:  Hacer gráficos (matplotlib o bokeh)
        
        option = input ("""
¿Qué desea ver?
                            
1. Top 5 canciones más escuchadas
2. Top 5 álbumes más escuchados
3. Top 5 artistas más escuchados
4. Top 5 escuchas más escuchados
5. Regresar
                                                       
---> """)
        
        top_5_songs = []
        top_5_artists = []
        top_5_playlists = []
        top_5_listeners = []

        if option =="1":
            for i in top_5_songs:
                print(i.read)

        elif option =="2":
            for i in top_5_artists:
                print(i.read)

        elif option =="3":
            for i in top_5_playlists:
                print(i.read)

        elif option =="4":
            for i in top_5_listeners:
                print(i.read)

        elif option =="5":
            Program.menu()

        else:
            print ("Opción inválida")
    
    #TODO: Revisar funcionalidad
    def listener_menu(self):
        os.system('cls')

        active_listener = input ("Nombre de usuario del escucha activo (username): ")

        
        registered_listeners = len(self.listeners)
        if registered_listeners > 0:
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
                            break

                        elif listener_option == "2":
                            Program.create_playlist(self, listener_id)
                            break

                        elif listener_option == "3":
                            Program.modify_user(self, listener_id)
                            break

                        elif listener_option == "4":
                            Program.delete_account_data(self, listener_id)
                            break

                        elif listener_option == "5":
                            Program.menu(self)
                            break

                        else:
                            print("\nOpción inválida. Introduzca una opción válida por favor.\n")
                else:
                    continue
            else:
                print ("...El nombre de usuario no se encuentra registrado. Introduzca un nombre de usuario válido\n")
        else:
            print ("...El nombre de usuario no se encuentra registrado. Introduzca un nombre de usuario válido")
    


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

    def start_program(self):
            print ("\nInicializando programa...")
            print ("""
                    Bienvenido a Metrotify!""")
            Program.menu(self)