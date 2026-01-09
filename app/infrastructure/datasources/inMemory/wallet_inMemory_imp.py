from typing import List, Dict
from uuid import UUID
from domain.contracts.datasources.wallet_datasources import WalletDatasources
from ....domain.contracts.data_contract.wallet.wallet_data_contract import WalletDataContract



class WalletDatasourcesImp(WalletDatasources):

    def __init__(self) -> None:
        self.data: Dict[str, WalletDataContract] = {}

    def get_wallet_by_id(self, wallet_id: UUID) -> WalletDataContract:

        wallet: WalletDataContract | None= self.data.get(str(wallet_id))
        if not wallet:
            raise Exception("Wallet not found")

        return wallet

    def create_wallet(self, wallet: WalletDataContract) -> WalletDataContract:

        # if not self.data.get(str(wallet.id)):
        #     raise Exception("wallet not found")

        if self.data.get(str(wallet.wallet_id)):
            raise Exception("Wallet already exists")

        self.data[str(wallet.wallet_id)] = wallet
        return wallet

    def update_wallet_by_id(self, wallet_new:WalletDataContract) -> WalletDataContract:
        

        wallet: WalletDataContract | None =  self.data.get(str(wallet_new.wallet_id))
        
        if not wallet:
            raise Exception("Wallet not found")

        self.data[str(wallet.wallet_id)] = wallet_new

        return wallet_new

    def delete_wallet_by_id(self, wallet_id: UUID) -> WalletDataContract:

        wallet: WalletDataContract | None = self.data.get(str(wallet_id))

        if not wallet:
            raise Exception("Wallet not found")
        
        del self.data[str(wallet_id)]

        return wallet
       
    def list_all_wallets(self) -> List[WalletDataContract]:
        return list(self.data.values())