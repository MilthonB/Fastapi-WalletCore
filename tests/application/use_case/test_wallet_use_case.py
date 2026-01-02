
import pytest
from uuid import uuid4, UUID
from datetime import datetime
from typing import List

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

def test_get_wallet_by_id():

    from app.application.dto.wallet_id_dto import WalletIdDTO
    from app.application.use_cases.wallet.get_wallet_by_id_use_case import WalletGetByIdUseCase
    # Arrage

    dto = WalletIdDTO(wallet_id=uuid4())

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

    use_case = WalletGetByIdUseCase(repository)

    # Act
    wallet_entity = use_case.execute(dto)
    
    # Assert
    # que el id sea el mismo que el id que obtuve de la consulta
    assert dto.wallet_id == wallet_entity.id
    
def  test_create_wallet():

    from app.application.dto.wallet_dto import WalletDto
    from app.application.use_cases.wallet.create_wallet_use_case import CreateWalletUseCase
    dto =  WalletDto(
        wallet_id = "d0660593-0ab5-4247-8ef3-01633455c64f",
        currency = "MXN",
        balance={"amount":"250.10"},
        is_active = True,
        created_at="2026-01-02T17:48:29Z",
        # datetime.now()
    )

    # entity = WalletMapper.dto_to_entity(dto):


    datasources =  WalletDatasourcesImp()
    repository = WalletRepositoryImp(datasources=datasources)


    use_case = CreateWalletUseCase(repository)

    entity: WalletEntity = use_case.execute(dto)



    assert entity.is_active
    assert isinstance(entity.id, UUID)


    ...


def test_delete_wallet_by_id():

    from app.application.dto.wallet_id_dto import WalletIdDTO
    from app.application.use_cases.wallet.delete_wallet_by_id_use_case import DeleteWalletByIdUseCase
    
    #Arrange
    dto = WalletIdDTO(wallet_id=uuid4())

    wallet = WalletEntity(
        id=dto.wallet_id,
        currency=CurrencyValueObject("MXN"),
        balance=MoneyValueObject(Decimal("0.00"), CurrencyValueObject("MXN")),
        is_active=True,
        created_at=datetime.now(),
    )

    datasources = WalletDatasourcesImp()
    datasources.create_wallet(wallet=wallet)

    repository = WalletRepositoryImp(datasources=datasources)

    use_case = DeleteWalletByIdUseCase(repository)




    #Act
    entity: WalletEntity = use_case.execute(dto)
    list_wallets =  datasources.list_all_wallets()

    #Assert
    assert entity.id == dto.wallet_id
    assert len(list_wallets) == 0


    ...

def test_list_all_wallets():

    from app.application.use_cases.wallet.list_all_wallet_use_case import ListAllWalletsUseCase
    
    wallet1 = WalletEntity(
        id=uuid4(),
        currency=CurrencyValueObject("MXN"),
        balance=MoneyValueObject(Decimal("0.00"), CurrencyValueObject("MXN")),
        is_active=True,
        created_at=datetime.now(),
    )

    wallet2 = WalletEntity(
        id=uuid4(),
        currency=CurrencyValueObject("MXN"),
        balance=MoneyValueObject(Decimal("0.00"), CurrencyValueObject("MXN")),
        is_active=True,
        created_at=datetime.now(),
    )

    datasources = WalletDatasourcesImp()

    datasources.create_wallet(wallet=wallet1)
    datasources.create_wallet(wallet=wallet2)

    repository = WalletRepositoryImp(datasources=datasources)

     
    use_case = ListAllWalletsUseCase(repository)


    entity: List[WalletEntity] = use_case.execute()

    assert entity[0].id == wallet1.id
    assert entity[1].id == wallet2.id
    assert len(entity) > 1

    ...
