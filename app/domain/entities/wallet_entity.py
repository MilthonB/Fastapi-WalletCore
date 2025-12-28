
from dataclasses import dataclass, replace
from uuid import UUID
from datetime import datetime
from typing import Optional

from domain.value_objects.currency_value_object import CurrencyValueObject

@dataclass(frozen=True)
class WalletEntity:
    id: UUID
    currency: CurrencyValueObject
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