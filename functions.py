documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}


def people():
    numeric = 0
    document_number = (input('Введите номер документа: '))
    for document in documents:
        if document['number'] == document_number:
            print(f'Владелец документа: {document["name"]}')
            numeric += 1
    if numeric == 0:
        print('Документа с таким номером нет')
    print('\n')


def list_1():
    for document in documents:
        print(f'{document["type"]} {document["number"]} {document["name"]}')


def shelf():
    numeric = 0
    document_number = input('Введите номер документа: ')
    for directory in directories:
        for document in directories.get(directory):
            if document == document_number:
                numeric += 1
                print(f'Документ находится на полке: {directory}')
    if numeric == 0:
        print('Документа с таким номером на полках нет')
    print('\n')


def add_document():
    doc_doc = input('Введите название документа: ')
    doc_number = input('Введите номер документа: ')
    doc_name = input('Введите имя владельца документа: ')
    doc_shelf = input('Введите номер полки, где должен храниться документ: ')

    doc_dict = {"type": doc_doc, "number": doc_number, "name": doc_name}
    documents.append(doc_dict)

    numeric = 0

    for directory in directories:
        if doc_shelf == directory:
            directories[doc_shelf].append(doc_number)
            numeric += 1

    if numeric == 0:
        doc_list = [doc_number]
        directories.setdefault(doc_shelf, doc_list)
        # print(directories)

def print_names():
    for document in documents:
        try:
            print(document["name"])
        except(KeyError):
            print('У документа нет поля name')

def main():
    while True:
        user_input = input('Введите команду: ')
        if user_input == 'p':
            people()
            print('\n')
        elif user_input == 'l':
            list_1()
            print('\n')
        elif user_input == 's':
            shelf()
            print('\n')
        elif user_input == 'a':
            add_document()
            print('\n')
        elif user_input == 'q':
            break
        elif user_input == 'n': #для запуска новой команды необходимо ввести n
            print_names()
            print('\n')

main()