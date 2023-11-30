

class message:
    def __init__(self, message, destUser, srcUser):
        self.message = message
        self.destUser = destUser
        self.srcUser = srcUser
        
    def __str__(self):
        return self.message

    def __repr__(self):
        return self.message
