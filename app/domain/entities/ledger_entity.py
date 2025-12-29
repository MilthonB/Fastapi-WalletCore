from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from domain.enums.ledger_direction_enum import LedgerDirection
from domain.value_objects.money_value_object import MoneyValueObject


@dataclass(frozen=True)
class LedgerEntity:
    id: UUID
    wallet_id: UUID
    transaction_id: UUID
    amount: MoneyValueObject
    direction: LedgerDirection
    created_at: datetime
