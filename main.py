import click
from utils import get_vacancies, get_employer, create_table, add_to_table
from db_manager import DBManager

employers_list = [3529, 4181, 78638, 80, 7944, 113649, 1057, 26624, 2562304, 3778]
create_table()
add_to_table(employers_list)


@click.group()
def cli():
    pass


@cli.command()
def companies():
    dbmanager = DBManager()
    for result in dbmanager.get_companies_and_vacancies_count():
        print(f" Компания: {result[0]}, Количество вакансий: {result[1]}")


@cli.command()
def vacancies():
    dbmanager = DBManager()
    for result in dbmanager.get_all_vacancies():
        print(f" Компания: {result[0]}, Позиция: {result[1]}, Зарплата {result[2]}, Ссылка: {result[3]}")


@cli.command()
def avgsalary():
    dbmanager = DBManager()
    result = dbmanager.get_avg_salary()
    print(result)


@cli.command()
def highsalary():
    dbmanager = DBManager()
    for result in dbmanager.get_vacancies_with_higher_salary():
        print(f" ID_Вакансии: {result[0]}, Позиция: {result[1]}, Зарплата {result[2]},"
              f" Описание: {result[3]}, Ссылка: {result[4]}")


@cli.command()
@click.option('--keyword', help='Input keyword', required=True)
def find(keyword):
    dbmanager = DBManager()
    for result in dbmanager.get_vacancies_with_keyword(keyword=keyword):
        print(f" ID_Вакансии: {result[0]}, Позиция: {result[1]}, Зарплата {result[2]},"
              f" Описание: {result[3]}, Ссылка: {result[4]}")


if __name__ == '__main__':
    cli()
