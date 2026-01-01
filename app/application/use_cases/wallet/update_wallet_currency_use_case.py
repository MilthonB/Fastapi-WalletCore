

from ...dto.wallet_currency_update_dto import WalletCurrencyUpdateDTO
from domain.contracts.repository.wallet_repository_domain import WalletRepository
from domain.entities.wallet_entity import WalletEntity



class UpdateWalletCurrencyUseCase:
    def __init__(self, wallet_repository: WalletRepository) -> None:
        self.wallet_repository = wallet_repository

    def execute(self, dto: WalletCurrencyUpdateDTO) -> WalletEntity:
        wallet_data_update = dto.model_dump()

        return self.wallet_repository.update_wallet_by_id(wallet_data_update)
