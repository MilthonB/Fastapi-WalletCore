def test_ledger_creation() -> None:
    from datetime import datetime
    from decimal import Decimal
    from uuid import uuid4

    from app.domain.entities.ledger_entity import LedgerEntity
    from app.domain.enums.ledger_direction_enum import LedgerDirection
    from app.domain.value_objects.currency_value_object import CurrencyValueObject
    from app.domain.value_objects.money_value_object import MoneyValueObject

    ledger = LedgerEntity(
        id=uuid4(),
        wallet_id=uuid4(),
        transaction_id=uuid4(),
        amount=MoneyValueObject(Decimal("200.00"), CurrencyValueObject("MXN")),
        direction=LedgerDirection.CREDIT,
        created_at=datetime.now(),
    )

    assert ledger.amount.amount == Decimal("200.00")
    assert ledger.direction == LedgerDirection.CREDIT
