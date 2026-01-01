from typing import List, Dict
from uuid import UUID
from abc import ABC, abstractmethod

from domain.entities.wallet_entity import WalletEntity


class WalletDatasources(ABC):
    @abstractmethod
    def get_wallet_by_id(self, wallet_id: UUID) -> WalletEntity: ...
    @abstractmethod
    def create_wallet(self, wallet: WalletEntity) -> WalletEntity: ...
    @abstractmethod
    def update_wallet_by_id(self, wallet_data_update: Dict[str, str]) -> WalletEntity: ...
    @abstractmethod
    def delete_wallet_by_id(self, wallet_id: UUID) -> WalletEntity: ...
    @abstractmethod
    def list_all_wallets(self) -> List[WalletEntity]: ...
