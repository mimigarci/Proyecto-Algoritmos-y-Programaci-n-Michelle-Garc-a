from User import User
from Artist import Artist
from Listener import Listener
from Album import Album
from Playlist import Playlist
from Song import Song 
from Functions import Functions
import json


"""Clase Programa: Es la encargada de abrir y gestionar todas las operaciones que se tienen que llevar a cabo para gestionar Metrotify"""

class Program(Functions):

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
        
        """ ------------------------ Función para leer toda la información dentro de las bases de datos -------------------------

        Args:
            users (list): Lista de los usuarios registrados dentro de la base de datos.
            albums (list): Lista de los álbums registrados dentro de la base de datos.
            playlists (list): Lista de las playlists registradas dentro de la base de datos.

        """ 

        """
        -------------------------------------------------------------------------------------------------------------------------------
        Esta parte de la función trabaja con la lista de usuarios de la base de datos. Es la encargada de separar toda la información 
        relevante para crear los objetos de tipo "User" (Usuarios de Metrotify). Además, los clasifica de acuerdo a su tipo. Si el tipo
        del usuario es músico, se agregará a la lista de artistas, si es escucha se agregará a la lista de escuchas. De no ser ninguno 
        de los dos, se enviará un mensaje de error dentro del sistema.
        -------------------------------------------------------------------------------------------------------------------------------
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


        """
        -------------------------------------------------------------------------------------------------------------------------------
        Esta parte de la función trabaja con la lista de albums de la base de datos. Separa toda la información relevante para crear 
        los objetos de tipo "Album" (Álbumes de Metrotify). Además, creará los objetos de tipo "Song" correspondientes antes de añadirlos 
        a la lista del álbum. Los mismos serán añadidos a la lista de canciones de Metrotify. Igualmente, se buscará al artista 
        correspondiente al álbum dentro de la base de datos y este se registrará como su intérprete.
        -------------------------------------------------------------------------------------------------------------------------------
        """       
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
                    self.songs.append(newSong)
                    tracklist.append(newSong)

                newAlbum = Album(album_id, album_name, album_description, album_cover, album_published, album_genre, album_artist, tracklist)
                self.albums.append(newAlbum)

        """
        -------------------------------------------------------------------------------------------------------------------------------
        Esta parte de la función trabaja con la lista de playlists de la base de datos. Separa toda la información relevante para crear 
        los objetos de tipo "Playlist" (Playlists de Metrotify).
        -------------------------------------------------------------------------------------------------------------------------------
        """    
        with open('playlist.text','r') as playlists_file:
            playlists = json.load(playlists_file)
            for i in playlists:

                playlist_id = i["id"]
                playlist_name = i["name"]
                playlist_description = i["description"]
                playlist_creator = i["creator"]
                playlist_tracks = i["tracks"]
                
                """En la lista playlist_tracks se registra el ID de las canciones correspondientes a la lista de reproducción. Para registrar 
                las canciones correspondientes, se verificará si el id de la canción coincide con alguno que se encuentre registrado dentro 
                de la lista de canciones de Metrotify. En caso de coincidir, se agregará a la lista de canciones de la playlist, si no coincide 
                no se agregará nada a la lista de canciones.
                """            
                tracks = []
                for id_song in playlist_tracks:
                    for song in self.songs:
                        if id_song == song.id:
                            tracks.append(song)
                        else:
                            continue

                newPlaylist = Playlist(playlist_id, playlist_name, playlist_description, playlist_creator, tracks)
                self.playlists.append(newPlaylist)


    def manage_profile (self):
        """ ------------------------ Menu definido para gestionar un perfil de un usuario  ------------------------- """ 
        option = input ("""
¿Cómo desea acceder al programa?
                            
1. Registrar perfil nuevo
2. Buscar un perfil
3. Cambiar la información personal de una cuenta
4. Borrar los datos de una cuenta
5. Regresar
                                                    
---> """)
        
        if option == "1":
            Program.register_profile(self)
      
        elif option == "2":
            search = input("Introduzca el nombre del usuario (username): ")

            if Program.existent_user(self, search) == True:
                for i in self.users:
                    if i.username == search:
                        print (i.name)
                        i.read_attribute
                    else:
                        continue
            else:
                print ("")

        elif option == "3":
            modify_user = ("Nombre de usuario de la cuenta que desea modificar: ")

            if Program.existent_user(self, modify_user) == True:
                for i in self.users:
                    if i.username == search:
                        i.read
                        Program.modify_user(self, modify_user)
                    else:
                        continue
            else:
                print ("")

        elif option == "4":
            eraseAccountData = input("Introduzca el ID de la cuenta a la que desea resetear")
            if Program.existent_user(self, eraseAccountData) == True:
                for i in self.users:
                    if i.username == search:
                        i.read
                        Program.delete_AccountData(self, eraseAccountData)
                    else:
                        continue
            else:
                print ("ID no registrado. No es posible acceder a la información")

        elif option == "5":
            Program.menu()
        else:
            print ("Opción inválida")

        

    def manage_music(self):
        option = input ("""
¿Cómo desea acceder al programa?
                            
1. Escucha
2. Musico
3. Regresar
                                                       
---> """)
        
        if option =="1":
            Functions.listener_menu()
        elif option =="2":
            Functions.artist_menu()
        elif option =="3":
            Program.menu()
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


    def menu(self):
        while True:
            print ("Bienvenido a Metrotify!")

            choice = input("""
Seleccione una acción a realizar:                

1. Gestionar Perfil                                             
2. Gestionar Musica                                                                                   
3. Ver Indicadores                                              
4. Salir                                           

---> """)
            
            if choice == "1":
                Program.manage_profile(self)
            elif choice == "2":
                Program.manage_music(self)
            elif choice == "3":
                Program.indicators(self)
            elif choice == "4":
                break
            else:
                print ("Opción inválida")