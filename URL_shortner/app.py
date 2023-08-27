from fastapi import FastAPI,HTTPException ,Depends 
from uvicorn import run 
import validators,secrets
from .schemas import URLBase  
from sqlalchemy.orm import Session
from . import db_models,schemas
from .db_models import sessionLocal,engine 
from random import randint 

app = FastAPI()

db_models.Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    try: 
        yield db 
    finally:
        db.close()
        


def raise_bad_req(message):
    raise HTTPException(status_code=400,detail=message )


@app.post("/url", response_model=schemas.URL)
def create_url(url: URLBase, db: Session = Depends(get_db)):
    if not validators.url(url.target_url):
        raise_bad_req(message="Your provided URL is not valid")
    
    secret_key="".join((chr(randint(65,90)) for _ in range(8)))
    key="".join((chr(randint(65,90)) for _ in range(5)))
    
    # chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # key = "".join(secrets.choice(chars) for _ in range(5))
    # secret_key = "".join(secrets.choice(chars) for _ in range(8))
    
    db_url = db_models.URL(
        target_url=url.target_url, key=key, secret_key=secret_key
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    db_url.url = key
    db_url.admin_url = secret_key

    return db_url



'''

Import external modules:
The first step is to import the required functions and classes from external modules. These modules may include the FastAPI framework, SQLAlchemy for working with databases, and other third-party packages.

Import internal modules:
After importing external modules, you then import your own internal modules, which may include your models and schemas.

Define database engine:
Next, you import SessionLocal and engine from your database module. SessionLocal is a factory function that creates a new database session with each request, and engine is the database engine that you use to connect to your database.

Bind database engine:
You then bind your database engine with models.Base.metadata.create_all(). This line of code creates all of the necessary tables in your database based on the models that you've defined. If the database you've defined in engine doesn't exist yet, it'll be created with all modeled tables once you run your app the first time.

Define get_db() function:
The next step is to define the get_db() function, which creates and yields new database sessions with each request. Once the request is finished, you close the session with db.close(). The try … finally block ensures that the database connection is always closed,even when an error occurs during the request

Define path operation decorator:
You then define a path operation decorator using the @app.post() syntax. This decorator ensures that the create_url() function responds to any POST requests at the /url path.

Define create_url() function:
The create_url() function requires a URLBase schema as an argument and depends on the database session. By passing get_db into Depends(), you establish a database session for the request and close the session when the request is finished.

Check validity of target_url:
Within create_url(), you ensure that the provided target_url data is a valid URL. If the URL isn't valid, then you call raise_bad_request().

Generate key and secret_key:
You then provide random strings for key and secret_key, which are required for the URLInfo schema that you need to return at the end of the function.

Create database entry:
You create a database entry for your target_url.

Return URLInfo schema:
Finally, you add key and secret_key to db_url to match the required URLInfo schema that you need to return at the end of the function. The URLInfo schema includes information about the created URL, such as the original URL, the shortened URL, and the associated key and secret_key.



'''