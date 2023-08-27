from pydantic import BaseSettings 
from functools import lru_cache 

#lru_cache is the least recently used caching approach 
# we are using it so that env variables can be cached and not be loaded time to time. 

class Setttings(BaseSettings): 
    #defining the default values for the env config settings
    env_name :str ="local"
    base_url : str ="https://localhost:8000"
    db_url : str = "sqlite:///./shortener.db"
    class Config():  
        #importing values form .env files
        env_file = ".env"

      
@lru_cache()
def get_settings()->Setttings: 
    settings = Setttings()
    print(f"loading setting for {settings.env_name}")
    return settings 




