
""" Clase Song: Canciones de Metrotify. """

class Song:

    def __init__(self, id: str, name: str, duration: str, link: str, artistId):
        
        self.id = id
        self.name = name
        self.duration = duration
        self.link = link
        self.artistId = artistId
        self.streams = 0
        self.liked = []

        """Constructor de la clase Song:

            self.id: ID de la canción
            self.name: Nombre de la canción
            self.duration: Duración de la canción
            self.link: Link de la canción
            self.liked: Lista de usuarios que le dieron me gusta a la canción.
        """ 


    def read(self):
        """Función para leer los atributos de la clase Song

        Returns:
            str: Atributos de la clase función
        """        
        return f"""
ID: {self.id}
Nombre: {self.id}
Duración: {self.id}
Link: {self.id}
"""

#TODO: Terminar reproductor de canciones
    def play_song(self):
        pass
    