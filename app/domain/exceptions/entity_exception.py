

class EntityException(Exception):
    """ Base para error de logica de base en el estado de entidad"""
    ...

"""Excepciones de Entidad de Wallet"""
class WalletInactiveError(EntityException):
    """Se lanza al intentar operar en una wallet inactiva"""
    ...

class WalletWithBalanceError(EntityException):
    """Se lanza cuando tratas de cambia la moneda con saldo pendiente"""
    ...

class InfrastructureDataError(EntityException):
    """Se lanza cuando los datos de viene de fuera estan corruptos"""
    ...


"""Excepciones de Entidad de Transaction"""


"""Excepciones de Entidad de ledger"""
