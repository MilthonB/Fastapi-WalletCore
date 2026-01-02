

from ...dto.wallet_id_dto import WalletIdDTO
from ....domain.entities.wallet_entity import WalletEntity
from typing import Protocol



class DeleteWalletByIdUseCaseProtocol(Protocol):
    def execute(self, dto: WalletIdDTO) -> WalletEntity:
        pass