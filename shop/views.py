from django.shortcuts import render, redirect

from shop.models import Sort, Card, Customer, Order


def main_page(request):
    if request.method == 'GET':
        sorts = Sort.objects.all()
        context = {'sorts': sorts}
        return render(request, 'main_page.html', context)
    if request.method == 'POST' and 'order' in request.POST:
        return redirect('order')
    if request.method == 'POST':
        sort = request.POST['sort_name']
        return redirect('beer_page', sort)


def beer_page(request, sort):
    if request.method == 'GET':
        beer_sort = Sort.objects.get(name=sort)
        beers = beer_sort.beers.all()
        context = {'beers': beers, 'sort': beer_sort}
        return render(request, 'beer_page.html', context)

    if request.method == 'POST' and 'back' in request.POST:
        return redirect('main_page')

    if request.method == 'POST':
        value = request.POST.get('number')
        beer_sort = Sort.objects.get(name=sort)
        beers = beer_sort.beers.all()
        for beer in beers:
            if not request.POST.get(beer.beer_name):
                continue
            else:
                Card.objects.create(beer=beer.beer_name, value=value)
                context = {'beers': beers, 'sort': beer_sort, 'valid': 'Added to card'}
                return render(request, 'beer_page.html', context)


def order(request):
    if request.method == 'GET':
        beers = Card.objects.all()
        context = {'beers': beers}
        return render(request, 'order_page.html', context)
    elif request.method == 'POST' and 'back' in request.POST:
        return redirect('main_page')
    elif request.method == 'POST' and 'confirm' in request.POST:
        name = request.POST.get('name_1')
        address = request.POST.get('address')
        if not name or not address:
            beers = Card.objects.all()
            context = {'beers': beers, 'valid': 'Please, fill in your name and address'}
            return render(request, 'order_page.html', context)
        else:
            customer = Customer(name=name, address=address)
            customer.save()
            all_card = Card.objects.all()
            for orders in all_card:
                Order.objects.create(beer=orders.beer, value=orders.value, customer=customer)
            card = Card.objects.all()
            card.delete()
            return render(request, 'succ_page.html')
    else:
        id_del = request.POST.get('id')
        all_card = Card.objects.get(id=id_del)
        all_card.delete()
        beers = Card.objects.all()
        context = {'beers': beers}
        return render(request, 'order_page.html', context)




