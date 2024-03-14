from Song import Song
from User import User


""" Clase Playlist: Playlists de Metrotify. """
 
class Playlist:

    def __init__(self, id: str, name: str, description: str, creator: str, tracks: list):
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
        self.tracks = tracks
        self.liked = []

         
    def read(self):
        """Función para leer los datos de la playlist

        Returns:
            string: Información de la playlist
        """        

        for i in self.tracks:
            tracks = print (Song.read(i))

        likes = len(self.liked)
        # for j in self.liked:
        #     users = print(User.read(i))

        return f""" -------- Información de la Playlist {self.name} --------

id: {self.id}
name: {self.name}
description: {self.description}
creator: {self.creator}
tracklist: {tracks}
likes playlist: {likes}
"""
        