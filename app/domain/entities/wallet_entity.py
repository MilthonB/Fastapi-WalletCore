from dataclasses import dataclass, replace
from datetime import datetime
from typing import Optional
from decimal import Decimal
from uuid import UUID, uuid4

from ...domain.value_objects.currency_value_object import CurrencyValueObject
from ...domain.value_objects.money_value_object import MoneyValueObject
from ..contracts.data_contract.wallet.wallet_data_contract import WalletDataContract
from ..exceptions.entity_exception import InvalidWalletDataError,WalletInactiveError,WalletWithBalanceError


@dataclass(frozen=True)
class WalletEntity:
    id: UUID
    currency: CurrencyValueObject
    balance: MoneyValueObject
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    @classmethod
    def create_new(cls, currency_code: str, inital_amount: Decimal) -> "WalletEntity":

        currency : CurrencyValueObject = CurrencyValueObject(currency_code)
        balance: MoneyValueObject = MoneyValueObject( amount=inital_amount, currency=currency)

        return cls(
            id=uuid4(),
            currency=currency,
            balance=balance,
            is_active= True,
            created_at=datetime.now(),
        )

    @classmethod
    def rehydrate(cls, wallet_data_contract: WalletDataContract) -> "WalletEntity":
        currency : CurrencyValueObject = CurrencyValueObject(wallet_data_contract.currency)
        balance: MoneyValueObject = MoneyValueObject( amount=Decimal(wallet_data_contract.balance), currency=currency)

        try:
            wallet_id = UUID(wallet_data_contract.wallet_id)
        except (ValueError, TypeError):
            raise InvalidWalletDataError(f"Invalid wallet_id from data source: {wallet_data_contract.wallet_id}")

        return cls(
            id=wallet_id,
            currency=currency,
            balance = balance,
            is_active=wallet_data_contract.is_active,
            created_at=datetime.fromisoformat(wallet_data_contract.created_at),
            updated_at=datetime.fromisoformat(wallet_data_contract.updated_at) if wallet_data_contract.updated_at else None
        )

    def activate(self) -> "WalletEntity":
        if self.is_active:
            return self
        return replace(self, is_active=True, updated_at=datetime.now())

    def deactivate(self) -> "WalletEntity":
        if not self.is_active:
            return self
        return replace(self, is_active=False, updated_at=datetime.now())

    def change_currency(self, currency_new: str) -> "WalletEntity":
        if not self.is_active:
            raise WalletInactiveError("Cannot change currency of an inactive wallet")
        
        if not self.balance.is_zero():
            raise WalletWithBalanceError("Cannot change currency when wallet has balance")
        
        currency: CurrencyValueObject =  CurrencyValueObject(code=currency_new)

        if self.currency == currency:
            return self
        
        return replace(self,currency=currency, updated_at=datetime.now())
        
