from fastapi import APIRouter, Depends, Path

from ..dependencies.wallet_dependencies import get_wallet_controller
from ..controllers.wallet.wallet_controller import WalletController
from ...application.dto_response.wallet.wallet_dto_response import WalletResponseDTO

router: APIRouter = APIRouter(prefix="/wallets", tags=["wallets"])


@router.get("/{wallet_id}", response_model=WalletResponseDTO)
async def get_wallet_by_id(
    wallet_id: str = Path(..., description="Wallet ID"),
    controller:WalletController = Depends(get_wallet_controller)
)->WalletResponseDTO:

    wallet_entity = controller.get_wallet_by_id(wallet_id=wallet_id)

    return WalletResponseDTO(
        id=wallet_entity.id,
        currency=wallet_entity.currency.code,
        balance=wallet_entity.balance.amount,
        is_active=wallet_entity.is_active,
        created_at=wallet_entity.created_at.isoformat(),
        updated_at=wallet_entity.updated_at.isoformat() if wallet_entity.updated_at else None
    )

    # return controller.get_wallet_by_id(wallet_id=wallet_id)