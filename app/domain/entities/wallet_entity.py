from dataclasses import dataclass, replace
from datetime import datetime
from typing import Optional
from decimal import Decimal
from uuid import UUID, uuid4

from domain.value_objects.currency_value_object import CurrencyValueObject
from domain.value_objects.money_value_object import MoneyValueObject


@dataclass(frozen=True)
class WalletEntity:
    id: UUID
    currency: CurrencyValueObject
    balance: MoneyValueObject
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    @classmethod
    def create_new(cls, currency_code: str, inital_amount: float = 0.0) -> "WalletEntity":

        currency : CurrencyValueObject = CurrencyValueObject(currency_code)
        balance: MoneyValueObject = MoneyValueObject( amount=Decimal(str(inital_amount)), currency=currency)

        return cls(
            id=uuid4(),
            currency=currency,
            balance=balance,
            is_active= True,
            created_at=datetime.now(),
        )

    def activate(self) -> "WalletEntity":
        if self.is_active:
            return self
        return replace(self, is_active=True, updated_at=datetime.now())

    def deactivate(self) -> "WalletEntity":
        if not self.is_active:
            return self
        return replace(self, is_active=False, updated_at=datetime.now())
