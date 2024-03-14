class Indicators:
    
    def set_top_5 (self, list_to_check):
        """Función para definir el top 5 de una lista. Método utilizado: selection sort.

        Args:
            listToCheck (list): lista cuyo top 5 se ha de definir.

        Returns:
            top_5_list: lista nueva con el top 5 de esa lista inicial.
        """
        
        top_5_list = list_to_check
        n = len(top_5_list)

        registered_list = len(top_5_list)
        if registered_list > 0:
            for i in top_5_list:
                registered_list -= 1
                for j in range(1, n):
                    max_streams = Indicators.compare_items_streams(self, i, top_5_list[j])
                
                top_5_list.append(max_streams)
            
            
            
            if top_5_list > 0:
                return top_5_list
            else:
                return None
        else:
            print ("----- NO STREAMS REGISTERED -----")

    
    def read_top_5 (self, top_5_list):

        if top_5_list == None:
            print ("----- NO STREAMS REGISTERED -----")
        else:
            for i in top_5_list:
                print (f"{top_5_list.index(i)+1}. {i.name}" )

    def compare_items_streams (self, item1, item2):

        if item1.streams > item2.streams:
            more_streams = item1
        elif item1.streams < item2.streams:
            more_streams = item2
        elif item1.streams == item2.streams:
            more_streams = item1
        else:
            print ("Compare items error")

        return more_streams
