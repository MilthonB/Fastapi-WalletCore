
from app.domain.contracts.repository.wallet_repository_domain import WalletRepository
from app.domain.contracts.datasources.wallet_datasources import WalletDatasources
from app.infrastructure.repository.wallet_repository_imp import WalletRepositoryImp
from app.infrastructure.datasources.inMemory.wallet_inMemory_imp import WalletDatasourcesImp
from app.presentation.controllers.wallet.wallet_controller import WalletController

def get_wallet_controller() -> WalletController:
    datasources:WalletDatasources =  WalletDatasourcesImp()
    repository: WalletRepository =  WalletRepositoryImp(datasources=datasources)
    return WalletController(repository=repository)
