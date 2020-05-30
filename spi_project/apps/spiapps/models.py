from __future__ import unicode_literals
from django.db import models
from django.db import connection
import re #, bcrypt
# from bycrypt import checkpw
import datetime 

PN_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+$')

class AFHS_Manager(models.Manager):
    def validatePartsData(self, postData):
        errors = []
        mytime=datetime.datetime.strptime(postData['part_date'], '%Y-%m-%d').date()
        time2 = datetime.datetime.today().date()
        if len(postData['part_pn']) < 1:
            errors.append("Part number should be more than 1 character long")
        if not PN_REGEX.match(postData['part_pn']):
            errors.append("Part number should contain: Letters, numbers, or one of these characters(. - / \\ or #)")
        if mytime > time2 :
            errors.append("Date shouldn't be a future date.")
        return errors

class AFHS(models.Model):
    source=models.CharField(max_length=255)
    date=models.DateField(default= datetime.date.today)
    PN=models.CharField(max_length=255, primary_key=True)   
    Description=models.CharField(max_length=255)
    part_type=models.CharField(max_length=255)
    cost=models.DecimalField(decimal_places=2, max_digits=8)
    fleet=models.CharField(max_length=255)
    ata=models.CharField(max_length=255)
    uom=models.CharField(max_length=255)
    object = AFHS_Manager()

class Airlines_Manager(models.Manager):
    def validatePartsData(self, postData):
        errors = []
        mytime=datetime.datetime.strptime(postData['part_date'], '%Y-%m-%d').date()
        time2 = datetime.datetime.today().date()
        if len(postData['part_pn']) < 1:
            errors.append("Part number should be more than 1 character long")
        if not PN_REGEX.match(postData['part_pn']):
            errors.append("Part number should contain: Letters, numbers, or one of these characters(. - / \\ or #)")
        if mytime > time2 :
            errors.append("Date shouldn't be a future date.")
        return errors

class Airlines(models.Model):
    source=models.CharField(max_length=255)
    date=models.DateField(default= datetime.date.today)
    PN=models.CharField(max_length=255, primary_key=True)   
    Description=models.CharField(max_length=255)
    part_type=models.CharField(max_length=255)
    cost=models.DecimalField(decimal_places=2, max_digits=8)
    fleet=models.CharField(max_length=255)
    ata=models.CharField(max_length=255)
    uom=models.CharField(max_length=255)
    object = Airlines_Manager()
 

class avref_Manager(models.Manager):
    def validatePartsData(self, postData):
        errors = []
        mytime=datetime.datetime.strptime(postData['update'], '%Y-%m-%d').date()
        time2 = datetime.datetime.today().date()
        if len(postData['part_pn']) < 1:
            errors.append("Part number should be more than 1 character long")
        if not PN_REGEX.match(postData['part_pn']):
            errors.append("Part number should contain: Letters, numbers, or one of these characters(. - / \\ or #)")
        if mytime > time2 :
            errors.append("Date shouldn't be a future date.")
        return errors
class avref(models.Model):
    p_sysid=models.AutoField(primary_key=True)
    p_part_nam=models.CharField(max_length=255)
    oldPN=models.CharField(max_length=255)
    PN=models.CharField(max_length=255) 
    p_cage=models.CharField(max_length=255) 
    p_nsn=models.CharField(max_length=255) 
    p_descript=models.CharField(max_length=255)
    Price=models.DecimalField(decimal_places=2, max_digits=8)
    p_condit=models.CharField(max_length=255)
    p_Type=models.CharField(max_length=255)
    p_update=models.DateField(default= datetime.date.today)
    p_unit=models.CharField(max_length=255)
    
    object = avref_Manager()   
class spiInv_Manager(models.Manager):
    def validatePartsData(self, postData):
        errors = []
        mytime=datetime.datetime.strptime(postData['part_date'], '%Y-%m-%d').date()
        time2 = datetime.datetime.today().date()
        if len(postData['part_pn']) < 1:
            errors.append("Part number should be more than 1 character long")
        if not PN_REGEX.match(postData['part_pn']):
            errors.append("Part number should contain: Letters, numbers, or one of these characters(. - / \\ or #)")
        if mytime > time2 :
            errors.append("Date shouldn't be a future date.")
        return errors

class spiInv(models.Model):
    # id=models.AutoField(primary_key=True)
    source=models.CharField(max_length=255)
    date=models.DateField(default= datetime.date.today)
    PN=models.CharField(max_length=255)   
    Description=models.CharField(max_length=255)
    part_type=models.CharField(max_length=255)
    cond=models.CharField(max_length=255)
    cost=models.DecimalField(decimal_places=2, max_digits=8)
    fleet=models.CharField(max_length=255)
    ata=models.CharField(max_length=255)
    uom=models.CharField(max_length=255)
    Serialized=models.CharField(max_length=255)
    LLP=models.CharField(max_length=255)
    Effectivity=models.CharField(max_length=255)
    object = spiInv_Manager()

class SatairList_Manager(models.Manager):
    def validatePartsData(self, postData):
        errors = []
        mytime=datetime.datetime.strptime(postData['part_date'], '%Y-%m-%d').date()
        time2 = datetime.datetime.today().date()
        if len(postData['part_pn']) < 1:
            errors.append("Part number should be more than 1 character long")
        if not PN_REGEX.match(postData['part_pn']):
            errors.append("Part number should contain: Letters, numbers, or one of these characters(. - / \\ or #)")
        if mytime > time2 :
            errors.append("Date shouldn't be a future date.")
        return errors

class SatairList(models.Model):
    source=models.CharField(max_length=255)
    date=models.DateField(default= datetime.date.today)
    PN=models.CharField(max_length=255, primary_key=True)   
    Description=models.CharField(max_length=255)
    part_type=models.CharField(max_length=255)
    Price=models.DecimalField(decimal_places=2, max_digits=8)
    fleet=models.CharField(max_length=255)
    ata=models.CharField(max_length=255)
    uom=models.CharField(max_length=255)
    object = SatairList_Manager()

class ILSQH_Manager(models.Manager):
    def validatePartsData(self, postData):
        errors = []
        mytime=datetime.datetime.strptime(postData['part_date'], '%Y-%m-%d').date()
        time2 = datetime.datetime.today().date()
        if len(postData['part_pn']) < 1:
            errors.append("Part number should be more than 1 character long")
        if not PN_REGEX.match(postData['part_pn']):
            errors.append("Part number should contain: Letters, numbers, or one of these characters(. - / \\ or #)")
        if mytime > time2 :
            errors.append("Date shouldn't be a future date.")
        return errors

class ILSQH(models.Model):
    date=models.DateField(default= datetime.date.today)
    PO_Number=models.FloatField()   
    PN=models.CharField(max_length=255, primary_key=True)
    Provided_Description=models.CharField(max_length=255)
    Stripped_part_Number=models.CharField(max_length=255)
    Quote_Description=models.CharField(max_length=255)
    Condition=models.CharField(max_length=255)
    Quantity=models.FloatField() 
    Quote_Price=models.DecimalField(decimal_places=2, max_digits=8)
    UM=models.CharField(max_length=255)
    Exchange=models.CharField(max_length=255)
    Quote_Date=models.DateField(default= datetime.date.today)
    
    object = ILSQH_Manager()

""" 
    class UsersManager(models.Manager):

        def validateLoginData(self, postData):
            errors = []
            if not postData['username']:
                errors.append("username is needed for login.")
            if not postData['password']:
                errors.append("Password is needed for login.")
            if Users.object.filter(username = postData['username']):
                obj= Users.object.get(username = postData['username'])
                temp=obj.password
                if not bcrypt.checkpw(postData['password'].encode(),temp.encode()):
                    errors.append("Invalid Password")
            else:
                errors.append( "There is no registered email address")

            if len(postData['password']) < 8:
                errors.append( "User password should be more than 8 characters")

            return errors

    class Users(models.Model):
        firstName = models.CharField(max_length=255)
        lastName = models.CharField(max_length=255)
        username = models.CharField(max_length=255)
        password = models.CharField(max_length=255)

        object = UsersManager() """