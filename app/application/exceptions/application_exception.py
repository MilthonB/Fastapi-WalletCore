
# from ...domain.exceptions.entity_exception import WalletInactiveError, WalletWithBalanceError
from app.domain.exceptions.entity_exception import InvalidWalletDataError, WalletInactiveError, WalletWithBalanceError
from app.domain.exceptions.value_object_exception import InvalidCurrencyError, NegativeAmountError
from typing import Tuple, Dict, Type
class ApplicationException(Exception):
    def __init__(self, message:str, status_code:int|None = None)-> None:
        super().__init__(message)

        self.status_code =  status_code or 400
    ...

"""Excepciones de Entidad de Wallet"""
class WalletInactiveAppError(ApplicationException):
    """Se lanza al intentar operar en una wallet inactiva"""
    ...

class WalletWithBalanceAppError(ApplicationException):
    """Se lanza cuando tratas de cambia la moneda con saldo pendiente"""
    ...

class InvalidWalletDataAppError(ApplicationException):
    """Se lanza cuando los datos de viene de fuera estan corruptos"""
    ...

class InvalidCurrencyAppError(ApplicationException):
    ...

class NegativeAmountAppError(ApplicationException):
    ...



DOMAIN_TO_APP: Dict[Type[Exception], Tuple[Type[ApplicationException], int]] = {
    WalletInactiveError: (WalletInactiveAppError, 400),
    WalletWithBalanceError: (WalletWithBalanceAppError,409),
    InvalidWalletDataError: (InvalidWalletDataAppError,500),
    InvalidCurrencyError: (InvalidCurrencyAppError, 422),
    NegativeAmountError:(NegativeAmountAppError, 422)
}

def translate_domain_error(exc:Exception, custom_message: str | None = None) -> ApplicationException:
    
    message:str = custom_message or str(exc)
    app_class, code =  DOMAIN_TO_APP.get(type(exc), (ApplicationException, 400)) 
    
    return app_class(message=message, status_code=code)

