from typing import List
from uuid import UUID

from domain.entities.wallet_entity import WalletEntity
from domain.contracts.repository.wallet_repository_domain import WalletRepository
from domain.contracts.datasources.wallet_datasources import WalletDatasources


class WalletRepositoryImp(WalletRepository):

    _datasources: WalletDatasources

    def __init__(self, datasources: WalletDatasources) -> None:
        self._datasources = datasources

    def get_wallet_by_id(self, wallet_id: UUID) -> WalletEntity:
        return self._datasources.get_wallet_by_id(wallet_id)

    def create_wallet(self, wallet: WalletEntity) -> WalletEntity:
         return self._datasources.create_wallet(wallet)

    def update_wallet_by_id(self, wallet_id: UUID) -> WalletEntity:
        return self._datasources.update_wallet_by_id(wallet_id)

    def delete_wallet_by_id(self, wallet_id: UUID) -> WalletEntity:
        return self._datasources.delete_wallet_by_id(wallet_id)

    def list_all_wallets(self) -> List[WalletEntity]:
        return self._datasources.list_all_wallets()
    
    