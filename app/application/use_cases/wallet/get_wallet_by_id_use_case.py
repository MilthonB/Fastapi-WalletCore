

from domain.contracts.repository.wallet_repository_domain import WalletRepository
from domain.entities.wallet_entity import WalletEntity
from ...dto.wallet_id_dto import WalletIdDTO
from ...exceptions.application_exception import ApplicationError
from ....domain.exceptions.entity_exception import InvalidWalletDataError, WalletInactiveError, WalletWithBalanceError
from ....domain.exceptions.value_object_exception import NegativeAmountError, InvalidCurrencyError
class WalletGetByIdUseCase():
    def __init__(self, repository: WalletRepository) -> None:
        self.repository: WalletRepository = repository

    def execute(self, dto: WalletIdDTO ) -> WalletEntity:

        # Traducir exceptiones de dominio a exceptciones de aplicacion
        try:
            return self.repository.get_wallet_by_id(wallet_id=dto.wallet_id)
        except InvalidWalletDataError:
            raise ApplicationError("Los datos que se obtuvieron de la fuente de datos esta corruptos o son invalidos")




    
    
