from pydantic import BaseModel

class CDate(BaseModel):
    month: int
    year: int
