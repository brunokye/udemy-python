def price_format(value):
    return f"R${value:,.2f}".replace(".", ",")


def cart_total_qtt(cart):
    return sum([item["quantity"] for item in cart.values()])


def cart_total(cart):
    return sum(
        [
            (
                item.get("quantitative_promotional_price")
                if item.get("quantitative_promotional_price")
                else item.get("quantitative_price")
            )
            for item in cart.values()
        ]
    )
