from pydantic import BaseModel, Field

# Text model


class IDSInputFormat(BaseModel):
    from_ip: str = Field(default=None, max_length=15 , pattern=r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    text: str = Field(..., max_length=1000)
