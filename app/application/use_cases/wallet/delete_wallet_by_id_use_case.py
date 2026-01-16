

from ....domain.contracts.repository.wallet_repository_domain import WalletRepository
from ...dto.wallet_id_dto import WalletIdDTO
from ....domain.entities.wallet_entity import WalletEntity

class DeleteWalletByIdUseCase():
    def __init__(self, repository: WalletRepository) -> None:
        self.repository = repository

    def execute(self, dto: WalletIdDTO) -> WalletEntity:
        # tengo que verificar si ese wallet existe 
        wallet: WalletEntity = self.repository.get_wallet_by_id(wallet_id=dto.wallet_id)
        return self.repository.delete_wallet_by_id(wallet_id=wallet.id)