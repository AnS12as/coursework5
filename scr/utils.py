import requests
from scr.data import HHParser
from scr.db_manager import DBManager

def run():
    session = requests.Session()
    try:
        hh_parser = HHParser(session)
        db_manager = DBManager()

        db_manager.create_tables()
        employers = hh_parser.get_employers()
        vacancies = hh_parser.filter_vacancies()

        db_manager.insert_employers(employers)
        db_manager.insert_vacancies(vacancies)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()

if __name__ == '__main__':
    run()

