
import pytest
from uuid import uuid4
from datetime import datetime

from app.infrastructure.datasources.inMemory.wallet_inMemory_imp import WalletDatasourcesImp
from app.application.dto.wallet_currency_update_dto import WalletCurrencyUpdateDTO
from app.application.use_cases.wallet.update_wallet_currency_use_case import UpdateWalletCurrencyUseCase
from app.infrastructure.repository.wallet_repository_imp import WalletRepositoryImp
from app.domain.entities.wallet_entity import WalletEntity
from app.domain.value_objects.currency_value_object import CurrencyValueObject
from app.domain.value_objects.money_value_object import MoneyValueObject
from decimal import Decimal



def test_update_wallet_currency_success() -> None:
    # Arrange
    dto = WalletCurrencyUpdateDTO(wallet_id=str(uuid4()), currency="USD")

    datasources = WalletDatasourcesImp()

    wallet = WalletEntity(
        id=dto.wallet_id,
        currency=CurrencyValueObject("MXN"),
        balance=MoneyValueObject(Decimal("0.00"), CurrencyValueObject("MXN")),
        is_active=True,
        created_at=datetime.now(),
    )

    datasources.create_wallet(wallet)

    repository = WalletRepositoryImp(datasources)
    use_case = UpdateWalletCurrencyUseCase(repository)

    # Act
    wallet_entity = use_case.execute(dto)

    # Assert
    assert isinstance(wallet_entity, WalletEntity)
    assert wallet_entity.id == dto.wallet_id
    assert wallet_entity.currency.code == "USD"
    assert wallet_entity.updated_at is not None

# def test_get_wallet_by_id():
    
#     # Arrage

#     dto = WalletGetByIdDTO(wallet_id:str(uuid4()))

#     datasources = WalletDatasourcesImp()

#     wallet = WalletEntity(
#         id=dto.wallet_id,
#         currency=CurrencyValueObject("MXN"),
#         balance=MoneyValueObject(Decimal("0.00"), CurrencyValueObject("MXN")),
#         is_active=True,
#         created_at=datetime.now(),
#     )

#     datasources.create_wallet(wallet)

#     repository = WalletRepositoryImp(datasources)

#     use_case = GetWalletByIdUseCase(repository)

#     # Act
#     wallet_entity = use_case.execute(dto)
    
#     # Assert
#     # que el id sea el mismo que el id que obtuve de la consulta
#     assert dto.wallet_id == wallet_entity.id
    
def  test_create_wallet():
    ...

def test_delete_wallet_by_id():
    ...

def test_list_all_wallets():
    ...
