

from uuid import UUID
from pydantic import BaseModel, Field, field_validator, ConfigDict

class WalletCurrencyUpdateDTO(BaseModel):
    wallet_id: UUID =  Field(..., description="Id unique in wallet")
    currency: str = Field(..., min_length=3, max_length=3)


    @field_validator("currency", mode="before")
    def uppercase_currency(cls, curr:str) -> str:
        return curr.upper().strip()


    model_config = ConfigDict(from_attributes=True)

    # class Config:
    #     from_attributes = True # Permite que Pydantic lea datos de objetos (no solo dicts)
    #     anystr_strip_whitespace = True  # Elimina espacios automáticamente de todos los strings
    #     validate_assignment = True  # Valida si reasignas valores a los campos después de creado el DTO






# from uuid import UUID
# from typing import Tuple, Dict, Any, Optional
# from dataclasses import dataclass

# @dataclass
# class WalletCurrencyUpdateDTO:
#     wallet_id: UUID
#     currency:str
    
#     @staticmethod
#     def validate(data:Dict[str, Any]) -> Tuple[bool,str, Optional['WalletCurrencyUpdateDTO']]:
#         wallet_id:UUID

#         if "wallet_id" not in data or "currency" not in data:
#             return False, "Missing required fields", None

#         if not isinstance(data["wallet_id"], str):
#             return False, "Invalid wallet_id type", None
        
#         if not isinstance(data["currency"], str):
#             return False, "Invalid currency type", None
        
#         try:
#             wallet_id = UUID(data["wallet_id"])
#         except ValueError:
#             return False, "Invalid wallet_id format", None

#         currency:str = data["currency"].upper().strip()

#         if not currency or len(currency) != 3:
#             return False, "Unsupported currency code", None
        
#         dto = WalletCurrencyUpdateDTO(wallet_id=wallet_id, currency=currency)

#         return True, "Valid data", dto