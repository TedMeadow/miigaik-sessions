from tortoise import models, fields
from tortoise.contrib.pydantic.creator import pydantic_model_creator


class Group(models.Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=40)
    course = fields.CharField(max_length=3)
    direction = fields.ForeignKeyField('models.Direction')


class Direction(models.Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=80)
    faculty = fields.ForeignKeyField('models.Faculty')

class Faculty(models.Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=100)

Group_Pydantic = pydantic_model_creator(Group, name='Group')
GroupIn_Pydentic = pydantic_model_creator(Group, name='GroupIn', exclude_readonly=True)

Direction_Pydantic = pydantic_model_creator(Direction, name='Direction')
DirectionIn_Pydentic = pydantic_model_creator(Direction, name='DirectionIn', exclude_readonly=True)

Faculty_Pydantic = pydantic_model_creator(Faculty, name='Faculty')
FacultyIn_Pydantic = pydantic_model_creator(Faculty, name='FacultyIn', exclude_readonly=True)