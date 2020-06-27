from src.shared.general_utils import GeneralEntity
from src.user.domain import UserEntity
from src.user.repository import UserRepository


class UserMongoRepository(UserRepository):

    def find_by_id(self, entity_id) -> GeneralEntity:
        return UserEntity.objects(id=entity_id)

    def update(self, entity: GeneralEntity) -> GeneralEntity:
        return entity.update()

    def delete_by_id(self, entity_id):
        entity = UserEntity.objects(id=entity_id)
        if entity:
            entity.delete()

    def save(self, entity: GeneralEntity) -> UserEntity:
        return entity.save()
