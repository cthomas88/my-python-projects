def tax_calc(cost, tax):

    total = cost * tax

    print(f'\nThe total amount to pay is ${total:.2f}')

users_item = float(input('How much does your item cost? $'))

users_tax = float(input('\nHow much is the tax in your area? '))

tax_calc(users_item, users_tax)
