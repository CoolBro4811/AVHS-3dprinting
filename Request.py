from typing import Optional
from Order import *
from User import *

class Request():
    def __init__(self, user : Optional[User], order : Optional[Order]) -> None:
        self.user = user
        self.order = order

    def __str__(self) -> str:
        return f"{self.user.__str__()},\n{self.order.__str__()}"
    def __del__(self) -> None:
        print(f"deleting {self}")
    

    def send() -> None:
        ## to send a request
        ## self.invoice setup here
        return
    