from django.contrib import admin
from .models import *
from django.contrib import admin
from .models import Commande, DetailCommande, Produit

admin.site.register(User)
admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(Contact)
admin.site.register(BonnesAffaire)
admin.site.register(Service)
# admin.site.register(Commande)
admin.site.register(DetailCommande)
admin.site.register(Pub)

class DetailCommandeInline(admin.TabularInline):  # Ou admin.StackedInline pour une autre présentation
    model = DetailCommande
    extra = 1  # Nombre de lignes vides supplémentaires
    readonly_fields = ('produit', 'quantite', 'prix')  # Empêche la modification

class CommandeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'telephone', 'ville', 'total', 'date_commande')
    list_filter = ('date_commande', 'ville')
    search_fields = ('nom', 'prenom', 'telephone')
    inlines = [DetailCommandeInline]  # Ajoute les détails de commande

admin.site.register(Commande, CommandeAdmin)
