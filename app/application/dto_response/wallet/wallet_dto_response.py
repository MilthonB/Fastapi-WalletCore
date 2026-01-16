from pydantic import BaseModel, ConfigDict
from uuid import UUID
from decimal import Decimal
from typing import Optional

class WalletResponseDTO(BaseModel):
    id: UUID
    currency: str
    balance: Decimal
    is_active: bool
    created_at: str
    updated_at: Optional[str]


    model_config = ConfigDict(
        from_attributes=True
    )

    # class Config:
    #     from_attributes = True  # Permite crear este DTO desde objetos (entidades) directamente
