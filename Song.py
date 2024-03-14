
""" Clase Song: Canciones de Metrotify. """
 
class Song:

    def __init__(self, id: str, name: str, duration: str, link: str, artistId):
        """Constructor de la clase Song:

        Args:
            id (str): ID de la canción
            name (str): Nombre de la canción
            duration (str): Duración de la canción
            link (str): Link de la canción
            artistId (_type_): Id del músico que publicó la canción.
        """        

        self.id = id
        self.name = name
        self.duration = duration
        self.link = link
        self.artistId = artistId
        self.streams = 0
        self.liked = []


    def read(self):
        """Función para leer los atributos de la clase Song

        Returns:
            str: Atributos de la clase función
        """        
        return f"""
Nombre: {self.id}
Duración: {self.id}
"""


#TODO: Terminar reproductor de canciones
    def play_song(self, active_userId):
        pass
    