from django.db import models
from django.conf import settings 
from django.db import models
# Create your models here.
User = settings.AUTH_USER_MODEL
class Voyage(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    num = models.IntegerField(primary_key=True)
    pays=models.CharField(max_length=30,null=True,blank=True)
    image=models.ImageField(null=True , blank=True)
    voyageDate = models.DateTimeField()
    prix = models.IntegerField()
    nmbPlace = models.IntegerField()

    def __str__(self):
        return self.pays
    
class utilisateur(models.Model):
    nom=models.CharField(max_length=30)
    prenom=models.CharField(max_length=30)
    email=models.EmailField()
    pw=models.CharField(max_length=30)
    def __str__(self):
        return self.email
    
class mess(models.Model):
    sender=models.CharField(max_length=30)
    emails=models.EmailField()
    msg=models.CharField(max_length=3000)
    def __str__(self):
        return self.sender

    

    
