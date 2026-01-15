
from pydantic import BaseModel
class WalletDataContract(BaseModel):
    wallet_id:str
    currency:str
    balance:str|int|float
    is_active:bool
    created_at:str
    updated_at:str
