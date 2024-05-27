from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.conf import settings

# Create your views here.

def add_card(request):
    if request.method == 'POST':
        form = ItemInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        data = Card.objects.all()
        return render(request, 'app/add_card.html',{'form':form, 'data':data})
    form = ItemInfoForm()
    data = Card.objects.all()
    return render(request, 'app/add_card.html', {'form': form})

def card_list(request):
    cards = Card.objects.all()
    return render(request, 'app/card_list.html', {'cards': cards})


def addtocard(request, pk):
    data = Card.objects.get(id=pk)
    if request.method == 'POST':
        card = request.session.get('card', [])
        card.add(pk)
        request.session['card'] = card
        form = ItemInfoForm()
        data = Card.objects.all()
        # return redirect('card')
    return render(request, 'app/show.html', {'cards': data, 'media_url': settings.MEDIA_URL})
