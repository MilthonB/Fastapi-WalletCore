
from ...domain.contracts.repository.wallet_repository_domain import WalletRepository
from ...domain.contracts.datasources.wallet_datasources import WalletDatasources
from ...infrastructure.repository.wallet_repository_imp import WalletRepositoryImp
from ...infrastructure.datasources.inMemory.wallet_inMemory_imp import WalletDatasourcesImp
from ..controllers.wallet.wallet_controller import WalletController

def get_wallet_controller() -> WalletController:
    datasources:WalletDatasources =  WalletDatasourcesImp()
    repository: WalletRepository =  WalletRepositoryImp(datasources=datasources)
    return WalletController(repository=repository)
