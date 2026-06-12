from pydantic import BaseModel, Field, EmailStr, ConfigDict
from fastapi import FastAPI
import uvicorn

from CustomModules import __main__

app = FastAPI()

data = {
    "email": "aveq@mail.hr",
    "bio": "AJDNIQNijsakq",
    "age": 22,
}
class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=100)


users = []
@app.post("/users")
def add_user(user: UserSchema):
    users.append(user)
    return {"OK":True, "msg": "User added"}

@app.get("/users")
def add_user():
    return users




class UserAgeSchema(UserSchema):
    age: int = Field(ge=0, le=120)

# print(UserSchema(**data))

if __name__ == "__main__":
    uvicorn.run("Pydantic:app", reload=True)
