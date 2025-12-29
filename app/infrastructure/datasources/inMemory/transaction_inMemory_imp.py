from typing import List, Protocol
from uuid import UUID

from domain.entities.transaction_entity import TransactionEntity
from domain.enums.transaction_status_enum import TransactionStatus


class TransactionRepositoryImp(Protocol):
    def get_by_id(self, transaction_id: UUID) -> TransactionEntity: ...
    def create(self, transaction: TransactionEntity) -> TransactionEntity: ...
    def update_status(
        self, transaction_id: UUID, status: TransactionStatus
    ) -> TransactionEntity: ...
    def list_all(self) -> List[TransactionEntity]: ...
