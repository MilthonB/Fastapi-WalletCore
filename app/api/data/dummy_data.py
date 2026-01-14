
from typing import List, Dict
from ...domain.contracts.data_contract.wallet.wallet_data_contract import WalletDataContract
from uuid import uuid4
from datetime import datetime, timezone

IN_MEMORY_WALLET: Dict[str,WalletDataContract] = {}

def _seed_wallets()->None:
    wallets: List[WalletDataContract] = [
        WalletDataContract(
            wallet_id=str(uuid4()),
            currency="MXN",
            balance=1200,
            is_active=True,
            created_at=datetime.now(timezone.utc).isoformat(),
            updated_at=""
        ),
        WalletDataContract(
            wallet_id=str(uuid4()),
            currency="USD",
            balance=200,
            is_active=True,
            created_at=datetime.now(timezone.utc).isoformat(),
            updated_at=""
        ),
        WalletDataContract(
            wallet_id=str(uuid4()),
            currency="GBP",
            balance=5200,
            is_active=True,
            created_at=datetime.now(timezone.utc).isoformat(),
            updated_at=""
        ),
        WalletDataContract(
            wallet_id=str(uuid4()),
            currency="CAD",
            balance=1900,
            is_active=True,
            created_at=datetime.now(timezone.utc).isoformat(),
            updated_at=""
        ),
        WalletDataContract(
            wallet_id=str(uuid4()),
            currency="NZD",
            balance=12000,
            is_active=True,
            created_at=datetime.now(timezone.utc).isoformat(),
            updated_at=""
        )
    ]
    
    for wallet in wallets:
        IN_MEMORY_WALLET[wallet.wallet_id] = wallet


_seed_wallets()