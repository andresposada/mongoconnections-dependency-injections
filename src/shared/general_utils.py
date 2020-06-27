import datetime
import mongoengine as me
from marshmallow import Schema, fields


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
    id = fields.String(attribute='_id', data_key='id')
