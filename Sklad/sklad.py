all_products = {'Store': {'apple': 10}}  # List
shopping_basket = {'Basket': {}}  # List

process = True

while process:
    service = input('Hi! Please identify yourself: (customer seller)')
    if service.lower() == 'customer':  # Customer

        question = bool(True)
        while question:
            question = input('What do u want to do? (purchase, change, remove) ')

            if question.lower() == 'purchase':
                print('We have: ', all_products['Store'])
                product_name = input('Name of product: ')
                if not product_name in all_products['Store']:
                    print('You have entered wrong name')
                    break

                product_count = int(input('Quantity: '))
                if all_products['Store'][product_name] < product_count:
                    print('Sorry, we have no that amount of ', product_name)
                    break

                if product_name in shopping_basket['Basket']:
                    shopping_basket['Basket'][product_name] = shopping_basket['Basket'][product_name] + product_count
                else:
                    shopping_basket['Basket'][product_name] = product_count  

                all_products['Store'][product_name] = all_products['Store'][product_name] - product_count

                print('Product added to basket')
                print(shopping_basket['Basket'])

            elif question.lower() == 'change':
                product_name = input('Name of product: ')

                if product_name in shopping_basket['Basket']:
                    shopping_basket['Basket'][product_name] = int(input('Change quantity: '))
                    print('Products in basket changed')
                    print(shopping_basket['Basket'])

                else:
                    print('Product not found')

            elif question.lower() == 'remove':
                product_name = input('Name of product: ')
                if product_name in shopping_basket['Basket']:
                    del shopping_basket['Basket'][product_name]
                    print('you successfully removed ', product_name)
                    print(shopping_basket['Basket'])
                else:
                    print('This product does not exist in your basket')
            elif question.lower() == 'products':
                print(shopping_basket['Basket'])

            elif question.lower() == 'back':
                question = False

    elif service.lower() == 'seller':  # Seller

        command = bool(True)
        while command:
            command = input('What do u want to do?')

            if command.lower() == 'change':
                product_name = input('Name of product: ')


                if product_name in all_products['Store']:
                    x = int(input('Change quantity: '))
                    all_products['Store'][product_name] = x
                    if x == 0:
                        del all_products['Store'][product_name]
                    elif x < 0:
                        print('Sorry, quantity < 0 not allowed ')
                        break
                    print('Products in store changed')
                    print(all_products)

                else:
                    product_count = int(input('Quantity: '))
                    all_products['Store'][product_name] = product_count
                    print('Product added to store')
                    print(all_products)

            elif command.lower() == 'products':
                print(all_products)

            elif command.lower() == 'back':
                break
    else:
        print('Good luck')
        process = False


