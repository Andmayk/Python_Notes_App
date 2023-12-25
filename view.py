
class Message:
    def MainMenu(self):
        print()
        print("Выберите пункт меню:\n"
              "1. Добавить заметку.\n"
              "2. Вывести все заметки.\n"
              "3. Вывести заметки за дату.\n"
              "4. Изменить заметку.\n"
              "5. Удалить заметку.\n"
              "0. Выход.")

    def show_note(self, note):
        print(f"ID: {note['id']}; Заголовок: {note['title']};   Дата/время : {note['datetime']} ")
        print(f"Заметка: {note['body']}")
        print()

    def display_notes(self, notes):
        if not notes:
            print("Заметки не найдены.")
        else:
            print("-"*60)
            print("Заметки:")
            for note in notes:
                self.show_note(note)

    def display_notes_date(self, notes, date_note):
        bool: not_found_notes
        not_found_notes = True
        if not notes:
            print("Заметки не найдены.")
        else:
            print("-"*60)
            print(f"Заметки на дату {date_note}")
            for note in notes:
                if note['datetime'][0:10]==date_note:
                    self.show_note(note)
                    not_found_notes = False
        if not_found_notes:
            print(f"Заметки на дату {date_note} не найдены.")
        
    def display_notes_id(self, notes, id_note):
        bool: not_found_notes
        not_found_notes = True
        if not notes:
            print("Заметки не найдены.")
        else:
            print("-"*60)
            print(f"Заметка по ID {id_note}")
            for note in notes:
                if note['id']==id_note:
                    self.show_note(note)
                    not_found_notes = False
                    break
        if not_found_notes:
            print(f"Заметка по ID {id_note} не найдена.")
        
                