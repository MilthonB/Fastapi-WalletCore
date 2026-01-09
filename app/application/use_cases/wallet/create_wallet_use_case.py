

from domain.contracts.repository.wallet_repository_domain import WalletRepository
from ...dto.wallet_dto import WalletDto
from ....domain.entities.wallet_entity import WalletEntity

class CreateWalletUseCase():
    def __init__(self, repository: WalletRepository):
        self.repository = repository

    
    def execute(self, dto:WalletDto) -> WalletEntity:
        return self.repository.create_wallet(dto_wallet=dto)




