from typing import List, Dict, Any
from uuid import UUID
from datetime import datetime
from domain.contracts.datasources.wallet_datasources import WalletDatasources, WalletDataContract



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

    def update_wallet_by_id(self, wallet_data_update: Dict[str, Any]) -> WalletDataContract:
        
        wallet_id: UUID = wallet_data_update["wallet_id"]
        currency: str = wallet_data_update["currency"]

        wallet: WalletDataContract | None =  self.data.get(str(wallet_id))

        if not wallet:
            raise Exception("Wallet not found")

        wallet_new: WalletDataContract = WalletDataContract(
            wallet_id=wallet.wallet_id,
            currency=currency,
            balance=wallet.balance,
            is_active=wallet.is_active,
            created_at=wallet.created_at,
            updated_at=str(datetime.now())
        )


        self.data[str(wallet_id)] = wallet_new

        return wallet_new

    def delete_wallet_by_id(self, wallet_id: UUID) -> WalletDataContract:

        wallet: WalletDataContract | None = self.data.get(str(wallet_id))

        if not wallet:
            raise Exception("Wallet not found")
        
        del self.data[str(wallet_id)]

        return wallet
       
    def list_all_wallets(self) -> List[WalletDataContract]:
        return list(self.data.values())