


class DatasourcesExceptions(Exception):
    def __init__(self, message:str, status_code:int=500):
        super().__init__(message)
        self.status_code = status_code

class DatasourceConnectionError(DatasourcesExceptions):
    pass

class DatasourceTimeoutError(DatasourcesExceptions):
    pass

class DatasourceAuthError(DatasourcesExceptions):
    pass

class DatasourceIntegrityError(DatasourcesExceptions):
    pass

class DatasourceNotFoundError(DatasourcesExceptions):
    ...