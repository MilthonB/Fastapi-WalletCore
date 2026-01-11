


class DatasourcesExceptions(Exception):
    ...

class DatasourceConnectionError(DatasourcesExceptions):
    pass

class DatasourceTimeoutError(DatasourcesExceptions):
    pass

class DatasourceAuthError(DatasourcesExceptions):
    pass

class DatasourceIntegrityError(DatasourcesExceptions):
    pass