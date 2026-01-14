from fastapi import APIRouter, Depends, Path, Query
from typung import List

from ..dependencies.wallet_dependencies import get_wallet_controller
from ..controllers.wallet.wallet_controller import WalletController
from ...application.dto_response.wallet.wallet_dto_response import WalletResponseDTO
from ...application.dto.wallet_dto import WalletDto

router: APIRouter = APIRouter(prefix="/wallets", tags=["wallets"])

@router.post("/", response_model=WalletResponseDTO, response_model_exclude_none=True, status_code=201)
async def create_wallet(
    payload: WalletDto,
    controller: WalletController = Depends(get_wallet_controller)
)-> WalletResponseDTO:
    response: WalletResponseDTO = await controller.create_wallet(payload)

    return response


@router.get("/{wallet_id}", response_model=WalletResponseDTO)
async def get_wallet_by_id(
    wallet_id: str = Path(..., description="Wallet ID"),
    controller:WalletController = Depends(get_wallet_controller)
)->WalletResponseDTO:

    response:WalletResponseDTO = await controller.get_wallet_by_id(wallet_id=wallet_id)

    return response
    # return controller.get_wallet_by_id(wallet_id=wallet_id)


@router.patch("/{wallet_id}/currency", response_model=WalletResponseDTO, status_code=200)
async def update_wallet_currency(
    wallet_id:str,
    currency:str,
    controller:WalletController = Depends(get_wallet_controller)
) -> WalletResponseDTO:

    response:WalletResponseDTO  = await controller.update_wallet_by_id(wallet_id=wallet_id, currency=currency)

    return response

@router.delete("/{wallet_id}", response_model=WalletResponseDTO, status_code=200)
async def delete_wallet_by_id(
    wallet_id: str,
    controller:WalletController = Depends(get_wallet_controller)
) -> WalletResponseDTO:

    response: WalletResponseDTO =  await controller.delete_wallet_by_id(wallet_id=wallet_id)

    return response

@router.get("/all", response_model=List[WalletResponseDTO], status_code=200)
async def get_all_wallets(
    limit:int = Query(...),
    offset:int = Query(...),
    controller: WalletController = Depends(get_wallet_controller)
) -> List[WalletResponseDTO]:

    response: List[WalletResponseDTO] = await controller.list_all_wallets(limit=limit, offset=offset)

    return response

