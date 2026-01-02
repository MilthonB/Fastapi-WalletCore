from typing import List, Dict, Any
from dataclasses import replace
from uuid import UUID
#from decimal import Decimal
from datetime import datetime

from domain.entities.wallet_entity import WalletEntity
from domain.value_objects.currency_value_object import CurrencyValueObject
#from domain.value_objects.money_value_object import MoneyValueObject
from domain.contracts.repository.wallet_repository_domain import WalletRepository



class WalletDatasourcesImp(WalletRepository):

    def __init__(self) -> None:
        self.data: Dict[str, WalletEntity] = {}

    def get_wallet_by_id(self, wallet_id: UUID) -> WalletEntity:

        wallet: WalletEntity | None= self.data.get(str(wallet_id))
        if not wallet:
            raise Exception("Wallet not found")

        return wallet

    def create_wallet(self, wallet: WalletEntity) -> WalletEntity:

        # if not self.data.get(str(wallet.id)):
        #     raise Exception("wallet not found")

        if self.data.get(str(wallet.id)):
            raise Exception("Wallet already exists")

        self.data[str(wallet.id)] = wallet
        return wallet

    def update_wallet_by_id(self, wallet_data_update: Dict[str, Any]) -> WalletEntity:
        
        wallet_id: UUID = wallet_data_update["wallet_id"]
        currency: str = wallet_data_update["currency"]

        wallet: WalletEntity | None =  self.data.get(str(wallet_id))

        if not wallet:
            raise Exception("Wallet not found")

        wallet_new: WalletEntity = replace(
            wallet,
            currency=CurrencyValueObject(code=currency),
            updated_at=datetime.now()
        )


        self.data[str(wallet_id)] = wallet_new

        return wallet_new

    def delete_wallet_by_id(self, wallet_id: UUID) -> WalletEntity:

        wallet: WalletEntity | None = self.data.get(str(wallet_id))

        if not wallet:
            raise Exception("Wallet not found")
        
        del self.data[str(wallet_id)]

        return wallet
       
    def list_all_wallets(self) -> List[WalletEntity]:
        return list(self.data.values())