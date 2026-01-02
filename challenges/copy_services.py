# Welcome Message
print('\nWelcome to Emelly Beatriz Pereira\'s Copy Service')
user_name = input('To get started, please enter your name: ')  
print(f'\nHello {user_name}! Please enter the type of service you want.')

def service_menu():
    '''
    Lists the available services at the copy shop, displaying identification codes, their descriptions, and unit prices
    '''
    print('DIG - Digitization - $1.10')
    print('ICO - Color Printing - $1.00')
    print('IPB - Black and White Printing - $0.40')
    print('FOT - Photocopy - $0.20 ')


def extra_service():
    '''
    Offers additional services or allows finishing without extras. 
    Validates user input and returns the additional cost
    '''
    print('\nWould you like to add any service? ')
    print('1 - Simple Binding - $15.00')
    print('2 - Hard Cover Binding - $40.00')
    print('3 - I do not want anything else')
    chosen_extra = int(input('>> '))
    while True:
        try: # validating the chosen extra service
            match(chosen_extra):
                case 1:
                    print('Simple Binding chosen: $15.00')
                    additional_cost = 15.00
                case 2:
                    print('Hard Cover Binding chosen: $40.00')
                    additional_cost = 40.00
                case 3:
                    additional_cost = 0
                    break    
                case _:
                    print('Invalid option! Please try again.')
                    continue
        except ValueError:
            print('Invalid option! Please try again.')
            continue
        return additional_cost
    

def number_of_pages():
    '''
    Requests and validates the number of pages for the service, in the range of 1 to 2000. 
    Calculates the discount based on the quantity
    '''
    max_pages = 2000
    min_pages =  1
    discount = 0
    
    # Validation of the number of pages
    number_of_pages = int(input('Enter the number of pages: '))     
    while min_pages < number_of_pages > max_pages:
        print('We do not accept that many pages at once. \nPlease try again. ')
        number_of_pages = 0
        number_of_pages = int(input('\nEnter the number of pages: '))  
        
        if number_of_pages <  20:
            discount = 0
        elif  20 <= number_of_pages < 200:
            discount = 0.15
        elif  200 <= number_of_pages < 2000:
            discount = 0.20
        elif 2000 <= number_of_pages > max_pages:
            discount = 0.25
        
    return number_of_pages, discount 

def choose_service():
    '''
    Displays the service menu via service_menu() and validates the user's choice. 
    Returns the unit price of the selected service
    '''
    while True:
        service_menu()
        chosen_service = input('>> ').upper()
        
        match(chosen_service):
            case 'DIG':
                service_cost = 1.10
            case 'ICO':
                service_cost = 1.00
            case 'IPB':
                service_cost = 0.40
            case 'FOT':
                service_cost = 0.20
            case _:
                print('\nInvalid choice, please enter the type of service again.')
                continue
        
        return service_cost
                
# Calling functions
service_cost = choose_service()
chosen_pages, discount = number_of_pages()
extra_cost = extra_service()

# Calculating total and applying discount
service_total = service_cost * chosen_pages
total_without_discount = service_total + extra_cost
discount_value = service_total * discount  # Discounting only on the service cost
discounted_pages = chosen_pages - (chosen_pages * discount)

total = total_without_discount - discount_value  # Final total with discount applied
print(f'Total to pay: $ {total:.2f} (Service: $ {service_cost:.2f} * Pages: {round(discounted_pages)} + Extra: $ {extra_cost:.2f})')