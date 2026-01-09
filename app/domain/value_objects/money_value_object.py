from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal

from .currency_value_object import CurrencyValueObject


@dataclass(frozen=True)
class MoneyValueObject:
    amount: Decimal
    currency: CurrencyValueObject

    def __post_init__(self) -> None:
        if self.amount < Decimal("0.00"):
            raise ValueError("Amount can not be negative")

        object.__setattr__(
            self,
            "amount",
            self.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        )

    def is_zero(self) -> bool:
        return self.amount == Decimal("0")
