
from typing import Protocol
from ...dto.wallet_id_dto import WalletIdDTO
from domain.entities.wallet_entity import WalletEntity

class GetWalletByIdUseCaseProtocol(Protocol):
    def execute(self, dto: WalletIdDTO ) -> WalletEntity:
        ...
