from dataclasses import dataclass, replace
from datetime import datetime
from typing import Optional
from uuid import UUID

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

    def activate(self) -> "WalletEntity":
        if self.is_active:
            return self
        return replace(self, is_active=True, updated_at=datetime.now())

    def deactivate(self) -> "WalletEntity":
        if not self.is_active:
            return self
        return replace(self, is_active=False, updated_at=datetime.now())
