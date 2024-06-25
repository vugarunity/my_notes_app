import csv
import os
from datetime import datetime

FILE_NAME = 'notes.csv'
FIELDNAMES = ['id', 'title', 'body', 'timestamp']

def read_notes():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        return list(reader)

def write_notes(notes):
    with open(FILE_NAME, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES, delimiter=';')
        writer.writeheader()
        writer.writerows(notes)

def add_note():
    notes = read_notes()
    new_id = max([int(note['id']) for note in notes], default=0) + 1
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    notes.append({'id': new_id, 'title': title, 'body': body, 'timestamp': timestamp})
    write_notes(notes)
    print("Заметка успешно сохранена!")

def edit_note():
    notes = read_notes()
    note_id = input("Введите ID заметки для редактирования: ")
    for note in notes:
        if note['id'] == note_id:
            note['title'] = input(f"Введите новый заголовок заметки (старый: {note['title']}): ") or note['title']
            note['body'] = input(f"Введите новый текст заметки (старый: {note['body']}): ") or note['body']
            note['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            write_notes(notes)
            print("Заметка обновлена!")
            return
    print("Заметка с таким ID не найдена.")

def delete_note():
    notes = read_notes()
    note_id = input("Введите ID заметки для удаления: ")
    notes = [note for note in notes if note['id'] != note_id]
    write_notes(notes)
    print("Заметка удалена!")

def list_notes():
    notes = read_notes()
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата: {note['timestamp']}")
        print(f"Текст: {note['body']}\n")

