from webbrowser import get
from django.shortcuts import redirect, render
from django.http import HttpResponse
from listings.forms import contactUsForm
from listings.models import Listing, band
from django.core.mail import send_mail

def band_list(Request):
    return render(Request, 'listings/band_list.html',{'bands':band.objects.all()})

def band_details(req,aId):
    aBand=band.objects.get(id=aId)
    return render(req,'listings/band_details.html',{'band':aBand,'forListing':aBand.name.replace(" ","-")})

    
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
