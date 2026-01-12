
# from ...domain.exceptions.entity_exception import WalletInactiveError, WalletWithBalanceError


class ApplicationException(Exception):
    ...

class ApplicationError(ApplicationException):
    ... 
    # @classmethod
    # def from_domain(cls, err:Exception) -> "ApplicationError":
    #     if isinstance(err, WalletInactiveError):
    #         return cls("La wallet esta incativa")
    #     if isinstance(err, WalletWithBalanceError):
    #         return cls("La wallet tiene saldo pendiente")
    #     return cls("Error de negocio")