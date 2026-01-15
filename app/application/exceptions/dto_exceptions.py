


class DtoException(Exception):
    status_code:int=400
    ...

class InvalidCurrencyError(DtoException):
    status_code=422
    ...

class InvalidTypeError(DtoException):
    status_code=400
    ...

class InvalidBalanceError(DtoException):
    status_code=422
    ...

class InvalidValueError(DtoException):
    status_code=400
    ...





