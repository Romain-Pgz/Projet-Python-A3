from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid # Ce module est nécessaire à la gestion des identifiants unique (RFC 4122) pour les copies des livres
from django.contrib.auth.models import AbstractBaseUser

class Produit(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    nom = models.CharField(max_length=50, help_text='Enter field documentation')
    aliment = 'A'
    medicament = 'M'
    type_produit_choices = [(aliment,'A'),(medicament,'M'),]
    type_produit = models.CharField(max_length=1, choices=type_produit_choices,default=aliment)
    id_p = models.IntegerField(default=1)

    # Metadata
    class Meta: 
        ordering = ['nom']


    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.nom

    
class Client(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    adresse = models.CharField(max_length=500)
    nombre_personnes = models.IntegerField()

class Selection(models.Model):
#    client = models.ForeignKey(User,on_delete=models.CASCADE)
    choix = models.TextField(default = " ") 
    
    class Meta:
        ordering = ['choix']
        
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.choix
