

from ....domain.contracts.repository.wallet_repository_domain import WalletRepository

from ....domain.entities.wallet_entity import WalletEntity
from typing import List
from ...dto.wallet_limit_offsset import WalletLimitOffset
class ListAllWalletsUseCase():
    def __init__(self, repository: WalletRepository) -> None:
        self.repository = repository

    def execute(self, dto:WalletLimitOffset) -> List[WalletEntity]:
        wallets: List[WalletEntity] = self.repository.list_all_wallets(limit=dto.limit, offset=dto.offset)
        return wallets