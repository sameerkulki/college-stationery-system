from data import items, max_limit
# data.py contains the items and max_limit dictionary (any changes can be made directly there to avoid redundancy and inconsistency)

def get_discounted_cost(cart):
    total_cost = 0
    total_discount = 0
    for item in cart['items']:
        #calculate the total cost and total discount
        total_cost += items[item]['cost'] * cart['items'][item]
        total_discount = total_discount + \
            (items[item]['cost'] * items[item]
             ['discount'] * cart['items'][item])/100
    
    #if the total cost is less than 1000, no discount is applied
    if total_cost < 1000:
        total_discount = 0
    #if the total cost is greater than 3000, 5% additional discount is applied on the total cost - current discount
    if total_cost-total_discount >= 3000:
        total_discount = total_discount + ((total_cost-total_discount) * 0.05)
    
    total_cost = total_cost - total_discount
    total_cost = total_cost + total_cost * 0.1
    total_cost = format(total_cost, ".2f")
    total_discount = format(total_discount, ".2f")
    return total_cost, total_discount


def add_item_to_cart(cart, item, quantity):
    output = ""
    # if the item is not in the list of items
    if item not in items:
        output = "Item not found"
    else:
        if int(quantity) > max_limit[items[item]['category']]:
            output = "ERROR_QUANTITY_EXCEEDED"
            return cart, output
        if item in cart:
            cart['items'][item] += int(quantity)
            cart[items[item]['category']] = cart.get(
                items[item]['category'], 0) + int(quantity)
        else:
            cart['items'][item] = int(quantity)
            cart[items[item]['category']] = cart.get(
                items[item]['category'], 0) + int(quantity)
        output = "ITEM_ADDED"

    return cart, output
