from typing import List, Dict
from uuid import UUID
from abc import ABC, abstractmethod
from ..data_contract.wallet.wallet_data_contract import WalletDataContract


class WalletDatasources(ABC):
    @abstractmethod
    def get_wallet_by_id(self, wallet_id: UUID) -> WalletDataContract: ...
    @abstractmethod
    def create_wallet(self, wallet: WalletDataContract) -> WalletDataContract: ...
    @abstractmethod
    def update_wallet_by_id(self, wallet:WalletDataContract) -> WalletDataContract: ...
    @abstractmethod
    def delete_wallet_by_id(self, wallet_id: UUID) -> WalletDataContract: ...
    @abstractmethod
    def list_all_wallets(self) -> List[WalletDataContract]: ...
