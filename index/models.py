from django.contrib.auth.models import User
from django.db import models

# Create your models here.




class Group(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User)
    def __str__(self):
        return self.name;

class GroupMember(models.Model):
    groupId = models.ForeignKey(Group)
    member = models.ForeignKey(User)
    def __str__(self):
        return self.member.email;
