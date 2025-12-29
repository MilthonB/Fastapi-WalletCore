from typing import List
from uuid import UUID
from decimal import Decimal
from datetime import datetime

from domain.entities.wallet_entity import WalletEntity
from domain.value_objects.currency_value_object import CurrencyValueObject
from domain.value_objects.money_value_object import MoneyValueObject
from domain.contracts.repository.wallet_repository_domain import WalletRepository



class WalletRepositoryImp(WalletRepository):
    def get_wallet_by_id(self, wallet_id: UUID) -> WalletEntity:
        return WalletEntity(
            id=wallet_id,
            currency=CurrencyValueObject(code="USD"),
            balance=MoneyValueObject(amount=Decimal("10.0"), currency=CurrencyValueObject(code="USD")),
            is_active=True,
            created_at=datetime.now(),
        )
    def create_wallet(self, wallet: WalletEntity) -> WalletEntity:
         return WalletEntity(
            id=wallet.id,
            currency=wallet.currency,
            balance=MoneyValueObject(amount=Decimal("10.0"), currency=CurrencyValueObject(code="USD")),
            is_active=True,
            created_at=datetime.now(),
        )
    def update_wallet_by_id(self, wallet_id: UUID) -> WalletEntity:
        return WalletEntity(
            id=wallet_id,
            currency=CurrencyValueObject(code="USD"),
            balance=MoneyValueObject(amount=Decimal("20.0"), currency=CurrencyValueObject(code="USD")),
            is_active=True,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
    def delete_wallet_by_id(self, wallet_id: UUID) -> WalletEntity:
        return WalletEntity(
            id=wallet_id,
            currency=CurrencyValueObject(code="USD"),
            balance=MoneyValueObject(amount=Decimal("0.0"), currency=CurrencyValueObject(code="USD")),
            is_active=False,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
    def list_all_wallets(self) -> List[WalletEntity]:
        return [
            WalletEntity(
                id=UUID("123e4567-e89b-12d3-a456-426614174000"),
                currency=CurrencyValueObject(code="USD"),
                balance=MoneyValueObject(amount=Decimal("10.0"), currency=CurrencyValueObject(code="USD")),
                is_active=True,
                created_at=datetime.now(),
            ),
            WalletEntity(
                id=UUID("123e4567-e89b-12d3-a456-426614174001"),
                currency=CurrencyValueObject(code="EUR"),
                balance=MoneyValueObject(amount=Decimal("15.0"), currency=CurrencyValueObject(code="EUR")),
                is_active=True,
                created_at=datetime.now(),
            ),
        ]