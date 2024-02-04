import psycopg2


class DBManager:
    """Класс для подключения к БД"""
    def __init__(self, host: str = 'localhost', database: str = 'hh_db',
                 user: str = 'hh_admin_db', password: str = '12345678'):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def get_companies_and_vacancies_count(self):
        """Метод получает список всех компаний и количество вакансий для каждой компании"""

        with psycopg2.connect(host=self.host, database=self.database,
                              user=self.user, password=self.password) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT company_name, open_vacancies  "
                            f"FROM employers"
                            )
                result = cur.fetchall()
            conn.commit()
        conn.close()
        return result

    def get_all_vacancies(self):
        """Метод получает список всех вакансий с названием компании, вакансии, зарплаты и ссылки на вакансию"""
        with psycopg2.connect(host=self.host, database=self.database,
                              user=self.user, password=self.password) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT employers.company_name, vacancies.vacancies_name, "
                            f"vacancies.payment, vacancies_url "
                            f"FROM employers "
                            f"JOIN vacancies USING (employer_id)")
                result = cur.fetchall()
            conn.commit()
        return result

    def get_avg_salary(self):
        """Метод получает среднюю зарплату по вакансиям"""
        with psycopg2.connect(host=self.host, database=self.database,
                              user=self.user, password=self.password) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT AVG(payment) as avg_payment FROM vacancies ")
                result = cur.fetchall()
            conn.commit()
        return result

    def get_vacancies_with_higher_salary(self):
        """Метод получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        with psycopg2.connect(host=self.host, database=self.database,
                              user=self.user, password=self.password) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM vacancies "
                            f"WHERE payment > (SELECT AVG(payment) FROM vacancies) ")
                result = cur.fetchall()
            conn.commit()
        return result

    def get_vacancies_with_keyword(self, keyword):
        """Метод получает список всех вакансий, в названии которых содержатся переданные в метод слова"""
        with psycopg2.connect(host=self.host, database=self.database,
                              user=self.user, password=self.password) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM vacancies "
                            f"WHERE lower(vacancies_name) LIKE '%{keyword}%' "
                            f"OR lower(vacancies_name) LIKE '%{keyword}'"
                            f"OR lower(vacancies_name) LIKE '{keyword}%';")
                result = cur.fetchall()
            conn.commit()
        return result
