
from notes_backend import add_note, edit_note, delete_note, list_notes

def interface():
    while True:  
        print("\n1. Добавить заметку")
        print("2. Редактировать заметку")
        print("3. Удалить заметку")
        print("4. Показать все заметки")
        print("5. Выход")
        choice = input("Выберите действие: ")
        if choice == '1':
            add_note()
        elif choice == '2':
            edit_note()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            list_notes() 
        elif choice == '5':
            break  
        else:
            print("Неверный выбор. Попробуйте снова.")

    




    
