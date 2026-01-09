
from fastapi import HTTPException, status
from typing import Any, Dict
from ....domain.contracts.repository.wallet_repository_domain import WalletRepository
from ....application.dto.wallet_dto import WalletDto
from ....application.use_cases.wallet.create_wallet_use_case import CreateWalletUseCase
from ....application.protocolos.wallet.create_wallet_use_case_protocol import CreateWalletUseCaseProtocol
from ....domain.entities.wallet_entity import WalletEntity
class WalletController:

    def __init__(self, repository : WalletRepository) -> None:
        self.repository = repository

    
    def create_wallet(self, dto: WalletDto) -> WalletEntity:
        try:            
            use_case:CreateWalletUseCaseProtocol = CreateWalletUseCase(self.repository)

            wallet_entity: WalletEntity = use_case.execute(dto=dto)

            return wallet_entity

        except TypeError as typeError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(typeError)
            )
        
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error"
            )

        