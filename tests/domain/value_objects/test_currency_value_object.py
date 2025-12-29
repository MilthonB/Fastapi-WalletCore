def test_currency_value_object_creation() -> None:
    from app.domain.value_objects.currency_value_object import CurrencyValueObject

    currency = CurrencyValueObject("USD")

    assert currency.code == "USD"


def test_currency_value_object_invalid_code() -> None:
    import pytest

    from app.domain.value_objects.currency_value_object import CurrencyValueObject

    with pytest.raises(ValueError):
        CurrencyValueObject("UERM")  # Invalid code, should be 3 letters
