from datetime import datetime
from decimal import Decimal
from uuid import uuid4

# from domain.entities.wallet_entity import WalletEntity
from app.domain.entities.wallet_entity import WalletEntity
from app.domain.value_objects.currency_value_object import CurrencyValueObject
from app.domain.value_objects.money_value_object import MoneyValueObject


def test_wallet_activation() -> None:
    wallet = WalletEntity(
        id=uuid4(),
        currency=CurrencyValueObject("MXN"),
        balance=MoneyValueObject(
            amount=Decimal("100.00"), currency=CurrencyValueObject("MXN")
        ),
        is_active=False,
        created_at=datetime.now(),
    )

    activated = wallet.activate()
    assert activated.is_active
    assert activated.updated_at is not None


def test_wallet_deactivation() -> None:
    wallet = WalletEntity(
        id=uuid4(),
        currency=CurrencyValueObject("MXN"),
        balance=MoneyValueObject(
            amount=Decimal("100.00"), currency=CurrencyValueObject("MXN")
        ),
        is_active=True,
        created_at=datetime.now(),
    )

    deactivated = wallet.deactivate()
    assert deactivated.is_active is False
    assert deactivated.updated_at is not None
