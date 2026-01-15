
from typing import List, Dict
from ...domain.contracts.data_contract.wallet.wallet_data_contract import WalletDataContract
from datetime import datetime, timezone

IN_MEMORY_WALLET: Dict[str,WalletDataContract] = {}

def _seed_wallets()->None:
    wallets: List[WalletDataContract] = [
        WalletDataContract(
            wallet_id="202fdb60-5fd7-4ac5-bc1d-0828af07583a",
            currency="MXN",
            balance=1200,
            is_active=True,
            created_at=datetime.now(timezone.utc).isoformat(),
            updated_at=""
        ),
        WalletDataContract(
            wallet_id="f65b65bc-3ee9-4fc7-a286-57c6238f5189",
            currency="USD",
            balance=200,
            is_active=True,
            created_at=datetime.now(timezone.utc).isoformat(),
            updated_at=""
        ),
        WalletDataContract(
            wallet_id="1ef10861-b52b-449f-aac4-8ba44b07afb0",
            currency="GBP",
            balance=5200,
            is_active=True,
            created_at=datetime.now(timezone.utc).isoformat(),
            updated_at=""
        ),
        WalletDataContract(
            wallet_id="4fa2d46d-120b-4c70-bf8f-51e5c87f52d0",
            currency="CAD",
            balance=1900,
            is_active=True,
            created_at=datetime.now(timezone.utc).isoformat(),
            updated_at=""
        ),
        WalletDataContract(
            wallet_id="a0abe520-021e-42bf-996e-d4d90f7a4271",
            currency="NZD",
            balance=12000,
            is_active=True,
            created_at=datetime.now(timezone.utc).isoformat(),
            updated_at=""
        ),
         WalletDataContract(
            wallet_id="800318a6-8ada-488e-b35b-a7679a78c26e",
            currency="NZD",
            balance=0,
            is_active=True,
            created_at=datetime.now(timezone.utc).isoformat(),
            updated_at=""
        ),
    ]
    
    for wallet in wallets:
        IN_MEMORY_WALLET[wallet.wallet_id] = wallet


_seed_wallets()