from Song import Song
from User import User


""" Clase Playlist: Playlists de Metrotify. """
 
class Playlist:

    def __init__(self, id: str, name: str, description: str, creator: str, tracks: list):

        self.id = id
        self.name = name
        self.description = description
        self.creator = creator
        self.tracks = tracks
        self.liked = []

        """Constructor de la clase Playlist:

            self.id: ID de la playlist
            self.name: Nombre de la playlist
            self.description: Descripción de la playlist
            self.creator: Usuario que creó la playlist
            self.tracks: Canciones de la playlist
            self.liked: Lista de usuarios que le dieron me gusta a la playlist.
        """ 

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
        