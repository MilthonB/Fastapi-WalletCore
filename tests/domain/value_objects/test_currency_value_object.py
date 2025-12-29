



def test_currency_value_object_creation():
    from app.domain.value_objects.currency_value_object import CurrencyValueObject

    currency = CurrencyValueObject("USD")

    assert currency.code == "USD"


def test_currency_value_object_invalid_code():
    from app.domain.value_objects.currency_value_object import CurrencyValueObject
    import pytest

    with pytest.raises(ValueError):
        CurrencyValueObject("UERM")  # Invalid code, should be 3 letters