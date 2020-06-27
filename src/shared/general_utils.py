import datetime
import mongoengine as me
from marshmallow import Schema, fields
from abc import ABC, abstractmethod


class GeneralEntity(me.Document):
    """
    Generic entity to assign default values to all collections such as:
    created_at: Datetime when entity has been created
    updated_at: Datetime when entity has been updated
    """
    created_at = me.DateTimeField(db_field='createdAt')
    updated_at = me.DateTimeField(db_field='updatedAt', default=datetime.datetime.now)
    meta = {'abstract': True}

    def clean(self):
        if self.created_at is None:
            self.created_at = datetime.datetime.now


class GenericSchema(Schema):
    """
    Generic scheme to define common attributes
    """
    id = fields.String(db_field='_id')


class GeneralRepository(ABC):

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
