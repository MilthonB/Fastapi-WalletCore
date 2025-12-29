from decimal import Decimal


def test_money_value_object_creation() -> None:
    from app.domain.value_objects.currency_value_object import CurrencyValueObject
    from app.domain.value_objects.money_value_object import MoneyValueObject

    money = MoneyValueObject(
        amount=Decimal("150.00"), currency=CurrencyValueObject("USD")
    )

    assert money.amount == Decimal("150.00")
    assert money.currency.code == "USD"


def test_money_value_object_negative_amount() -> None:
    import pytest

    from app.domain.value_objects.currency_value_object import CurrencyValueObject
    from app.domain.value_objects.money_value_object import MoneyValueObject

    # from decimal import Decimal

    with pytest.raises(ValueError):
        MoneyValueObject(amount=Decimal("-10.00"), currency=CurrencyValueObject("USD"))
