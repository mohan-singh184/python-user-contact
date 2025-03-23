'''contacts = {}

while True:
    print('\ncontact book app')
    print('1. create contact')
    print('2. view contact')
    print('3. update contact')
    print('4. delete contact')
    print('5. search contact')
    print('6. count contact')
    print('7. exit')

    choice = input('Enter your choice =')

    if choice == '1':
        name = input('Enter your name = ')
        if name in contacts:
            print(f'contact name {name} already exists!')
        else:
            age = input('Enter age = ')
            email = input('Enter email = ')
            if '@' not in email  or not email.endswith('@gmail.com'):
                print('Invalid email! Email must contain "@" symbol, end with "@gmail.com" ')
            mobile = input('Enter mobile number =')
            if len(mobile) != 10 or not mobile.isdigit():
                print('Invalid mobile number! Mobile number must be exactly 10 digits.')
                continue
            contacts[name] = {'age':int(age), 'email':email, 'mobile':mobile}
            print(f'contact name {name} has been created successuflly!')

    elif choice == '2':
        name = input('Enter contact name to view =')
        if name in contacts:
            contacts = contacts[name]
            print(f'name: {name},age:{age},mobile number:{mobile}')
        else:
            print('contact not found!')

    elif choice == '3':
        name = input('Enter name to update contact =')
        if name in contacts:
            age = input('Enter update age =')
            email = input('Enter update email =')
            mobile = input('Enter update mobile number =')
            conatcts[name] = {'age':(age),'email':email,'mobile':mobile}
        else:
            print('contact not found!')
            
    elif choice == '4':
        name = input('Enter contact name to delete =')
        if name in contacts:
            del contacts[name]
            print(f'contact name {name} has been deleted succesfully!')
        else:
            print('contact not found')
            
    elif choice == '5':
        search_name = input('Enter contact name to search =')
        found = False
        for name,contact in contacts,item():
            if serach_name.lower() in name.lower():
                print(f'found - name {name}, age:{age}, mobile number:{mobile}, Email:{email}')
                found = True
        if not found:
            print('no contact found with that name')
    elif choice == '6':
       print(f'total contacts in your bool:{len(conatcts)}')
    elif choice == '7':
       print('good bye...closing the program')
       break
    else:
       print('Invalid input')'''

contacts = {}

while True:
    print('\ncontact book app')
    print('1. create contact')
    print('2. view contact')
    print('3. update contact')
    print('4. delete contact')
    print('5. search contact')
    print('6. count contact')
    print('7. exit')

    choice = input('Enter your choice =')

    if choice == '1':
        name = input('Enter your name = ')
        if name in contacts:
            print(f'contact name {name} already exists!')
        else:
            age = input('Enter age = ')
            email = input('Enter email = ')
            if '@' not in email  or not email.endswith('@gmail.com'):
                print('Invalid email! Email must contain "@" symbol and end with "@gmail.com" ')
                continue
            mobile = input('Enter mobile number =')
            if len(mobile) != 10 or not mobile.isdigit():
                print('Invalid mobile number! Mobile number must be exactly 10 digits.')
                continue
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f'contact name {name} has been created successfully!')

    elif choice == '2':
        name = input('Enter contact name to view =')
        if name in contacts:
            contact = contacts[name]
            print(f'name: {name}, age: {contact["age"]}, mobile number: {contact["mobile"]}, email: {contact["email"]}')
        else:
            print('contact not found!')

    elif choice == '3':
        name = input('Enter name to update contact =')
        if name in contacts:
            age = input('Enter update age =')
            email = input('Enter update email =')
            mobile = input('Enter update mobile number =')
            contacts[name] = {'age': age, 'email': email, 'mobile': mobile}
            print(f'contact name {name} has been updated successfully!')
        else:
            print('contact not found!')
            
    elif choice == '4':
        name = input('Enter contact name to delete =')
        if name in contacts:
            del contacts[name]
            print(f'contact name {name} has been deleted successfully!')
        else:
            print('contact not found!')
            
    elif choice == '5':
        search_name = input('Enter contact name to search =')
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'found - name: {name}, age: {contact["age"]}, mobile number: {contact["mobile"]}, email: {contact["email"]}')
                found = True
        if not found:
            print('no contact found with that name!')
            
    elif choice == '6':
        print(f'total contacts in your book: {len(contacts)}')
        
    elif choice == '7':
        print('goodbye... closing the program')
        break
        
    else:
        print('Invalid input')

                
















            
    
            
