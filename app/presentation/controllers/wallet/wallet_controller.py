

from ....domain.contracts.repository.wallet_repository_domain import WalletRepository
from ....application.dto.wallet_dto import WalletDto
from ....application.dto.wallet_id_dto import WalletIdDTO
from ....application.use_cases.wallet.create_wallet_use_case import CreateWalletUseCase
from ....application.use_cases.wallet.get_wallet_by_id_use_case import WalletGetByIdUseCase
from ....domain.entities.wallet_entity import WalletEntity
from ....application.dto_response.wallet.wallet_dto_response import WalletResponseDTO
from ....application.dto.wallet_currency_update_dto import WalletCurrencyUpdateDTO
from ....application.mapper.wallet_mapper import WalletMapper
from ....application.use_cases.wallet.update_wallet_currency_use_case import UpdateWalletCurrencyUseCase 
from ....application.use_cases.wallet.delete_wallet_by_id_use_case import DeleteWalletByIdUseCase
from typing import List
from ....application.dto.wallet_limit_offsset import WalletLimitOffsetDto
from ....application.use_cases.wallet.list_all_wallet_use_case import ListAllWalletsUseCase

class WalletController:

    def __init__(self, repository : WalletRepository) -> None:
        self.repository = repository

    
    async def create_wallet(self, dto:WalletDto) -> WalletResponseDTO:
        # dto:WalletDto = WalletDto(currency=dto.currency, balance=dto.balance)

        use_case: CreateWalletUseCase = CreateWalletUseCase(self.repository)

        execute:WalletEntity = use_case.execute(dto)

        response =  WalletMapper.entity_to_dto_response(wallet_entity=execute)

        return response
 
    async def get_wallet_by_id(self, wallet_id:str)->WalletResponseDTO:
        dto: WalletIdDTO = WalletIdDTO(wallet_id)

        use_case:WalletGetByIdUseCase = WalletGetByIdUseCase(self.repository)
        execute:WalletEntity = use_case.execute(dto)

        response =  WalletMapper.entity_to_dto_response(execute)

        return response

    async def update_wallet_by_id(self, wallet_id:str, currency:str) -> WalletResponseDTO:
        dto: WalletCurrencyUpdateDTO = WalletCurrencyUpdateDTO(wallet_id, currency)

        use_case: UpdateWalletCurrencyUseCase = UpdateWalletCurrencyUseCase(self.repository)

        execute: WalletEntity =  use_case.execute(dto)
        
        response = WalletMapper.entity_to_dto_response(wallet_entity=execute)

        return response

    
    async  def delete_wallet_by_id(self, wallet_id:str) -> WalletResponseDTO:
        dto: WalletIdDTO = WalletIdDTO(wallet_id)

        use_case: DeleteWalletByIdUseCase = DeleteWalletByIdUseCase(self.repository)

        execute: WalletEntity = use_case.execute(dto)

        response = WalletMapper.entity_to_dto_response(execute)

        return response

    async def list_all_wallets(self, limit:int, offset:int) -> List[WalletResponseDTO]:
        dto: WalletLimitOffsetDto = WalletLimitOffsetDto(
            limit=limit, offset=offset)

        use_case: ListAllWalletsUseCase = ListAllWalletsUseCase(self.repository)

        execute:List[WalletEntity] = use_case.execute(dto)

        response:List[WalletResponseDTO] = [WalletMapper.entity_to_dto_response(entity) for entity in execute]

        return response
