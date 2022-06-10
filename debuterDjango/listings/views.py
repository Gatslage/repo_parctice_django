from re import A
from webbrowser import get
from django.shortcuts import redirect, render
from django.http import HttpResponse
from listings.forms import contactUsForm,bandForm,annonceForm,annonceFormMod
from listings.models import Listing, band
from django.core.mail import send_mail

def band_list(Request):
    return render(Request, 'listings/band_list.html',{'bands':band.objects.all().reverse()})

def band_details(req,aId):
    aBand=band.objects.get(id=aId)
    return render(req,'listings/band_details.html',{'band':aBand,'forListing':aBand.name.replace(" ","-")})
def band_up(req,id=-1):
    if id==-1:
        form=bandForm()
        title='Enregistrement nouveau groupe'
        if(req.method =='POST'  ):
            if bandForm(req.POST).is_valid():
                form=bandForm(req.POST)
                newBand=form.save()
                return redirect('band-create')
    else:
        myBand=band.objects.get(id=id)
        if(req.method =='POST'):
            if bandForm(req.POST):
                form=bandForm(req.POST,instance=myBand)
                upBand=form.save()
                return redirect('band-details',upBand.id)
            
        title="Modification de ce groupe"
        form=bandForm(instance=myBand)
    return render(req,'listings/band_up.html',{'form':form,'title':title})
    
def band_del(req,id):
    myBand=band.objects.get(id=id)
    if(req.method=='POST'):
        myBand.delete()
        return redirect('band-list')
    
    return render(req,'listings/delete.html',{'object':myBand,'name':'le groupe','precedente':'band-list'})

def contactUs(request):
    if(request.method=='POST'):
        form=contactUsForm(request.POST)
        if(form.is_valid()):
            send_mail(subject=f'{form.cleaned_data["name"]}',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list='gamtchessiapollos@gmail.com')

            redirect('receive')
    else:
        form= contactUsForm()


    return render(request,"listings/contactUs.html",{'form':form})

def receive(req):
    return render(req,'listings/receive.html')

def aboutUs(request):

    return render(request,'listings/about-us.html')
# Create your views here.


def annonce(request,title="Actuelles",idBand=-1):
    title=("Annonces "+title).replace("-"," ")
    if(idBand==-1):
        return render(request,'listings/annonce_list.html',{'annonces':Listing.objects.all(),'title':title})
    else:
        return render(request,'listings/annonce_list.html',{'annonces':band.objects.get(id=idBand).listing_set.all,'title':title})

def annonce_up(req,id=-1):
    if id==-1:
        form=annonceForm()
        title='Enregistrement d\'une annonce'
        if(req.method =='POST'  ):
            if annonceForm(req.POST).is_valid():
                form=annonceForm(req.POST)
                newAnnonce=form.save()
                return redirect('annonce-create')
    else:
        myAnn=Listing.objects.get(id=id)
        if(req.method =='POST'):
            if annonceFormMod(req.POST).is_valid():
                form=annonceFormMod(req.POST,instance=myAnn)
                form.save()
                return redirect('annonce-list')

        title="Modifié mon annonce"
        form=annonceFormMod(instance=myAnn)
    return render(req,'listings/annonce_up.html',{'form':form,'title':title})
    
def annonce_del(req,id):
    Ann=Listing.objects.get(id=id)
    if req.method=='POST':
        Ann.delete()
        return redirect('annonce-list')
    return render(req,'listings/delete.html',{'object':Ann,'name':'l\'annonce','precedente':'annonce-list'})