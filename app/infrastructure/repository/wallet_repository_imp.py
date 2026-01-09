from typing import List, Dict
from uuid import UUID

from domain.entities.wallet_entity import WalletEntity
from domain.contracts.repository.wallet_repository_domain import WalletRepository
from domain.contracts.datasources.wallet_datasources import WalletDatasources
from ...domain.contracts.datasources.wallet_datasources import WalletDataContract
from ...application.mapper.wallet_mapper import WalletMapper


class WalletRepositoryImp(WalletRepository):

    _datasources: WalletDatasources

    def __init__(self, datasources: WalletDatasources) -> None:
        self._datasources = datasources

    def get_wallet_by_id(self, wallet_id: UUID) -> WalletEntity:
        resp_datasoruces:WalletDataContract = self._datasources.get_wallet_by_id(wallet_id=wallet_id)
        wallet_entity: WalletEntity = WalletMapper.data_contract_to_entity(data_contract=resp_datasoruces)
        return wallet_entity


    def create_wallet(self, wallet: WalletEntity ) -> WalletEntity:
        
        data_contract: WalletDataContract = WalletMapper.entity_to_data_contract(wallet_entity=wallet)
        res_data_sources: WalletDataContract = self._datasources.create_wallet(wallet=data_contract)
        wallet_entity: WalletEntity = WalletMapper.data_contract_to_entity(res_data_sources)
        
        return wallet_entity

    def update_wallet_by_id(self, wallet:WalletEntity) -> WalletEntity:
        data_cotract = WalletMapper.entity_to_data_contract(wallet_entity=wallet)
        resp_datasources: WalletDataContract = self._datasources.update_wallet_by_id(wallet=data_cotract)
        wallet_entity:WalletEntity = WalletMapper.data_contract_to_entity(resp_datasources)
        return wallet_entity

    def delete_wallet_by_id(self, wallet_id: UUID) -> WalletEntity:
        resp_datasources: WalletDataContract = self._datasources.delete_wallet_by_id(wallet_id)
        wallet_entity: WalletEntity = WalletMapper.data_contract_to_entity(resp_datasources)
        return wallet_entity


    def list_all_wallets(self) -> List[WalletEntity]:
        return [WalletMapper.data_contract_to_entity(wallet_data) for wallet_data in self._datasources.list_all_wallets()]
    
    