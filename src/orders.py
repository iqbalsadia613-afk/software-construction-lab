def calculate_order_total(order):
    subtotal = 0

    for item in order["items"]:
        price = item["price"]
        quantity = item["qty"]

        if price > 0:
            if quantity > 0:
                subtotal = subtotal + price * quantity

    if order["member"] == True:
        if subtotal > 100:
            discount_amount = subtotal * 0.2
        else:
            if subtotal > 50:
                discount_amount = subtotal * 0.1
            else:
                discount_amount = 0
    else:
        discount_amount = 0

    subtotal = subtotal - discount_amount

    if order["country"] == "PK":
        shipping_cost = 5
    else:
        if order["country"] == "US":
            shipping_cost = 15
        else:
            shipping_cost = 25

    subtotal = subtotal + shipping_cost

    print("Total: " + str(subtotal))
    return subtotal