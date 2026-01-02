
from pydantic import BaseModel, Field
from uuid import UUID

class WalletIdDTO(BaseModel):
    wallet_id: UUID =  Field(..., description="Unique id by wallet")