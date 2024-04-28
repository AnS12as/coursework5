from scr.db_manager import DBManager


def show_data(db_manager):
    print("Выберите данные для отображения:")
    print("1 - Работодатели")
    print("2 - Вакансии")
    choice = input("Введите выбор: ")

    if choice == '1':
        print("Список всех работодателей:")
        employers = db_manager.get_all_employers()
        for emp in employers:
            print(f"ID: {emp[0]}, Имя: {emp[1]}, Открытые вакансии: {emp[2]}")
    elif choice == '2':
        print("Список всех вакансий:")
        vacancies = db_manager.get_all_vacancies()
        for vac in vacancies:
            print(f"ID: {vac[0]}, Название: {vac[1]}, Зарплата от: {vac[2]}, Зарплата до: {vac[3]}, Ссылка: {vac[4]}")
    else:
        print("Неверный ввод, пожалуйста, попробуйте снова.")


def add_data(db_manager):
    print("Что вы хотите добавить?")
    print("1 - Работодатель")
    print("2 - Вакансия")
    choice = input("Введите выбор: ")

    if choice == '1':
        name = input("Введите имя работодателя: ")
        open_vacancies = input("Введите количество открытых вакансий: ")
        db_manager.insert_employer(name, int(open_vacancies))
        print("Работодатель добавлен.")
    elif choice == '2':
        name = input("Введите название вакансии: ")
        salary_from = input("Введите минимальную зарплату: ")
        salary_to = input("Введите максимальную зарплату: ")
        url = input("Введите URL вакансии: ")
        employer_id = input("Введите ID работодателя: ")
        db_manager.insert_vacancy(name, int(salary_from), int(salary_to), url, int(employer_id))
        print("Вакансия добавлена.")
    else:
        print("Неверный ввод, пожалуйста, попробуйте снова.")


def main_menu():
    actions = {
        '1': show_data,
        '2': add_data,
        '3': lambda db_manager: print("Выход из программы.")
    }

    db_manager = DBManager()
    while True:
        print("\n1 - Показать данные, 2 - Добавить данные, 3 - Выход")
        choice = input("Выберите действие: ")
        action = actions.get(choice)
        if action:
            action(db_manager)
            if choice == '3':
                break
        else:
            print("Неверный ввод. Пожалуйста, попробуйте снова.")


if __name__ == '__main__':
    main_menu()

