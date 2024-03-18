from rich import print
from socket import gethostbyname, create_connection, error
import webbrowser
 
class Song:
    """Canciones de Metrotify.

    Returns:
        Objeto de la clase Song.
    """   

    def __init__(self, id: str, name: str, duration: str, link: str, artist_id):
        """Constructor de la clase Song:

        Args:
            id (str): ID de la canción
            name (str): Nombre de la canción
            duration (str): Duración de la canción
            link (str): Link de la canción
        """        

        self.id = id
        self.name = name
        self.duration = duration
        self.link = link
        self.streams = 0


    def read(self):
        """Función para leer los atributos de la clase Song

        Returns:
            str: Información de la clase.
        """        
        return f"""
------ {self.name} ------
Duración: {self.duration}
Streams: {self.streams}
"""

    def play_song(self, active_user_id: str, users_list: list, albums_list: list, song_list: list):
        song_id = self.id

        for s in song_list:
            if s.id == song_id:
                song_link = s.link 
            else:
                continue
        
        for u in users_list:
            if active_user_id == u.id:
                u.streams += 1
            else:
                continue

        for a in albums_list:
            for t in a.tracklist:
                if song_id == t.id:
                    t.streams += 1
                    a.streams += 1
                else:
                    continue
            else:
                continue
        
        reproduce = Song.confirm_connection(self)
        
        if reproduce == True:
            webbrowser.open(song_link)
            print ("\n[italic green]...Canción reproducida correctamente\n")
        else:
            print ("\n[italic red]...No se pudo reproducir la canción. Compruebe su conexión a internet")


    def confirm_connection (self):
        """Función para verificar si el usuario tiene conexión a internet.

        Returns:
            Bool: Retorna True si hay conexión a internet. Retorna False si no hay conexión a internet.
        """        
        try:
            gethostbyname('google.com')
            connection = create_connection(('google.com', 80), 1)
            connection.close()
            reproduce = True
            return reproduce
                
        except error:
            reproduce = False

        
    