"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from vente import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.accueil,name=""),
    path('apropos', views.apropos,name="apropos"),
    path('boutique/', views.boutique,name="boutique"),
    path('categorie/', views.categorie,name="categorie"),
    path('categorie/<int:category_id>/', views.categorie, name='categorie_filtre'),
    path('commande/', views.commande,name="commande"),
    path('condition_utilisation/',views.condition_utilisation,name="condition_utilisation"),
    path('connexion/',views.connexion,name="connexion"),
    path('contact/',views.contact,name="contact"),
    path('detail_commande/',views.detail_commande,name="detail_commande"),
    path('detail_produit/<int:produit_id>/', views.detail_produit, name="detail_produit"),
    path('panier/',views.panier,name="panier"),
    path('politique_confidentialite/',views.politique_confidentialite,name="politique_confidentialite"),
    path('profil/',views.profil,name="profil"),
    path('succee/',views.succee,name="succee"),
    path('recup_mdp_web/',views.recup_mdp_web,name="recup_mdp_web"),
    path('register/',views.register,name="register"),
    path('services/',views.services,name="services"),
    path('ajouter_au_panier/<int:produit_id>/',views.ajouter_au_panier,name="ajouter_au_panier"),
    path('incrementer/<int:produit_id>/',views.incrementer,name="incrementer"),
    path('decrementer/<int:produit_id>/',views.decrementer,name="decrementer"),
    path('supprimer/<int:produit_id>/',views.supprimer,name="supprimer"),
    path("enregistrer_commande/", views.enregistrer_commande, name="enregistrer_commande"),
    path("commande/", views.enregistrer_commande, name="commande"),
    path('confirmation_commande/<int:commande_id>/', views.confirmation_commande, name='confirmation_commande'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
