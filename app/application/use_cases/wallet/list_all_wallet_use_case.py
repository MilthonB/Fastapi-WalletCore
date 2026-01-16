

from app.domain.contracts.repository.wallet_repository_domain import WalletRepository

from app.domain.entities.wallet_entity import WalletEntity
from typing import List
from app.application.dto.wallet_limit_offsset_dto import WalletLimitOffsetDto
class ListAllWalletsUseCase():
    def __init__(self, repository: WalletRepository) -> None:
        self.repository = repository

    def execute(self, dto:WalletLimitOffsetDto) -> List[WalletEntity]:
        wallets: List[WalletEntity] = self.repository.list_all_wallets(limit=dto.limit, offset=dto.offset)
        return wallets