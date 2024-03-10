class Like:

    def __init__(self, item, user):
        
        self.item = item
        self.user = user

    def read(self):
        return f"""
El like es de: {self.user}
Le dió like a: {self.item}"""