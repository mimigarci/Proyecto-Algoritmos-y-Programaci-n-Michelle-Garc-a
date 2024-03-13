from Like import Like

class InteractionManagement:
    """Clase con las funciones pertenecientes al módulo de gestión de perfiles
    """ 


#TODO: Terminar función de definir top 5 de cada lista
    def top_5 (self, listToCheck):
        """Función para definir el top 5 de una lista.

        Args:
            listToCheck (list): lista cuyo top 5 se ha de definir.

        Returns:
            top_5_list: lista nueva con el top 5 de esa lista inicial.
        """
        
        top_5_list = []
        for i in range(0, listToCheck+1):
            for j in listToCheck:
                if j.streams > [i].streams:
                    top_5_list.append()
        return top_5_list

#-------------------------------------------------------------------------------------------------------------------------------------------------
#TODO: Terminar función de crear playlist de un usuario
    def create_playlist (self, creator_id):
        
        for i in self.users:
            if i.d == creator_id:
                pass

#-------------------------------------------------------------------------------------------------------------------------------------------------
#TODO: Terminar función de lanzar album de un artista
    def launch_album (self, artist_id):

        for i in self.artists:
            if i.id == artist_id:
                pass

#-------------------------------------------------------------------------------------------------------------------------------------------------

    def give_like (self, item_id, user_id):
        """Función para dar like a un objeto.

        Args:
            item_id (): ID del objeto para dar like.
            user_id (): ID del usuario que dará el like.
        """    

        for i in self.liked:
            if i.item == item_id and i.user == user_id:
                print ("Ya le diste like! ")

            elif i.item1 != item_id or i.user != user_id:
                newLike = Like(item_id, user_id)
                self.liked.append(newLike)
                

                for k in self.albums:
                    if k.item == item_id:
                        k.liked.append(newLike)
                    else:
                        continue

                for j in self.songs:
                    if j.item == item_id:
                        j.liked.append(newLike)
                    else:
                        continue

                for m in self.playlists:
                    if m.item == item_id:
                        m.liked.append(newLike)
                    else:
                        continue

                for p in self.artists:
                    if p.item == item_id:
                        p.liked.append(newLike)
                    else:
                        continue
            else:
                continue


#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def remove_like (self, item, user):
        """Función para quitar un like

        Args:
            item (_type_): _description_
            user (_type_): _description_
        """    
        for i in self.liked:
            if i.item == item and i.user == user:
                self.liked.remove(i)
            else:
                continue
#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def interactionsMenu (self, item_id, user_id):

        action = input ("""
1. Agregar a me gusta
2. Quitar de me gusta
                        """)
            
        if action == "1":
            InteractionManagement.give_like(self, item_id, user_id)
        elif action == "2":
            InteractionManagement.remove_like(self, item_id, user_id)
        else:
            print ("Opción inválida... Regresando al menu principal")