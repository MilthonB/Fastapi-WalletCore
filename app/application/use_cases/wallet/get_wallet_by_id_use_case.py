

from domain.contracts.repository.wallet_repository_domain import WalletRepository
from domain.entities.wallet_entity import WalletEntity
from ...dto.wallet_id_dto import WalletIdDTO

class WalletGetByIdUseCase():
    def __init__(self, repository: WalletRepository) -> None:
        self.repository: WalletRepository = repository

    def execute(self, dto: WalletIdDTO ) -> WalletEntity:
        return self.repository.get_wallet_by_id(wallet_id=dto.wallet_id)
    
    
