import os
import psycopg2

class DBManager:
    def __init__(self):
        self.conn = psycopg2.connect(**self.config())
        self.ensure_tables_exist()

    def ensure_tables_exist(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS employers (
                    employer_id SERIAL PRIMARY KEY,
                    name VARCHAR(255) UNIQUE NOT NULL,
                    open_vacancies INT
                );
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS vacancies (
                    vacancy_id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    salary_from INT,
                    salary_to INT,
                    url VARCHAR(255),
                    employer_id INT REFERENCES employers(employer_id) ON DELETE CASCADE
                );
            """)
            self.conn.commit()

    def get_all_employers(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT employer_id, name, open_vacancies FROM employers")
            return cur.fetchall()

    def get_all_vacancies(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT vacancy_id, name, salary_from, salary_to, url, employer_id FROM vacancies")
            return cur.fetchall()

    def insert_employer(self, name, open_vacancies):
        with self.conn.cursor() as cur:
            cur.execute("INSERT INTO employers (name, open_vacancies) VALUES (%s, %s) ON CONFLICT (name) DO NOTHING", (name, open_vacancies))
            self.conn.commit()

    def insert_vacancy(self, name, salary_from, salary_to, url, employer_id):
        """Добавляет новую вакансию в базу данных."""
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO vacancies (name, salary_from, salary_to, url, employer_id) VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (vacancy_id) DO NOTHING
            """, (name, salary_from, salary_to, url, employer_id))
            self.conn.commit()
            print("Вакансия успешно добавлена.")

    def config(self):
        return {
            'host': 'localhost',
            'database': 'north',
            'user': 'postgres',
            'password': os.getenv('DB_PASSWORD', '1014'),
            'port': '5433'
        }
