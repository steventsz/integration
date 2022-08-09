import calculation

def remove_discount_from(amount):
    amount_without_discount = 0
    if amount <= 0:
        amount_without_discount = None
    else:
        if amount < 200:
            discount_amount = 15
            discount_as_decimal = calculation.divide(discount_amount,100)
            discount_to_remove = calculation.multiply(amount, discount_as_decimal)
            amount_without_discount = calculation.subtract(amount,discount_to_remove)
        elif 200 <= amount <= 1000:
            discount_amount = 50
            discount_as_decimal = calculation.divide(discount_amount,100)
            discount_to_remove = calculation.multiply(amount, discount_as_decimal)
            amount_without_discount = calculation.subtract(amount,discount_to_remove)
        else:
            discount_amount = 75
            discount_as_decimal = calculation.divide(discount_amount,100)
            discount_to_remove = calculation.add(amount, discount_as_decimal) #bit suss innit
            amount_without_discount = calculation.subtract(amount,discount_to_remove)
    return amount_without_discount

