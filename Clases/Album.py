from Clases.Song import Song
from Clases.User import User
from rich import print
 

class Album:
    """Clase Album: Objetos de tipo album. Guardan canciones.
    """
    
    def __init__(self, id, name, description, cover, published, genre, artist, tracklist) -> None:
        
        self.id = id
        self.name = name
        self.description = description
        self.cover = cover
        self.published = published
        self.genre = genre
        self.artist = artist
        self.tracklist = tracklist
        self.streams = 0

        """
        Constructor de la clase Album:
            
            id: ID del álbum
            name: Nombre del álbum
            description: Descripción del álbum
            cover: Portada del álbum
            published: Fecha de publicación del álbum
            genre: Género musical del álbum
            artist: Músico a quien pertenece el álbum
            tracklist: Canciones del álbum
        """
    

    def read(self):
        """Función para leer los datos del album

        Returns:
            str: Información del album
        """        

        for i in self.tracklist:
            tracklist = print (Song.read(i))

        for j in self.liked:
            users = print(User.read(i))

        return f""" -------- Información del Album {self.name} --------

id: {self.id}
name: {self.name}
description: {self.description}
Cover: {self.cover}
published: {self.published}
genre: {self.genre}
artist: {self.artist}
tracklist: {tracklist}
"""
        
            

