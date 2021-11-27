from tortoise.models import Model
from tortoise import fields

#В нем содержится вся основная информация:
#  - email; CharField
#  - phone; CharField
#  - role (student, teacher, dean); Model
#  - full_name; CharField
#  - admission_year; IntField
#  - course; Model
#  - direction; Model
#  - group; Model
#  - mb course and direction in Model Group???
#  - student_number; IntField
#  - hostel; Bool? mb ChoiceField(Svechka, Studak, No)

class User(Model):
    id = fields.UUIDField(pk=True)
    email = fields.CharField(50)
    phone = fields.CharField(15)
    role = fields.ManyToManyField()
    full_name = fields.CharField(60)
    admission_year = fields.IntField()
