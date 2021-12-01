from tortoise import models, fields
from tortoise.contrib.pydantic.creator import pydantic_model_creator


class User(models.Model):
    id = fields.UUIDField(pk=True)
    student_id = fields.IntField()
    email = fields.CharField(50)
    phone = fields.CharField(15)
    role = fields.ManyToManyField('models.Role')
    full_name = fields.CharField(60)
    admission_year = fields.IntField()
    group = fields.ForeignKeyField('models.Group')
    hostel = fields.ForeignKeyField('models.Hostel')
    password_hash = fields.CharField(max_length=200)
    class PydanticMeta:
        exclude = ['']
        

User_Pydentic = pydantic_model_creator(User, name='User')
UserIn_Pydentic = pydantic_model_creator(User, name='UserIn', exclude_readonly=True)

