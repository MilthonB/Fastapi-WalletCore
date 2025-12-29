
from uuid import UUID
from datetime import datetime
from dataclasses import dataclass, replace
from typing import Optional

from domain.enums.transaction_type_enum import TransactionType
from domain.enums.transaction_status_enum import TransactionStatus
from domain.value_objects.money_value_object import MoneyValueObject


@dataclass(frozen=True)
class TransactionEntity:
    id: UUID
    wallet_id: UUID
    amount: MoneyValueObject
    transaction_type: TransactionType  # e.g., 'deposit', 'withdrawal'
    status: TransactionStatus  # e.g., 'pending', 'completed', 'failed'
    created_at: datetime
    updated_at: Optional[datetime] = None

    def mark_completed(self) -> "TransactionEntity":
        if(self.status != TransactionStatus.PENDING):
            raise ValueError("Only pending transactions can be marked as completed.")

        return replace(self, status=TransactionStatus.COMPLETED, updated_at=datetime.now())