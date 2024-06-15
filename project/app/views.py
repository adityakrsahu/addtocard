from django.shortcuts import render, redirect
from .models import Card
from .forms import ItemInfoForm
from django.conf import settings

def add_card(request):
    if request.method == 'POST':
        form = ItemInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        data = Card.objects.all()
        return redirect('card_list')
    form = ItemInfoForm()
    data = Card.objects.all()
    if data:
        return render(request, 'app/add_card.html', {'form': form,'data':data}) 
    else:
        return render(request, 'app/add_card.html', {'form': form})


def card_list(request):
    cards = Card.objects.all()
    return render(request, 'app/card_list.html', {'cards': cards})

def addtocard(request, pk):
    if request.method == 'POST':
        quantity = request.session.get('quantity', [])
        quantity1 =int(request.POST.get('quantity'))
        quantity.append(quantity1)
        # print("quantity :",quantity)
        request.session['quantity'] = quantity
        cart = request.session.get('cart', [])
        cart.append(pk)
        request.session['cart'] = cart
        form = ItemInfoForm()
        data = Card.objects.all()
        return render(request,'app/card_list.html',{'form':form,'data':data,'media_url': settings.MEDIA_URL})
    return redirect('app/card_list.html')
    
