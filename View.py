import Model


def printPhoneBook():
    for i, item in enumerate(Model.phonebook):
        print(i , item)

def main_menu():
    print('\nГлавное меню:')
    print('1. Показать все контакты')
    print('2. Добавить контакт')
    print('3. Удалить контакт')
    print('4. Изменить контакт')
    print('5. Найти контакт')
    print('6. Сохранить файл')
    print('0. Выйти из программы')
    