from secrets import token_hex
from random import randint
from typing import Final 

KEY : Final = token_hex(16)



secret_key="".join((chr(randint(65,90)) for _ in range(8)))
key="".join((chr(randint(65,90)) for _ in range(5)))
