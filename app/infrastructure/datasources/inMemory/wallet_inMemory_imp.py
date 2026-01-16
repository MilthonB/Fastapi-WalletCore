from typing import List, Dict
from uuid import UUID
from app.domain.contracts.datasources.wallet_datasources import WalletDatasources
from ....domain.contracts.data_contract.wallet.wallet_data_contract import WalletDataContract
from ....api.data.dummy_data import IN_MEMORY_WALLET
from datetime import datetime, timezone
from app.infrastructure.exceptions.datasources_exeptions import DatasourceNotFoundError


class WalletDatasourcesImp(WalletDatasources):

    def __init__(self) -> None:
        self.data: Dict[str, WalletDataContract] = IN_MEMORY_WALLET

    def get_wallet_by_id(self, wallet_id: UUID) -> WalletDataContract:

        wallet: WalletDataContract | None= self.data.get(str(wallet_id))
        if not wallet:
            raise 

        return wallet

    def create_wallet(self, wallet: WalletDataContract) -> WalletDataContract:

        # if not self.data.get(str(wallet.id)):
        #     raise Exception("wallet not found")

        if self.data.get(str(wallet.wallet_id)):
            raise DatasourceNotFoundError(message="Wallet existente", status_code=404)

        self.data[str(wallet.wallet_id)] = wallet
        return wallet

    def update_wallet_by_id(self, wallet:WalletDataContract) -> WalletDataContract:
        
        print(wallet)
        wallet_new: WalletDataContract | None =  self.data.get(str(wallet.wallet_id))
        
        if not wallet_new:
            raise DatasourceNotFoundError(message="Wallet no encontrada", status_code=404)
            

        wallet.updated_at = datetime.now(timezone.utc).isoformat()

        self.data[str(wallet_new.wallet_id)] = wallet

        return wallet

    def delete_wallet_by_id(self, wallet_id: UUID) -> WalletDataContract:

        wallet: WalletDataContract | None = self.data.get(str(wallet_id))

        if not wallet:
            raise DatasourceNotFoundError(message="Wallet no encontrada", status_code=404)
        
        del self.data[str(wallet_id)]

        return wallet
       
    def list_all_wallets(self, limit:int, offset:int) -> List[WalletDataContract]:
        return list(self.data.values())