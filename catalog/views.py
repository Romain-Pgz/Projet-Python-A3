from catalog.models import Selection
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from catalog.forms import InscriptionForm,CommandeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def accueil(request):
    """View function for home page of site."""

    inscription = 'inscription'
    connexion = 'connexion'
    informations = 'informations'

#    
    context = {
        'inscription': inscription,
        'connexion': connexion,
        'informations': informations,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'accueil.html', context=context)
  
def commander(request):
    selection = Selection()
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            selection.choix = form.cleaned_data['choix']
            messages.info(request,'Vous avez commandé: ' + str(selection.choix))
            selection.choix.append(request.user.username)
            selection.save()
            return redirect('accueil')
    else:
        form = CommandeForm(initial={})
    context = {
        'form': form
    }
    return render(request, 'catalog/produit_list.html', context)
 

    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('accueil'))
    
def renew_inscription(request):
    form = InscriptionForm()
    if request.method == 'POST':
        form =  InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data['username']
            messages.success(request,'Vous êtes maintenant inscrit(e) ' + user + ' !')
            return redirect('user_login')
            
    context = {'form':form}
    return render(request, 'catalog/inscription.html',context)
    
def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('accueil')
        else:
            messages.info(request,'Username or password in incorrect')
    context = {}
    return render(request,'catalog/user_login.html',context)
