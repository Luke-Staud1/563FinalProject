import json
import userClass

class clientClass:

    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    
    