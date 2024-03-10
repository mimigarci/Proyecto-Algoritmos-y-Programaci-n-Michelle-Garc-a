from User import User
from Song import Song
from Playlist import Playlist
from Album import Album

""" Clase Artist: Músicos de Metrotify. """

class Artist(User):
    
    def __init__(self, id: str, name: str, email: str, username: str, type: str):
        super().__init__(id, name, email, username, type)
        super().read

        self.albums = []
        self.top_10 = []
        self.streams = 0
        self.liked = []
        self.songs = []

        """Constructor de la clase Artist:

            self.albums: Lista de los álbumes del artista.
            self.top_10: Lista con el top_10 de canciones más escuchadas del artista.
            self.reproductions: Cantidad de veces que se ha reproducido este artista.
            self.liked: Lista de usuarios que le dieron me gusta a este artista.
        """               

    """Función para leer las albums, cancions y reproducciones de un músico de Metrotify"""   

    def read_attribute (self):
        """Función para leer los datos del artista

        Returns:
            string: Información del artista
        """  

        choice = input("""
1. Ver albums
2. Ver top 10 canciones más escuchadas del artista
3. Cantidad de reproducciones totales
""")
        
        if choice == "1":   #Albums
            for i in self.albums:
                msg = f"{Album.read(i)}"
        elif choice == "2":   #Top 10 canciones
            for j in self.top_10:
                msg = f"{Song.read(j)}"
        elif choice == "3":   #Albums favoritos
            msg = f"{self.streams}"
        else:
            msg = "Invalid"
        return msg

