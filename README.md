Программа для работы с вакансиями работодателей на платформе HeadHunter

Для корректной работы программы необходима версия Python не ниже версии 3.11

Программа имеет следущий функционал:

Скачивание 10-ти вакансий определнных работодателей с платформы. При этом происходит автосохрание результата базу данных PostgreSQL.

Вывод списка всех компаний и количество вакансий для каждой компании.
Вывод списка всех вакансий с названием компании, вакансии, зарплаты и ссылки на вакансию.
Вывод средней зарплаты по вакансиям.
Вывод списка всех вакансий, у которых зарплата выше средней по всем вакансиям.
Вывод списка всех вакансий, в названии которых содержатся переданные в метод слова.

Для работы с программой используется командный интерфейс CLI, выполненный на основе библиотеки Click.

Логика работы программы:

Запуск программы происходит при помощи python3 основного файла main.py с добавлением ключей.

Запуск main.py без ключей выведет подсказу по существующим ключам.

Запуск main.py с ключём но без требуемого аргумента выведет ошибку с требованием ввести конкретный аргумент.

Запуск main.py с ключём и аргументом --help выведет список доступных аргументов ключа.

Список ключей и аргументов:

companies - производит вывод списка всех компаний и количество вакансий для каждой компании, не имеет аргументов.

vacancies - производит вывод списка всех вакансий с названием компании, вакансии, зарплаты и ссылки на вакансию, не имеет аргументов.

avgsalary - производит вывод средней зарплаты по вакансиям, не имеет аргументов.

highsalary - производит вывод списка всех вакансий, у которых зарплата выше средней по всем вакансиям, не имеет аргументов.

find - производит вывод списка всех вакансий, в названии которых содержатся переданные в метод слова, в аргументе --keyword= указывается ключевое слово для поиска.


Пример использования программы:

Загрузка данных в файл

python3 main.py companies

Поиск ключевых слов в вакансиях

python3 main.py find --keyword=стажер
