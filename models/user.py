from pydantic import BaseModel, EmailStr, Field, field_validator
from bcrypt import hashpw, gensalt


class User(BaseModel):
    name: str
    email: EmailStr | None = Field(default=None)
    password: str

    @field_validator('password')
    def hash_password(cls, value):
        hashed_password = hashpw(value.encode('utf-8'), gensalt())
        return hashed_password.decode('utf-8')
