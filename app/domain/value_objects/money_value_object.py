
from dataclasses import dataclass

from decimal import Decimal, ROUND_HALF_UP

@dataclass(frozen=True)
class MoneyValueObject:
    amount:Decimal
    currency:str = "MXN"

    def __post_init__(self):
        if self.amount < Decimal('0.00'):
            raise ValueError("Amount can not be negative")

        object.__setattr__(self, 'amount',self.amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

        