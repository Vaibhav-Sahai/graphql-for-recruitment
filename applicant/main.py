#******************************************************************************#
# Main Driver Code Should Be Here                                              #
#******************************************************************************#
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def ping():
    return {"ping": "pong!"}
