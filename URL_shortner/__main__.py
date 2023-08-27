import uvicorn 
from URL_shortner.app import app 
if __name__ == "__main__": 
    uvicorn.run(app=app)