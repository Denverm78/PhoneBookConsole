import Model
import View



def action():
    while True:
        choice = int(input('\nВыберите пункт: '))
        if choice == 1:
            View.printPhoneBook()
            View.main_menu()        
        elif choice == 2:
            add_contact()
            print('\nКонтакт добавлен\n')
        elif choice == 3:
            remove_contact()
            print('\nКонтакт удален\n')
        elif choice == 4:
            change_contact()
        elif choice == 5:
            find_contact()
        elif choice == 6:
            save_file()
            print('\nФайл сохранен!\n')
        else:
            exit()
        



def start():
    open_file()
    
    View.main_menu()
    action()



def open_file():
    with open(Model.path, "r", encoding="UTF-8") as data:
        contacts_list = data.read().split("\n")
        Model.phonebook = contacts_list

def save_file():
    with open(Model.path, "w", encoding="UTF-8") as data:
        data.write(('\n'.join(Model.phonebook)))

def add_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    last_name = input('Введите отчество: ')
    phone = input('Введите телефон: ')
    contact = f'{name}; {surname}; {last_name}; {phone};\n'
    Model.phonebook.append(contact)
    View.printPhoneBook()

def remove_contact():
    choice = int(input('Введите номер элемента для удаления: '))
    Model.phonebook.pop(choice)
    View.printPhoneBook()

def change_contact():
    choice = int(input('Введите номер элемента для изменения: '))
    choice2 = int(input('Что изменяем (0-имя, 1-фамилия, 2-отчество, 3-телефон): '))
    contact = Model.phonebook.pop(choice).split(';')
    print(contact)
    contact[choice2] = input('Введите новое значение: ')
    print(contact)
    Model.phonebook.insert(choice, ';'.join(contact))
    View.printPhoneBook()

def find_contact():
    find_contact = []
    find_string = input('\nВведите строку для поиска: ')
    for item in Model.phonebook:
        if find_string in item:
            find_contact.append(item)
    if find_contact:
        print('\nРезультаты поиска: ')
        for item in find_contact:
            print(item)
        print()
        View.main_menu()    
    else:
        print('\nНичего не найдено')
        View.main_menu()


