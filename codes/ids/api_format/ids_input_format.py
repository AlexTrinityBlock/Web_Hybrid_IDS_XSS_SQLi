from pydantic import BaseModel, Field

# Text model
class IDSInputFormat(BaseModel):
    text: str = Field(..., max_length=1000)