
def calculate_total_price(product_prices, discount, tax_rate=0):
    def apply_discount(price):
        return price * 0.9 if discount else price

    total_price = sum(apply_discount(price) for price in product_prices)
    return total_price * (1 + tax_rate)

# Usage examples:
print(calculate_total_price([100, 200, 300], True))
print(calculate_total_price([100, 200, 300], True, 0.2))
