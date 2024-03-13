from Song import Song

class MusicManagement:
    """Clase con las funciones pertenecientes al módulo de gestión de perfiles
    """    

#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def search_menu (self, active_user):
        while True:
            itemToSearch = input ("""-------- Buscador --------
                                
    1. Buscar canción
    2. Buscar album
    3. Buscar perfil                                                    
    4. Buscar playlist                                                                                                              
    5. Regresar                                                                                                              
                                
    ----> """)
            
            if itemToSearch == "1":
                MusicManagement.search_songs(self, active_user)
                break

            if itemToSearch == "2":  
                MusicManagement.search_songs(self, active_user)
                break

            elif itemToSearch == "3":
                MusicManagement.search_by_artist(self, active_user)
                break

            elif itemToSearch == "4":
                MusicManagement.search_playlists(self, active_user)
                break

            elif itemToSearch == "5":
                break
            else:
                print ("\nOpción inválida\n")
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
                
    def search_songs (self, active_user):
        song_name = input ("\nIntroduzca el nombre de la canción: ")
        song_self_list = self.songs

        if MusicManagement.check_name_registered(self, song_name, song_self_list) == False:
            print ("No hay canciones registradas bajo ese nombre")
        else:
            matched_songs = MusicManagement.check_name_registered(self, song_name, song_self_list) 
            for i in matched_songs:
                print (f"{matched_songs.index(i)+1}. {i.name}")

        # if Functions.select_option (self, ):
        # choice = input ("Desea reproducir una canción? (Y/N)")
        # if choice == "Y":
        #     Functions.select_option(self, matched_items)
        # elif choice == "N":
        #     print ("")
        # else:
        #     print ("...Opción inválida")

#-------------------------------------------------------------------------------------------------------------------------------------------------
                
    #TODO: Revisar funcionalidad
    def select_option (self, matched_items):
        chosen = input ("Número de la canción a reproducir:")

        if chosen == int:
            for i in matched_items:
                if matched_items.index(i) == chosen-1:
                    Song.song_menu(i)
                else:
                    continue

        else:
            print ("Introduzca un número dentro de la lista")

#-------------------------------------------------------------------------------------------------------------------------------------------------
            
    def check_name_registered(self, item_name: str, item_self_list: list):
        """Función para obtener todos los objetos registrados bajo un nombre. Si se encuentra registrado bajo ese nombre, se agregará a una lista con los
        objetos coincidentes. En caso contrario, se retornará un booleano indicando que no existen objetos bajo ese nombre.

        Args:
            item_name (str): Nombre del objeto
            item_self_list (list): Lista donde se encuentra el objeto

        Returns:
            matched_items (list): lista con los objetos coincidentes     or          Bool: False
        """        
        list_items = len(item_self_list)
        matched_items = []
        if list_items >= 0:
            for i in item_self_list:
                list_items -= 1
                if item_name in i.name:
                    matched_items.append(i)
                else:
                    continue
            
            return matched_items
        else:
            return False
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
        
#TODO: Temrinar funcion de busqueda por albums
    def search_albums (self):
        item_name = input ("\nIntroduzca el nombre de la canción o del álbum: ")
        registered_albums = len(self.albums)
        if registered_albums >= 0:
            for i in self.albums:
                registered_albums -= 1
                for p in range(1, len(i.tracklist)):

                    if item_name in i.name:
                        print (f"""Nombre del álbum: {i.name}
    Tracklist:
                               
    {p} {i.read_tracklist}
""")
                    else:
                        continue
        else:
            print("No hay albumes registrados bajo ese nombre.")

#-------------------------------------------------------------------------------------------------------------------------------------------------
            
#TODO: Terminar función de búsqueda de artistas
            
    def search_by_artist (self):
        artist_name = input ("Nombre del músico (Alias): ")

        registered_artist = len(self.artists)
        if registered_artist >= 0:
            for i in self.artists:
                registered_artist -= 1
                if artist_name in i.name:
                    print (i.read)

                    choose_view = input ("""
1. Ver canciones del músico
2. Ver albumes del músico
    
---> """)
                    if choose_view == "1":   
                        for s in i.albums:
                            print (s.read)
                            MusicManagement.wanna_play_song(self)
                                  
                    elif choose_view == "2":
                        for a in i.albums:
                            print (a.read)
                            MusicManagement.wanna_play_song(self)
                else:
                    continue
        else:
            print("No hay canciones registradas")

#-------------------------------------------------------------------------------------------------------------------------------------------------
            
#TODO: Terminar función de búsqueda de playlists
    def search_playlists (self, active_userId):
        pass
#-------------------------------------------------------------------------------------------------------------------------------------------------
    
#TODO: Terminar función de búsqueda de playlists
    def wanna_play_song(self):

        while True:
            select = input ("""
        Desea escuchar una canción?
                                                
        1. Si
        2. No
                                                
        --->""")
                                
            if select == "1":
                pass
                
            if select == "2":
                pass
                break

            else:
                print ("Opción inválida.")


#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def select_option(self):
        pass