#user/models.py
from django.db import models


# Create your models here.
class UserModel(models.Model):
    # class Meta:     # db table의 이름을 정해준다.(정보를 넣어준다)
    #     db_table = "my_user"
    email = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=256, null=False)

    def __init__(self,email,password):
        self.email = email
        self.password = password

