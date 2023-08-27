from pydantic import BaseModel 

class URLBase(BaseModel): 
    target_url: str 

class URL(URLBase):
    is_active:bool 
    click : int 
    class config(): 
        orm_mode = True 

class URL_info(URL):
    url:str 
    admin_url: str  



#json format 
'''
{
  "target_url": "https://realpython.com",
  "is_active": true,
  "clicks": 0,
  "url": "JNPGB",
  "admin_url": "MIZJZYVA"
}

'''