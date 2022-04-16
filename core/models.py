from distutils.command.upload import upload
import email
from datetime import datetime
from email import message
from email.policy import default
from pyexpat import model
from django.db import models
# from matplotlib.pyplot import cla

# Create your models here.


class Destination:
    id: int
    name: str
    img: str
    desc: str
    price: int


class State(models.Model):
    name = models.CharField(max_length=150)
    img = models.ImageField(upload_to="myimage", default="")
    desc = models.CharField(max_length=200)
    price = models.IntegerField()


class Slider(models.Model):
    img = models.ImageField(upload_to='slider', default="")


class News(models.Model):
    day = models.IntegerField()
    month = models.CharField(max_length=20)
    title = models.CharField(
        max_length=200, default="Best News About Rainfall in India")
    news_pic = models.ImageField(upload_to="news_pic", default="")
    news_desc = models.TextField()


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date=models.DateField(auto_now_add=True)

class Dataset(models.Model):
    SUBDIVISION = models.CharField(max_length=200)
    YEAR = models.IntegerField()
    JAN = models.FloatField()
    FEB = models.FloatField()
    MAR = models.FloatField()
    APR = models.FloatField()
    MAY = models.FloatField()
    JUN = models.FloatField()
    JUL = models.FloatField()
    AUG = models.FloatField()
    SEP = models.FloatField()
    OCT = models.FloatField()
    NOV = models.FloatField()
    DEC = models.FloatField()
    ANNUAL = models.FloatField()
    Jan_Feb = models.FloatField(db_column='Jan-Feb')
    Mar_May = models.FloatField(db_column='Mar-May')
    Jun_Sep = models.FloatField(db_column='Jun-Sep')
    Oct_Dec = models.FloatField(db_column='Oct-Dec')

class RegionDataset(models.Model):
    SUBDIVISION = models.CharField(max_length=200)
    YEAR = models.IntegerField()
    JAN = models.FloatField()
    FEB = models.FloatField()
    MAR = models.FloatField()
    APR = models.FloatField()
    MAY = models.FloatField()
    JUN = models.FloatField()
    JUL = models.FloatField()
    AUG = models.FloatField()
    SEP = models.FloatField()
    OCT = models.FloatField()
    NOV = models.FloatField()
    DEC = models.FloatField()
    ANNUAL = models.FloatField()
    Jan_Feb = models.FloatField(db_column='Jan-Feb')
    Mar_May = models.FloatField(db_column='Mar-May')
    Jun_Sep = models.FloatField(db_column='Jun-Sep')
    Oct_Dec = models.FloatField(db_column='Oct-Dec')
    Latitude = models.FloatField()
    Longitude = models.FloatField()