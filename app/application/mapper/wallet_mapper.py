

from ..dto.wallet_dto import WalletDto
from ...domain.entities.wallet_entity import WalletEntity

class WalletMapper():
    @staticmethod
    def dto_to_entity(dto: WalletDto) -> WalletEntity:
        return WalletEntity(
            id=dto.wallet_id,
            currency=dto.currency,
            balance=dto.balance,
            is_active=dto.is_active,
            created_at=dto.created_at,
            updated_at=dto.updated_at
        )



