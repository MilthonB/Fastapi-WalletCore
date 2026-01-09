

from domain.contracts.repository.wallet_repository_domain import WalletRepository
from ...dto.wallet_dto import WalletDto
from ....domain.entities.wallet_entity import WalletEntity
from ...mapper.wallet_mapper import WalletMapper

class CreateWalletUseCase():
    def __init__(self, repository: WalletRepository):
        self.repository = repository

    
    def execute(self, dto:WalletDto) -> WalletEntity:

        #tengo que mandar una entidad 
        wallet = WalletMapper.dto_to_entity(dto)
        return self.repository.create_wallet(wallet=wallet)




