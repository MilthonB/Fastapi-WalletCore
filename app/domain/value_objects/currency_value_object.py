from dataclasses import dataclass
from typing import ClassVar, List
from ..exceptions.value_object_exception import InvalidCurrencyError


@dataclass(frozen=True)
class CurrencyValueObject:
    code: str

    # VALID_CURRENCIES = {"USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD"}
    VALID_CURRENCIES: ClassVar[List[str]] = [
        "USD",
        "EUR",
        "GBP",
        "MXN",
        "AUD",
        "CAD",
        "CHF",
        "CNY",
        "SEK",
        "NZD",
    ]

    def __post_init__(self) -> None:
        if self.code not in self.VALID_CURRENCIES:
            raise InvalidCurrencyError(f"Currency '{self.code}' is not supported.")
