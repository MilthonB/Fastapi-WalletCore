
from pydantic import BaseModel, Field, field_validator
from uuid import UUID

class WalletIdDTO(BaseModel):
    wallet_id: UUID =  Field(..., description="Unique id by wallet")
