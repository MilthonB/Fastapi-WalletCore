from typing import List, Dict
from uuid import UUID
from abc import ABC, abstractmethod
from pydantic import BaseModel

class WalletDataContract(BaseModel):
    wallet_id:str
    currency:str
    balance:str
    is_active:bool
    created_at:str
    updated_at:str


class WalletDatasources(ABC):
    @abstractmethod
    def get_wallet_by_id(self, wallet_id: UUID) -> WalletDataContract: ...
    @abstractmethod
    def create_wallet(self, wallet: WalletDataContract) -> WalletDataContract: ...
    @abstractmethod
    def update_wallet_by_id(self, wallet_data_update: Dict[str, str]) -> WalletDataContract: ...
    @abstractmethod
    def delete_wallet_by_id(self, wallet_id: UUID) -> WalletDataContract: ...
    @abstractmethod
    def list_all_wallets(self) -> List[WalletDataContract]: ...
