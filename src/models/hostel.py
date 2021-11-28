from tortoise import models, fields
from tortoise.contrib.pydantic.creator import pydantic_model_creator

class Hostel(models.Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=150)

Hostel_Pydentic = pydantic_model_creator(Hostel, name='Hostel')
HostelIn_Pydentic = pydantic_model_creator(Hostel, name='HostelIn', exclude_readonly=True)