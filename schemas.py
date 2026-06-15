from pydantic import BaseModel, Field

class InsuranceCreate(BaseModel):
    smoker: int = Field(..., example=1)
    age: int = Field(..., example=20)
    bmi: float = Field(..., example=0.0)
        
class InsuranceResponse(BaseModel):
    id: int
    smoker: int = Field(..., example=1)
    age: int = Field(..., example=20)
    bmi: float = Field(..., example=0.0)
    charges: float = Field(..., example=0.0)