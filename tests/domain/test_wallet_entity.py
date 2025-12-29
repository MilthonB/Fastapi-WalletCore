
from uuid import uuid4
from datetime import datetime

#from domain.entities.wallet_entity import WalletEntity
from app.domain.entities.wallet_entity import WalletEntity
from app.domain.value_objects.currency_value_object import CurrencyValueObject




def test_wallet_activation():
    wallet = WalletEntity( id=uuid4(), currency=CurrencyValueObject("MXN"), is_active=False, created_at=datetime.now())

    activated = wallet.activate()
    assert activated.is_active
    assert activated.updated_at is not None


def test_wallet_deactivation():
    wallet = WalletEntity(id=uuid4(), currency=CurrencyValueObject("MXN"), is_active=True, created_at=datetime.now())

    deactivated = wallet.deactivate()
    assert deactivated.is_active is False
    assert deactivated.updated_at is not None