# from django.shortcuts import render,redirect
# from .models import *
# from .forms import *
# from django.conf import settings

# # Create your views here.

# def add_card(request):
#     if request.method == 'POST':
#         form = ItemInfoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#         data = Card.objects.all()
#         return render(request, 'app/add_card.html',{'form':form, 'data':data})
#     form = ItemInfoForm()
#     data = Card.objects.all()
#     return render(request, 'app/add_card.html', {'form': form})

# def card_list(request):
#     cards = Card.objects.all()
#     return render(request, 'app/card_list.html', {'cards': cards})


# def addtocard(request, pk):
#     data = Card.objects.get(id=pk)
#     if request.method == 'POST':
#         card = request.session.get('card')
#         card.append(pk)
#         request.session['card'] = card
#         form = ItemInfoForm()
#         data = Card.objects.all()
#     return render(request, 'app/show.html', {'cards': data, 'media_url': settings.MEDIA_URL})



from django.shortcuts import render, redirect
from .models import Card
from .forms import ItemInfoForm
from django.conf import settings

def add_card(request):
    if request.method == 'POST':
        form = ItemInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('card_list')
    else:
        form = ItemInfoForm()
    return render(request, 'app/add_card.html', {'form': form})

def card_list(request):
    cards = Card.objects.all()
    return render(request, 'app/card_list.html', {'cards': cards})

def addtocard(request, pk):
    if 'card' not in request.session:
        request.session['card'] = []
    
    card_list = request.session['card']
    card_list.append(pk)
    request.session['card'] = card_list
    
    cards = [Card.objects.get(id=id) for id in card_list]
    return render(request, 'app/show.html', {'cards': cards, 'media_url': settings.MEDIA_URL})



