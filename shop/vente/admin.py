from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(Contact)
admin.site.register(BonnesAffaire)
admin.site.register(Service)
admin.site.register(Commande)
admin.site.register(DetailCommande)
admin.site.register(Pub)

