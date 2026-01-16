
from uuid import uuid4, UUID
from datetime import datetime, timezone

from app.infrastructure.datasources.inMemory.wallet_inMemory_imp import WalletDatasourcesImp
from app.domain.contracts.data_contract.wallet.wallet_data_contract import WalletDataContract



def test_update_wallet_currency_success() -> None:

    # Arrange
    datasources = WalletDatasourcesImp()
    wallet_uuid:str = "800318a6-8ada-488e-b35b-a7679a78c26e"

    wallet = WalletDataContract(
        wallet_id=wallet_uuid,
        currency="MXN",
        balance="0.00",
        is_active=True,
        created_at=datetime.now(timezone.utc).isoformat(),
        updated_at=""
    )
    
    # Act
    wallet_contract:WalletDataContract = datasources.update_wallet_by_id(wallet=wallet)

    # Assert
    assert isinstance(wallet_contract, WalletDataContract)
    assert wallet.wallet_id == wallet_uuid
    assert wallet.currency == "MXN"





def test_get_wallet_by_id() -> None:

    # Arrage
    datasources = WalletDatasourcesImp()

    # Act
    wallet_contract = datasources.get_wallet_by_id(UUID("800318a6-8ada-488e-b35b-a7679a78c26e"))
    
    # Assert
    # que el id sea el mismo que el id que obtuve de la consulta
    assert wallet_contract.wallet_id == "800318a6-8ada-488e-b35b-a7679a78c26e"
    
def test_create_wallet() -> None:

    uuid_str: str = str(uuid4())
    wallet:WalletDataContract = WalletDataContract(
            wallet_id=uuid_str,
            currency="MXN",
            balance=1700,
            is_active=True,
            created_at=datetime.now(timezone.utc).isoformat(),
            updated_at=""
        )

    # entity = WalletMapper.dto_to_entity(dto):

    datasources =  WalletDatasourcesImp()


    #Act
    wallet_new = datasources.create_wallet(wallet=wallet)



    assert wallet_new.wallet_id == uuid_str


    ...


def test_delete_wallet_by_id() -> None:

    
    wallet_id = "202fdb60-5fd7-4ac5-bc1d-0828af07583a"

    datasources =  WalletDatasourcesImp()

    #Act
    wallet_del =  datasources.delete_wallet_by_id(UUID(wallet_id))


    #Assert
    assert wallet_del.wallet_id == wallet_id


    ...

def test_list_all_wallets() -> None:


    datasources = WalletDatasourcesImp()


    #act
    wallets = datasources.list_all_wallets(limit=10, offset=1)

   
    #asset
    assert len(wallets) > 1

    ...
