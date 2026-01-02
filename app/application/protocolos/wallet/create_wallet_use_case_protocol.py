
from typing import Protocol
from ...dto.wallet_dto import WalletDto
from domain.entities.wallet_entity import WalletEntity

class CreateWalletUseCaseProtocol(Protocol):
    def execute(self, dto: WalletDto) -> WalletEntity :
        pass
