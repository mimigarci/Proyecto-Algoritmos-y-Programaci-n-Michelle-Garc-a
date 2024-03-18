from Clases.User import User
from Clases.Playlist import Playlist
from rich import print

class Listener(User):
    """Escucha de Metrotify. Contiene la información clave de un escucha de Metrotify.

    Args:
        User (class): Clase usuario. Contiene la información base de todos los usuarios de Metrotify.
    """    
    def __init__(self, id: str, name: str, email: str, username: str, type: str):
        super().__init__(id, name, email, username, type)
        super().read
        

        self.liked_songs = []
        self.liked_albums = []
        self.liked_playlists = []
        self.liked_artists = []
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
        while True:
            choice = input("""
    1. Ver playlists
    2. Ver canciones favoritas
    3. Ver albumes favoritos
    4. Ver musicos favoritos
    5. Ver playlists favoritas
    
    ---> """)
            if choice == "1":   #Playlists
                if len(self.playlists) > 0:
                    for i in self.playlists:
                        Playlist.read(i)

                else:
                    print ("\nEste usuario no ha creado ninguna playlist\n")

                break
                    
            elif choice == "2":   #Canciones favoritas
                if len(self.liked_songs) > 0:
                    print("\n-----------------------------")
                    for j in self.liked_songs:
                        print (f"{self.liked_songs.index(j)+1}. {j.name}")
                    
                else:
                    print ("\nEste usuario no tiene canciones favoritas\n")

                break

            elif choice == "3":   #Albums favoritos
                if len(self.liked_albums) > 0:
                    print("\n-----------------------------")
                    for k in self.liked_albums:
                        print (f"{self.liked_albums.index(k)+1}. {k.name}")
                else:
                    print ("\nEste usuario no tiene albums favoritos\n")

                break

            elif choice == "4":   #Musicos
                if len(self.liked_artists) > 0:
                    print("\n-----------------------------")
                    for k in self.liked_artists:
                        print (f"{self.liked_artists.index(k)+1}. {k.name}")
                else:
                    print ("\nEste usuario no tiene musicos favoritos\n")

                break

            elif choice == "5":   #Playlists

                if len(self.playlists) > 0:
                    print(f"\n-----------------------------")
                    for k in self.playlists: 
                        print (f"{self.playlists.index(k)+1}. {k.name}")
                else:
                    print ("\nEste usuario no tiene playlists favoritas\n")

                break

            else:
                print("\n[italic red]Opción inválida\n")
                break


