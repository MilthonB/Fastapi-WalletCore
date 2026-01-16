
from typing import Protocol
from ...dto.wallet_currency_update_dto import WalletCurrencyUpdateDTO
from domain.entities.wallet_entity import WalletEntity

class UpdateWalletCurrencyUseCaseProtocol(Protocol):
    def execute(self, dto: WalletCurrencyUpdateDTO) -> WalletEntity:
        pass