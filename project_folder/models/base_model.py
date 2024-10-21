import unittest
import uuid
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage


class BaseModel:
    #public instances to initialize the methods
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        if isinstance(value, str):
                            value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                    
            # Fallback to default if some keys are missing
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
                    
        else:
            #initialize default  attribute if kwargs are not provided
                    # Initialise default attributes if no kwargs are provide
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()
                    storage.new(self)# Add new instances to storage


    
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    #Public  instance method
    def save(self):
        self.updated_at = datetime.now()
        storage.save()
        
    def to_dict(self):
        return{
            **self.__dict__,
            "id": self.id,
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
