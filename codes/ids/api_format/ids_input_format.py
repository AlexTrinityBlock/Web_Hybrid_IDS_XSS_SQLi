from pydantic import BaseModel

# Text model
class IDSInputFormat(BaseModel):
    text: str