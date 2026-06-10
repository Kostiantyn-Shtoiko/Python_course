import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/", summary="Hello word", tags=["Basic root"])
def root():
    return "Hello World"

if __name__ == "__main__":
    uvicorn.run("Start_FastApi:app", reload=True)
