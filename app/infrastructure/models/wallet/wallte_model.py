
from dataclasses import dataclass


@dataclass
class WalletModel():
    id:str
    currency:str
    balance:str
    is_active:bool
    created_at:str
    updated_at:str

