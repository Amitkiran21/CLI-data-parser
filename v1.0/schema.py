
from pydantic import BaseModel, Field, ValidationError
from typing import Optional
# basic schema design , will be changed based upon the required data set for the model
# This defines the basic required structured of a data input , If fails to be added in the Quarantine log
#later planned to implement a flexible Basemodel with declarable parameters with a clean UI
class structure_base(BaseModel):
    name: str = Field(..., description="Someone's FULL Name")
    age: int = Field(..., description="Someone's Age")
    role: str = Field(..., description="Someone's Role")
    department: Optional[str] = Field(None, description="Department name")