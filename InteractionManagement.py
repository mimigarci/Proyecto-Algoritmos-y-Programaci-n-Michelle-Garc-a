from Functions import Functions
from Like import Like

class InteractionManagement(Functions):
    """Clase con las funciones pertenecientes al módulo de gestión de perfiles
    """ 
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

