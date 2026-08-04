from pydantic import BaseModel


class User(BaseModel):
    """Pydantic model for validating API user responses."""
    id: int
    name: str
    username: str
    email: str