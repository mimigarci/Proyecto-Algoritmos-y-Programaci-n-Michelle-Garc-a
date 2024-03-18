from Clases.User import User
from Modules.Tools import Tools
from rich import print


 
class Artist(User):
    """Músico de Metrotify. Contiene la información clave de un músico de Metrotify.

    Args:
        User (class): Clase usuario. Contiene la información base de todos los usuarios de Metrotify.
    """   
    
    def __init__(self, id: str, name: str, email: str, username: str, type: str):
        super().__init__(id, name, email, username, type)
        super().read

        self.albums = []
        self.top_10 = []
        self.streams = 0
        self.songs = []
        
        """Constructor de la clase Artist:

            self.albums: Lista de los álbumes del artista.
            self.top_10: Lista con el top_10 de canciones más escuchadas del artista.
            self.reproductions: Cantidad de veces que se ha reproducido este artista.
            self.songs: Lista de canciones que interpreta el artista.
        """               


    def read_attribute (self):
        """Función para leer los albums, canciones y reproducción de un músico.

        Returns:
            str: Información del artista
        """  
        choice = input("""
1. Ver albums
2. Ver top 10 canciones más escuchadas del artista
3. Cantidad de streams totales

---> """)
        
        if choice == "1":
            if len(self.albums) > 0:
                for i in self.albums:
                    print (f"{self.albums.index(i)+1}. {i.name}")
            else:
                print ("Este usuario no tiene álbumes registrados")

        elif choice == "2": 
            registered_songs = self.songs

            top_10 = Tools.set_top(self,registered_songs, 10)
            if type(top_10) == None:
               print ("Este usuario no tiene canciones registradas")
            else:
                Tools.read_top(self, top_10)
                

        elif choice == "3": 
            print(f" >> {self.streams} <<")
        else:
            print ("Invalid")

    

