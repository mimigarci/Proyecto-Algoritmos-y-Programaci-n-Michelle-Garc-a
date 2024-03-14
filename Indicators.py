class Indicators:
    
#TODO: Crear algoritmo de comparación
    def set_top_5 (self, list_to_check):
        """Función para definir el top 5 de una lista.

        Args:
            listToCheck (list): lista cuyo top 5 se ha de definir.

        Returns:
            top_5_list: lista nueva con el top 5 de esa lista inicial.
        """
        
        top_5_list = []
        for i in range(0, list_to_check+1):
            for j in list_to_check:
                if j.streams > [i].streams:
                    top_5_list.append()
                    
        return top_5_list
    
    def read_top_5 (self, top_5_list):

        for i in top_5_list:
            print (f"{top_5_list.index(i)+1}. {i.name}" )

