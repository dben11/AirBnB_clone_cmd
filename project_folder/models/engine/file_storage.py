import json
from datetime import datetime

class FileStorage:
    
    
    def __init__(self):
        self.classes = {
            
        }
    # This is a private class attribute
    __file_path = "file.json"
    __objects = {}
    
    # This a public instance method
    def all(self):
        """Return the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
        
    def save(self):
        """Serialize __objects to the Json file."""
        with open(self.__file_path, 'w') as file:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, file)
            
    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                objects_dict = json.load(file)
                for key, value in objects_dict.items():
                    class_name = key.split('.')[0]
                    cls = globals().get(class_name)
                    if cls:
                        value['created_at'] = datetime.fromisoformat(value['created_at'])
                        value['updated_at'] = datetime.fromisoformat(value['updated_at'])
                        self.__objects[key] = cls(**value)        
        except FileNotFoundError:
            #If this file does not exist, do Nothing
            print("File not found, nothing to load.")

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from the file: {e}")
        
        