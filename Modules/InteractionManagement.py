from Modules.Tools import Tools
from Clases.Artist import Artist
from Clases.Album import Album
from Clases.Playlist import Playlist
from Clases.Song import Song
from rich import print

class InteractionManagement(Tools):
    """Clase con las funciones pertenecientes al módulo de gestión de perfiles
    """ 
#-------------------------------------------------------------------------------------------------------------------------------------------------

    def add_like (self, item: object, user_id: str):
        """Función para dar like a un objeto. Crea un objeto de tipo like a partir de las características que posee. Evalua y clasifica a partir 
        del tipo de objeto que posee el like y agrega el like a la lista de su objeto correspondiente.

        Args:
            item (str): Objeto para dar like.
            user_id (str): ID del usuario que dará el like.
        Returns:
            tuple: Like creado.
        """       

        newLike = (item, user_id)
        self.liked.append(newLike)

        for u in self.users:
            if u.id == user_id:
                user = u
            else:
                continue

        #Albums
        registered_albums = len(self.albums)  
        if registered_albums > 0:
            for a in self.albums:
                registered_albums -= 1
                if a == item:
                    if InteractionManagement.already_gave_like(self, newLike) == False:
                        user.liked_albums.append(a)
                        print ("""      [italic yellow]👍 +1""")
                    else:
                        self.liked.remove(newLike)
                        break
                else:
                    continue
        else:
            print ("\n[italic blue]No hay albumes registrados en la plataforma\n")

        #Canciones
        registered_songs = len(self.songs)  
        if registered_songs > 0:
            for s in self.songs:
                registered_songs -= 1
                if s == item: 
                    if InteractionManagement.already_gave_like(self, newLike) == False:
                        user.liked_songs.append(s)
                        print ("[italic yellow]👍 +1")   
                    else:
                        self.liked.remove(newLike)
                else:
                    continue
        else:
            print ("\n[italic blue]No hay canciones registradas en la plataforma.\n")

        #Playlists
        registered_playlists = len(self.playlists)  
        if registered_playlists > 0:
            for p in self.playlists:
                registered_playlists -= 1
                if p == item:
                    if InteractionManagement.already_gave_like(self, newLike) == False:
                        user.liked_playlists.append(p)
                        print ("[italic yellow]👍 +1")   
                    else:
                        self.liked.remove(newLike)
                        break
                else:
                    continue
        else:
            print ("\n[italic blue]No hay playlists registradas en la plataforma\n")

        #Artistas
        registered_users = len(self.users)  
        if registered_users > 0:
            for u in self.users:
                registered_users -= 1
                if type(u) == Artist:
                    if u == item:
                        if InteractionManagement.already_gave_like(self, newLike) == False:
                            u.likes.append(user)
                            user.liked_artists.append(u)
                            print ("""         [italic yellow]+👍""")   
                        else:
                            self.liked.remove(newLike)
                            break
                    else:
                        continue
                else:
                    continue
        else:
            print ("\n[italic blue]No hay usuarios registrados en la plataforma\n")      

        return newLike

#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def remove_like (self, item, user_id):
        """Función para quitar un like. Elimina el like de la lista de su objeto correspondiente y de la lista de likes registrados.

        Args:
            item_id (str): ID del objeto al que se le debe quitar el like.
            user_id (str): ID del usuario activo
        """    
        for u in self.users:
            if u.id == user_id:
                user = u
            else:
                continue

        if len(self.liked) >= 0:
            for i in self.liked:
                if i[0] == item and i[1] == user_id:

                    if type(item) == Album:
                        self.liked.remove(i)
                        user.liked_albums.remove(item)
                        print ("         [italic yellow]-👍")   

                    elif type(item) == Song:
                        self.liked.remove(i) 
                        user.liked_songs.remove(item)  
                        print ("         [italic yellow]👍-1")

                    elif type(item) == Playlist:
                        self.liked.remove(i)
                        user.liked_playlists.remove(item)
                        print ("         [italic yellow]👍-1")

                    elif type(item) == Artist:
                        self.liked.remove(i)
                        user.liked_artists.remove(item)
                        print ("         [italic yellow]👍-1")
                    else:
                        continue
                else:
                    continue
        else:
            print ("\n[italic blue]No hay likes registrados dentro de la plataforma.\n")

#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def interactions_menu (self, item, active_user_id):
        """Menu de interacciones. Ofrece las opciones de agregar o quitar un like de un objeto a partir de un usuario activo. 

        Args:
            item (object): Objeto al cual agregar o quitar un me gusta.
            active_user_id (str): ID del usuario al que pertenece el me gusta.
        """        

        action = input ("""                        
        1. Agregar a me gusta
        2. Quitar de me gusta
                        
        ---> """)
            
        if action == "1":
            InteractionManagement.add_like(self, item, active_user_id)
        elif action == "2":
            InteractionManagement.remove_like(self, item, active_user_id)
        else:
            print ("[italic red]Opción inválida... Regresando al menu principal")

#-------------------------------------------------------------------------------------------------------------------------------------------------

    def already_gave_like(self, like):
        """Función para verificar si un usuario le dió me gusta a un objeto.

        Args:
            like (tuple): Tupla con la información del usuario que dió like y a qué le dió like.

        Returns:
            Bool: Retorna True si el objeto ya tiene un like del usuario activo. Retorna False si el objeto no tiene un like del usuario activo
        """       
        registered_likes = len(self.liked)
        like_amount = 0

        if registered_likes >= 0:
            for l in self.liked:
                registered_likes-=1
                if l[0] == like[0] and l[1] == like[1]:
                    like_amount += 1
                else:
                    continue
            
            if like_amount > 1:
                print ("\n[italic blue]Este objeto ya tiene un like")
                return True
            else:
                return False
        else:
            return False