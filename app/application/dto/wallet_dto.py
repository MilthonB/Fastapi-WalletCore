
from pydantic import BaseModel,field_validator
from typing import Any
from decimal import Decimal, InvalidOperation

class WalletDto(BaseModel):
    # wallet_id: UUID
    currency: str
    balance: Decimal
    is_active: bool = True
    # created_at: datetime
    # updated_at: Optional[datetime] = Field(default=None)

    @field_validator("currency", mode="before")
    def validate_currency(cls, value: Any) -> str:
        if not isinstance(value, str):
            raise TypeError("Invalid currency type. A string is required")

        currency: str  =  value.strip().upper()

        if not currency:
            raise ValueError("Currency cannot be empty")
        
        return currency
        
    
    @field_validator("balance", mode="before")
    def validate_balance(cls, value: Any, info:Any) -> Decimal:

        if not isinstance(value, (str, int, float)):
            raise TypeError("Invalid balance type. A string, int, float is required")

        if isinstance(value, str) and not value.strip():
            raise ValueError("Balance cannot be empty")
        
            
        try:
            balance:Decimal = Decimal(str(value))
            return balance
        except InvalidOperation:
            raise ValueError("Balance must be numeric")
   
      




