from User import User
from Song import Song
from Playlist import Playlist
from Album import Album

""" Clase Listener: Escuchas de Metrotify. """

class Listener(User):

    def __init__(self, id: str, name: str, email: str, username: str, type: str):
        super().__init__(id, name, email, username, type)
        super().read

        self.favorite_songs = []
        self.favorite_albums = []
        self.playlists = []
        self.streams = 0

        """Constructor de la clase Listener, escuchas de Metrotify:

            self.favorite_songs: Canciones favoritas del escucha.
            self.favorite_albums: Albums favoritos del escucha.
            self.playlists: Playlists creadas por el escucha.
            self.streams: Cantidad de veces que el usuario ha reproducido una canción.

        """

    
    def read_attribute (self):
        
        """Función para leer las canciones, albums y playlist de un escucha de Metrotify

        Returns:
            string: Información del escucha
        """  
        choice = input("""
1. Ver playlists creados
2. Ver canciones favoritas
3. Ver albumes favoritos
""")
        if choice == "1":   #Playlists
            for i in self.playlists:
                msg = f"{Playlist.read(i)}"
                
        elif choice == "2":   #Canciones favoritas
            for j in self.favorite_songs:
                msg = f"{Song.read(j)}"

        elif choice == "3":   #Albums favoritos
            for k in self.favorite_albums:
                msg = f"{Album.read(k)}"
        else:
            msg = "Invalid"
        return msg

