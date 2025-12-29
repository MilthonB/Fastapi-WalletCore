from datetime import datetime
from decimal import Decimal
from uuid import uuid4

import pytest


def test_treasaction_cration() -> None:
    from app.domain.entities.transaction_entity import TransactionEntity
    from app.domain.enums.transaction_status_enum import TransactionStatus
    from app.domain.enums.transaction_type_enum import TransactionType
    from app.domain.value_objects.currency_value_object import CurrencyValueObject
    from app.domain.value_objects.money_value_object import MoneyValueObject

    transaction = TransactionEntity(
        id=uuid4(),
        wallet_id=uuid4(),
        amount=MoneyValueObject(Decimal("100.00"), CurrencyValueObject("MXN")),
        transaction_type=TransactionType.DEPOSIT,
        status=TransactionStatus.PENDING,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    assert transaction.id is not None
    assert transaction.wallet_id is not None
    assert transaction.amount.amount == Decimal("100.00")
    assert transaction.amount.currency == "MXN"
    assert transaction.transaction_type == TransactionType.DEPOSIT
    assert transaction.status == TransactionStatus.PENDING


def test_transaction_status_update() -> None:
    from app.domain.entities.transaction_entity import TransactionEntity
    from app.domain.enums.transaction_status_enum import TransactionStatus
    from app.domain.enums.transaction_type_enum import TransactionType
    from app.domain.value_objects.currency_value_object import CurrencyValueObject
    from app.domain.value_objects.money_value_object import MoneyValueObject

    transaction = TransactionEntity(
        id=uuid4(),
        wallet_id=uuid4(),
        amount=MoneyValueObject(Decimal("50.00"), CurrencyValueObject("MXN")),
        transaction_type=TransactionType.WITHDRAWAL,
        status=TransactionStatus.PENDING,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )

    completed_transaction = transaction.__class__(
        **{
            **transaction.__dict__,
            "status": TransactionStatus.COMPLETED,
            "updated_at": datetime.now(),
        }
    )

    assert completed_transaction.status == TransactionStatus.COMPLETED
    assert completed_transaction.updated_at is not None
    assert (
        transaction.status == TransactionStatus.PENDING
    )  # Original transaction remains unchanged

    with pytest.raises(ValueError):
        # failed_transaction = transaction.__class__(**{**transaction.__dict__, "status": TransactionStatus.FAILED, "updated_at": datetime.now()})
        completed_transaction.mark_completed()  # This should raise an error since it's not pending
