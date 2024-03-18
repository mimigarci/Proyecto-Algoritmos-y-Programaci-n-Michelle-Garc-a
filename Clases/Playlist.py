from rich import print


class Playlist:
    """Playlist de Metrotify.
    """    

    def __init__(self, id: str, name: str, description: str, creator: str, tracklist: list):
        """Constructor de la clase Playlist:

        Args:
            id (str): ID de la playlist
            name (str): Nombre de la playlist
            description (str): Descripción de la playlist
            creator (str): Usuario que creó la playlist
            tracks (list): Canciones de la playlist
        """        

        self.id = id
        self.name = name
        self.description = description
        self.creator = creator
        self.tracklist = tracklist

         
    def read(self):
        """Función para leer los datos de la playlist

        Returns:
            str: Información de la playlist
        """        
        print(f"""\n[bold white]-------- {self.name} --------
              
[italic white]
description: {self.description}

""")
        for i in self.tracklist:
            print (f"{self.tracklist.index(i)+1}. {i.name}")
        