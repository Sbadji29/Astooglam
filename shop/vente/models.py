from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
  telephone = models.CharField(max_length = 20)
#  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']
  def __str__(self):
        return "{}".format(self.email)



class Categorie(models.Model):
    nom= models.CharField(max_length=100)
    description= models.TextField()
    image = models.ImageField(upload_to= 'categorie_image/')

    def __str__(self):
        return self.nom



class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()
    description = models.TextField()
    categorie = models.ForeignKey(Categorie,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(upload_to= 'produit_image/')

    def __str__(self):
        return self.nom



class Contact(models.Model):
    email = models.EmailField(max_length=100)
    messages = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.date}"


 
class BonnesAffaire(models.Model):
    produit = models.ForeignKey(Produit,on_delete=models.SET_NULL,null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.produit} - {self.date}"
    


class Service(models.Model):
    nom = models.CharField(max_length=100)    

    def __str__(self):
        return self.nom
   


class Commande(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    date = models.DateField(auto_now_add=True)
    addresse = models.CharField(max_length=200,null=True)
    ville = models.CharField(max_length=200,null=True)

    def __str__(self):
        return f"{self.user} - {self.date}"
    


class DetailCommande(models.Model):
    commande = models.ForeignKey(Commande,on_delete=models.SET_NULL,null=True)
    produit = models.ForeignKey(Produit,on_delete=models.SET_NULL,null=True)
    quantite = models.IntegerField()
    prix = models.FloatField()

    def __str__(self):
        return f"{self.commande} - {self.prix}"
    


class Pub(models.Model):
    produit = models.ForeignKey(Produit,on_delete=models.SET_NULL,null=True)
    description = models.TextField()
    image = models.ImageField(upload_to= 'pub_image/')

    def __str__(self):
        return self.produit