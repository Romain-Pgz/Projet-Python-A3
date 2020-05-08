from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from catalog.models import Client,Selection,Produit
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class InscriptionForm(UserCreationForm):
    last_name = forms.CharField(required = True, label = 'Nom')
    first_name = forms.CharField(required = True, label = 'Prénom')
    email= forms.EmailField(required = True, label = 'Email')
    nombre_personnes = forms.IntegerField(required = True, label = 'Nombre de personnes dans le foyer')

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','nombre_personnes')
        
class Connexion(forms.ModelForm):
    username = forms.CharField(required = True, label = 'Username')
    password = forms.CharField(required=True,label='Mot de passe',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('password',)


class Info(forms.ModelForm):
    adresse = forms.CharField(required = True,label ='Adresse')
    nombre_personnes = forms.IntegerField(required = True, label = 'Nombre de personnes dans le foyer')

    class Meta:
        model = Client
        fields = ('nombre_personnes','adresse')

class CommandeForm(forms.ModelForm):
    def liste():
        l = []
        querySet = Produit.objects.all()
        for pdt in querySet:
            l.append((pdt.id_p,pdt.nom))
        return l
            
    choix = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices = [(x) for x in liste()])
    class Meta:
        model = Selection
        fields = ('choix',)
