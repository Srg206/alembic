from typing import List
from pydantic import BaseModel
from datetime import time

from sqlalchemy import Date, DateTime


class GlobalChat(BaseModel):
    id: int
    name:str
    last_msg_id:int
    users:List[int]
    
    
class CreateChat(BaseModel):
    name:str
    users: List[int]

    

class PydtcMessage(BaseModel):
    id:int
    content:str
    chat_id:int
    user_id:int
    date:str
    time:str
    timezone:str

class GotMsg(BaseModel):
    content:str
    chat_id:int
    token:str