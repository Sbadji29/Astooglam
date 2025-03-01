from django.shortcuts import get_object_or_404, render
from .models import *
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from .forms import ConnexionForm,InscriptionForm
# Create your views here.

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
    return render(request,'vente/commande.html')


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
    return render(request,'vente/detail_commande.html')


def detail_produit(request, produit_id):  
    produit = get_object_or_404(Produit, id=produit_id)
    return render(request, 'vente/detail_produit.html', {'produit': produit})


def panier(request):
    return render(request,'vente/panier.html')
    panier = request.session.get('panier', {})
    
    if produit_id in panier:
        del panier[produit_id]
    
    request.session['panier'] = panier
    return JsonResponse({'message': 'Supprimé du panier', 'panier': panier})

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
