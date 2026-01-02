

from ....domain.contracts.repository.wallet_repository_domain import WalletRepository

from ....domain.entities.wallet_entity import WalletEntity
from typing import List

class ListAllWalletsUseCase():
    def __init__(self, repository: WalletRepository) -> None:
        self.repository = repository

    def execute(self) -> List[WalletEntity]:
        wallets: List[WalletEntity] = self.repository.list_all_wallets()
        return wallets