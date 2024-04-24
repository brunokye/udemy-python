def price_format(value):
    return f"R${value:,.2f}".replace(".", ",")


def cart_total_qtt(cart):
    return sum([item["quantity"] for item in cart.values()])
