from typing import Optional
from datetime import datetime


class Author:
    def __init__(self, first_name: str, last_name: str, year_of_birth: int) -> None:
        """
        Створює об'єкт автор
        :param first_name: ім'я автора
        :param last_name: прізвище автора
        :param year_of_birth: рік народження автора
        """
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth

    def __repr__(self):
        """
        Дозволяє отримати рядок, що представляє об'єкт у вигляді Python коду, який можна використовувати
        для його відтворення.
        """
        return f"Author('{self.first_name}', '{self.last_name}', {self.year_of_birth})"

    def __str__(self):
        """
        Повертає рядок, що представляє об'єкт у зручному для читання форматі.
        """
        return f"'{self.first_name} {self.last_name}'"

    def __eq__(self, other: 'Author') -> bool:
        """
        Повертає значення, яке вказує, чи об'єкти є рівними (однаковими).
        """
        if not isinstance(other, Author):
            raise TypeError(f"for type Author and type {type(other)} operation is not implemented")
        return (self.first_name == other.first_name and self.last_name == other.last_name
                and self.year_of_birth == other.year_of_birth)

    def __hash__(self):
        """
         Повертає хеш-значення об'єкта - ціле число, яке використовується для швидкого ідентифікування
         об'єктів під час їх зберігання в хеш-таблицях.
        """
        return hash((self.first_name, self.last_name, self.year_of_birth))


class Genre:
    def __init__(self, genre_name: str, genre_description: str) -> None:
        """
        Створює об'єкт жанр
        :param genre_name: назва жанру
        :param genre_description: опис жанру
        """
        self.genre_name = genre_name
        self.genre_description = genre_description

    def __repr__(self) -> str:
        """
        Дозволяє отримати рядок, що представляє об'єкт у вигляді Python коду, який можна використовувати
        для його відтворення.
        """
        return f"Genre('{self.genre_name}', '{self.genre_description}')"

    def __str__(self) -> str:
        """
        Повертає рядок, що представляє об'єкт у зручному для читання форматі.
        """
        return f"'{self.genre_name}'"


class Book:
    def __init__(self, title: str, language: str, year: int, *authors: Author, genres: list[Genre] = None,
                 isbn: str = None, description: Optional[str] = None) -> None:
        """
        Створює об'єкт книги
        :param title: назва книги
        :param language: мова видання
        :param authors: список авторів (об'єкт автор отримуємо з класу Author)
        :param genres: список жанрів (об'єкт жанр отримуємо з класу Genre)
        :param year: рік видання
        :param isbn: міжнародний стандартний номер книги
        :param description: опис книги
        """
        self.title = title
        self.language = language
        self.authors = authors
        self.genres = genres
        self.year = year
        self.isbn = isbn
        self.description = description

    def __repr__(self):
        """
        Дозволяє отримати рядок, що представляє об'єкт у вигляді Python коду, який можна використовувати
        для його відтворення.
        """
        return (f"Book('{self.title}', '{self.language}', {self.year},  [{self.authors}], [{self.genres}],"
                f"'{self.isbn}', '{self.description}')")

    def __str__(self):
        """
        Повертає рядок, що представляє об'єкт у зручному для читання форматі.
        """
        return (f"book: '{self.title}', language: '{self.language}', year: {self.year}, authors: {self.authors},"
                f"genres: {self.genres},  ISBN: '{self.isbn}', description: '{self.description}'")

    def __eq__(self, other: "Book") -> bool:
        """
        Повертає значення, яке вказує, чи об'єкти є рівними (однаковими).
        """
        if not isinstance(other, Book):
            raise TypeError(f"for type Book and type {type(other)} operation is not implemented")
        return set(self.authors) == set(other.authors) and self.title == other.title

    def calculate_age(self) -> int:
        """
        Повертає вік книги в роках (відносно поточного).
        """
        current_year = datetime.now().year
        book_age = current_year - self.year
        return book_age


if __name__ == "__main__":
    author1 = Author('Mike', 'Mison', 1970)
    author2 = Author('Stiv', 'Stivenson', 1975)
    genre1 = Genre('horror', 'very scary movie')
    genre2 = Genre('triller', 'amazing effects')

    book = Book('Scary Movie', 'eng', 2020, author1, author2)

    print(book)
    print(f"Вік книги: {book.calculate_age()} років")
