from abc import abstractmethod
from src.shared.general_utils import GeneralRepository, GeneralEntity


class UserRepository(GeneralRepository):

    @abstractmethod
    def find_by_id(self, entity_id) -> GeneralEntity:
        pass

    @abstractmethod
    def save(self, entity: GeneralEntity) -> GeneralEntity:
        pass

    @abstractmethod
    def update(self, entity: GeneralEntity) -> GeneralEntity:
        pass

    @abstractmethod
    def delete_by_id(self, entity_id):
        pass
