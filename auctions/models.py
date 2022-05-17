from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auctions(models.Model):
    seller = User.username

class Bid(models.Model):
    auctions = Auctions

class comments(models.Model):
    auctions = Auctions
