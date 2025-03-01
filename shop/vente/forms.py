from django import forms
from django.contrib.auth.models import User

class ConnexionForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder": "Adresse Email",
        "id": "compte"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Mot de passe",
        "id": "pwd"
    }))


class InscriptionForm(forms.ModelForm):
    prenom = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Prénom", "id": "prenom"}))
    nom = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Nom", "id": "nom"}))
    telephone = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Téléphone", "id": "telephone"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Adresse Email", "id": "email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Mot de passe", "id": "password"}))
    
    class Meta:
        model = User
        fields = ["prenom", "nom", "telephone", "email", "password"]
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]  
        user.set_password(self.cleaned_data["password"])  
        if commit:
            user.save()
        return user