

from app.domain.contracts.repository.wallet_repository_domain import WalletRepository
from app.domain.entities.wallet_entity import WalletEntity
from app.application.dto.wallet_id_dto import WalletIdDTO
from app.domain.exceptions.entity_exception import InvalidWalletDataError
from app.application.exceptions.application_exception import translate_domain_error
class WalletGetByIdUseCase():
    def __init__(self, repository: WalletRepository) -> None:
        self.repository: WalletRepository = repository

    def execute(self, dto: WalletIdDTO ) -> WalletEntity:

        # Traducir exceptiones de dominio a exceptciones de aplicacion
        try:
            return self.repository.get_wallet_by_id(wallet_id=dto.wallet_id)
        except InvalidWalletDataError as err:
            raise translate_domain_error(err)
            # raise ApplicationError("Los datos que se obtuvieron de la fuente de datos esta corruptos o son invalidos")




    
    
