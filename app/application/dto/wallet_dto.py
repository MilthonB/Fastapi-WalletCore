
from pydantic import BaseModel,field_validator, Field
from  uuid import UUID
from domain.value_objects.currency_value_object import CurrencyValueObject
from domain.value_objects.money_value_object import MoneyValueObject
from datetime import datetime
from typing import Optional, Any
from decimal import Decimal

class WalletDto(BaseModel):
    wallet_id: UUID
    currency: CurrencyValueObject
    balance: MoneyValueObject = Field(
        default_factory=lambda:MoneyValueObject(
            amount=Decimal("100.0"),
            currency=CurrencyValueObject("MXN")
        ))
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = Field(default=None)

    @field_validator("currency", mode="before")
    def validate_currency(cls, value: Any) -> CurrencyValueObject:

        if isinstance(value, CurrencyValueObject):
            return value

        if not isinstance(value, str):
            raise TypeError("Invalid currency type. A string is required")
        
        cur:str = value.strip()
        if len(cur) != 3:
            raise ValueError("Invalid currency length. Currency must be 3 characters long")
        
        currency_format =  CurrencyValueObject(cur.upper())
        return currency_format
    
    @field_validator("balance", mode="before")
    def validate_balance(cls, value: Any, info:Any) -> MoneyValueObject:
        
        if isinstance(value, MoneyValueObject):
            return value
        
        if not isinstance(value, dict):
            raise TypeError("Balance must be dic with amount and currency")
        
        amount = value.get("amount")

        if not isinstance(amount, (str, int, float, Decimal)):
            raise TypeError("Amount must be String")

        if amount is None:
            raise ValueError("Balance dict must contain amount")

        try:
            amount = Decimal(str(amount))
        except Exception:
            raise TypeError("Amount must be String")
        
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        
        currency = info.data.get("currency")
        if not isinstance(currency, CurrencyValueObject):
            raise TypeError("Currency must be a CurrencyValueObject")
        
        return MoneyValueObject(amount=amount,currency=currency)




