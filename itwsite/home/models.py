from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Usr_Profile(models.Model):
    user = models.ForeignKey(User)
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField(default="abc@gmail.com")
    Room_number = models.CharField(max_length=6)
    Phone_number = models.CharField(max_length=10)
    user_mess = models.CharField(max_length=30)
    hostel_name = models.CharField(max_length=30)
    user_balance = models.IntegerField()
    user_expense = models.IntegerField()
    Branch_name = models.CharField(max_length=50)
    Year = models.CharField(max_length=4)
    #user_dp = models.ImageField()


    def __str__(self):
        return self.user_name


class Day(models.Model):
    name = models.CharField(max_length=10,default="not_set")
    breakfast = models.CharField(max_length=200)
    lunch = models.CharField(max_length=200)
    dinner = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Menu_mon(models.Model):
    mon = models.ForeignKey(Day)


class Menu_tue(models.Model):
    tue = models.ForeignKey(Day)


class Menu_wed(models.Model):
    wed = models.ForeignKey(Day)


class Menu_thr(models.Model):
    thr = models.ForeignKey(Day)


class Menu_fri(models.Model):
    fri = models.ForeignKey(Day)


class Menu_sat(models.Model):
    sat = models.ForeignKey(Day)


class Menu_sun(models.Model):
    sun = models.ForeignKey(Day)

class FirstLogin(models.Model):
    Maharaj = models.IntegerField(default=0)

class MessMaharaj(models.Model):
    user=models.ForeignKey(User)
    maharaj_name = models.CharField(max_length=30)
    maharaj_mess = models.CharField(max_length=30)
    maharaj_mob = models.CharField(max_length=10)
    tot_stud  = models.IntegerField(default=256)
    off_stud = models.IntegerField(default=24)
    veg_stud = models.IntegerField(default=126)
    #maharaj_dp = models.ImageField()

