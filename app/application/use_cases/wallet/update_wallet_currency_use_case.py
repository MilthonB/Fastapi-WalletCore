

from app.application.dto.wallet_currency_update_dto import WalletCurrencyUpdateDTO
from app.domain.contracts.repository.wallet_repository_domain import WalletRepository
from app.domain.entities.wallet_entity import WalletEntity

from app.application.exceptions.application_exception import ApplicationError
from app.domain.exceptions.entity_exception import WalletInactiveError, WalletWithBalanceError



class UpdateWalletCurrencyUseCase:
    def __init__(self, wallet_repository: WalletRepository) -> None:
        self.wallet_repository = wallet_repository

    def execute(self, dto: WalletCurrencyUpdateDTO) -> WalletEntity:

        wallet:WalletEntity = self.wallet_repository.get_wallet_by_id(wallet_id=dto.wallet_id)

        try:
            wallet.change_currency(currency_new=dto.currency)
        except WalletInactiveError:
            raise ApplicationError("La wallet está inactiva, no se puede cambiar la moneda")
        except WalletWithBalanceError:
            raise ApplicationError("No se puede cambiar la moneda con saldo pendiente")


        return self.wallet_repository.update_wallet_by_id(wallet=wallet)
