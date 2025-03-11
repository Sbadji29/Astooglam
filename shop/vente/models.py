from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

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
    prenom = models.CharField(max_length=100,default='Default Address')
    nom = models.CharField(max_length=100,default='Default nom')
    telephone = models.CharField(max_length=20,default='Default telephone')
    ville = models.CharField(max_length=100,default='Default ville')
    adresse = models.TextField()
    date_commande = models.DateTimeField(default=now)
    sous_total = models.DecimalField(max_digits=10, decimal_places=2)
    frais_livraison = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Commande de {self.nom} {self.prenom}"
    


class DetailCommande(models.Model):
    commande = models.ForeignKey(Commande,on_delete=models.SET_NULL,null=True)
    produit = models.ForeignKey(Produit,on_delete=models.SET_NULL,null=True)
    quantite = models.IntegerField()
    prix = models.FloatField()

    def __str__(self):
        if self.commande:  
            return f"Commande de {self.commande.prenom} {self.commande.nom} - Produit: {self.produit.nom} - {self.quantite} x {self.prix} FCFA"
        return f"Produit: {self.produit.nom} - {self.quantite} x {self.prix} FCFA (Commande supprimée)"
    


class Pub(models.Model):
    produit = models.ForeignKey(Produit,on_delete=models.SET_NULL,null=True)
    description = models.TextField()

    def __str__(self):
        return self.produit.nom if self.produit else "Pub sans produit"