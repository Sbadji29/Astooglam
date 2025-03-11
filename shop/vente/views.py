from django.shortcuts import get_object_or_404, render
from .models import *
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import ConnexionForm

def accueil(request):
    categories = Categorie.objects.all()  
    pubs = Pub.objects.all()
    produits = Produit.objects.all()  
    bonnesaffaire = BonnesAffaire.objects.all()
    return render(request,'vente/accueil.html',{'categories': categories, 'pubs': pubs,'produits': produits,'bonnesaffaires': bonnesaffaire})


def apropos(request):
    return render(request,'vente/apropos.html')


def boutique(request):
    produits = Produit.objects.all()  
    categories = Categorie.objects.all()  
    return render(request, 'vente/boutique.html', {'produits': produits, 'categories': categories})


def categorie(request,category_id=None):
    produits = Produit.objects.all()  
    categories = Categorie.objects.all() 
    if category_id:
        categorie_active = get_object_or_404(Categorie, id=category_id)
        produits = Produit.objects.filter(categorie=categorie_active)
    else:
        categorie_active = None
    return render(request,'vente/categorie.html', {'produits': produits, 'categories': categories, 'categorie_active': categorie_active})


def commande(request):
    if "panier" not in request.session:
        request.session["panier"] = []
    panier = request.session["panier"]

    produits = []
    sous_total=0
    total=0
    frais_livraison = 0
    for item in panier:
        sous_total+=item["prix"]*item["qte"]
        produit = get_object_or_404(Produit, id=item["produit_id"])
        produits.append({
            "nom": item["nom"],
            "qte": item["qte"],
            "prix": item["prix"],
            "categorie": produit.categorie.nom
        })
    commande = request.session.get("commande", {})
    ville = commande.get("ville", "")
    
    if ville == "Dakar":
        frais_livraison = 2000  
    elif ville == "Hors Dakar":
        frais_livraison = 5000 

    total = sous_total + frais_livraison


    context = {
        'panier': produits,  
        'sous_total': sous_total,  
        'commande': commande,  
        'frais_livraison': frais_livraison, 
        'total': total, 
    }

    return render(request,'vente/commande.html',context)


def enregistrer_commande(request):
    if request.method == "POST":
        prenom = request.POST.get("prenom")
        nom = request.POST.get("nom")
        telephone = request.POST.get("telephone")
        ville = request.POST.get("ville")
        adresse = request.POST.get("adresse")

        print("Commande enregistrée :", prenom, nom, telephone, ville, adresse)

        request.session["commande"] = {
            "prenom": prenom,
            "nom": nom,
            "telephone": telephone,
            "ville": ville,
            "adresse": adresse
        }

        return redirect("detail_commande")  
        
    return render(request, "vente/commande.html")
def condition_utilisation(request):
    return render(request,'vente/condition_utilisation.html')


def connexion(request):
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("accueil")  
            else:
                messages.error(request, "Email ou mot de passe incorrect.")
    else:
        form = ConnexionForm()
    
    return render(request, 'vente/connexion.html', {'form': form})


def contact(request):
    if request.method == "POST":
        email = request.POST.get("email")
        message = request.POST.get("message")

        if email and message:
            try:
                send_mail(
                    subject="Nouveau message de contact",
                    message=f"Email: {email}\n\nMessage:\n{message}",
                    from_email=email,  
                    recipient_list=["ton_email@gmail.com"],  
                    fail_silently=False,
                )
                messages.success(request, "Votre message a été envoyé avec succès !")
            except Exception as e:
                messages.error(request, "Erreur lors de l'envoi du message.")

        return redirect("contact")  

    return render(request, "vente/contact.html")


def detail_commande(request):
    if "panier" not in request.session:
        request.session["panier"] = []

    panier = request.session["panier"]
    produits = []
    sous_total = 0
    total=0
    frais_livraison=0

    for item in panier:
        sous_total += item["prix"] * item["qte"]
        produit = get_object_or_404(Produit, id=item["produit_id"])
        produits.append({
            "nom": item["nom"],
            "qte": item["qte"],
            "prix": item["prix"],
            "categorie": produit.categorie.nom
        })

    commande = request.session.get("commande", {})
    ville = commande.get("ville", "")
    if ville == "Dakar":
        frais_livraison = 2000  
    elif ville == "Hors Dakar":
        frais_livraison = 5000 
    total = sous_total + frais_livraison

    context = {
        'panier': produits,
        'sous_total': sous_total,
        'commande': commande,
        'frais_livraison': frais_livraison,
        'total': total,
    }

    return render(request, 'vente/detail_commande.html', context)



def detail_produit(request, produit_id):  
    produit = get_object_or_404(Produit, id=produit_id)
    return render(request, 'vente/detail_produit.html', {'produit': produit})


def panier(request):
    if "panier" not in request.session:
        request.session["panier"]=[]
    panier=request.session["panier"]
    total=0
    for item in panier:
        total+=item["prix"]*item["qte"]
    context={'panier':panier,'total':total}
    return render(request,'vente/panier.html',context)

def politique_confidentialite(request):
    return render(request,'vente/politique_confidentialite.html')


def profil(request):
    return render(request,'vente/profil.html')


def recup_mdp_web(request):
    return render(request,'vente/recup_mdp_web.html')


def register(request):
    if request.method == "POST":
        prenom = request.POST.get("prenom")
        nom = request.POST.get("nom")
        telephone = request.POST.get("telephone")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=email).exists():
            messages.error(request, "Cet email est déjà utilisé.")
            return redirect("register")

        user = User.objects.create_user(username=email, first_name=prenom, last_name=nom, email=email, password=password)
        user.save()

        login(request, user)

        messages.success(request, "Inscription réussie ! Vous êtes maintenant connecté.")
        return redirect("home") 

    return render(request, "vente/register.html")


def services(request):
    services = Service.objects.all()
    return render(request,'vente/services.html',{'services':services})


def ajouter_au_panier(request,produit_id):
    if "panier" not in request.session:
        request.session["panier"]=[]
    panier=request.session["panier"]
    #{"produit_id":1,"qte":1,"img":1,"prix":1,"nom":1}
    trouver=False
    for item in panier:
        if produit_id == item["produit_id"]:
            trouver = True
            break
    if trouver ==False:
        produit=get_object_or_404(Produit, id=produit_id)
        item={"produit_id":produit.id,"qte":1,"img":produit.image.url,"prix":produit.prix,"nom":produit.nom}
        panier.append(item)
        request.session["panier"]=panier
    return redirect('/panier')

def incrementer(request,produit_id):
    if "panier" not in request.session:
        request.session["panier"]=[]
    panier=request.session["panier"]
    for item in panier:
        if produit_id == item["produit_id"]:
            item["qte"]+=1
    request.session["panier"]=panier
    return redirect('/panier')

def decrementer(request,produit_id):
    if "panier" not in request.session:
        request.session["panier"]=[]
    panier=request.session["panier"]
    for item in panier:
        if produit_id == item["produit_id"]:
            if item["qte"] >1:
                item["qte"]-=1
    request.session["panier"]=panier
    return redirect('/panier')

def supprimer(request,produit_id):
    if "panier" not in request.session:
        request.session["panier"] = []
    panier = request.session["panier"]

    indice = None
    for ind, item in enumerate(panier):
        if produit_id == item["produit_id"]:
            indice = ind
            break

    if indice is not None:
        panier.pop(indice)
    request.session["panier"]=panier
    return redirect('/panier')

def succee(request):
    return render(request,'vente/succee.html')

def confirmation_commande(request, commande_id):
    commande = get_object_or_404(Commande, id=commande_id)
    details = DetailCommande.objects.filter(commande=commande)

    return render(request, 'vente/confirmation_commande.html', {'commande': commande,'details': details})
