from models.base_model import BaseModel

class User(BaseModel):
    """User Public class attributes that inherits from BaseModel."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""