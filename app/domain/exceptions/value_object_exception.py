
class ValueObjectException(Exception):
    ...

class InvalidCurrencyError(ValueObjectException):
    ...

class NegativeAmountError(ValueObjectException):
    ...

