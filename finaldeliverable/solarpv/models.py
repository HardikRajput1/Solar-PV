from django.db import models

# Create your models here.

USER_TYPE= (('Client', 'Client'),
    ('Staff', 'Staff'))

PREFIX= (('Dr', 'Dr.'),
    ('Mr', 'Mr.'),
    ('Ms', 'Ms.'),
    ('Mrs', 'Mrs.'))

CLIENT_TYPE= (('Dealer', 'Dealer'),
    ('Retailer', 'Retailer'),
    ('Reseller', 'Reseller'))


class Client(models.Model):
    clientname = models.CharField(max_length=200)
    clienttype = models.CharField(max_length=8, choices=CLIENT_TYPE)
    def __str__(self):
        return self.clientname

class User(models.Model):
    userid = models.CharField(max_length=200, unique=True)
    first = models.CharField(max_length=200)
    middle = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    office = models.IntegerField()
    cell = models.IntegerField()
    prefix = models.CharField(max_length=3, choices=PREFIX)
    password = models.CharField(max_length=200)
    choose_user = models.CharField(max_length=6,choices=USER_TYPE)
    clientid = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.first + ' ' + self.last
    
class Location(models.Model):
    clientid = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    add = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.CharField(max_length=200)
    mobile = models.IntegerField()
    fax = models.IntegerField()
    def __str__(self):
        return self.city + ' ' + self.state
    
class Product(models.Model):
    modelnum = models.CharField(max_length=200)
    mname = models.CharField(max_length=50)
    celltech = models.CharField(max_length=200)
    cellmanu = models.CharField(max_length=200)
    cellnum = models.IntegerField()
    cellseries = models.IntegerField()
    cellstring = models.IntegerField()
    diodenum = models.IntegerField()
    prolen = models.IntegerField()
    prowid = models.IntegerField()
    prowei = models.IntegerField()
    superstrate = models.CharField(max_length=200)
    def __str__(self):
        return self.modelnum + ' ' + self.mname
    
class TestStandard(models.Model):
    stdname = models.CharField(max_length=50)
    describe = models.CharField(max_length=200)
    pubdate = models.DateField()
    def __str__(self):
        return self.stdname

class Certificate(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    locationid = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    reportnum = models.CharField(max_length=50)
    stdid = models.ForeignKey(TestStandard, on_delete=models.CASCADE, null=True)
    modelnum = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    certissue = models.DateField()
    def __str__(self):
        return self.reportnum
   