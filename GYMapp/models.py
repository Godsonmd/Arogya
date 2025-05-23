from django.db import models

# Create your models here.
class reg(models.Model):
    reg_email=models.EmailField()
    reg_password=models.CharField(max_length=10)
    def __str__(self):
        return self.reg_email

class Gym(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    image=models.ImageField(upload_to='gymdp')
    link=models.CharField(max_length=1000)
    def __str__(self):
        return self.name
class trainer(models.Model):
    AVAILABILITY_CHOICES = [
  ('Now Available', 'Now Available'),
  ('Not Available', 'Not Available'),
  ]
    dr_name=models.CharField(max_length=100,null=True,blank=True)
    dr_email=models.EmailField()
    dr_password=models.CharField(max_length=10,null=True,blank=True)
    dr_image=models.ImageField(upload_to='gymdr',null=True,blank=True)
    dr_wa=models.CharField(max_length=10,null=True,blank=True)
    specialty=models.CharField(max_length=100,null=True,blank=True)
    availability = models.CharField(  max_length=20,  choices=AVAILABILITY_CHOICES,  default='Not Available',)
    def __str__(self):
        return self.dr_name+" "+self.dr_email