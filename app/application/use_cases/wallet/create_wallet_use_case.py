

from domain.contracts.repository.wallet_repository_domain import WalletRepository
from ...dto.wallet_dto import WalletDto
from ...mapper.wallet_mapper import WalletMapper
from ....domain.entities.wallet_entity import WalletEntity

class CreateWalletUseCase():
    def __init__(self, repository: WalletRepository):
        self.repository = repository

    
    def execute(self, dto:WalletDto) -> WalletEntity:
        entity: WalletEntity = WalletMapper.dto_to_entity(dto)

        return self.repository.create_wallet(entity)




