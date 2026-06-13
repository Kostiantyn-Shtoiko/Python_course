from fastapi import FastAPI, Depends, HTTPException, status, Response
from authx import AuthX, AuthXConfig
from pydantic import BaseModel

import uvicorn

app = FastAPI()

config = AuthXConfig()
config.JWT_SECRET_KEY = "your_secret"
config.JWT_ACCESS_COOKIE_NAME = "my_access_token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)


class UserLoginSchema(BaseModel):
    username: str
    password: str

@app.post("/login", tags=["Authentication"])
def login(credentials: UserLoginSchema, response: Response):
    if credentials.username == "admin" and credentials.password == "password":
        token = security.create_access_token(uid="12345")
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Invalid username or password")


@app.get("/protected", tags=["Authentication"], dependencies=[Depends(security.access_token_required)])
def protected():
    return {"data": "TOP SECRET DATA"}











if __name__ == "__main__":
    uvicorn.run("Authentication:app", reload=True)