from django.shortcuts import render

# Create your views here.

def accueil(request):
    return render(request,'vente/accueil.html')


def apropos(request):
    return render(request,'vente/apropos.html')


def boutique(request):
    return render(request,'vente/boutique.html')


def categorie(request):
    return render(request,'vente/categorie.html')


def commande(request):
    return render(request,'vente/commande.html')


def condition_utilisation(request):
    return render(request,'vente/condition_utilisation.html')


def connexion(request):
    return render(request,'vente/connexion.html')


def contact(request):
    return render(request,'vente/contact.html')


def detail_commande(request):
    return render(request,'vente/detail_commande.html')


def detail_produit(request):
    return render(request,'vente/detail_produit.html')


def panier(request):
    return render(request,'vente/panier.html')


def politique_confidentialite(request):
    return render(request,'vente/politique_confidentialite.html')


def profil(request):
    return render(request,'vente/profil.html')


def recup_mdp_web(request):
    return render(request,'vente/recup_mdp_web.html')


def register(request):
    return render(request,'vente/register.html')


def services(request):
    return render(request,'vente/services.html')
