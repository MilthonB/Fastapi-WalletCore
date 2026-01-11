
from ..dto.wallet_dto import WalletDto
from ...domain.entities.wallet_entity import WalletEntity
from ...domain.contracts.data_contract.wallet.wallet_data_contract import WalletDataContract

class WalletMapper():
    @staticmethod
    def dto_to_entity(dto: WalletDto) -> WalletEntity:
        return WalletEntity.create_new(
            currency=dto.currency,
            inital_amount=dto.balance,
        )

    @staticmethod
    def entity_to_data_contract(wallet_entity: WalletEntity) -> WalletDataContract:
        return WalletDataContract(
            wallet_id=str(wallet_entity.id),
            currency=wallet_entity.currency.code,
            balance=str(wallet_entity.balance.amount),
            is_active=wallet_entity.is_active,
            created_at=wallet_entity.created_at.isoformat(),
            updated_at=wallet_entity.updated_at.isoformat() if wallet_entity.updated_at else ""
            
        )

    @staticmethod
    def data_contract_to_entity(data_contract: WalletDataContract) -> WalletEntity:
        return WalletEntity.rehydrate(wallet_data_contract=data_contract)

    # @staticmethod
    # def json_to_data_contract(json: Dict[str, Any]) -> WalletDataContract:

    #     try:
    #         return WalletDataContract(

    #         )
    #     except Exception as error:
    #         raise ValueError("Error converting json to WalletDataContract:")


