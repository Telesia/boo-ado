from django.shortcuts import render, redirect


def view_bag(request):
    """ A view to return the shopping bag """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product ot the shopping bag """

    quantity = int(request.POST.get('quantity'))
    # 'redirect_url' in name on hidden input on form with attirbute of request.path
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # create a variable to hold the bag but check first if bag is in session otherwise
    # create a new variable and it is a dictionary.
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    # overwrite the current bag variable with the update version
    request.session['bag'] = bag
    return redirect(redirect_url)
