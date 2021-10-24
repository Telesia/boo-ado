from django import template

# Further reading/ explanaiton at Django doc: custom template tags and filters
register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ A function to calculate the subtotal of the product(s) in the shopping bag """
    return price * quantity
