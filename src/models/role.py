from tortoise import models, fields
from tortoise.contrib.pydantic.creator import pydantic_model_creator

class Role(models.Model):
    name = fields.CharField(max_length=20, pk=True)
    permissions = fields.ManyToManyField('models.Permission')

class Permission(models.Model):
    name = fields.CharField(pk=True, max_length=20)



Role_Pydentic = pydantic_model_creator(Role, name='Role')
RoleIn_Pydentic = pydantic_model_creator(Role, name='RoleIn', exclude_readonly=True)

Permisson_Pydentic = pydantic_model_creator(Permission, name='Permission')
PermissonIn_Pydentic = pydantic_model_creator(Permission, name='Permission', exclude_readonly=True)