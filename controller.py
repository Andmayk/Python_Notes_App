import json
import datetime

from view import Message

message = Message()

class OpenInterface:

    __notes = []

    def __init__(self):
        self.message = Message()

    def StartApp(self):
        self.__notes = self.load_notes()
        AppRun = 1

        while AppRun == 1:
            message.MainMenu()
            act_comand = input("Введите команду: ")
            act_comand = act_comand.lower()

            match act_comand:
                case '1'|'add':
                    self.add_note()
                case '2'|'list':
                    message.display_notes(self.__notes)
                case '3':
                    date_find = input("Введите дату дд.мм.гггг: ")
                    message.display_notes_date(self.__notes, date_find)
                case '4'|'edit':
                    id_find = int(input("Введите ID заметки для редактирования: "))
                    self.edit_note_by_id(id_find)
                case '5'|'del':
                    id_find = int(input("Введите ID заметки для удаления: "))
                    self.del_note_by_id(id_find)
                case '0'|'':
                    AppRun = 0
                case _:
                    print("Не верная команда повторите ввод")
            print("-"*60)

        self.save_notes()


    def add_note(self):

        if self.__notes:
            last_id = self.__notes[-1]['id']
        else:
            last_id = 0

        note_title = input("Введите заголовок заметки: ")
        note_body = input("Введите заметку: ")
        note_datetime = datetime.datetime.now().strftime("%d.%m.%Y / %H:%M")

        note = {
            'id': last_id + 1,
            'title': note_title,
            'body': note_body,
            'datetime': note_datetime
        }
        self.__notes.append(note)
        self.save_notes()
        print("Заметка успешно сохранена.")

    def del_note_by_id(self, id_note):
        bool: not_found_notes
        not_found_notes = True
        if not self.__notes:
            print("Заметки не найдены.")
        else:
            print("-"*60)
            # print(f"Заметка по ID {id_note}")
            for note in self.__notes:
                if note['id']==id_note:
                    print("Заметка")
                    message.show_note(note)
                    not_found_notes = False
                    print("Найдена, УДАЛИТЬ? ")
                    act_key = input("Да / Нет (Y/N): ")
                    act_key = act_key.lower()
                    if ((act_key=="y") or (act_key=="д")):
                        self.__notes.remove(note)
                        print("Заметка удалена!")
                        self.save_notes()
                    else:
                        print("Заметка НЕ удалена!")
                    break
        if not_found_notes:
            print(f"Заметка по ID {id_note} не найдена.")

    def edit_note_by_id(self, id_note):
        bool: not_found_notes
        not_found_notes = True
        if not self.__notes:
            print("Заметки не найдены.")
        else:
            print("-"*60)
            # print(f"Заметка по ID {id_note}")
            for note in self.__notes:
                if note['id']==id_note:
                    print("Редактируем заметку")
                    message.show_note(note)
                    not_found_notes = False
                    note_title = input("Введите новый заголовок заметки: ")
                    note_body = input("Введите новый текст заметки: ")
                    note_datetime = datetime.datetime.now().strftime("%d.%m.%Y / %H:%M")
                    note['title'] = note_title
                    note['body'] = note_body
                    note['datetime'] = note_datetime
                    self.save_notes()
                    break
        if not_found_notes:
            print(f"Заметка по ID {id_note} не найдена.")

    def load_notes(self):
        try:
            with open('notes.json', 'r', encoding='utf-8') as file_json:
                return json.load(file_json)
        except FileNotFoundError:
            return []

    def save_notes(self):
        with open('notes.json', 'w', encoding='utf-8') as file_json:
            json.dump(self.__notes, file_json, indent=4, ensure_ascii=False)

