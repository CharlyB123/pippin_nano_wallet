from tortoise.models import Model
from tortoise import fields

import rapidjson

class Block(Model):
    """A local storage of blocks we create, primarily for send blocks"""
    account  = fields.ForeignKeyField('db.Account', related_name='blocks', index=True)
    block_hash = fields.CharField(max_length=64, unique=True)
    block = fields.JSONField(encoder=rapidjson.dumps, decoder=rapidjson.loads)
    send_id = fields.CharField(max_length=64, null=True, index=True)
    subtype = fields.CharField(max_length=10)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = 'blocks'